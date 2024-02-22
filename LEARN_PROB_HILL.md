---
layout: default
title: Hill Climbing
parent: Probabilistic
grand_parent: Learning
nav_order: 1
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
Hill Climbing was one of the literature's first existing probabilistic optimization algorithms. The Hill Climbing method is also known as a local search method <a href="#ref1">[1]</a>.
<br><br>
The iterative procedure continuously improves the solution until the best solution is attained. The process consists of generating random neighbors of the current solution, according to equation <a href="#eq1">(1)</a>, where \(\symbf{N}\) indicates a Gaussian or Uniform distribution where the mean \(\symbf{x}^{t}\) is the current solution and \(cov\) is the coefficient of variation input by the user. \(k\) is the kth component of the design variable vector \(\symbf{x}\).
</p>

<table border = "0" style = "width:100%">
    <tr>
        <td style="width: 90%;">\[x_{k}^{t+1} \sim \symbf{N}(x_{k}^{t}, \sigma)\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq1">(1)</p></td>
    </tr>
    <tr>
        <td style="width: 90%;">\[\sigma = x_{k}^{t} \cdot \frac{cov}{100}\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq2">(2)</p></td>
    </tr>
</table>

<h3>Algorithm</h3>

```python
1:  Input initial parameters (cov, n_population, x_lower, x_upper, obj_function, n_dimensions)
2:  Input initial guess (x_pop)
3:  Calculate of and fit (initial population)
4:  for iter in range(n_iterations):
5:      x_temp = equation (1)
6:      if fit(x_temp) > fit(x_pop):
7:         x_pop(iter+1) = x_temp
8:      else:
9:         x_pop(iter+1) = x_pop(iter)
```

{: .note }
> The Hill Climbing algorithm saves a new solution when a new candidate improves the current best solution.

<p align = "justify">
See <a href="https://wmpjrufg.github.io/METAPY/FRA_SA_HILL.html" target="_blank">HC algorithm</a> in METApy Framework.
</p>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
      Use the Hill Climbing optimization method to optimize the 2D sphere function. Use a total of 2 iterations to perform the optimization. Consider the limits \(\mathbf{x}_L = [-5.0, -5.0]\) and \(\mathbf{x}_U = [5.0, 5.0]\) for the problem design variables. Consider the initial guess (two agents) \(\mathbf{pop}_0 = [-0.74, 1.25]\) and \(\mathbf{pop}_1 = [3.58, -3.33]\). Use \(cov = 20%\) and Gaussian random generator.
  </i>
</p>


<h5>Solution</h5>

```
Hill Climbing 01 - report 

Initial population
x0 = [-0.74, 1.25], of_pop 2.1101 - best solution
x1 = [3.58, -3.33], of_pop 23.9053 

Iterations

Iteration: 1
Pop id: 0 - particle movement - mutation procedure
    current x = [-0.74, 1.25], of = 2.1101, fit = 0.3215330696762162
    Dimension 0: mean = -0.74, sigma = 0.14800000000000002, neighbor = -0.7926797137057607
    Dimension 1: mean = 1.25, sigma = 0.25, neighbor = 1.1968980750267357
    update x = [-0.7926797137057607, 1.1968980750267357], of = 2.0609061305233523, fit = 0.32670064267178966
    fit_i_temp > fit_pop[pop] - accept this solution
Pop id: 1 - particle movement - mutation procedure
    current x = [3.58, -3.33], of = 23.9053, fit = 0.040152096140179
    Dimension 0: mean = 3.58, sigma = 0.716, neighbor = 4.2788810597797005
    Dimension 1: mean = -3.33, sigma = 0.6659999999999999, neighbor = -4.267602421556293
    update x = [4.2788810597797005, -4.267602421556293], of = 36.52125355221459, fit = 0.026651561590510287
    fit_i_temp < fit_pop[pop] - not accept this solution
update solutions
x0 = [-0.7926797137057607, 1.1968980750267357], of_pop 2.0609061305233523 - best solution
x1 = [3.58, -3.33], of_pop 23.9053  

Iteration: 2
Pop id: 0 - particle movement - mutation procedure
    current x = [-0.7926797137057607, 1.1968980750267357], of = 2.0609061305233523, fit = 0.32670064267178966
    Dimension 0: mean = -0.7926797137057607, sigma = 0.15853594274115215, neighbor = -0.9324681956705839
    Dimension 1: mean = 1.1968980750267357, sigma = 0.23937961500534716, neighbor = 1.0461578853187818
    update x = [-0.9324681956705839, 1.0461578853187818], of = 1.9639432569518198, fit = 0.33738837531877064
    fit_i_temp > fit_pop[pop] - accept this solution
Pop id: 1 - particle movement - mutation procedure
    current x = [3.58, -3.33], of = 23.9053, fit = 0.040152096140179
    Dimension 0: mean = 3.58, sigma = 0.716, neighbor = 4.2608072507498
    Dimension 1: mean = -3.33, sigma = 0.6659999999999999, neighbor = -4.65951251517491
    update x = [4.2608072507498, -4.65951251517491], of = 39.86553530711369, fit = 0.024470497999959505
    fit_i_temp < fit_pop[pop] - not accept this solution
update solutions
x0 = [-0.9324681956705839, 1.0461578853187818], of_pop 1.9639432569518198 - best solution
x1 = [3.58, -3.33], of_pop 23.9053  
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
            <td><p align = "left"><a href="https://doi.org/10.1007/s00521-016-2328-2" target="_blank" rel="noopener noreferrer">Al-Betar, Mohammed Azmi (2016). β-Hill climbing: an exploratory local search. Neural Computing and Applications.</a></p></td>
        </tr>
    </tbody>
</table>