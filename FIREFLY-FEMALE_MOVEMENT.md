---
layout: default
title: Female movement
grand_parent: Firefly
parent: Firefly functions
has_children: false
has_toc: true
nav_order: 4
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

```python
x_i_new, of_i_new, fit_i_new, neof, report = ff.male_movement(obj_function, 1, [1, 1], [0, 0], 0, [1, 1], 1, [-1, -1], 2, 2, [-5, -5],[5, 5])
```

<p align="justify">
This function movement a male firefly.
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
