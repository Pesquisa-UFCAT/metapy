---
layout: default
title: linear_crossover
grand_parent: Framework
parent: Genetic Algorithm functions
has_children: false
has_toc: false
nav_order: 200
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
x_i_new, of_i_new, fit_i_new, neof, report = linear_crossover(of_function, parent_0, parent_1, n_dimensions, x_upper, x_lower, none_variable=None)
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
       <td>Py function (def)</td>
   </tr>
   <tr>
       <td><code>parent_0</code></td>
       <td>First parent</td>
       <td>List</td>
   </tr>
   <tr>
       <td><code>parent_1</code></td>
       <td>Second parent</td>
       <td>List</td>
   </tr>  
   <tr>
       <td><code>n_dimensions</code></td>
       <td>Crossover point</td>
       <td>Integer</td>
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
       <td>None, List, Float, Dictionary, String or any</td>
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
       <td>Integer</td>
   </tr>
   <tr>
       <td><code>report</code></td>
       <td>Report about the crossover process</td>
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
father1 = [1.2, 1.4, 2.5, 4.8, 2.4]
father2 = [2.3, 1.5, 3.5, 4.8, 2.4]
nDimensions = len(father1)
xUpper = [5, 5, 5, 5, 5]
xLower = [1, 1, 1, 1, 1]
noneVariable = None

def objFunction(x, _):
    """Example objective function"""
    x0 = x[0]
    x1 = x[1]
    of = x0 ** 2 + x1 ** 2
    return of

# Call function
xNew, ofNew, fitNew, neof, report = linear_crossover(objFunction, father1, father2, nDimensions, xUpper, xLower, noneVariable)

# Output details
print('x new ', xNew)
print('of new ', ofNew)
print('fit new', fitNew)
print('number of evalutions objective function', neof)
```

```bash
x new  [1.0, 1.0, 1.0, 1.0, 1.0]
of new  2.0
fit new 0.3333333333333333
number of evalutions objective function 3
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
    Crossover operator - Linear crossover
    current p0 = [1.2, 1.4, 2.5, 4.8, 2.4]
    current p1 = [2.3, 1.5, 3.5, 4.8, 2.4]
    Dimension 0: alpha_a = 0.6, beta_a = 1.15, neighbor_a = 1.75
    Dimension 0: alpha_b = 1.7999999999999998, beta_b = 1.15, neighbor_b = 0.6499999999999999
    Dimension 0: alpha_c = 0.6, beta_c = 3.4499999999999997, neighbor_c = 2.8499999999999996
    Dimension 1: alpha_a = 0.7, beta_a = 0.75, neighbor_a = 1.45
    Dimension 1: alpha_b = 2.0999999999999996, beta_b = 0.75, neighbor_b = 1.3499999999999996
    Dimension 1: alpha_c = 0.7, beta_c = 2.25, neighbor_c = 1.55
    Dimension 2: alpha_a = 1.25, beta_a = 1.75, neighbor_a = 3.0
    Dimension 2: alpha_b = 3.75, beta_b = 1.75, neighbor_b = 2.0
    Dimension 2: alpha_c = 1.25, beta_c = 5.25, neighbor_c = 4.0
    Dimension 3: alpha_a = 2.4, beta_a = 2.4, neighbor_a = 4.8
    Dimension 3: alpha_b = 7.199999999999999, beta_b = 2.4, neighbor_b = 4.799999999999999
    Dimension 3: alpha_c = 2.4, beta_c = 7.199999999999999, neighbor_c = 4.799999999999999
    Dimension 4: alpha_a = 1.2, beta_a = 1.2, neighbor_a = 2.4
    Dimension 4: alpha_b = 3.5999999999999996, beta_b = 1.2, neighbor_b = 2.3999999999999995
    Dimension 4: alpha_c = 1.2, beta_c = 3.5999999999999996, neighbor_c = 2.3999999999999995
    offspring a = [1.0, 1.0, 1.0, 1.0, 1.0], of_a 2.0
    offspring b = [1.0, 1.0, 1.0, 1.0, 1.0], of_b 2.0
    offspring c = [1.0, 1.0, 1.0, 1.0, 1.0], of_c 2.0
    update x = [1.0, 1.0, 1.0, 1.0, 1.0], of = 2.0, fit = 0.3333333333333333
```
