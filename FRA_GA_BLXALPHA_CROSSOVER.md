---
layout: default
title: blxalpha_crossover
grand_parent: Framework
parent: Genetic Algorithm functions
has_children: false
has_toc: false
nav_order: 4
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>blxalpha_crossover</h3>
<br>

```python
xNew, ofNew, fitNew, neOf, reportMove = blxalpha_crossover(objFunction, father1, father2, n_dimensions, xUpper, xLower, noneVariable)
```

<p align = "justify">BLX alpha crossover operator.

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
       <td>Py function (<code>def</code>)</td>
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
# Import
from metapy_toolbox import blxalpha_crossover

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
xNew, ofNew, fitNew, neof, report = blxalpha_crossover(objFunction, father1, father2, nDimensions, xUpper, xLower, noneVariable)

# Output details
print('x new ', xNew)
print('of new ', ofNew)
print('fit new', fitNew)
print('number of evalutions objective function', neof)
```

```bash
x new  [1.0, 1.0, 1.0, 1.0, 1.0]
of new  5.0
fit new 0.16666666666666666
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
    Crossover operator - BLX-alpha
    current p0 = [1, 1, 1, 1, 1]
    current p1 = [10, 10, 10, 10, 10]
    Dimension 0: min_val = 1, max_val = 10, r_ij = 9
    neighbor_a = -0.34314858255610803, neighbor_b = 11.343148582556108
    Dimension 1: min_val = 1, max_val = 10, r_ij = 9
    neighbor_a = -0.34314858255610803, neighbor_b = 11.343148582556108
    Dimension 2: min_val = 1, max_val = 10, r_ij = 9
    neighbor_a = -0.34314858255610803, neighbor_b = 11.343148582556108
    Dimension 3: min_val = 1, max_val = 10, r_ij = 9
    neighbor_a = -0.34314858255610803, neighbor_b = 11.343148582556108
    Dimension 4: min_val = 1, max_val = 10, r_ij = 9
    neighbor_a = -0.34314858255610803, neighbor_b = 11.343148582556108
    offspring a = [1.0, 1.0, 1.0, 1.0, 1.0], of_a 5.0
    offspring b = [1.0, 1.0, 1.0, 1.0, 1.0], of_b 5.0
    update x = [1.0, 1.0, 1.0, 1.0, 1.0], of = 5.0, fit = 0.16666666666666666
```
