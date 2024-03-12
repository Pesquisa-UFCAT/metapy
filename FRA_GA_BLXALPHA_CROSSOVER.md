---
layout: default
title: blxalpha_crossover
grand_parent: Framework
parent: Genetic Algorithm functions
has_children: false
has_toc: false
nav_order: 201
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>blxalpha_crossover</h3>
<br>

```python
x_i_new, of_i_new, fit_i_new, neof, report = blxalpha_crossover(of_function, parent_0, parent_1, n_dimensions, x_upper, x_lower, none_variable)
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
#father1 = [1, 1, 1, 1, 1]
#father2 = [10, 10, 10, 10, 10]
# gere father 1 e father 2 com valores aleatórios
father1 = [1.5, 2.3, 1.8, 3.8, 2.4]
father2 = [2.3, 1.5, 1.5, 2.8, 4.4]
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
xNew, ofNew, fitNew, neof, report = blxalpha_crossover(objFunction, father1, father2, nDimensions, xUpper, xLower, noneVariable)

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
    current p0 = [1.5, 2.3, 1.8, 3.8, 2.4]
    current p1 = [2.3, 1.5, 1.5, 2.8, 4.4]
    Dimension 0: min_val = 1.5, max_val = 2.3, r_ij = 0.7999999999999998
    neighbor_a = 0.9591254809153907, neighbor_b = 2.840874519084609
    Dimension 1: min_val = 1.5, max_val = 2.3, r_ij = 0.7999999999999998
    neighbor_a = 0.7431857498245784, neighbor_b = 3.0568142501754214
    Dimension 2: min_val = 1.5, max_val = 1.8, r_ij = 0.30000000000000004
    neighbor_a = 1.473354543479718, neighbor_b = 1.826645456520282
    Dimension 3: min_val = 2.8, max_val = 3.8, r_ij = 1.0
    neighbor_a = 2.7797787480137583, neighbor_b = 3.8202212519862413
    Dimension 4: min_val = 2.4, max_val = 4.4, r_ij = 2.0000000000000004
    neighbor_a = 1.403318395158758, neighbor_b = 5.396681604841242
    offspring a = [1.0, 1.0, 1.0, 1.0, 1.0], of_a 2.0
    offspring b = [1.0, 1.0, 1.0, 1.0, 1.0], of_b 2.0
    update x = [1.0, 1.0, 1.0, 1.0, 1.0], of = 2.0, fit = 0.3333333333333333
```
