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
A genetic algorithm functions as a search heuristic, drawing inspiration from Charles Darwin's evolutionary theory.  This algorithm reflects the process of natural selection where the fittest individuals are selected for reproduction in order to produce offspring of the next generation <a href="#ref1">[1]</a>.
</p>


```python
1:  Input initial parameters (n_population,n_iteration, x_lower, x_upper, fit_function, obj_function, n_dimensions, crossover rate, mutation rate, type selection, type mutation, cov)
2:  Gerate initial population of n_population (x_pop)
3:  Calculate OF and FIT (population)
4:  for iter in range(n_iterations):
5:      Select a pair of agent to crossover
6:      Apply crossover operation on selected pair with crossover probability
7:      Apply mutation on the offspring with mutation probability
8:      x_temp = nwe generated population
9:      if fit(x_temp) > fit(x_pop):
10:         x_pop(iter+1) = x_temp
11:      else:
12:         x_pop(iter+1) = x_pop(iter)
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