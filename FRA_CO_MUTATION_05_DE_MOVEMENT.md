---
layout: default
title: mutation_05_de_movement
grand_parent: Framework
parent: Common Library functions
has_toc: false
nav_order: 104
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>mutation_05_de_movement</h3>

<br>

<p align = "justify">
  This function mutates a solution using a differential evolution mutation (best/1).
</p>

```python
x_i_new, of_i_new, fit_i_new, neof, report = mutation_05_de_movement(obj_function, x_r0_old, x_r1_old, x_best, x_lower, x_upper, n_dimensions, f, none_variable)
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
from metapy_toolbox import mutation_05_de_movement # or import *

# Data
xR0 = [2.0, 3.0]
xR1 = [4.0, 5.0]
xBest = [1.5, 1.5]
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

xNew, ofNew, fitNew, neof, report = mutation_05_de_movement(objFunction, xR0, xR1, xBest, xL, xU, d, f)

# Output details

print('x New: ', xNew)
print('of New: ', ofNew)
print('fit New: ', fitNew)
print('number of evalutions objective function: ', neof)
```

```bash
x New:  [1.0, 1.0]
of New:  2.0
fit New:  0.3333333333333333
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
    current xr0 = [2.0, 3.0]
    current xr1 = [4.0, 5.0]
    current x_best = [1.5, 1.5]
    Dimension 0: rij = -2.0, neighbor = -0.8999999999999999
    Dimension 1: rij = -2.0, neighbor = -0.8999999999999999
    update x = [1.0, 1.0], of = 2.0, fit = 0.3333333333333333
```
