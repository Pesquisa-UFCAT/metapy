---
layout: default
title: uniform_crossover
grand_parent: Framework
parent: Genetic Algorithm functions
has_children: false
has_toc: true
nav_order: 206
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>uniform_crossover</h3>

<br>

```python
x_i_new, of_i_new, fit_i_new, neof, report = uniform_crossover(of_function, parent_0, parent_1, n_dimensions, x_upper, x_lower, none_variable=None)
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
from metapy_toolbox import uniform_crossover

# Data
father1 = [2.9, 4.3, 1.5, 5.0, 3.5]
father2 = [3.9, 1.2, 2.4, 2.7, 2.7]
nDimensions = len(father1)
xUpper = [5, 5, 5, 5, 5]
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
xNew, ofNew, fitNew, neof, report = uniform_crossover(objFunction, father1, father2, nDimensions, xUpper, xLower, noneVariable)

# Output details
print('x new ', xNew)
print('of new ', ofNew)
print('fit new', fitNew)
print('number of evalutions objective function', neof)
```

```bash
x new  [3.9, 1.2, 1.5, 2.7, 3.5]
of new  16.65
fit new 0.056657223796034
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
    current p0 = [2.9, 4.3, 1.5, 5.0, 3.5]
    current p1 = [3.9, 1.2, 2.4, 2.7, 2.7]
    random number = 0.23851568162300685 < 0.50
    cut parent_0 -> of_a 2.9
    cut parent_1 -> of_b 3.9
    random number = 0.26714707277389294 < 0.50
    cut parent_0 -> of_a 4.3
    cut parent_1 -> of_b 1.2
    random number = 0.7958990231757312 >= 0.50
    cut parent_1 -> of_a 2.4
    cut parent_0 -> of_b 1.5
    random number = 0.15613086364369877 < 0.50
    cut parent_0 -> of_a 5.0
    cut parent_1 -> of_b 2.7
    random number = 0.7254672965043522 >= 0.50
    cut parent_1 -> of_a 2.7
    cut parent_0 -> of_b 3.5
    offspring a = [2.9, 4.3, 2.4, 5.0, 2.7], of_a = 26.9
    offspring b = [3.9, 1.2, 1.5, 2.7, 3.5], of_b = 16.65
    update pos = [3.9, 1.2, 1.5, 2.7, 3.5], of = 16.65, fit = 0.056657223796034
```
