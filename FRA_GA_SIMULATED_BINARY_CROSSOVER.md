---
layout: default
title: simulated_binary_crossover
grand_parent: Framework
parent: Genetic Algorithm functions
has_children: false
has_toc: true
nav_order: 203
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>simulated_binary_crossover</h3>
<br>

```python
xNew, ofNew, fitNew, neof, report = simulated_binary_crossover(objFunction, father1, father2, eta_c, nDimensions, xUpper, xLower, noneVariable)
```

<p align = "justify">
This function performs the simulated binary crossover operator. Two new points are generated from the two parent points (offspring).</p>

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
       <td><code>eta_c</code></td>
       <td>Distribution index</td>
       <td>List</td>
   </tr>
   <tr>
       <td><code>n_dimensions</code></td>
       <td>Problem dimension</td>
       <td>Integer</td>
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
from metapy_toolbox import simulated_binary_crossover

# Data
father1 = [1, 1, 1, 1, 1]
father2 = [10, 10, 10, 10, 10]
eta_c = 0.30
nDimensions = len(father1)
xUpper = [10, 10, 10, 10, 10]
xLower = [1, 1, 1, 1, 1]
noneVariable = None

# Objective function
def objFunction(x, _):
    """Example objective function"""
    return sum(x)

# Call function
xNew, ofNew, fitNew, neof, report = simulated_binary_crossover(objFunction, father1, father2, eta_c, nDimensions, xUpper, xLower, noneVariable)

# Output details
print('x new ', xNew)
print('of new ', ofNew)
print('fit new', fitNew)
print('number of evalutions objective function', neof)
```

```bash
x new  [1.0, 1.0, 1.0, 1.0, 2.731940424514889]
of new  6.731940424514889
fit new 0.12933364008204204
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
    Crossover operator - simulated binary crossover
    current p0 = [1, 1, 1, 1, 1]
    current p1 = [10, 10, 10, 10, 10]
    random number = 0.5576541499991551 > 0.50, beta = 1.0988268604398106
    neighbor_a 0.5552791280208524
    neighbor_b 0.5552791280208524
    random number = 0.5974221402308133 > 0.50, beta = 1.1814084981062363
    neighbor_a 0.1836617585219369
    neighbor_b 0.1836617585219369
    random number = 0.6769307747448554 > 0.50, beta = 1.3992760328161298
    neighbor_a -0.796742147672584
    neighbor_b -0.796742147672584
    random number = 0.6120755210924433 > 0.50, beta = 1.215589062507092
    neighbor_a 0.0298492187180861
    neighbor_b 0.0298492187180861
    random number = 0.2658409004451048 <= 0.50, beta = 0.6151243501078025
    neighbor_a 2.731940424514889
    neighbor_b 2.731940424514889
    offspring a = [1.0, 1.0, 1.0, 1.0, 2.731940424514889], of_a = 6.731940424514889
    offspring b = [1.0, 1.0, 1.0, 1.0, 2.731940424514889], of_b = 6.731940424514889
    update pos = [1.0, 1.0, 1.0, 1.0, 2.731940424514889], of = 6.731940424514889, fit = 0.12933364008204204
```
