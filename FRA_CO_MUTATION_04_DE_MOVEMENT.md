---
layout: default
title: mutation_04_de_movement
grand_parent: Framework
parent: Common Library functions
has_toc: false
nav_order: 103
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>mutation_04_de_movement</h3>

<br>

<p align = "justify">
  This function mutates a solution using a differential evolution mutation rand/1.
</p>

```python

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
        <td><code>x_r2_old</code></td>
        <td>Current design variables of the random \(r_2\) agent</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>x_r3_old</code></td>
        <td>Current design variables of the random \(r_3\) agent</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>x_r4_old</code></td>
        <td>Current design variables of the random \(r_4\) agent</td>
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
from metapy_toolbox import mutation_04_de_movement # or import *

# Data

xR0 = [2.0, 3.0]
xR1 = [4.0, 5.0]
xR2 = [3.6, 2.8]
xR3 = [3.0, 4.0]
xR4 = [2.6, 3.7]
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

xNew, ofNew, fitNew, neof, report = mutation_04_de_movement(objFunction, xR0, xR1, xR2, xR3, xR4, xL, xU, d, f)

# Output details

print('x New: ', xNew)
print('of New: ', ofNew)
print('fit New: ', fitNew)
print('number of evalutions objective function: ', neof)
```

```bash
x New:  [2.96, 5.0]
of New:  33.7616
fit New:  0.028767375494798856
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
    current xr2 = [3.6, 2.8]
    current xr3 = [3.0, 4.0]
    current xr4 = [2.6, 3.7]
    Dimension 0: rij_1 = 0.3999999999999999, rij_2 = 0.3999999999999999, neighbor = 2.96
    Dimension 1: rij_1 = 2.2, rij_2 = 0.2999999999999998, neighbor = 6.0
    update x = [2.96, 5.0], of = 33.7616, fit = 0.028767375494798856
```
