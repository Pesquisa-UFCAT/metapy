---
layout: default
title: mutation_03_movement
grand_parent: Framework
parent: Common Library functions
has_toc: false
nav_order: 8
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>mutation_02_chaos_movement</h3>

<br>

<p align = "justify">
  This function mutates a solution using a Chaotic maps.
</p>

```python
x_i_new, of_i_new, fit_i_new, neof = mutation_01_movement(obj_function, x_i_old,
                 x_lower, x_upper, n_dimensions, pdf, cov, none_variable=None)
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
        <td>Current design variables of the i agent</td>
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
        <td>Probability density function. Options: <code>'gaussian'</code> or <code>'uniform'</code></td>
        <td>String</td>
    </tr>
    <tr>
        <td><code>cov</code></td>
        <td>Coefficient of variation in percentage</td>
        <td>Float</td>
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

Theory
{: .label .label-red }

<p align = "justify">
    See Hill Climbing <a href="https://wmpjrufg.github.io/METAPY/FRA_ALG_HILL_01.html" target="_blank">movement</a>.
</p>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
      Use the <code>mutation_01_movement</code> function to generate a new solution from an existing solution, applying a coefficient of variation of 15% in current design variables. Use the range \(\mathbf{x}_L = [1.0, 1.0, 1.0]\) and \(\mathbf{x}_L = [3.0, 3.0, 3.0]\). Consider current solution \(\mathbf{x}_i = [2.0, 2.0, 2.0]\). Use a uniform distribution to generate.
  </i>
</p>

```python
# Data
xL = [1, 1]
xU = [5, 5]
d = len(xL)
cov = 15 # 15%
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
xII, ofINew, fitINew, neof, report = mutation_01_movement(obj_function, xI, xL, xU,
                                                          d, pdf, cov)

# Output details
print('x New: ', xII)
print('of New: ', ofINew)
print('fit New: ', fitINew)
print('number of evalutions objective function: ', neof)
```

```bash
x New:  [1.7076684887543652, 1.992422964391923]
of New:  6.885880936520915
fit New:  0.12680891431784397
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
    Particle movement
    Dimension 0: mean = 2, sigma = 0.3 neighbor = 1.7076684887543652
    Dimension 1: mean = 2, sigma = 0.3 neighbor = 1.992422964391923
    update x = [1.7076684887543652, 1.992422964391923], of = 6.885880936520915, fit = 0.12680891431784397
```
