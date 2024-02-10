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
    <td>An objective function to be optimized. Presumably, it's a function that takes an input vector (in this case, y_i_new) and possibly other parameters (none_variable) and returns a scalar value representing the objective to be minimized or maximized.</td>
    <td>Py function</td>
  </tr>
  <tr>
    <td><code>beta_0</code></td>
    <td>An initial adjustment parameter.</td>
    <td>float</td>
  </tr>
  <tr>
    <td><code>gamma</code></td>
    <td>An adjustment parameter influencing the strength of attraction between fireflies.</td>
    <td>float</td>
  </tr>
  <tr>
    <td><code>x_i_old_best</code></td>
    <td>The best point found so far in the search.</td>
    <td>Py list</td>
  </tr>
  <tr>
    <td><code>y_j_old</code></td>
    <td>The current point being evaluated.</td>
    <td>Py list</td>
  </tr>
  <tr>
    <td><code>n_dimensions</code></td>
    <td>The number of dimensions in the search space.</td>
    <td>int</td>
  </tr>
  <tr>
    <td><code>x_lower</code></td>
    <td>A vector representing the lower bounds of each dimension in the search space.</td>
    <td>Py list</td>
  </tr>
  <tr>
    <td><code>x_upper</code></td>
    <td>A vector representing the upper bounds of each dimension in the search space.</td>
    <td>Py list</td>
  </tr>
  <tr>
    <td><code>report</code></td>
    <td>A string likely used to record information about the algorithm's progress.</td>
    <td>String</td>
  </tr>
  <tr>
    <td><code>none_variable</code></td>
    <td>An optional parameter that seems to be passed to the objective function.</td>
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
    <td><code>y_i_new</code></td>
    <td>The new point resulting from the firefly's movement, possibly a better candidate.</td>
    <td>Py list</td>
  </tr>
  <tr>
    <td><code>of_i_new</code></td>
    <td>The value of the objective function for the new point <code>y_i_new</code>.</td>
    <td>float</td>
  </tr>
  <tr>
    <td><code>fit_i_new</code></td>
    <td>The fitness value associated with the point <code>y_i_new</code>.</td>
    <td>float</td>
  </tr>
  <tr>
    <td><code>neof</code></td>
    <td>A value that seems to indicate if there was an update in the best-found point.</td>
    <td>int</td>
  </tr>
  <tr>
    <td><code>report</code></td>
    <td>The updated report string, likely containing information about the firefly's movement and evaluation.</td>
    <td>String</td>
  </tr>
</table>
