<div align="center">
  <img src="./assets/flow-header.svg" width="100%" alt="Bing Gao — CFD engineering, simulation tooling, and open-source software" />
</div>

<p align="center">
  <code>Paris La Défense</code> · <code>CFD Engineer &amp; Developer</code> · <code>Open to CFD / Aerodynamics internships — 2026</code>
</p>

---

## About Me

I'm Bing Gao, a computational-mechanics engineering student in Paris and an aerodynamics engineer with **Vinci Eco Drive, ESILV Formula Student**. My current work covers external-aerodynamics CFD, thermal-fluid modelling, numerical verification, and simulation tooling.

Before returning to engineering study, I spent nearly seven years building mobile software and leading development. I helped take **Lao You** from its first version to more than **2 million users**, wrote 70% of its initial core code, and built delivery, security, and real-time systems. I now apply the same delivery discipline to simulation: geometry, mesh, solver settings, post-processing, acceptance gates, and evidence remain linked.

My open-source work follows the same rule. A parser, numerical routine, serializer, or scientific file reader should fail in a reproducible test before it is changed. I collect the reasoning behind selected fixes in **[Python Bugfix Notes](https://github.com/gaoflow/python-bugfix-notes)**.

---

### `01` · OPEN SOURCE CONTRIBUTIONS

> `reproduce → isolate the contract → add a regression test → make the smallest correct patch`

More than **600 merged pull requests** across scientific computing, parsers, serialization, data tooling, and numerical libraries. A representative selection:

| Project | What changed | Pull request |
| --- | --- | --- |
| `SU2` | Fixed Nastran small-field real parsing in the modal structural solver | [`su2code/SU2#2859`](https://github.com/su2code/SU2/pull/2859) |
| `PyFR` | Namespaced Gmsh physical-group IDs by dimension | [`PyFR/PyFR#580`](https://github.com/PyFR/PyFR/pull/580) |
| `statsmodels` | Back-transformed the univariate smoothed measurement disturbance | [`statsmodels/statsmodels#9979`](https://github.com/statsmodels/statsmodels/pull/9979) |
| `foamlib` | Preserved unit scale multipliers and accepted OpenFOAM-legal dictionary grammar | [`gerlero/foamlib#833`](https://github.com/gerlero/foamlib/pull/833) · [`#829`](https://github.com/gerlero/foamlib/pull/829) |
| `PyMeasure` | Prevented SR830/SR860 auxiliary outputs from truncating sub-microvolt values | [`pymeasure/pymeasure#1495`](https://github.com/pymeasure/pymeasure/pull/1495) |
| `pyserde` | Fixed heterogeneous enum deserialization and Optional/Union serialization | [`yukinarit/pyserde#774`](https://github.com/yukinarit/pyserde/pull/774) · [`#764`](https://github.com/yukinarit/pyserde/pull/764) |
| `jsonpickle` | Rebuilt NumPy scalars from their declared dtype and preserved datetime fold | [`jsonpickle/jsonpickle#619`](https://github.com/jsonpickle/jsonpickle/pull/619) · [`#618`](https://github.com/jsonpickle/jsonpickle/pull/618) |
| `py7zr` | Required passwords for crypto write filters and bounded extract worker tasks | [`miurahr/py7zr#739`](https://github.com/miurahr/py7zr/pull/739) · [`#740`](https://github.com/miurahr/py7zr/pull/740) |
| `sqlparse` | Recognized `MATERIALIZED` as a SQL keyword | [`andialbrecht/sqlparse#854`](https://github.com/andialbrecht/sqlparse/pull/854) |

<p align="right"><a href="https://github.com/search?q=is%3Apr+author%3Agaoflow+is%3Amerged&type=pullrequests">Browse all merged pull requests →</a></p>

---

### `02` · STACK

<table width="100%">
  <thead>
    <tr>
      <th width="34%">SIMULATION</th>
      <th width="33%">CAD &amp; 3D</th>
      <th width="33%">SOFTWARE &amp; AUTOMATION</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center" valign="top">
        <img src="https://img.shields.io/badge/OpenFOAM-0065BD?style=flat-square" alt="" />
        <img src="https://img.shields.io/badge/Ansys_Fluent-FFB71B?style=flat-square&amp;logo=ansys&amp;logoColor=black" alt="" />
        <img src="https://img.shields.io/badge/Abaqus-005386?style=flat-square" alt="" /><br/>
        <sub>OpenFOAM · Ansys Fluent · Ansys Mechanical · Star-CCM+ · Abaqus</sub><br/>
        <sub>FVM · RANS · FEA · LBM · POD/DMD · thermal-fluid modelling</sub>
      </td>
      <td align="center" valign="top">
        <img src="https://skillicons.dev/icons?i=blender&amp;theme=dark" alt="" /><br/>
        <sub>CATIA · SolidWorks · Blender</sub><br/>
        <sub>reference reconstruction · geometry audits · browser-ready GLB</sub>
      </td>
      <td align="center" valign="top">
        <img src="https://skillicons.dev/icons?i=python,cpp,rust,java,kotlin,ts,nodejs,ruby&amp;theme=dark" alt="" /><br/>
        <sub>Python · C/C++ · Rust · Java/Kotlin · TypeScript/React · Node.js · Ruby · Bash</sub><br/>
        <sub>MATLAB/Simulink · CI/CD · regression testing</sub>
      </td>
    </tr>
  </tbody>
</table>

---

### `03` · THE TOOLBOX

<div align="center">

> `~/toolbox` &nbsp;→&nbsp; the checks around the solver

**`snappyHexMesh`** · **`pytest`** · **`GitHub Actions`** · **`Blender audit scripts`** · **`evidence manifests`** · **`Python/Bash pipelines`**

<br/>

<img src="https://skillicons.dev/icons?i=python,bash,git,github,linux,blender&amp;theme=dark" alt="" />

</div>

---

### `04` · SELECTED ENGINEERING WORK

The figures below are taken from my **[current engineering CV](./assets/Bing-Gao-CV.pdf#page=2)**. Each row keeps the validation boundary beside the result.

| Project | Result retained | Declared boundary |
| --- | --- | --- |
| `Formula Student Cooling System` | Coupled fan, radiator, pump, and an 80-cell coolant model; found a 10.03 L/min operating point and rejected the unchanged passive E3 architecture before procurement | Numerical screening and OpenFOAM surrogate qualification, not installed-vehicle validation |
| `F1 External-Aerodynamics RANS Pilot` | Ran a 4.35M-cell OpenFOAM half-car baseline and a 23-variant campaign; retained nine valid sensitivities and preserved two diverged roughness runs | Pilot workflow with material mesh sensitivity; no absolute aerodynamic-performance claim |
| `FlowLab & FlowROM` | Validated one dependency-free D2Q9 solver at Re=100, then achieved 0.123% rank-8 POD holdout error with 48.8× compression and 0.100% DMD full-state holdout error | Controlled two-dimensional internal flow |
| `Space Rider Digital Model` | Reconstructed a 4.88 m body from public blueprints, verified ±6 mm side-view and ±8.4 mm top-view agreement, and reduced the browser GLB from 11.6 MB to 639 KB | Reference-led internship work, not manufacturer CAD or flight-article validation |
| [`AirfRANS conformal-OOD audit`](https://github.com/gaoflow/airfrans-conformal-ood-audit) | Audited grouping, score normalization, calibration allocation, finite-rank refusal, identity overlap, selective availability, and predictor error under physical shift | Target-pool empirical audit; no claim of source-to-OOD conformal validity or field coverage |

---

### `05` · CONNECT

<p align="center">
  If your work needs reproducible CFD, numerical verification, or engineering software that keeps its evidence attached, get in touch.
</p>

<p align="center">
  <a href="mailto:gaobing1230@gmail.com"><img src="https://img.shields.io/badge/EMAIL-gaobing1230%40gmail.com-2563EB?style=for-the-badge&amp;labelColor=0F172A&amp;logo=gmail&amp;logoColor=white" alt="Email Bing Gao" /></a>
  &nbsp;
  <a href="https://www.linkedin.com/in/bing-gao/"><img src="https://img.shields.io/badge/LINKEDIN-BING_GAO-14B8A6?style=for-the-badge&amp;labelColor=0F172A&amp;logo=linkedin&amp;logoColor=white" alt="Bing Gao on LinkedIn" /></a>
  &nbsp;
  <a href="./assets/Bing-Gao-CV.pdf"><img src="https://img.shields.io/badge/RESUME-PDF-E2E8F0?style=for-the-badge&amp;labelColor=0F172A&amp;logo=adobeacrobatreader&amp;logoColor=white" alt="Download Bing Gao's CV" /></a>
  &nbsp;
  <a href="https://github.com/gaoflow?tab=repositories"><img src="https://img.shields.io/badge/GITHUB-REPOSITORIES-38BDF8?style=for-the-badge&amp;labelColor=0F172A&amp;logo=github&amp;logoColor=white" alt="Browse gaoflow repositories" /></a>
</p>

<p align="center"><sub><code>$ discuss --topics "CFD | aerodynamics | simulation tooling"</code></sub></p>
