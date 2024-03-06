---
layout: default
title: single_point_crossover
grand_parent: Framework
parent: Genetic Algorithm functions
has_children: false
has_toc: true
nav_order: 6
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>single_point_crossover</h3>

<br>

<p align = "justify">
    Single point crossover operator.
</p>

```python
xNew, ofNew, fitNew, neOf, reportMove = single_point_crossover(objFunction, father1, father2, nDimensions, xUpper, xLower, noneVariable)
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
       <td>Integer</td>
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
       <td>Integer</td>
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
from metapy_toolbox import single_point_crossover

# Data
father1 = [1, 1, 1, 1, 1]
father2 = [10, 10, 10, 10, 10]
nDimensions = len(father1)
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
xNew, ofNew, fitNew, neOf, reportMove = single_point_crossover(objFunction, father1, father2, nDimensions, xUpper, xLower, noneVariable)

# Output details
print(xNew)
print(ofNew)
print(fitNew)
print(neOf)
print(reportMove)
```

```bash
[1, 1, 10, 10, 10]
2
0.3333333333333333
2
    Crossover operator - Single point
    current p0 = [1, 1, 1, 1, 1]
    current p1 = [10, 10, 10, 10, 10]
    cut position 2
    cut parent_0 -> of_a [1, 1]
    cut parent_1 -> of_a [10, 10, 10]
    cut parent_1 -> of_b [10, 10]
    cut parent_0 -> of_b [1, 1, 1]
    offspring a = [1, 1, 10, 10, 10], of_a = 2
    offspring b = [10, 10, 1, 1, 1], of_b = 200
    update n_dimensions = [1, 1, 10, 10, 10], of = 2, fit = 0.3333333333333333
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

```
