<!--
layout: default
title: binomial_crossover
grand_parent: Framework
parent: Genetic Algorithm functions
has_children: false
has_toc: true
nav_order: 4
--- -->

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>binomial_crossover</h3>
<br>

```python
result = meta.binomial_crossover(father_1, father_2, binomial_rate, objective_function, null_dic, x_l, x_u)

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
       <td><code>father_1</code></td>
       <td>Represents the first parent for the crossover.</td>
       <td>Py list</td>
   </tr>
   <tr>
       <td><code>father_2</code></td>
       <td>Represents the second parent for the crossover.</td>
       <td>Py list</td>
   </tr> 
   <tr>
       <td><code>binomial_rate</code></td>
       <td> This is the binomial crossover rate.</td>
       <td>Float</td>
   </tr> 
   <tr>
       <td><code>of_function</code></td>
       <td>Is the objective function that will be used to evaluate the result of the crossover.</td>
       <td>Py function</td>
   </tr> 
   <tr>
       <td><code>null_dic</code></td>
       <td>This dictionary is used as a parameter for the objective function.</td>
       <td>Py dict</td>
   </tr>   
   <tr>
       <td><code>x_l</code></td>
       <td>Represents the lower limits of the range for the problem variables.</td>
       <td>Py list</td>
   </tr>
   <tr>
       <td><code>x_u</code></td>
       <td>Represents the upper limits of the range for the problem variables.</td>
       <td>Py list</td>
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
       <td><code>x_t1i</code></td>
       <td>List of values resulting from the binomial crossover between parents father_1 and father_2.</td>
       <td>Py list</td>
   </tr>
   <tr>
       <td><code>of_t1i</code></td>
       <td></td>
       <td>Float</td>
   </tr>
   <tr>
       <td><code>fit_t1i</code></td>
       <td></td>
       <td>Float</td>
   </tr>
   <tr>
       <td><code>neof</code></td>
       <td>New solution indicator. It is a Boolean value (1 to indicate a new solution)</td>
       <td>Int</td>
   </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
 <i>
    Use the <code>binomial_crossover</code> function to combine two 'parents' (father_1 and father_2) and generate a 'child' using binomial crossover rate.  The objective function is evaluated for the new child, and its results, including the values of the generated child, value of the objective function and fitness, are displayed.
 </i>
</p>

```python
import numpy as np
import meta_ga_library as meta

def objective_function(x, null_dic):
    return sum(xi**2 for xi in x)

father_1 = [1, 2, 3, 4, 5]
father_2 = [5, 4, 3, 2, 1]
binomial_rate = 0.8
null_dic = {}
x_l = [0, 0, 0, 0, 0]
x_u = [10, 10, 10, 10, 10]

result = meta.binomial_crossover(father_1, father_2, binomial_rate, objective_function, null_dic, x_l, x_u)

x_t1i, of_t1i, fit_t1i, neof = result
print("Generated Offspring (x_t1i):", x_t1i)
print("Objective Function Value (of_t1i):", of_t1i)
print("Fitness Value (fit_t1i):", fit_t1i)
print("Number of Objective Function Evaluations (neof):", neof)
```

```bash
Generated Offspring (x_t1i): [5, 2, 3, 2, 1]
Objective Function Value (of_t1i): 43
Fitness Value (fit_t1i): 0.022727272727272728
Number of Objective Function Evaluations (neof): 1
```
