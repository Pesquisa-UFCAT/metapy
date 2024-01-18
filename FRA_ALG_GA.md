---
layout: default
title: Genetic Algorithm functions
parent: Metaheuristics
grand_parent: Framework
nav_order: 1
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

ROULETE_WHEEL_SELECTION
{: .label .label-green }

<p align = "justify">This function selects a position from the population using the roulette wheel selection method.</p>

```python
selected_index = meta.roulete_wheel_selection(fitness, n_pop, 2)
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
       <td><code>fit</code></td>
       <td>It represents the fitness of the individuals in the population. It is supplied as input to the function.</td>
       <td>NumPy list</td>
   </tr>
   <tr>
       <td><code>n_pop</code></td>
       <td>Indicates the size of the population, i.e. the total number of individuals.</td>
       <td>Int</td>
   </tr> 
   <tr>
       <td><code>i</code></td>
       <td>Represents the index of the individual who will be excluded during the roulette wheel selection process.</td>
       <td>Int</td>
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
       <td><code>selected</code></td>
       <td>Stores the index of the individual selected after the roulette method.</td>
       <td>Int</td>
   </tr>
 
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
 <i>
Use the <code>ROULETE_WHEEL_SELECTION</code> function to select an individual based on probabilities proportional to their fitness. In this example, fitness is a list of aptitudes for each individual in the population. The number 2 passed as the third argument to the function indicates that you want to exclude the third individual when performing the roulette wheel selection. 
 </i>
</p>

```python
import meta_ga_library as meta
import numpy as np

n_pop = 10
fitness = np.random.rand(n_pop)
selected_index = meta.roulete_wheel_selection(fitness, n_pop, 2)

print(f"Selected index: {selected_index}")
```

```bash
Selected index: 7
```

TOURNAMENT_SELECTION
{: .label .label-green }

<p align = "justify">This function selects a position from the population using the tournament selection method.</p>

```python
selected_index = meta.tournament_selection(fitness, n_pop, 2, 5)
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
       <td><code>fit</code></td>
       <td>A matrix that stores the fitness values for each individual in the population.</td>
       <td>NumPy list</td>
   </tr>
   <tr>
       <td><code>n_pop</code></td>
       <td>Indicates the size of the population, i.e. the total number of individuals.</td>
       <td>Int</td>
   </tr> 
   <tr>
       <td><code>i</code></td>
       <td>Index of the individual for whom tournament selection will be carried out. This is the index that will be temporarily removed during the selection process.</td>
       <td>Int</td>
   </tr>
      <tr>
       <td><code>runs</code></td>
       <td>Number of times the tournament will be run to choose the individual. Each run of the tournament involves randomly choosing two individuals from the population.</td>
       <td>Int</td>
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
       <td><code>selected</code></td>
       <td>Index of the selected individual in the population. This is the index of the individual who won the tournament.</td>
       <td>Int</td>
   </tr>
 
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
 <i>
 Use the <code>TOURNAMENT_SELECTION</code> function to select an individual based on probabilities proportional to their aptitude. In this example, the aptitude is a list of aptitudes for each individual in the population. The number 2 passed as the third argument to the function indicates that you want to exclude the third individual when performing the tournament selection. And 5 is the number of times the tournament will be played.
 </i>
</p>

```python
import numpy as np
import meta_ga_library as meta

n_pop = 10
fitness = np.random.rand(n_pop, 1)

selected_index = meta.tournament_selection(fitness, n_pop, 2, 5)

print("Selected individual:", selected_index)

```

```bash
Selected individual: 6
```

LINEAR_CROSSOVER
{: .label .label-green }

<p align = "justify">This function is a linear crossover between two individuals (represented by father_1 and father_2) in an optimization algorithm. </p>

```
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
       <td>List of values resulting from the linear crossover between parents father_1 and father_2.</td>
       <td>Py list</td>
   </tr>
   <tr>
       <td><code>of_t1i</code></td>
       <td>Value of the objective function (or fitness function) evaluated on the set of x_t1i values.</td>
       <td>Float</td>
   </tr>
   <tr>
       <td><code>fit_t1i</code></td>
       <td>Fitness value corresponding to the result of the of_t1i objective function.</td>
       <td>Float</td>
   </tr>
   <tr>
       <td><code>neof</code></td>
       <td>Value indicating the number of evaluations of new solutions generated by the function.</td>
       <td>Int</td>
   </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
 <i>
    Use the <code>linear_crossover</code> function to perform a linear crossover process between two populations of individuals, represented by <code>father_1</code> and <code>father_2</code>. These individuals have numerical characteristics represented by vectors of values. The linear crossover process combines the values of these vectors to create three new individuals, represented by <code>OFFSPRING_A</code>, <code>OFFSPRING_B</code> and <code>OFFSPRING_C</code>.
 </i>
</p>

```python
def objective_function(x, null_dic):
    return sum([(i + 1) * x[i]**2 for i in range(len(x))])

father1 = [1, 2, 3]
father2 = [4, 5, 6]
xL = [0, 0, 0]
xU = [10, 10, 10]
nullDic = None

result = linear_crossover(father1, father2, objective_function, nullDic, xL, xU)

print("The best son:", result[0])
print("Objective function value:", result[1])
print("Fitness value:", result[2])
print("Number of job evaluations:", result[3])
```

```bash
The best son: [0.0, 0.5, 1.5]
Objective function value: 7.25
Fitness value: 0.12121212121212122
Number of job evaluations: 3
```
