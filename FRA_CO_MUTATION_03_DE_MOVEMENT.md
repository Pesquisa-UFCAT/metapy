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
xIOLD = [2, 2]
xIIOLD = [3, 3]
xIIIOLD = [4, 4]
xLower = [1, 1]
xUpper = [5, 5]
nDimensions = len(xLower)
f = 1.2
noneVariable = None


# Objective function
def objFunction(x, _):
    """Example objective function"""
    x0 = x[0]
    x1 = x[1]
    of = x0 ** 2 + x1 ** 2
    return of

# Call function
xNew, ofNew, fitNew, neof, report = mutation_03_de_movement(objFunction, xIOLD, xIIOLD, xIIIOLD, xLower, xUpper, nDimensions, f, noneVariable)

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
    Try 0 fit best = 0.5
    Dimension 0: epsilon = 1.0, ch = 4.2, neighbor = 4.2
    Dimension 1: epsilon = 1.0, ch = 4.2, neighbor = 4.2
    temporary move x = [4.2, 4.2], of = 35.28, fit = 0.027563395810363836
    fit_i_temp 0.027563395810363836 < fit_pop[pop] 0.5 - not accept this solution
    Try 1 fit best = -1000
    Dimension 0: epsilon = 1.0, ch = 1.3199999999999998, neighbor = 1.3199999999999998
    Dimension 1: epsilon = 1.0, ch = 1.3199999999999998, neighbor = 1.3199999999999998
    temporary move x = [1.3199999999999998, 1.3199999999999998], of = 3.484799999999999, fit = 0.2229753835176597
    fit_i_temp 0.2229753835176597 > fit_pop[pop] -1000 - accept this solution
    update x = [1.3199999999999998, 1.3199999999999998], of = 3.484799999999999, fit = 0.2229753835176597
    Try 2 fit best = 0.2229753835176597
    Dimension 0: epsilon = 1.0, ch = 1.1472, neighbor = 1.1472
    Dimension 1: epsilon = 1.0, ch = 1.1472, neighbor = 1.1472
    temporary move x = [1.1472, 1.1472], of = 2.63213568, fit = 0.27532011138967144
    fit_i_temp 0.27532011138967144 > fit_pop[pop] 0.2229753835176597 - accept this solution
    update x = [1.1472, 1.1472], of = 2.63213568, fit = 0.27532011138967144
    Try 3 fit best = 0.27532011138967144
    Dimension 0: epsilon = 1.0, ch = 1.07089152, neighbor = 1.07089152
    Dimension 1: epsilon = 1.0, ch = 1.07089152, neighbor = 1.07089152
    temporary move x = [1.07089152, 1.07089152], of = 2.293617295215821, fit = 0.3036175458067216
    fit_i_temp 0.3036175458067216 > fit_pop[pop] 0.27532011138967144 - accept this solution
    update x = [1.07089152, 1.07089152], of = 2.293617295215821, fit = 0.3036175458067216
    Try 4 fit best = 0.3036175458067216
    Dimension 0: epsilon = 1.0, ch = 1.0348175590490112, neighbor = 1.0348175590490112
    Dimension 1: epsilon = 1.0, ch = 1.0348175590490112, neighbor = 1.0348175590490112
    temporary move x = [1.0348175590490112, 1.0348175590490112], of = 2.1416947610323076, fit = 0.31829954087309775
    fit_i_temp 0.31829954087309775 > fit_pop[pop] 0.3036175458067216 - accept this solution
    update x = [1.0348175590490112, 1.0348175590490112], of = 2.1416947610323076, fit = 0.31829954087309775
```
