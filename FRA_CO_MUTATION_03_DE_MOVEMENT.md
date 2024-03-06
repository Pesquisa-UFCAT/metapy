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
        <td>Current design variables of the random \(r_0\) agent</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>x_ii_old</code></td>
        <td>Current design variables of the random \(r_1\) agent</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>x_iii_old</code></td>
        <td>Current design variables of the random \(r_2\) agent</td>
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
      Use the <code>mutation_03_de_movement</code> function to generate a new solution from three existing solutions. Use the range \(\mathbf{x}_L = [1.0, 1.0]\) and \(\mathbf{x}_L = [5.0, 5.0]\). Consider  current solutions \(\mathbf{x}_r0 = [2.0, 3.0]\), \(\mathbf{x}_r1 = [4.0, 5.0]\) and \(\mathbf{x}_r2 = [3.6, 2.8]\). Use a scale factor equals 2.0.
  </i>
</p>
```python
# Import 
from metapy_toolbox import mutation_03_de_movement # or import *

# Data
xi = [2.0, 3.0]
xii = [4.0, 5.0]
xiii = [3.6, 2.8]
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
xNew, ofNew, fitNew, neof, report = mutation_03_de_movement(objFunction, xi, xii, xiii, xL, xU, d, f)

# Output details
print('x New: ', xNew) 
print('of New: ', ofNew)
print('fit New: ', fitNew)
print('number of evalutions objective function: ', neof)
```

```bash
x New:  [2.48, 5.0]
of New:  31.1504
fit New:  0.031103812083208913
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
    current x0 = [2, 3]
    current x1 = [4, 5]
    current x2 = [3.6, 2.8]
    Dimension 0: rij = 0.3999999999999999, neighbor = 2.48
    Dimension 1: rij = 2.2, neighbor = 5.640000000000001
    update x = [2.48, 5.0], of = 31.1504, fit = 0.031103812083208913
```
