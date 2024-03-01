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
uniform_crossover(my_obj_function, father_1, father_2, n_dimensions, x_upper, x_lower, none_variable)
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
       <td>Py function</td>
   </tr> 
   <tr>
       <td><code>father_1</code></td>
       <td>Represents the first parent for the crossover</td>
       <td>List</td>
   </tr>
   <tr>
       <td><code>father_2</code></td>
       <td>Represents the second parent for the crossover</td>
       <td>List</td>
   </tr> 
   <tr>
       <td><code>n_dimensions</code></td>
       <td> number of dimensions</td>
       <td>Float</td>
   </tr>   
    <tr>
       <td><code>x_upper</code></td>
       <td>Upper limit of the design variables.</td>
       <td>List</td>
   </tr> 
   <tr>
       <td><code>x_l</code></td>
       <td>Lower limit of the design variables.</td>
       <td>List</td>
   </tr>
      <tr>
       <td><code>none_variable</code></td>
       <td>None variable. Default is None. Use in objective function</td>
       <td>Object  or None</td>
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
       <td>Int</td>
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
father_1 = [1, 1, 1, 1, 1]
father_2 = [10, 10, 10, 10, 10]
n_dimensions = 5
x_upper = [10, 10, 10, 10, 10]
x_lower = [1, 1, 1, 1, 1]
none_variable = None

x_i_new, of_i_new, fit_i_new, neof, report_move = uniform_crossover(my_obj_function, father_1, father_2, n_dimensions, x_upper, x_lower, none_variable)

print(x_i_new)
print(of_i_new)
print(fit_i_new)
print(neof)
print(report_move)
```

```bash
[1, 1, 1, 1, 10]
2
0.3333333333333333
2
    Crossover operator - uniform
    offspring a = [10, 10, 10, 10, 1], of_a = 200
    offspring b = [1, 1, 1, 1, 10], of_b = 2
    update pos = [1, 1, 1, 1, 10], of = 2, fit = 0.3333333333333333
```
