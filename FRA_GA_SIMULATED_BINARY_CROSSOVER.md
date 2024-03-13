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
x_i_new, of_i_new, fit_i_new, neof, report = simulated_binary_crossover(of_function, parent_0, parent_1, eta_c, n_dimensions, x_upper, x_lower, none_variable)
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
from metapy_toolbox import simulated_binary_crossover

# Data
father1 = [3.8, 3.0, 2.7, 3.6, 4.5]
father2 = [4.3, 2.5, 2.1, 1.1, 1.8]
eta_c = 0.30
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
xNew, ofNew, fitNew, neof, report = simulated_binary_crossover(objFunction, father1, father2, eta_c, nDimensions, xUpper, xLower, noneVariable)

# Output details
print('x new ', xNew)
print('of new ', ofNew)
print('fit new', fitNew)
print('number of evalutions objective function', neof)
```

```bash
x new  [3.6371818435745453, 2.81116885353825, 2.4485231406036525, 3.520665834632936, 5.0]
of new  21.13176208633189
fit new 0.04518393050219797
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
    current p0 = [3.8, 3.0, 2.7, 3.6, 4.5]
    current p1 = [4.3, 2.5, 2.1, 1.1, 1.8]
    random number = 0.7395012830572558 > 0.50, beta = 1.6512726257018162
    neighbor_a 3.6371818435745453
    neighbor_b 3.6371818435745453
    random number = 0.08019318011743659 <= 0.50, beta = 0.24467541415300118
    neighbor_a 2.81116885353825
    neighbor_b 2.81116885353825
    random number = 0.04682156719983155 <= 0.50, beta = 0.16174380201217442
    neighbor_a 2.4485231406036525
    neighbor_b 2.4485231406036525
    random number = 0.4591449525617629 <= 0.50, beta = 0.9365326677063486
    neighbor_a 3.520665834632936
    neighbor_b 3.520665834632936
    random number = 0.8856693688660848 > 0.50, beta = 3.1112060299510342
    neighbor_a 7.350128140433897
    neighbor_b 7.350128140433897
    offspring a = [3.6371818435745453, 2.81116885353825, 2.4485231406036525, 3.520665834632936, 5.0], of_a = 21.13176208633189
    offspring b = [3.6371818435745453, 2.81116885353825, 2.4485231406036525, 3.520665834632936, 5.0], of_b = 21.13176208633189
    update pos = [3.6371818435745453, 2.81116885353825, 2.4485231406036525, 3.520665834632936, 5.0], of = 21.13176208633189, fit = 0.04518393050219797
```
