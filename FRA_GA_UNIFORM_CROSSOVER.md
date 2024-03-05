---
layout: default
title: uniform_crossover
grand_parent: Framework
parent: Genetic Algorithm functions
has_children: false
has_toc: true
nav_order: 7
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>uniform_crossover</h3>

<br>

```python
uniform_crossover(my_obj_function, father_1, father_2, n_dimensions, x_upper, x_lower, none_variable)
```

<p align = "justify">
    Uniform crossover operator.
</p>

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
       <td>Is the objective function that will be used to evaluate the result of the crossover</td>
       <td>Py function</td>
   </tr> 
   <tr>
       <td><code>father_1</code></td>
       <td>Represents the first parent for the crossover</td>
       <td>List</td>
   </tr>
   <tr>
       <td><code>father_2</code></td>
       <td>Represents the second parent for the crossover</td>
       <td>List</td>
   </tr> 
   <tr>
       <td><code>n_dimensions</code></td>
       <td> number of dimensions</td>
       <td>Float</td>
   </tr>   
    <tr>
       <td><code>x_upper</code></td>
       <td>Upper limit of the design variables.</td>
       <td>List</td>
   </tr> 
   <tr>
       <td><code>x_lower</code></td>
       <td>Lower limit of the design variables.</td>
       <td>List</td>
   </tr>
      <tr>
       <td><code>none_variable</code></td>
       <td>None variable. Default is None. Use in objective function</td>
       <td>Object  or None</td>
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
       <td>Update variables of the i agent.</td>
       <td>List</td>
   </tr>
   <tr>
       <td><code>of_i_new</code></td>
       <td>Update objective function value of the i agent.</td>
       <td>Float</td>
   </tr>
   <tr>
       <td><code>fit_i_new</code></td>
       <td>Update fitness value of the i agent.</td>
       <td>Float</td>
   </tr>
   <tr>
       <td><code>neof</code></td>
       <td>Number of evaluations of the objective function.</td>
       <td>Int</td>
   </tr>
    <tr>
       <td><code>report_move</code></td>
       <td>Report about the male moviment process.</td>
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
from metapy_toolbox import uniform_crossover

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
xNew, ofNew, fitNew, neOf, reportMove = uniform_crossover(objFunction, father1, father2, n_dimensions, xUpper, xLower, noneVariable)

# Output details
print(xNew)
print(ofNew)
print(fitNew)
print(neOf)
print(reportMove)
```

```bash
[10, 1, 10, 1, 1]
101
0.00980392156862745
2
    Crossover operator - uniform crossover
    current p0 = [1, 1, 1, 1, 1]
    current p1 = [10, 10, 10, 10, 10]
    random number = 0.7478519274262806 >= 0.50
    cut parent_1 -> of_a 10
    cut parent_0 -> of_b 1
    random number = 0.20080697224913402 < 0.50
    cut parent_0 -> of_a 1
    cut parent_1 -> of_b 10
    random number = 0.7940691407555555 >= 0.50
    cut parent_1 -> of_a 10
    cut parent_0 -> of_b 1
    random number = 0.10942639168077117 < 0.50
    cut parent_0 -> of_a 1
    cut parent_1 -> of_b 10
    random number = 0.10578989658759796 < 0.50
    cut parent_0 -> of_a 1
    cut parent_1 -> of_b 10
    offspring a = [10, 1, 10, 1, 1], of_a = 101
    offspring b = [1, 10, 1, 10, 10], of_b = 101
    update pos = [10, 1, 10, 1, 1], of = 101, fit = 0.00980392156862745
```
