---
layout: default
title: laplace_crossover
grand_parent: Framework
parent: Genetic Algorithm functions
has_children: false
has_toc: true
nav_order: 205
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>laplace_crossover</h3>
<br>

```python
x_i_new, of_i_new, fit_i_new, neof, report = laplace_crossover(of_function, parent_0, parent_1, mu, sigma, n_dimensions, x_upper, x_lower, none_variable)
```

<p align = "justify">This function performs the laplace crossover operator. Two new points are generated from the two parent points (offspring).</p>

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
       <td><code>mu</code></td>
       <td>location parameter</td>
       <td>Float</td>
   </tr>
      <tr>
       <td><code>sigma</code></td>
       <td>scale parameter</td>
       <td>Float</td>
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
from metapy_toolbox import laplace_crossover

# Data
father1 = [1, 1, 1, 1, 1]
father2 = [10, 10, 10, 10, 10]
mu = 0.75
sigma = 0.25
nDimensions = len(father1)
xUpper = [10, 10, 10, 10, 10]
xLower = [1, 1, 1, 1, 1]
noneVariable = None

# Objective function
def objFunction(x, _):
    """Example objective function"""
    return sum(x)

# Call function
xNew, ofNew, fitNew, neof, report = laplace_crossover(objFunction, father1, father2, mu, sigma, nDimensions, xUpper, xLower, noneVariable)

# Output details
print('x new ', xNew)
print('of new ', ofNew)
print('fit new', fitNew)
print('number of evalutions objective function', neof)
```

```bash
x new  [7.548562129830823, 9.716816253769316, 9.401494014953634, 10.0, 10.0]
of new  46.66687239855378
fit new 0.02097893043283327
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
    Crossover operator - laplace crossover
    current p0 = [1, 1, 1, 1, 1]
    current p1 = [10, 10, 10, 10, 10]
    random number = 0.9143627153724113 > 0.50, beta = 0.727618014425647
    rij = 9, neighbor_a 7.548562129830823
    rij = 9, neighbor_b 16.548562129830824
    random number = 0.4172204427270587 <= 0.50, beta = 0.9685351393077017
    rij = 9, neighbor_a 9.716816253769316
    rij = 9, neighbor_b 18.716816253769316
    random number = 0.4799864810387685 <= 0.50, beta = 0.9334993349948483
    rij = 9, neighbor_a 9.401494014953634
    rij = 9, neighbor_b 18.401494014953634
    random number = 0.27737859073355475 <= 0.50, beta = 1.0705929881003815
    rij = 9, neighbor_a 10.635336892903434
    rij = 9, neighbor_b 19.63533689290343
    random number = 0.04691434859350141 <= 0.50, beta = 1.5148579275400267
    rij = 9, neighbor_a 14.63372134786024
    rij = 9, neighbor_b 23.633721347860238
    offspring a = [7.548562129830823, 9.716816253769316, 9.401494014953634, 10.0, 10.0], of_a = 46.66687239855378
    offspring b = [10.0, 10.0, 10.0, 10.0, 10.0], of_b = 50.0
    update pos = [7.548562129830823, 9.716816253769316, 9.401494014953634, 10.0, 10.0], of = 46.66687239855378, fit = 0.02097893043283327
```
