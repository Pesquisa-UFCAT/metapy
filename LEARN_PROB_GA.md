---
layout: default
title: Genetic Algorithm
parent: Probabilistic
grand_parent: Learning
nav_order: 3
has_children: true
has_toc: true
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<p align = "justify">
    This section presents an review of the optimization methods and their applications.
</p>



<h3>
Algorithm
</h3>

<p aling = "justify">
A genetic algorithm (GA) functions as a search heuristic, drawing inspiration from Charles Darwin's evolutionary theory.  This algorithm reflects the process of natural selection where the fittest individuals are selected for reproduction in order to produce offspring of the next generation <a href="#ref1">[1]</a>.
<br><br>
The new populations are produced by iterative use of genetic operators on agents present in the population. The chromosome representation, selection, crossover, mutation, and fitness function computation are the key elements of GA.
<br><br>
The procedure of GA is as follows. A population (X) of n agents are initialized randomly. The fitness and object function of each agent X is computed. Two agents say A1 and A2 are selected from the population X according to the fitness value. The single-point crossover operator with crossover probability (crossover rate) is applied on A1 and A2 to produce an offspring say O. Thereafter, uniform mutation operator is applied on produced offspring (iter) with mutation probability (mutation rate) to generate iter. The new offspring iter’ is placed in new population. The selection, crossover, and mutation operations will be repeated on current population until the new population is complete <a href="#ref1">[1]</a>. 

<h4>
Linear Crossover
</h4>

<p align = "justify">

</p>
Step 1- Select two agents to crossover.

<br>

Step 2- Select a single gene (k) at random.

<br>

Step 3- Define \(\alpha\) and \(\beta\) parameters.

Parameters




<table border = "0" style = "width:100%">
    <tr>
        <td colspan="3" align = "center">Parameters</td>
    </tr>
    <tr>
        <td>\[\alpha_1 = 0.5\]</td>
        <td><p align = "justify">\[\alpha_2 = 1.5\]</p></td>
        <td><p align = "justigy"> </p>\[\alpha_3 = -0.5\]</td>
    </tr>
    <tr>
        <td>\[\beta_1 = 0.5\]</td>
        <td><p align = "justify">\[\beta_2 = -0.5\]</p></td>
        <td><p align = "justify">\[\alpha_3 = -0.5\]</p></td>
    </tr>
</table>


</p>


```python
1:  Input initial parameters (n_population,n_iteration, x_lower, x_upper, fit_function, obj_function, n_dimensions, crossover rate, mutation rate, type selection, type mutation, cov)
2:  Gerate initial population of n_population (x_pop)
3:  Calculate OF and FIT (population)
4:  for iter in range(n_iterations):
5:      Select a pair of agent to crossover
6:      Apply crossover operation on selected pair with crossover probability
7:      Apply mutation on the offspring with mutation probability
8:      x_temp = new generated population
9:  return (Best Solution) 
```

<h3>
Solution
</h3>

<h3>Reference list</h3>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Reference</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><p align = "center" id = "ref1">[1]</p></td>
            <td><p align = "left"><a href="https://doi.org/10.1007/s11042-020-10139-6" target="_blank" rel="noopener noreferrer">Katoch, S., Chauhan, S.S. & Kumar, V. A review on genetic algorithm: past, present, and future. Multimed Tools Appl 80, 8091–8126 (2021)</a></p></td>
        </tr>
    </tbody>
</table>