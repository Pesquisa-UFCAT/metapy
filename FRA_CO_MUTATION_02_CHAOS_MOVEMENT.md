---
layout: default
title: mutation_02_chaos_movement
grand_parent: Framework
parent: Common Library functions
has_toc: false
nav_order: 101
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
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>alpha</code></td>
        <td>Chaotic map control parameter</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>n_tries</code></td>
        <td>Number of tries to find a better solution</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>iteration</code></td>
        <td>Current iteration number</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>n_iter</code></td>
        <td>Number of iterations</td>
        <td>Integer</td>
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
      Use the <code>mutation_02_chaos_movement</code> function to generate a new solution from an existing solution. Use the range \(\mathbf{x}_L = [1.0, 1.0]\) and \(\mathbf{x}_L = [5.0, 5.0]\). Consider current solution \(\mathbf{x}_i = [2.0, 2.0]\). Use a \(\alpha = 4\) to control the chaotic map. The total iterations optimization method is 10, and the current iteration is 1.
  </i>
</p>

```python
# Import
from metapy_toolbox import mutation_02_chaos_movement, fit_value # or import *

# Data
xI = [2, 2]
xL = [1, 1]
xU = [5, 5]
d = len(xL)
alpha = 4
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

# OF and fit value
ofI = objFunction(xI, None)
fitI = fit_value(ofI)

# Call function
xNew, ofNew, fitNew, neof, report = mutation_02_chaos_movement(objFunction, xI, fitI, xL, xU, d, alpha, nTries, iteration, nIter)

# Output details
print('x New: ', xNew)
print('of New: ', ofNew)
print('fit New: ', fitNew)
print('number of evalutions objective function: ', neof)
```

```bash
x New:  [1.9506356875187332, 1.9506356875187332]
of New:  7.609959170843362
fit New:  0.11614456934782981
number of evalutions objective function:  5
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
    Try 0 -> current x = [2, 2], fit best = 0.1111111111111111
    Dimension 0: epsilon = 1.0, ch = 0.08857213820471488, chaos value = 1.3542885528188595, neighbor = 1.3542885528188595
    Dimension 1: epsilon = 1.0, ch = 0.08857213820471488, chaos value = 1.3542885528188595, neighbor = 1.3542885528188595
    temporary move x = [1.3542885528188595, 1.3542885528188595], of = 3.6681949685924016, fit = 0.2142155601314847
    fit_i_temp 0.2142155601314847 > fit_pop[pop] 0.1111111111111111 - accept this solution
    update x = [1.3542885528188595, 1.3542885528188595], of = 3.6681949685924016, fit = 0.2142155601314847
    Try 1 -> current x = [1.3542885528188595, 1.3542885528188595], fit best = 0.2142155601314847
    Dimension 0: epsilon = 1.0, ch = 0.3229084581542391, chaos value = 2.2916338326169563, neighbor = 2.2916338326169563
    Dimension 1: epsilon = 1.0, ch = 0.3229084581542391, chaos value = 2.2916338326169563, neighbor = 2.2916338326169563
    temporary move x = [2.2916338326169563, 2.2916338326169563], of = 10.50317124558936, fit = 0.08693254917711742
    fit_i_temp 0.08693254917711742 < fit_pop[pop] 0.2142155601314847 - not accept this solution
    update x = [1.3542885528188595, 1.3542885528188595], of = 3.6681949685924016, fit = 0.2142155601314847
    Try 2 -> current x = [1.3542885528188595, 1.3542885528188595], fit best = 0.2142155601314847
    Dimension 0: epsilon = 1.0, ch = 0.8745543432267644, chaos value = 4.498217372907058, neighbor = 4.498217372907058
    Dimension 1: epsilon = 1.0, ch = 0.8745543432267644, chaos value = 4.498217372907058, neighbor = 4.498217372907058
    temporary move x = [4.498217372907058, 4.498217372907058], of = 40.46791906784574, fit = 0.024115027290467557
    fit_i_temp 0.024115027290467557 < fit_pop[pop] 0.2142155601314847 - not accept this solution
    update x = [1.3542885528188595, 1.3542885528188595], of = 3.6681949685924016, fit = 0.2142155601314847
    Try 3 -> current x = [1.3542885528188595, 1.3542885528188595], fit best = 0.2142155601314847
    Dimension 0: epsilon = 1.0, ch = 0.4388361758798687, chaos value = 2.7553447035194747, neighbor = 2.7553447035194747
    Dimension 1: epsilon = 1.0, ch = 0.4388361758798687, chaos value = 2.7553447035194747, neighbor = 2.7553447035194747
    temporary move x = [2.7553447035194747, 2.7553447035194747], of = 15.183848870425644, fit = 0.06178999865893456
    fit_i_temp 0.06178999865893456 < fit_pop[pop] 0.2142155601314847 - not accept this solution
    update x = [1.3542885528188595, 1.3542885528188595], of = 3.6681949685924016, fit = 0.2142155601314847
    Try 4 -> current x = [1.3542885528188595, 1.3542885528188595], fit best = 0.2142155601314847
    Dimension 0: epsilon = 1.0, ch = 0.9850359464760066, chaos value = 4.940143785904026, neighbor = 4.940143785904026
    Dimension 1: epsilon = 1.0, ch = 0.9850359464760066, chaos value = 4.940143785904026, neighbor = 4.940143785904026
    temporary move x = [4.940143785904026, 4.940143785904026], of = 48.81004125081233, fit = 0.020076273275194113
    fit_i_temp 0.020076273275194113 < fit_pop[pop] 0.2142155601314847 - not accept this solution
    update x = [1.3542885528188595, 1.3542885528188595], of = 3.6681949685924016, fit = 0.2142155601314847
```
