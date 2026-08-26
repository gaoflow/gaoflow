<div align="center">
  <img src="./assets/flow-header.svg" width="100%" alt="Bing Gao — CFD engineering, simulation tooling, and open-source software" />
</div>

<p align="center">
  <code>Paris</code> · <code>CFD Engineer &amp; Developer</code> · <code>Open to safety / Aerodynamic work</code>
</p>

---

## About Me

I'm Bing Gao, a computational-mechanics engineering student in Paris and an aerodynamics engineer with **Vinci Eco Drive, ESILV Formula Student**. My current work covers external-aerodynamics CFD, thermal-fluid modelling, numerical verification, and simulation tooling.

Before returning to engineering study, I spent nearly seven years building mobile software and leading development. I helped take **Lao You** from its first version to more than **2 million users**, wrote 70% of its initial core code, and built delivery, security, and real-time systems. I now apply the same delivery discipline to simulation: geometry, mesh, solver settings, post-processing, acceptance gates, and evidence remain linked.

I also contribute upstream across scientific-computing, parser, serialization, data-tooling, and engineering libraries. Each contribution starts from a reproduced defect and ends with a regression test and a narrowly scoped patch. **[Python Bugfix Notes](https://github.com/gaoflow/python-bugfix-notes)** records a few of those investigations; the table below links directly to a broader selection of merged work.

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

<h4 align="center">MECHANICAL · SIMULATION · CAD / 3D</h4>

<p align="center">
  <img src="https://www.openfoam.com/themes/bs4esi/img/openfoam-logo.png?v20210416" height="28" alt="OpenFOAM" />
  &nbsp;
  <img src="https://img.shields.io/badge/Ansys_Fluent-FFB71B?style=flat-square&amp;logo=ansys&amp;logoColor=black" alt="Ansys Fluent" />
  <img src="https://img.shields.io/badge/Ansys_Mechanical-FFB71B?style=flat-square&amp;logo=ansys&amp;logoColor=black" alt="Ansys Mechanical" />
  <img src="https://img.shields.io/badge/Simcenter_STAR--CCM%2B-009999?style=flat-square&amp;logo=siemens&amp;logoColor=white" alt="Simcenter STAR-CCM+" />
  <img src="https://img.shields.io/badge/Abaqus-005386?style=flat-square&amp;logo=dassaultsystemes&amp;logoColor=white" alt="Abaqus" />
  <img src="https://img.shields.io/badge/CATIA-005386?style=flat-square&amp;logo=dassaultsystemes&amp;logoColor=white" alt="CATIA" />
  <img src="https://img.shields.io/badge/SolidWorks-DA1F26?style=flat-square&amp;logo=dassaultsystemes&amp;logoColor=white" alt="SolidWorks" />
  <img src="https://img.shields.io/badge/Blender-E87D0D?style=flat-square&amp;logo=blender&amp;logoColor=white" alt="Blender" />
  &nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/matlab/matlab-original.svg" height="28" alt="" /> <code>MATLAB / Simulink</code>
</p>

<h4 align="center">SOFTWARE DEVELOPMENT</h4>

<table width="100%">
  <thead>
    <tr>
      <th width="33%">FRONTEND</th>
      <th width="34%">BACKEND</th>
      <th width="33%">MOBILE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center" valign="top">
        <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&amp;logo=typescript&amp;logoColor=white" alt="TypeScript" />
        <img src="https://img.shields.io/badge/React-20232A?style=flat-square&amp;logo=react&amp;logoColor=61DAFB" alt="React" />
        <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&amp;logo=javascript&amp;logoColor=black" alt="JavaScript" />
      </td>
      <td align="center" valign="top">
        <img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&amp;logo=nodedotjs&amp;logoColor=white" alt="Node.js" />
        <img src="https://img.shields.io/badge/Ruby_on_Rails-D30001?style=flat-square&amp;logo=rubyonrails&amp;logoColor=white" alt="Ruby on Rails" />
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&amp;logo=python&amp;logoColor=white" alt="Python" />
      </td>
      <td align="center" valign="top">
        <img src="https://img.shields.io/badge/Android-3DDC84?style=flat-square&amp;logo=android&amp;logoColor=white" alt="Android" />
        <img src="https://img.shields.io/badge/Java-ED8B00?style=flat-square&amp;logo=openjdk&amp;logoColor=white" alt="Java" />
        <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&amp;logo=kotlin&amp;logoColor=white" alt="Kotlin" />
        <img src="https://img.shields.io/badge/React_Native-20232A?style=flat-square&amp;logo=react&amp;logoColor=61DAFB" alt="React Native" />
      </td>
    </tr>
  </tbody>
</table>

---

### `03` · CONNECT

<p align="center">
  <a href="mailto:gaobing1230@gmail.com"><img src="https://img.shields.io/badge/EMAIL-gaobing1230%40gmail.com-2563EB?style=for-the-badge&amp;labelColor=0F172A&amp;logo=gmail&amp;logoColor=white" alt="Email Bing Gao" /></a>
  &nbsp;
  <a href="https://www.linkedin.com/in/bing-gao/"><img src="https://img.shields.io/badge/LINKEDIN-BING_GAO-14B8A6?style=for-the-badge&amp;labelColor=0F172A&amp;logo=linkedin&amp;logoColor=white" alt="Bing Gao on LinkedIn" /></a>
  &nbsp;
  <a href="https://vinzzy.com"><img src="https://img.shields.io/badge/HOMEPAGE-vinzzy.com-1B365D?style=for-the-badge&amp;logo=safari&amp;logoColor=white" alt="Bing Gao's homepage" /></a>
  &nbsp;
  <a href="https://github.com/gaoflow?tab=repositories"><img src="https://img.shields.io/badge/GITHUB-REPOSITORIES-38BDF8?style=for-the-badge&amp;labelColor=0F172A&amp;logo=github&amp;logoColor=white" alt="Browse gaoflow repositories" /></a>
</p>
