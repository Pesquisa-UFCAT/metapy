---
layout: default
title: Genetic Algorithm
parent: Probabilistic
grand_parent: Learning
nav_order: 3
has_children: false
has_toc: false
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>Theory</h3>

<br>

<p align = "justify">
A genetic Algorithm (GA) functions as a search metaheuristic, drawing inspiration from Charles Darwin's evolutionary theory.  This algorithm reflects the process of natural selection, where the fittest individuals are selected for reproduction to produce offspring of the next generation <a href="#ref1">[1]</a>.
<br><br>
Genetic Algorithm was developed by J. Holland [https://mitpress.mit.edu/9780262581110/adaptation-in-natural-and-artificial-systems/]. The main goal 
<br><br>
In GA the new populations are produced by iterative use of genetic operators on agents present in the population. These are genetic operators considered in this algorithm: 
</p>


<h3>Genetic operators</h3>

<h4><i>Selection</i></h4>

<p align = "justify">
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
</p>

<h4><i>Crossover</i></h4>

<p align = "justify">
Crossover is an operator that allows the combination of the genetic material of two
or more solutions. Crossover operators in Genetic Algorithms implement a mechanism that
mixes the genetic material of the parents [].

G. Syswerda. Simulated crossover in genetic algorithms. In Foundations of Genetic Algorithms (FOGA), pages 239–255, 1992.

https://link.springer.com/book/10.1007/978-3-319-52156-5

https://sci-hub.wf/10.1016/j.amc.2006.10.047

https://sci-hub.wf/10.1109/CEC.2001.934452

https://engineering.purdue.edu/~sudhoff/ee630/Lecture04.pdf
</p>

<h5><u>Linear crossover</u></h5>

<p aling = "justify">
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
</p>

<table border = "0" style = "width:100%">
    <thead>
        <tr>
            <td><p align = "center">offspring 0</p></td>
            <td><p align = "center">offspring 1</p></td>
            <td><p align = "center">offspring 2</p></td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>\[\alpha_1 = 0.5\]</td>
            <td>\[\alpha_2 = 1.5\]</td>
            <td>\[\alpha_3 = -0.5\]</td>
        </tr>
        <tr>
            <td>\[\beta_1 = 0.5\]</td>
            <td>\[\beta_2 = -0.5\]</td>
            <td>\[\alpha_3 = 1.5\]</td>
        </tr>
    </tbody>
</table>
<p align = "center" id = "tab01"><b>Table 1.</b> Linear crossover parameters.</p>

<h4><i>Mutation</i></h4>

<p align = "justify">
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
</p>

```python
1:  Input initial parameters (p_c, p_m, n_population,n_iteration, x_lower, x_upper, fit_function, obj_function, n_dimensions)
2:  Input initial guess (x_pop)
3:  Calculate of and fit (initial population)
4:  for iter in range(n_iterations):
5:      Apply selection operator
6:      r = random number [0,1]
7:      if r <=p_c: 
8:         Apply crossover operator
9:      r = random number [0,1]
10:     if r <= p_m:              
11:        Apply mutation operator
12:     if fit(x_temp) > fit(x_pop):
13:        x_pop(iter+1) = x_temp
14:     else:
15:        x_pop(iter+1) = x_pop(iter)
```

<p align = "justify">
See <a href="https://wmpjrufg.github.io/METAPY/FRA_ALG_SA_01.html" target="_blank">GA algorithm</a> in METApy Framework.
</p>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
      Use the Genetic algorithm optimization method to optimize the 2D sphere function. Use a total of 2 iterations to perform the optimization. Consider the limits \(\mathbf{x}_L = [-5.0, -5.0]\) and \(\mathbf{x}_U = [5.0, 5.0]\) for the problem design variables. Consider the initial guess (two agents) \(\mathbf{pop}_0 = [-0.74, 1.25]\) and \(\mathbf{pop}_1 = [3.58, -3.33]\). Use \(cov = 20%\), Gaussian random generator, \(T_0 = 15\) and geometric schedule (\(\alpha = 0.90\)).
  </i>
</p>


<h5>Solution</h5>

```
Simulated Annealing 01 - report 

Initial population
x0 = [-0.74, 1.25], of_pop 2.1101 - best solution
x1 = [3.58, -3.33], of_pop 23.9053 

Iterations

Iteration: 1
Temperature: 15
Pop id: 0 - particle movement - mutation procedure
    current x = [-0.74, 1.25], of = 2.1101, fit = 0.3215330696762162
    Dimension 0: mean = -0.74, sigma = 0.14800000000000002, neighbor = -1.0351744807425902
    Dimension 1: mean = 1.25, sigma = 0.25, neighbor = 1.5447852100500892
    update x = [-1.0351744807425902, 1.5447852100500892], of = 3.4579475507701893, fit = 0.22431847584820336
    energy = 1.3478475507701893, prob. state = 0.9140623407129066
    prob. state 0.9140623407129066 >= random number 0.6630641248277662 - accept this solution
Pop id: 1 - particle movement - mutation procedure
    current x = [3.58, -3.33], of = 23.9053, fit = 0.040152096140179
    Dimension 0: mean = 3.58, sigma = 0.716, neighbor = 3.9447170160318668
    Dimension 1: mean = -3.33, sigma = 0.6659999999999999, neighbor = -3.7756500200969305
    update x = [3.9447170160318668, -3.7756500200969305], of = 29.816325410829307, fit = 0.03245033230498615
    energy = 5.911025410829307, prob. state = 0.674307958485963
    prob. state 0.674307958485963 >= random number 0.11118541366280277 - accept this solution
update solutions
x0 = [-1.0351744807425902, 1.5447852100500892], of_pop 3.4579475507701893 - best solution
x1 = [3.9447170160318668, -3.7756500200969305], of_pop 29.816325410829307 

Iteration: 2
Temperature: 13.5
Pop id: 0 - particle movement - mutation procedure
    current x = [-1.0351744807425902, 1.5447852100500892], of = 3.4579475507701893, fit = 0.22431847584820336
    Dimension 0: mean = -1.0351744807425902, sigma = 0.20703489614851806, neighbor = -0.9559782630786865
    Dimension 1: mean = 1.5447852100500892, sigma = 0.30895704201001783, neighbor = 1.0793006180821911
    update x = [-0.9559782630786865, 1.0793006180821911], of = 2.078784263671542, fit = 0.3248035309909861
    energy = -1.3791632870986472, prob. state = 1
    prob. state 1 >= random number 0.40559404312719416 - accept this solution
Pop id: 1 - particle movement - mutation procedure
    current x = [3.9447170160318668, -3.7756500200969305], of = 29.816325410829307, fit = 0.03245033230498615
    Dimension 0: mean = 3.9447170160318668, sigma = 0.7889434032063734, neighbor = 3.3478221189294404
    Dimension 1: mean = -3.7756500200969305, sigma = 0.7551300040193861, neighbor = -3.871949506115549
    update x = [3.3478221189294404, -3.871949506115549], of = 26.199905917901653, fit = 0.03676483304825877
    energy = -3.6164194929276547, prob. state = 1
    prob. state 1 >= random number 0.5368960666312674 - accept this solution
update solutions
x0 = [-0.9559782630786865, 1.0793006180821911], of_pop 2.078784263671542 - best solution
x1 = [3.3478221189294404, -3.871949506115549], of_pop 26.199905917901653   
```

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
            <td><p align = "left"><a href="https://doi.org/10.1007/s11042-020-10139-6" target="_blank" rel="noopener noreferrer">Katoch, S., Chauhan, S.S. & Kumar, V  (2021). A review on genetic algorithm: past, present, and future. Multimed Tools Appl 80, 8091–8126.</a></p></td>
        </tr>
    </tbody>
</table>
