---
layout: default
title: mutation_02_chaos_movement
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
x_i_new, of_i_new,\
    fit_i_new, neof = mutation_02_chaos_movement(obj_function,
                                                    x_i_old, fit_i_old,
                                                    x_lower, x_upper,
                                                    n_dimensions, ch,
                                                    alpha, n_tries,
                                                    iteration, n_iter,
                                                    none_variable=None)
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
        <td>Initial value of chaotic map</td>
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
from metapy_toolbox import mutation_02_chaos_movement # or import *

# Data
xIOLD = [2, 2]
fitIOld = 0.5
xLower = [1, 1]
xUpper = [5, 5]
nDimensions = len(xLower)
ch = 0.80
alpha = 0.5
nTries = 5
iteration = 1
nIter = 10
noneVariable = None

# Objective function
def objFunction(x, _):
    """Example objective function"""
    x0 = x[0]
    x1 = x[1]
    of = x0 ** 2 + x1 ** 2
    return of

# Call function
xNew, ofNew, fitNew, neof, report = mutation_02_chaos_movement(objFunction, xIOLD, fitIOld, xLower, xUpper, nDimensions, ch, alpha, nTries, iteration, nIter, noneVariable)

# Output details
print('x New: ', xNew)
print('of New: ', ofNew)
print('fit New: ', fitNew)
print('number of evalutions objective function: ', neof)
print(report)
```

```bash
x New:  [1.0348175590490112, 1.0348175590490112]
of New:  2.1416947610323076
fit New:  0.31829954087309775
number of evalutions objective function:  5
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
