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
xNew, ofNew, fitNew, neOf, reportMove = uniform_crossover(objFunction, father1, father2, n_dimensions, xUpper, xLower, noneVariable)
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
       <td>Py function (def)</td>
   </tr> 
   <tr>
       <td><code>parent_0</code></td>
       <td>Represents the first parent for the crossover</td>
       <td>List</td>
   </tr>
   <tr>
       <td><code>parent_1</code></td>
       <td>Represents the second parent for the crossover</td>
       <td>List</td>
   </tr> 
   <tr>     
       <td><code>n_dimensions</code></td>
       <td>Number of dimensions</td>
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
from metapy_toolbox import uniform_crossover

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
    return sum(x)

# Call function
#x_i_new, of_i_new, fit_i_new, neof, report_move = uniform_crossover(obj_function, father_1, father_2, n_dimensions, x_upper, x_lower, none_variable)
xNew, ofNew, fitNew, neof, report = uniform_crossover(objFunction, father1, father2, nDimensions, xUpper, xLower, noneVariable)

# Output details
print('x new ', xNew)
print('of new ', ofNew)
print('fit new', fitNew)
print('number of evalutions objective function', neof)
```

```bash
x new  [1, 10, 10, 1, 1]
of new  23
fit new 0.041666666666666664
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
    Crossover operator - uniform crossover
    current p0 = [1, 1, 1, 1, 1]
    current p1 = [10, 10, 10, 10, 10]
    random number = 0.7199165515530207 >= 0.50
    cut parent_1 -> of_a 10
    cut parent_0 -> of_b 1
    random number = 0.1549652415470777 < 0.50
    cut parent_0 -> of_a 1
    cut parent_1 -> of_b 10
    random number = 0.09435939132671411 < 0.50
    cut parent_0 -> of_a 1
    cut parent_1 -> of_b 10
    random number = 0.6257906862963849 >= 0.50
    cut parent_1 -> of_a 10
    cut parent_0 -> of_b 1
    random number = 0.717497870698087 >= 0.50
    cut parent_1 -> of_a 10
    cut parent_0 -> of_b 1
    offspring a = [10, 1, 1, 10, 10], of_a = 32
    offspring b = [1, 10, 10, 1, 1], of_b = 23
    update pos = [1, 10, 10, 1, 1], of = 23, fit = 0.041666666666666664
```
