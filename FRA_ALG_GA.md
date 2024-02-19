---
layout: default
title: Genetic Algorithm functions
parent: Framework
nav_order: 3
has_children: true
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

TOURNAMENT_SELECTION
{: .label .label-green }

```python
selected_index = meta.tournament_selection(fitness, n_pop, 2, 5)
```

<p align = "justify">This function selects a position from the population using the tournament selection method.</p>

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

```python
result = linear_crossover(father1, father2, objective_function, nullDic, xL, xU)
```

<p align = "justify">This function is a linear crossover between two individuals (represented by father_1 and father_2) in an optimization algorithm. </p>

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

BINOMIAL_CROSSOVER
{: .label .label-green }

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

BLXALPHA_CROSSOVER
{: .label .label-green }

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

MP_CROSSOVER
{: .label .label-green }

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
