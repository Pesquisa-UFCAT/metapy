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
# Import
from metapy_toolbox import mutation_02_chaos_movement # or import *

# Data
x_i_old = [2, 2, 2]
fit_i_old = 0.5
x_lower = [1, 1, 1]
x_upper = [5, 5, 5]
n_dimensions = len(x_lower)
ch = 0.5
alpha = 0.5
n_tries = 10
iteration = 0
n_iter = 10
none_variable = None

# Objective function
def obj_function(x, _):
    """Example objective function"""
    x0 = x[0]
    x1 = x[1]
    of = x0 ** 2 + x1 ** 2
    return of

# Call function
x_i_new, of_i_new, fit_i_new, neof, report = mutation_02_chaos_movement(obj_function, x_i_old, fit_i_old, x_lower, x_upper, n_dimensions, ch, alpha, n_tries, iteration, n_iter, none_variable)

# Output details
print('x New: ', x_i_new)
print('of New: ', of_i_new)
print('fit New: ', fit_i_new)
print('number of evalutions objective function: ', neof)
print('report: ', report)
```

```bash
x New:  [3.1, 3.1, 3.1, 1.45, 1.45, 1.45]
of New:  19.220000000000002
fit New:  0.04945598417408506
number of evalutions objective function:  10
report:      Try 0 fit best = 0.5
    Dimension 0: epsilon = 1.1, ch = 3.0, neighbor = 3.1
    Dimension 1: epsilon = 1.1, ch = 3.0, neighbor = 3.1
    Dimension 2: epsilon = 1.1, ch = 3.0, neighbor = 3.1
    temporary move x = [3.1, 3.1, 3.1], of = 19.220000000000002, fit = 0.04945598417408506
    fit_i_temp < fit_pop[pop] - not accept this solution
    Try 1 fit best = 0.0
    Dimension 0: epsilon = 1.1, ch = 1.5, neighbor = 1.45
    Dimension 1: epsilon = 1.1, ch = 1.5, neighbor = 1.45
    Dimension 2: epsilon = 1.1, ch = 1.5, neighbor = 1.45
    temporary move x = [3.1, 3.1, 3.1, 1.45, 1.45, 1.45], of = 19.220000000000002, fit = 0.04945598417408506
    fit_i_temp > fit_pop[pop] - accept this solution
    update x = [3.1, 3.1, 3.1, 1.45, 1.45, 1.45], of = 19.220000000000002, fit = 0.04945598417408506
    Try 2 fit best = 0.04945598417408506
    Dimension 0: epsilon = 1.1, ch = 1.21875, neighbor = 1.140625
    Dimension 1: epsilon = 1.1, ch = 1.21875, neighbor = 1.140625
    Dimension 2: epsilon = 1.1, ch = 1.21875, neighbor = 1.140625
    temporary move x = [3.1, 3.1, 3.1, 1.45, 1.45, 1.45, 1.140625, 1.140625, 1.140625], of = 19.220000000000002, fit = 0.04945598417408506
    fit_i_temp < fit_pop[pop] - not accept this solution
    Try 3 fit best = 0.04945598417408506
    Dimension 0: epsilon = 1.1, ch = 1.1033935546875, neighbor = 1.01373291015625
    Dimension 1: epsilon = 1.1, ch = 1.1033935546875, neighbor = 1.01373291015625
    Dimension 2: epsilon = 1.1, ch = 1.1033935546875, neighbor = 1.01373291015625
    temporary move x = [3.1, 3.1, 3.1, 1.45, 1.45, 1.45, 1.140625, 1.140625, 1.140625, 1.01373291015625, 1.01373291015625, 1.01373291015625], of = 19.220000000000002, fit = 0.04945598417408506
    fit_i_temp < fit_pop[pop] - not accept this solution
    Try 4 fit best = 0.04945598417408506
    Dimension 0: epsilon = 1.1, ch = 1.0503604989498854, neighbor = 0.9553965488448739
    Dimension 1: epsilon = 1.1, ch = 1.0503604989498854, neighbor = 0.9553965488448739
    Dimension 2: epsilon = 1.1, ch = 1.0503604989498854, neighbor = 0.9553965488448739
    temporary move x = [3.1, 3.1, 3.1, 1.45, 1.45, 1.45, 1.140625, 1.140625, 1.140625, 1.01373291015625, 1.01373291015625, 1.01373291015625, 1.0, 1.0, 1.0], of = 19.220000000000002, fit = 0.04945598417408506
    fit_i_temp < fit_pop[pop] - not accept this solution
    Try 5 fit best = 0.04945598417408506
    Dimension 0: epsilon = 1.1, ch = 1.0248632269931326, neighbor = 0.9273495496924458
    Dimension 1: epsilon = 1.1, ch = 1.0248632269931326, neighbor = 0.9273495496924458
    Dimension 2: epsilon = 1.1, ch = 1.0248632269931326, neighbor = 0.9273495496924458
    temporary move x = [3.1, 3.1, 3.1, 1.45, 1.45, 1.45, 1.140625, 1.140625, 1.140625, 1.01373291015625, 1.01373291015625, 1.01373291015625, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], of = 19.220000000000002, fit = 0.04945598417408506
    fit_i_temp < fit_pop[pop] - not accept this solution
    Try 6 fit best = 0.04945598417408506
    Dimension 0: epsilon = 1.1, ch = 1.0123543409895022, neighbor = 0.9135897750884523
    Dimension 1: epsilon = 1.1, ch = 1.0123543409895022, neighbor = 0.9135897750884523
    Dimension 2: epsilon = 1.1, ch = 1.0123543409895022, neighbor = 0.9135897750884523
...
    Dimension 2: epsilon = 1.1, ch = 1.0015359713939909, neighbor = 0.9016895685333899
    temporary move x = [3.1, 3.1, 3.1, 1.45, 1.45, 1.45, 1.140625, 1.140625, 1.140625, 1.01373291015625, 1.01373291015625, 1.01373291015625, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], of = 19.220000000000002, fit = 0.04945598417408506
    fit_i_temp < fit_pop[pop] - not accept this solution
```
