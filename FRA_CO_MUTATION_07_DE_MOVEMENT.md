---
layout: default
title: mutation_07_de_movement
grand_parent: Framework
parent: Common Library functions
has_toc: false
nav_order: 106
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>mutation_07_de_movement</h3>

<br>

<p align = "justify">
    This function mutates a solution using a differential evolution mutation (DE/target-to-get/1).
</p>

```python
x_i_new, of_i_new, fit_i_new, neof, report = mutation_07_de_movement(obj_function, x_r0_old, x_r1_old, x_r2_old, x_best, x_lower, x_upper, n_dimensions, f, none_variable)
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
        <td><code>x_r0_old</code></td>
        <td>Current design variables of the random \(r_0\) agent</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>x_r1_old</code></td>
        <td>Current design variables of the random \(r_1\) agent</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>x_r2_old</code></td>
        <td>Current design variables of the random \(r_2\) agent</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>x_best</code></td>
        <td>Best design variables from the population</td>
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
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>f</code></td>
        <td>Scaling factor</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>none_variable</code></td>
        <td>None variable. Default is None. User can use this variable in objective function</td>
        <td>None, list, float, dictionary, str or any</td>
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
from metapy_toolbox import mutation_07_de_movement # or import *

# Data
xI = [2.0, 2.0]
xR0 = [1.4, 2.6]
xR1 = [3.1, 4.7]
xR2 = [2.1, 4.9]
xBest = [1.2, 1.2]
xL = [1.0, 1.0]
xU = [5.0, 5.0]
d = len(xL)
f = 1.2

# Objective function

def objFunction(x, _):
    """Example objective function"""
    x0 = x[0]
    x1 = x[1]
    of = x0 ** 2 + x1 ** 2
    return of

# Call function

xNew, ofNew, fitNew, neof, report = mutation_07_de_movement(objFunction, xI, xR0, xR1, xR3, xBest, xL, xU, d, f)

# Output details

print('x New: ', xNew)
print('of New: ', ofNew)
print('fit New: ', fitNew)
print('number of evalutions objective function: ', neof)
```

```bash
x New:  [1.8800000000000001, 1.1600000000000001]
of New:  4.880000000000001
fit New:  0.17006802721088432
number of evalutions objective function:  1
```

<p align = "justify">
  To check the movement report just apply the following instruction.
</p>

```python
# Report details
arq = "report_example.txt"

# Writing report
with open(arq, "w") as file:
    file.write(report)
```

<p align = "justify">
  Open <code>report_example.txt</code>. 
</p>

```bash
    current xi = [2.0, 2.0]
    current xr0 = [1.4, 2.6]
    current xr1 = [3.1, 4.7]
    current xr2 = [3.0, 4.0]
    current x_best = [1.2, 1.2]
    Dimension 0: rij_1 = -0.19999999999999996, rij_2 = 0.10000000000000009, neighbor = 1.8800000000000001
    Dimension 1: rij_1 = -1.4000000000000001, rij_2 = 0.7000000000000002, neighbor = 1.1600000000000001
    update x = [1.8800000000000001, 1.1600000000000001], of = 4.880000000000001, fit = 0.17006802721088432
```
