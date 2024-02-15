---
layout: default
title: Hill Climbing
parent: Probabilistic
grand_parent: Learning
nav_order: 1
has_children: true
has_toc: true
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>Theory</h3>

<p align = "justify">
Hill Climbing was one of the literature's first existing probabilistic optimization algorithms. The Hill Climbing method is also known as a local search method <a href="#ref1">[1]</a>.
<br><br>
The iterative procedure continuously improves the solution until the best solution is attained. The process consists of generating random neighbors of the current solution, according to equation <a href="#eq1">(1)</a>, where \(\symbf{N}\) indicates a Gaussian or Uniform distribution where the mean \(\symbf{x}^{t}\) is the current solution and \(\sigma\) is the standard deviation input by the user. \(k\) is the kth component of the design variable vector \(\symbf{x}\).
</p>

<table border = "0" style = "width:100%">
    <tr>
        <td>\[\symbf{x}_{k}^{t+1} \sim \symbf{N}(\symbf{x}_{k}^{t}, \sigma)\]</td>
        <td><p align = "justify">random neighbour</p></td>
        <td><p align = "right" id = "eq1">(1)</p></td>
    </tr>
</table>

<h3>Algorithm</h3>

```python
1:  Input initial parameters (pdf, sigma, n_population, x_lower, x_upper, obj_function, n_dimensions)
2:  Input initial guess (x_pop)
3:  Calculate OF and FIT (initial population)
4:  for iter in range(n_iterations):
5:      x_temp = neighbor solution equation (1)
6:      if fit(x_temp) > fit(x_pop):
7:         x_pop(iter+1) = x_temp
```

{: .note }
> In hill climbing process, the algorithm save a new soluton when new candidate improve the current best solution.

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
            <td><p align = "left"><a href="https://doi.org/10.1007/s00521-016-2328-2" target="_blank" rel="noopener noreferrer">Al-Betar MA. β -Hill climbing: an exploratory local search. Neural Comput & Applic 2017;28:153–68</a></p></td>
        </tr>
    </tbody>
</table>