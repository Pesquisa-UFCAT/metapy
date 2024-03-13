---
layout: default
title: mutation_01_hill_movement
grand_parent: Framework
parent: Common Library functions
has_toc: false
nav_order: 100
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>mutation_01_hill_movement</h3>

<br>

<p align = "justify">
  This function mutates a solution using a Gaussian or Uniform distribution. Hill Climbing movement.
</p>

```python
x_i_new, of_i_new,\
    fit_i_new, neof = mutation_01_hill_movement(obj_function, x_i_old,
                                                    x_lower, x_upper,
                                                    n_dimensions,
                                                    pdf, cov,
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
        <td><code>pdf</code></td>
        <td>Probability density function used in random generator. Options: 'gaussian' or 'uniform'</td>
        <td>String</td>
    </tr>
    <tr>
        <td><code>cov</code></td>
        <td>Coefficient of variation in percentage</td>
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
        <td>Update objective function value of the i agent</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>fit_i_new</code></td>
        <td>Update fitness value of the i agent</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>neof</code></td>
        <td>Number of evaluations of the objective function</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>report</code></td>
        <td>Report about the mutation process</td>
        <td>String</td>
    </tr>
</table>

<h3>Theory</h3>

<p align = "justify">
    See Hill Climbing <a href="https://wmpjrufg.github.io/METAPY/LEARN_PROB_HILL.html" target="_blank">movement</a>.
</p>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
      Use the <code>mutation_01_hill_movement</code> function to generate a new solution from an existing solution, applying a coefficient of variation of 15% in current design variables. Use the range \(\mathbf{x}_L = [1.0, 1.0]\) and \(\mathbf{x}_L = [5.0, 5.0]\). Consider current solution \(\mathbf{x}_i = [2.0, 2.0]\). Use a uniform distribution to generate.
  </i>
</p>

```python
# Import
from metapy_toolbox import mutation_01_hill_movement # or import *

# Data
xL = [1, 1]
xU = [5, 5]
d = len(xL)
sigma = 15 # 15%
xI = [2, 2]
pdf = 'uniform'

# Objective function
def obj_function(x, _):
    """Example objective function"""
    x0 = x[0]
    x1 = x[1]
    of = x0 ** 2 + x1 ** 2
    return of

# Call function
xII, ofINew, fitINew, neof, report = mutation_01_hill_movement(obj_function, xI, xL, xU,
                                                               d, pdf, sigma)

# Output details
print('x New: ', xII)
print('of New: ', ofINew)
print('fit New: ', fitINew)
print('number of evalutions objective function: ', neof)
```

```bash
x New:  [2.2555966876941307, 2.1080630093627852]
of New:  9.531646068980415
fit New:  0.09495191857475814
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
    current x = [2, 2]
    Dimension 0: mean = 2, sigma = 0.3, neighbor = 2.2555966876941307
    Dimension 1: mean = 2, sigma = 0.3, neighbor = 2.1080630093627852
    update x = [2.2555966876941307, 2.1080630093627852], of = 9.531646068980415, fit = 0.09495191857475814
```
