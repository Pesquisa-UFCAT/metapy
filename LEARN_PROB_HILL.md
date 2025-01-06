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
The iterative procedure continuously improves the solution until the best solution is attained. The process consists of generating random neighbors of the current solution \left(\symbf{x}_i\right), according to equation <a href="#eq1">(1)</a>, where \(\symbf{N}\) indicates a Gaussian or Uniform distribution where the mean \(\symbf{x}^{t}\) is the current solution and \(cov\) is the coefficient of variation input by the user. \(k\) is the \(k\)th component of the design variable vector \(\symbf{x}\) and \(t\) is a current iteration.
</p>

<table border = "0" style = "width:100%">
    <tr>
        <td style="width: 90%;">\[x_{i,k}^{t+1} \sim \symbf{N}(x_{i,k}^{t}, \sigma)\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq1">(1)</p></td>
    </tr>
    <tr>
        <td style="width: 90%;">\[\sigma = x_{i,k}^{t} \cdot \frac{cov}{100}\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq2">(2)</p></td>
    </tr>
</table>

<p align = "justify">
A small value of \(\sigma\) gives a higher probability for creating ‘near-parent’ solutions and a large value of \(\sigma\) allows distant solutions.
</p>

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
    current x = [-0.74, 1.25]
    Dimension 0: mean = -0.74, sigma = 0.14800000000000002, neighbor = -0.9023477757469192
    Dimension 1: mean = 1.25, sigma = 0.25, neighbor = 1.2619927898303909
    update x = [-0.9023477757469192, 1.2619927898303909], of = 2.4068573099793054, fit = 0.29352564813055654
    fit_i_temp=0.29352564813055654 < fit_pop[pop]=0.3215330696762162 - not accept this solution
Pop id: 1 - particle movement - mutation procedure
    current x = [3.58, -3.33]
    Dimension 0: mean = 3.58, sigma = 0.716, neighbor = 3.6241680241318215
    Dimension 1: mean = -3.33, sigma = 0.6659999999999999, neighbor = -3.2320736729816724
    update x = [3.6241680241318215, -3.2320736729816724], of = 23.58089409472079, fit = 0.040682002702854034
    fit_i_temp=0.040682002702854034 > fit_pop[pop]=0.040152096140179 - accept this solution
update solutions
x0 = [-0.74, 1.25], of_pop 2.1101 - best solution
x1 = [3.6241680241318215, -3.2320736729816724], of_pop 23.58089409472079  

Iteration: 2
Pop id: 0 - particle movement - mutation procedure
    current x = [-0.74, 1.25]
    Dimension 0: mean = -0.74, sigma = 0.14800000000000002, neighbor = -0.6839602767380419
    Dimension 1: mean = 1.25, sigma = 0.25, neighbor = 0.9611420858210487
    update x = [-0.6839602767380419, 0.9611420858210487], of = 1.391595769292015, fit = 0.41813086176182296
    fit_i_temp=0.41813086176182296 > fit_pop[pop]=0.3215330696762162 - accept this solution
Pop id: 1 - particle movement - mutation procedure
    current x = [3.6241680241318215, -3.2320736729816724]
    Dimension 0: mean = 3.6241680241318215, sigma = 0.7248336048263643, neighbor = 2.9304941843959953
    Dimension 1: mean = -3.2320736729816724, sigma = 0.6464147345963345, neighbor = -3.1041458794450945
    update x = [2.9304941843959953, -3.1041458794450945], of = 18.22351780565471, fit = 0.05201961524991249
    fit_i_temp=0.05201961524991249 > fit_pop[pop]=0.040682002702854034 - accept this solution
update solutions
x0 = [-0.6839602767380419, 0.9611420858210487], of_pop 1.391595769292015 - best solution
x1 = [2.9304941843959953, -3.1041458794450945], of_pop 18.22351780565471   
```

<h2>Guia de Cálculo Manual - Hill Climbing</h2>

<h2>População Inicial</h2>

<p align="justify">A população inicial é composta pelo seguinte vetor de solução:</p>

<ul>
    <li>\( x_0 = [88.25395326699595], \ \text{of}_{\text{pop}} = -7.5079 \) - <strong>melhor solução</strong></li>
</ul>

<hr>

<h2>Iterações</h2>

<h3>Iteração 1</h3>

<p align="justify">Na primeira iteração, o algoritmo aplica o procedimento de mutação para explorar a vizinhança da solução atual. O cálculo é realizado utilizando uma distribuição normal \( \text{N}(\mu, \sigma) \), onde \( \mu \) é o valor atual e \( \sigma \) é igual ao valor da dimensão correspondente. A seguir, apresentamos os cálculos detalhados para cada dimensão:</p>

<h4>Dimensão 0</h4>
<table style="width:100%; border: 1px solid black; border-collapse: collapse;">
    <tr style="border: 1px solid black;">
        <th style="border: 1px solid black;">Parâmetro</th>
        <th style="border: 1px solid black;">Valor</th>
    </tr>
    <tr style="border: 1px solid black;">
        <td style="border: 1px solid black;">Valor inicial (\( \mu \))</td>
        <td style="border: 1px solid black;">\( 88.25395326699595 \)</td>
    </tr>
    <tr style="border: 1px solid black;">
        <td style="border: 1px solid black;">Desvio padrão (\( \sigma \))</td>
        <td style="border: 1px solid black;">\( 88.25395326699596 \)</td>
    </tr>
    <tr style="border: 1px solid black;">
        <td style="border: 1px solid black;">Valor amostrado (\( \text{N}(\mu, \sigma) \))</td>
        <td style="border: 1px solid black;">\( 145.67723926735943 \)</td>
    </tr>
</table>

<h3>Atualização e Avaliação</h3>

<p align="justify">O novo valor gerado pela mutação é \( x' = [145.67723926735943] \). A função objetivo (\( \text{of} \)) e o fitness são calculados para comparar a solução mutada com a solução atual.</p>

<ul>
    <li>\( x_{\text{mutado}} = [145.67723926735943], \ \text{of}_{\text{mutado}} = -6.3297 \)</li>
    <li>Fitness da solução mutada: \( \text{fit}_{\text{mutado}} = 7.3297 \)</li>
    <li>Fitness da solução atual: \( \text{fit}_{\text{atual}} = 8.5079 \)</li>
</ul>

<p align="justify">Como o fitness da solução mutada (\( 7.3297 \)) é menor que o fitness da solução atual (\( 8.5079 \)), a nova solução <strong>não é aceita</strong>.</p>

<hr>

<h2>Atualização Final</h2>

<p align="justify">Ao final da iteração, a solução atual permanece inalterada, pois a solução mutada não foi aceita. O vetor atualizado é:</p>

<ul>
    <li>\( x_0 = [88.25395326699595], \ \text{of}_{\text{pop}} = -7.5079 \) - <strong>melhor solução</strong></li>
</ul>

<hr>

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
