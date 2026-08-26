#!/usr/bin/env python3
"""Update the merged pull-request count embedded in the profile README."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "README.md"
GRAPHQL_URL = "https://api.github.com/graphql"
START_MARKER = "<!-- merged-pr-count:start -->"
END_MARKER = "<!-- merged-pr-count:end -->"
COUNT_PATTERN = re.compile(r"\*\*(\d+) merged pull requests\*\*")
QUERY = """
query MergedPullRequests($login: String!) {
  user(login: $login) {
    pullRequests(states: MERGED) {
      totalCount
    }
  }
}
""".strip()


def validate_count(value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError("merged pull-request count must be a non-negative integer")
    return value


def fetch_merged_pr_count(login: str, token: str) -> int:
    payload = json.dumps({"query": QUERY, "variables": {"login": login}}).encode(
        "utf-8"
    )
    request = urllib.request.Request(
        GRAPHQL_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "gaoflow-profile-merged-pr-count",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            data = json.load(response)
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as error:
        raise RuntimeError(f"GitHub GraphQL request failed: {error}") from error

    if data.get("errors"):
        raise RuntimeError(f"GitHub GraphQL returned errors: {data['errors']}")

    user = data.get("data", {}).get("user")
    if user is None:
        raise RuntimeError(f"GitHub user not found: {login}")

    count = user.get("pullRequests", {}).get("totalCount")
    return validate_count(count)


def replace_count(readme: str, count: int) -> str:
    count = validate_count(count)
    if readme.count(START_MARKER) != 1 or readme.count(END_MARKER) != 1:
        raise ValueError("README must contain exactly one merged PR marker pair")

    start = readme.index(START_MARKER)
    end = readme.index(END_MARKER)
    if start >= end:
        raise ValueError("merged PR markers are reversed")

    block_start = start + len(START_MARKER)
    block = readme[block_start:end]
    matches = list(COUNT_PATTERN.finditer(block))
    if len(matches) != 1:
        raise ValueError("merged PR marker block must contain exactly one count phrase")

    updated_block = COUNT_PATTERN.sub(
        f"**{count} merged pull requests**", block, count=1
    )
    return readme[:block_start] + updated_block + readme[end:]


def write_if_changed(output: Path, content: str) -> bool:
    output = output.resolve()
    encoded = content.encode("utf-8")
    if output.exists() and output.read_bytes() == encoded:
        return False

    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="wb", dir=output.parent, prefix=f".{output.name}.", delete=False
    ) as temporary:
        temporary.write(encoded)
        temporary_path = Path(temporary.name)

    try:
        temporary_path.chmod(0o644)
        temporary_path.replace(output)
    finally:
        if temporary_path.exists():
            temporary_path.unlink()
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--login", default=os.environ.get("GITHUB_USERNAME", "gaoflow"))
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--count", type=int, help="offline count override")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    login = args.login.strip()
    if not login:
        raise ValueError("GitHub login must not be empty")
    if not args.output.exists():
        raise RuntimeError(f"README not found: {args.output}")

    if args.count is None:
        token = os.environ.get("GITHUB_TOKEN")
        if not token:
            raise RuntimeError("GITHUB_TOKEN is required for a live update")
        count = fetch_merged_pr_count(login, token)
    else:
        count = validate_count(args.count)

    original = args.output.read_text(encoding="utf-8")
    updated = replace_count(original, count)
    changed = write_if_changed(args.output, updated)
    print(count)
    print("updated" if changed else "unchanged", file=sys.stderr)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1) from None
