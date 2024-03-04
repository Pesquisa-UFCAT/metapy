---
layout: default
title: linear_crossover
grand_parent: Framework
parent: Genetic Algorithm functions
has_children: false
has_toc: false
nav_order: 3
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>linear_crossover</h3>
<br>

<p align = "justify">
    This function is a linear crossover between two individuals (represented by parent_0 and parent_1) in an optimization algorithm.
</p>

```python
result = linear_crossover(father1, father2, objective_function, nullDic, xL, xU)
```

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
       <td>This is the objective function that will be applied to the offspring to assess their fitness.</td>
       <td>Py function (<code>def</code>)</td>
   </tr>
   <tr>
       <td><code>father_1</code></td>
       <td>First parent</td>
       <td>List</td>
   </tr>
   <tr>
       <td><code>father_2</code></td>
       <td>Second parent</td>
       <td>List</td>
   </tr>  
   <tr>
       <td><code>n_dimensions</code></td>
       <td>Crossover point</td>
       <td>Int</td>
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
       <td>None variable. Default is None. Use in objective function.</td>
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
       <td>List</td>
   </tr>
   <tr>
       <td><code>of_i_new</code></td>
       <td>Update objective function value of the i agent</td>
       <td>Float</td>
   </tr>
   <tr>
       <td><code>fit_i_new</code></td>
       <td>Update fitness value of the i agent</td>
       <td>Float</td>
   </tr>
   <tr>
       <td><code>neof</code></td>
       <td>Number of evaluations of the objective function</td>
       <td>Int</td>
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

```

```bash

```
