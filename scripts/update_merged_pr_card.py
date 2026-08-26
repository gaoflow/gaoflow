#!/usr/bin/env python3
"""Generate the profile's merged pull-request SVG from GitHub GraphQL."""

from __future__ import annotations

import argparse
import html
import json
import os
import sys
import tempfile
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "assets" / "merged-prs.svg"
GRAPHQL_URL = "https://api.github.com/graphql"
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
            "User-Agent": "gaoflow-profile-merged-pr-card",
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


def render_svg(count: int, login: str) -> str:
    count = validate_count(count)
    safe_login = html.escape(login.strip(), quote=True)
    if not safe_login:
        raise ValueError("GitHub login must not be empty")

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="680" height="150" viewBox="0 0 680 150" role="img" aria-labelledby="title desc">
  <title id="title">{count} merged pull requests by @{safe_login}</title>
  <desc id="desc">Live GitHub metric showing {count} merged pull requests authored by @{safe_login}.</desc>
  <defs>
    <linearGradient id="surface" x1="18" y1="14" x2="662" y2="136" gradientUnits="userSpaceOnUse">
      <stop stop-color="#FAF9F5"/>
      <stop offset="1" stop-color="#EEF2F7"/>
    </linearGradient>
    <style>
      .mono {{ font-family: ui-monospace, "SFMono-Regular", "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; }}
    </style>
  </defs>
  <rect width="680" height="150" fill="#F5F4ED"/>
  <rect x="1" y="1" width="678" height="148" rx="14" fill="url(#surface)" stroke="#D8D5C9" stroke-width="2"/>
  <g opacity=".65" stroke="#E8E6DC">
    <path d="M1 50H679M1 100H679"/>
    <path d="M170 1V149M340 1V149M510 1V149"/>
  </g>
  <g class="mono">
    <text x="36" y="36" font-size="11" letter-spacing="2.4" fill="#6B6A64">OPEN-SOURCE TRACK RECORD</text>
    <text x="34" y="116" font-size="64" font-weight="700" letter-spacing="1" fill="#141413">{count}</text>
    <text x="238" y="78" font-size="20" font-weight="700" letter-spacing="1.8" fill="#1B365D">MERGED PULL REQUESTS</text>
    <text x="240" y="104" font-size="11" letter-spacing="2" fill="#6B6A64">AUTHORED BY @{safe_login.upper()}</text>
  </g>
  <g transform="translate(600 40)" fill="none" stroke="#1B365D" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="12" cy="12" r="6" fill="#FAF9F5"/>
    <circle cx="12" cy="70" r="6" fill="#FAF9F5"/>
    <circle cx="48" cy="41" r="6" fill="#FAF9F5" stroke="#8B4513"/>
    <path d="M12 18V64M18 41H31C40 41 48 33 48 24V18M42 24L48 18L54 24"/>
  </g>
  <path d="M18 34V18H34M646 18H662V34M18 116V132H34M646 132H662V116" stroke="#1B365D" stroke-width="1.5" opacity=".72"/>
</svg>
"""


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

    if args.count is None:
        token = os.environ.get("GITHUB_TOKEN")
        if not token:
            raise RuntimeError("GITHUB_TOKEN is required for a live update")
        count = fetch_merged_pr_count(login, token)
    else:
        count = validate_count(args.count)

    svg = render_svg(count, login)
    ET.fromstring(svg)
    changed = write_if_changed(args.output, svg)
    print(count)
    print("updated" if changed else "unchanged", file=sys.stderr)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1) from None
