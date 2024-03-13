---
layout: default
title: arithmetic_crossover
grand_parent: Framework
parent: Genetic Algorithm functions
has_children: false
has_toc: true
nav_order: 204
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>arithmetic_crossover</h3>
<br>

```python
x_i_new, of_i_new, fit_i_new, neof, report = arithmetic_crossover(of_function, parent_0, parent_1, n_dimensions, x_upper, x_lower, none_variable=None)
```

<p align = "justify">
This function performs the arithmetic crossover operator. Two new points are generated from the two parent points (offspring).
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
       <td>Objective function</td>
       <td>Py function (def)</td>
   </tr> 
   <tr>
       <td><code>parent_0</code></td>
       <td>Current design variables of the first parent</td>
       <td>List</td>
   </tr>
   <tr>
       <td><code>parent_1</code></td>
       <td>Current design variables of the second parent</td>
       <td>List</td>
   </tr> 
   <tr>
       <td><code>n_dimensions</code></td>
       <td>Problem dimension</td>
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
       <td>L'ist</td>
   </tr>
   <tr>
       <td><code>of_i_new</code></td>
       <td> Update objective function value of the i agent</td>
       <td>Float</td>
   </tr>
   <tr>
       <td><code>fit_i_new</code></td>
       <td>Update fitness value of the i agent</td>
       <td>Float</td>
   </tr>
   <tr>
       <td><code>neof</code></td>
       <td>New solution indicator. It is a Boolean value (1 to indicate a new solution)</td>
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
from metapy_toolbox import arithmetic_crossover

# Data
father1 = [2.0, 1.5, 1.6, 3.7, 3.4]
father2 = [2.6, 4.9, 1.9, 3.2, 2.9]
alpha = 0.5
nDimensions = len(father1)
xUpper = [5, 5, 5, 5, 5]
xLower = [2, 2, 2, 2, 2]
noneVariable = None

# Objective function
def objFunction(x, _):
    """Example objective function"""
    x0 = x[0]
    x1 = x[1]
    of = x0 ** 2 + x1 ** 2
    return of

# Call function
xNew, ofNew, fitNew, neof, report = arithmetic_crossover(objFunction, father1, father2, nDimensions, xUpper, xLower, noneVariable)

# Output details
print('x new ', xNew)
print('of new ', ofNew)
print('fit new', fitNew)
print('number of evalutions objective function', neof)
```

```bash
x new  [2.099209543646729, 3.1226423497299867, 2.0, 3.5158093202927043, 3.0300633766390743]
of new  14.157575952464722
fit new 0.06597360970752011
number of evalutions objective function 2
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
    Crossover operator - Arithmetic crossover
    current p0 = [2.0, 1.5, 1.6, 3.7, 3.4]
    current p1 = [2.6, 4.9, 1.9, 3.2, 2.9]
    neighbor_a = 2.099209543646729, neighbor_b = 2.500790456353271
    neighbor_a = 3.1226423497299867, neighbor_b = 3.2773576502700137
    neighbor_a = 1.8636934930092481, neighbor_b = 1.6363065069907519
    neighbor_a = 3.5158093202927043, neighbor_b = 3.384190679707296
    neighbor_a = 3.0300633766390743, neighbor_b = 3.2699366233609255
    offspring a = [2.099209543646729, 3.1226423497299867, 2.0, 3.5158093202927043, 3.0300633766390743], of_a = 14.157575952464722
    offspring b = [2.500790456353271, 3.2773576502700137, 2.0, 3.384190679707296, 3.2699366233609255], of_b = 16.995026074370987
    update pos = [2.099209543646729, 3.1226423497299867, 2.0, 3.5158093202927043, 3.0300633766390743], of = 14.157575952464722, fit = 0.06597360970752011

```
