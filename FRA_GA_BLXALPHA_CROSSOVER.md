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
result = meta.blxalpha_crossover(father_1, father_2, example_of_function, {}, x_lower, x_upper)
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
       <td><code>of_function</code></td>
       <td>This is the objective function that will be applied to the offspring to assess their fitness.</td>
       <td>Py function</td>
   </tr> 
   <tr>
       <td><code>null_dic</code></td>
       <td> This is an empty dictionary or object that can be used in the objective function, but is not used directly in the crossover function.</td>
       <td>Py dict</td>
   </tr>   
   <tr>
       <td><code>x_l</code></td>
       <td>Represents the lower limit of the interval for checking.</td>
       <td>Py list</td>
   </tr>
   <tr>
       <td><code>x_u</code></td>
       <td>Represents the upper limit of the interval for checking.</td>
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
       <td>List of values resulting from the blx alpha crossover between parents father_1 and father_2.</td>
       <td>Py list</td>
   </tr>
   <tr>
       <td><code>of_t1i</code></td>
       <td> The value of the objective function for the descendant.</td>
       <td>Float</td>
   </tr>
   <tr>
       <td><code>fit_t1i</code></td>
       <td>The fitness value associated with the descendant.</td>
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
   Use the <code> BLXALPHA_CROSSOVER</code> function to perform crossover between two 'parents' (father_1 and father_2). The objective function (example_of_function) is defined to illustrate a performance evaluation. The results include the resulting descendant (x_t1i), the value of the objective function (of_t1i), the fit value (fit_t1i), and the number of evaluations of the objective function (neof). This process is commonly used in evolutionary algorithms for optimization.

 </i>
</p>

```python
import numpy as np
import meta_ga_library as meta

def example_of_function(x, null_dic):
    return sum(x)

x_lower = [0, 0, 0]
x_upper = [1, 1, 1]
father_1 = [0.2, 0.5, 0.8]
father_2 = [0.7, 0.3, 0.6]

result = meta.blxalpha_crossover(father_1, father_2, example_of_function, {}, x_lower, x_upper)

print("Offspring (x_t1i):", result[0])
print("Objective function value (of_t1i):", result[1])
print("Fitness value (fit_t1i):", result[2])
print("Number of objective function evaluations (neof):", result[3])
```

```bash
Offspring (x_t1i): [0.14290572546555452, 0.2771622901862218, 0.5771622901862218]
Objective function value (of_t1i): 0.9972303058379981
Fitness value (fit_t1i): 0.5006933837709917
Number of objective function evaluations (neof): 2
```
