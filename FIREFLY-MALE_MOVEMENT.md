---
layout: default
title: Male movement
grand_parent: Firefly
parent: Firefly functions
has_children: false
has_toc: true
nav_order: 3
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

<table style="width:100%">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Type</th>
    </tr>
  </thead>
  <tr>
    <td><code>obj_function</code></td>
    <td>Objective function</td>
    <td>Py function</td>
  </tr>
  <tr>
    <td><code>beta_0</code></td>
    <td>Attractiveness at <code>r = 0</code></td>
    <td>Py list</td>
  </tr>
  <tr>
    <td><code>gamma</code></td>
    <td>Light absorption coefficient  1 / (X_U - X_L) ** M</td>
    <td>Py list</td>
  </tr>
  <tr>
    <td><code>x_i_old</code></td>
    <td>Design variables <code>i</code> (male) Firefly</td>
    <td>Py list</td>
  </tr>
  <tr>
    <td><code>fit_i_old</code></td>
    <td>Fitness of the <code>i</code> firefly</td>
    <td>float</td>
  </tr>
  <tr>
    <td><code>y_j_old</code></td>
    <td>Design variables <code>j</code> (female) Firefly</td>
    <td>Py list</td>
  </tr>
  <tr>
    <td><code>fit_j_old</code></td>
    <td>Fitness of the <code>j</code> firefly</td>
    <td>float</td>
  </tr>
  <tr>
    <td><code>y_k_old</code></td>
    <td>Design variables <code>k</code> (female) Firefly</td>
    <td>Py list</td>
  </tr>
  <tr>
    <td><code>fit_k_old</code></td>
    <td>Fitness of the <code>k</code> firefly</td>
    <td>float</td>
  </tr>
  <tr>
    <td><code>n_dimensions</code></td>
    <td>Problem dimension</td>
    <td>int</td>
  </tr>
  <tr>
    <td><code>x_lower</code></td>
    <td>Lower limit of the problem</td>
    <td>Py list</td>
  </tr>
  <tr>
    <td><code>x_upper</code></td>
    <td>Upper limit of the problem</td>
    <td>Py list</td>
  </tr>
  <tr>
    <td><code>report</code></td>
    <td>Report about the mutation process. Default is "".</td>
    <td>String</td>
  </tr>
  <tr>
    <td><code>none_variable</code></td>
    <td>None variable. Default is None. Use in objective function.</td>
    <td>Py Object or None</td>
  </tr>
</table>

Output variables
{: .label .label-yellow }

<table style="width:100%">
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th>Type</th>
    </tr>
  </thead>
  <tr>
    <td><code>x_i_new</code></td>
    <td>Update variables of the <code>i</code> agent.</td>
    <td>Py list</td>
  </tr>
  <tr>
    <td><code>of_i_new</code></td>
    <td>Update objective function value of the <code>i</code> agent.</td>
    <td>Py float</td>
  </tr>
  <tr>
    <td><code>fit_i_new</code></td>
    <td>Update fitness value of the <code>i</code> agent.</td>
    <td>Py float</td>
  </tr>
  <tr>
    <td><code>neof</code></td>
    <td>Number of evaluations of the objective function.</td>
    <td>Py int</td>
  </tr>
  <tr>
    <td><code>report</code></td>
    <td>Report about the male movement process.</td>
    <td>Py str</td>
  </tr>
</table>
