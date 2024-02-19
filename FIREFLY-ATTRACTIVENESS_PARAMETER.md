---
layout: default
title: Attractiveness parameter
grand_parent: Framework
parent: Firefly functions
has_children: false
has_toc: true
nav_order: 2
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

```python
result = ff.attractiveness_parameter(0.5, [1,2,3,4,5], [1,1,1,1,1], [5,5,5,5,5], 5)
```

<p align="justify">
This function calculates at attractiveness parameter between <code>x_i</code> and <code>x_j</code> fireflies.
</p>

Input variables
{: .label .label-yellow }

<table style = "width:100%">
    <thead>
      <tr>
        <th>Name</th>
        <th>Description</th>
        <th>Type</th>
      </tr>
    </thead>
    <tr>
        <td><code>beta_0</code></td>
        <td>Attractiveness at <code>r = 0</code></td>
        <td>float</td>
    </tr>
    <tr>
        <td><code>gamma</code></td>
        <td>Light absorption coefficient  <code>1 / (x_lower - x_upper) ** m</code>.</td>
        <td>Py list</td>
    </tr>
     <tr>
        <td><code>x_i</code></td>
        <td>Design variables <code>i</code> Firefly</td>
        <td>Py list</td>
    </tr>
     <tr>
        <td><code>x_j</code></td>
        <td>Design variables <code>j</code> Firefly.</td>
        <td>Py list</td>
    </tr>
     <tr>
        <td><code>n_dimensions</code></td>
        <td>Problem dimension.</td>
        <td>Py list</td>
    </tr>
</table>

Output variables
{: .label .label-yellow }

<table style = "width:100%">
    <thead>
      <tr>
        <th>Name</th>
        <th>Description</th>
        <th>Type</th>
      </tr>
    </thead>
    <tr>
        <td><code>beta</code></td>
        <td>Attractiveness.</td>
        <td>Py list</td>
    </tr>
</table>
