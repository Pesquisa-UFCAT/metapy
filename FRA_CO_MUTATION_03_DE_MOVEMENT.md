---
layout: default
title: mutation_03_de_movement
grand_parent: Framework
parent: Common Library functions
has_toc: false
nav_order: 8
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>mutation_03_de_movement</h3>

<br>

<p align = "justify">
  This function mutates a solution using a differential evolution mutation.
</p>

```python
x_i_new, of_i_new,\
    fit_i_new, neof = mutation_03_de_movement(obj_function,
                                                x_i_old, x_ii_old,
                                                x_iii_old, x_lower,
                                                x_upper, n_dimensions,
                                                f, none_variable=None)
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
        <td>Py function (def)</td>
    </tr>
    <tr>
        <td><code>x_i_old</code></td>
        <td>Current design variables of the \(i\) agent</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>x_ii_old</code></td>
        <td>Current design variables of the random \(r_0\) agent</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>x_iii_old</code></td>
        <td>Current design variables of the random \(r_1\) agent</td>
        <td>List</td>
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
        <td><code>f</code></td>
        <td>Scaling factor</td>
        <td>Float</td>
    </tr>
     <tr>
        <td><code>none_variable</code></td>
        <td>None variable. Default is None. Use in objective function</td>
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
# Import
from metapy_toolbox import mutation_03_de_movement # or import *

# Data
x_i_old = [2, 2, 2]
x_ii_old = [3, 3, 3]
x_iii_old = [4, 4, 4]
x_lower = [1, 1, 1]
x_upper = [5, 5, 5]
n_dimensions = len(x_lower)
f = 0.5
none_variable = None

# Objective function
def obj_function(x, _):
    """Example objective function"""
    x0 = x[0]
    x1 = x[1]
    of = x0 ** 2 + x1 ** 2
    return of

# Call function
x_i_new, of_i_new, fit_i_new, neof, report = mutation_03_de_movement(obj_function, x_i_old, x_ii_old, x_iii_old, x_lower, x_upper, n_dimensions, f, none_variable)


# Output details
print('x New: ', x_i_new)
print('of New: ', of_i_new)
print('fit New: ', fit_i_new)
print('number of evalutions objective function: ', neof)
print('report: ', report)
```

```bash
x New:  [1.5, 1.5, 1.5]
of New:  4.5
fit New:  0.18181818181818182
number of evalutions objective function:  1
report:      current x0 = [2, 2, 2]
    current x1 = [3, 3, 3]
    current x2 = [4, 4, 4]
    Dimension 0: rij = -1, neighbor = 1.5
    Dimension 1: rij = -1, neighbor = 1.5
    Dimension 2: rij = -1, neighbor = 1.5
    update x = [1.5, 1.5, 1.5], of = 4.5, fit = 0.18181818181818182
```
