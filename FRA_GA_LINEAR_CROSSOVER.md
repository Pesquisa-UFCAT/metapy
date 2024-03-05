---
layout: default
title: linear_crossover
grand_parent: Framework
parent: Genetic Algorithm functions
has_children: false
has_toc: false
nav_order: 3
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>linear_crossover</h3>
<br>

<p align = "justify">
    This function is a linear crossover between two individuals (represented by parent_0 and parent_1) in an optimization algorithm.
</p>

```python
xNew, ofNew, fitNew, neOf, reportMove = linear_crossover(objFunction, father1, father2, n_dimensions, xUpper, xLower, noneVariable)
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
       <td><code>of_function</code></td>
       <td>Objective function</td>
       <td>Py function (<code>def</code>)</td>
   </tr>
   <tr>
       <td><code>father_1</code></td>
       <td>First parent</td>
       <td>List</td>
   </tr>
   <tr>
       <td><code>father_2</code></td>
       <td>Second parent</td>
       <td>List</td>
   </tr>  
   <tr>
       <td><code>n_dimensions</code></td>
       <td>Crossover point</td>
       <td>Int</td>
   </tr>   
   <tr>
       <td><code>x_upper</code></td>
       <td>Upper limit of the design variables</td>
       <td>List</td>
   </tr>
   <tr>
       <td><code>x_lower</code></td>
       <td>Lower limit of the design variables</td>
       <td>List</td>
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
       <td>Update variables of the i agent</td>
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
       <td>Int</td>
   </tr>
   <tr>
       <td><code>report</code></td>
       <td>Report about the male movement process</td>
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
from metapy_toolbox import linear_crossover

# Data
father1 = [1, 1, 1, 1, 1]
father2 = [10, 10, 10, 10, 10]
n_dimensions = 5
xUpper = [10, 10, 10, 10, 10]
xLower = [1, 1, 1, 1, 1]
noneVariable = None

# Objective function
def objFunction(x, _):
    """Example objective function"""
    x0 = x[0]
    x1 = x[1]
    of = x0 ** 2 + x1 ** 2
    return of

# Call function
xNew, ofNew, fitNew, neOf, reportMove = linear_crossover(objFunction, father1, father2, n_dimensions, xUpper, xLower, noneVariable)

# Output details
print(xNew)
print(ofNew)
print(fitNew)
print(neOf)
print(reportMove)
```

```bash
[1.0, 1.0, 1.0, 1.0, 1.0]
2.0
0.3333333333333333
3
    Crossover operator - Linear crossover
    current p0 = [1, 1, 1, 1, 1]
    current p1 = [10, 10, 10, 10, 10]
    Dimension 0: alpha_a = 0.5, beta_a = 5.0, neighbor_a = 5.5
    Dimension 0: alpha_b = 1.5, beta_b = 5.0, neighbor_b = -3.5
    Dimension 0: alpha_c = 0.5, beta_c = 15.0, neighbor_c = 14.5
    Dimension 1: alpha_a = 0.5, beta_a = 5.0, neighbor_a = 5.5
    Dimension 1: alpha_b = 1.5, beta_b = 5.0, neighbor_b = -3.5
    Dimension 1: alpha_c = 0.5, beta_c = 15.0, neighbor_c = 14.5
    Dimension 2: alpha_a = 0.5, beta_a = 5.0, neighbor_a = 5.5
    Dimension 2: alpha_b = 1.5, beta_b = 5.0, neighbor_b = -3.5
    Dimension 2: alpha_c = 0.5, beta_c = 15.0, neighbor_c = 14.5
    Dimension 3: alpha_a = 0.5, beta_a = 5.0, neighbor_a = 5.5
    Dimension 3: alpha_b = 1.5, beta_b = 5.0, neighbor_b = -3.5
    Dimension 3: alpha_c = 0.5, beta_c = 15.0, neighbor_c = 14.5
    Dimension 4: alpha_a = 0.5, beta_a = 5.0, neighbor_a = 5.5
    Dimension 4: alpha_b = 1.5, beta_b = 5.0, neighbor_b = -3.5
    Dimension 4: alpha_c = 0.5, beta_c = 15.0, neighbor_c = 14.5
    offspring a = [1.0, 1.0, 1.0, 1.0, 1.0], of_a 2.0
    offspring b = [1.0, 1.0, 1.0, 1.0, 1.0], of_b 2.0
    offspring c = [1.0, 1.0, 1.0, 1.0, 1.0], of_c 2.0
    update x = [1.0, 1.0, 1.0, 1.0, 1.0], of = 2.0, fit = 0.3333333333333333
```
