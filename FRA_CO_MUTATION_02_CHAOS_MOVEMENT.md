---
layout: default
title: mutation_02_movement
grand_parent: Framework
parent: Common Library functions
has_toc: false
nav_order: 7
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>mutation_02_chaos_movement</h3>

<br>

<p align = "justify">
  This function mutates a solution using a chaotic maps.
</p>

```python
mutation_02_chaos_movement(obj_function, x_i_old, fit_i_old, x_lower, x_upper,\
                         n_dimensions, ch, alpha, n_tries, iteration, n_iter,\
                         none_variable)
```

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
        <td><code>obj_function</code></td>
        <td>Objective function. The Metapy user defined this function</td>
        <td>Py function (<code>def</code>)</td>
    </tr>
    <tr>
        <td><code>x_i_old</code></td>
        <td>Current design variables of the \(i\) agent</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>fit_i_old</code></td>
        <td>Current fitness value of the \(i\) agent</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>x_lower</code></td>
        <td>Lower limit of the design variables</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>x_upper</code></td>
        <td>Upper limit of the design variables</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>n_dimensions</code></td>
        <td>Problem dimension</td>
        <td>Int</td>
    </tr>
    <tr>
        <td><code>ch</code></td>
        <td>Chaotic value</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>alpha</code></td>
        <td>Chaotic map control parameter</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>n_tries</code></td>
        <td>Number of tries to find a better solution</td>
        <td>Int</td>
    </tr>
    <tr>
        <td><code>iteration</code></td>
        <td>Current iteration number</td>
        <td>Int</td>
    </tr>
    <tr>
        <td><code>n_iter</code></td>
        <td>Total number of iterations</td>
        <td>Int</td>
    </tr>
    <tr>
        <td><code>none_variable</code></td>
        <td>None variable. Default is <code>None</code>. Use in objective function</td>
        <td>Object or None</td>
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
        <td><code>x_i_new</code></td>
        <td>Update variables of the \(i\) agent</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>of_i_new</code></td>
        <td>Update objective function value of the \(i\) agent</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>fit_i_new</code></td>
        <td>Update fitness value of the \(i\) agent</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>neof</code></td>
        <td>Number of evaluations of the objective function</td>
        <td>Int</td>
    </tr>
    <tr>
        <td><code>report</code></td>
        <td>Report about the mutation process</td>
        <td>String</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
      
  </i>
</p>

```python

```

```bash

```
