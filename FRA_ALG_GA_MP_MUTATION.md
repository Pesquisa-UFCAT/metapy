---
layout: default
title: MP Mutation
grand_parent: Framework
parent: Genetic Algorithm functions
has_children: false
has_toc: true
nav_order: 6
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

MP_MUTATION
{: .label .label-green }

```python
resulting_chromosome, resulting_objective, fitness_value, neof = meta.mp_mutation(
    chromosome=initial_chromosome,
    seed=seed,
    of_chro=objective_function(initial_chromosome, null_dic),
    of_function=lambda x, dic: objective_function(generate_offspring(x), dic),
    null_dic=null_dic
)
```

<p align = "justify">   Multi-point inversion mutation. A random mask encodes which elements will keep the original order or the reversed one.</p>

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
       <td><code>chromosome</code></td>
       <td>Encoding of a solution (chromosome). This parameter represents the genetic encoding of an individual solution or candidate solution.</td>
       <td>Np array</td>
   </tr>
   <tr>
       <td><code>seed</code></td>
       <td> Seed for pseudo-random numbers generation. This parameter is optional, and if provided, it is used to initialize the random number generator. If not provided (default is None), the random number generator is initialized without a specific seed.</td>
       <td>None or Int</td>
   </tr> 
   <tr>
       <td><code>of_chro</code></td>
       <td>Objective function for the input chromosome. It is a function that takes the chromosome as input and returns a numerical value representing the objective (fitness) of the chromosome.</td>
       <td>Py function</td>
   </tr> 
   <tr>
       <td><code>of_function</code></td>
       <td>Objective function for the mutated individual. Similar to of_chro, it takes an individual (mutated chromosome) as input and returns the objective value.</td>
       <td>Py function</td>
   </tr>   
   <tr>
       <td><code>null_dic</code></td>
       <td>A dictionary used as an additional input for the objective functions (of_chro and of_function). The specific contents and purpose of this dictionary depend on the implementation of the objective functions.</td>
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
       <td>The resulting chromosome after mutation. It could be the original chromosome or the mutated individual, depending on the comparison of objective values.</td>
       <td>Np array</td>
   </tr>
   <tr>
       <td><code>of_t1i</code></td>
       <td>The objective value (fitness) corresponding to the resulting chromosome.</td>
       <td>Float</td>
   </tr>
   <tr>
       <td><code>fit_t1i</code></td>
       <td>The fitness value corresponding to the objective value (of_t1i). The fitness value is obtained using a common function called common.fit_value.</td>
       <td>Float</td>
   </tr>
   <tr>
       <td><code>neof</code></td>
       <td>An integer representing the number of objective function evaluations performed during the mutation process. In this case, it is always set to 1.</td>
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
