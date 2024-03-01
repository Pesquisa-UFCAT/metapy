<!-- ---
layout: default
title: mp_crossover
grand_parent: Framework
parent: Genetic Algorithm functions
has_children: false
has_toc: true
nav_order: 5
--- -->

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>mp_crossover</h3>
<br>

```python
result = meta.mp_crossover(chromosome_a, chromosome_b, seed, of_function, {})
```

<p align = "justify">This function makes the multipoint inversion mutation for a genetic algorithm. The function receives a chromosome (representation of a solution), a seed for generating pseudo-random numbers and other parameters.</p>

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
       <td><code>chromosome_a</code></td>
       <td> Encoding of the first solution (chromosome).</td>
       <td>Np array</td>
   </tr>
   <tr>
       <td><code>chromosome_b</code></td>
       <td>Encoding of the second solution (chromosome)</td>
       <td>Np array</td>
   </tr> 
   <tr>
       <td><code>seed</code></td>
       <td>Seed for pseudo-random number generation. If not provided, the default is None.</td>
       <td>Py function</td>
   </tr> 
   <tr>
       <td><code>of_function</code></td>
       <td>Objective function that evaluates the fitness of a chromosome. It takes a chromosome and a null dictionary (null_dic) as inputs.</td>
       <td>Py function</td>
   </tr>   
   <tr>
       <td><code>null_dic</code></td>
       <td>A null dictionary used as an input for the objective function.</td>
       <td>Py dict</td>
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
       <td>The resulting chromosome after crossover.</td>
       <td>Py list</td>
   </tr>
   <tr>
       <td><code>of_t1i</code></td>
       <td>The objective function value of the resulting chromosome.</td>
       <td>Float</td>
   </tr>
   <tr>
       <td><code>fit_t1i</code></td>
       <td>The fitness value of the resulting chromosome, computed from the objective function value.</td>
       <td>Float</td>
   </tr>
   <tr>
       <td><code>neof</code></td>
       <td>A constant value representing the number of objective function evaluations (set to 2 in this case).</td>
       <td>Int</td>
   </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
 <i>

 </i>
</p>

```python
import numpy as np
import meta_ga_library as meta

chromosome_a = np.array([1, 2, 3, 4, 5])
chromosome_b = np.array([5, 4, 3, 2, 1])

seed = 42
of_function = lambda x, _: sum(x)

result = meta.mp_crossover(chromosome_a, chromosome_b, seed, of_function, {})
child_chromosome, of_child, fit_child, neof_child = result

print("Parent A:", chromosome_a)
print("Parent B:", chromosome_b)
print("Child Chromosome:", child_chromosome)
print("Objective Function Value of Child:", of_child)
print("Fitness Value of Child:", fit_child)
print("Number of Evaluations of the Objective Function:", neof_child)
```

```bash
Parent A: [1 2 3 4 5]
Parent B: [5 4 3 2 1]
Child Chromosome: [5 2 4 3 1]
Objective Function Value of Child: 15
Fitness Value of Child: 0.0625
Number of Evaluations of the Objective Function: 2
```
