---
layout: default
title: binomial_crossover
grand_parent: Framework
parent: Genetic Algorithm functions
has_children: false
has_toc: true
nav_order: 207
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>binomial_crossover</h3>
<br>

```python
x_i_new, of_i_new, fit_i_new, neof, report = binomial_crossover(of_function, parent_0, parent_1, p_c, n_dimensions, x_upper, x_lower, none_variable=None)
```

<p align = "justify"></p>

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
       <td>Objective function. The Metapy user defined this function</td>
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
       <td><code>p_c</code></td>
       <td>Crossover probability rate  (% * 0.01)</td>
       <td>Float</td>
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
       <td>Represents the lower limits of the range for the problem variables.</td>
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
from metapy_toolbox import binomial_crossover

# Data
father1 = [4.3, 3.1, 4.8, 3.5, 4.8]
father2 = [3.9, 4.0, 1.6, 1.7, 4.2]
p_c = 0.30
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
xNew, ofNew, fitNew, neof, report = binomial_crossover(objFunction, father1, father2, p_c, nDimensions, xUpper, xLower, noneVariable)

# Output details
print('x new ', xNew)
print('of new ', ofNew)
print('fit new', fitNew)
print('number of evalutions objective function', neof)
```

```bash
x new  [4.3, 3.1, 1.6, 1.7, 4.2]
of new  28.1
fit new 0.034364261168384876
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
    current p0 = [4.3, 3.1, 4.8, 3.5, 4.8]
    current p1 = [3.9, 4.0, 1.6, 1.7, 4.2]
    random number = 0.24575911573158438 < p_c = 0.3
    cut parent_0 -> of_a 4.3
    cut parent_1 -> of_b 3.9
    random number = 0.2597531030020548 < p_c = 0.3
    cut parent_0 -> of_a 3.1
    cut parent_1 -> of_b 4.0
    random number = 0.4561316060102293 >= 0.50
    cut parent_1 -> of_a 1.6
    cut parent_0 -> of_b 4.8
    random number = 0.506621634648928 >= 0.50
    cut parent_1 -> of_a 1.7
    cut parent_0 -> of_b 3.5
    random number = 0.5382296135101402 >= 0.50
    cut parent_1 -> of_a 4.2
    cut parent_0 -> of_b 4.8
    offspring a = [4.3, 3.1, 1.6, 1.7, 4.2], of_a = 28.1
    offspring b = [3.9, 4.0, 4.8, 3.5, 4.8], of_b = 31.21
    update pos = [4.3, 3.1, 1.6, 1.7, 4.2], of = 28.1, fit = 0.034364261168384876

```
