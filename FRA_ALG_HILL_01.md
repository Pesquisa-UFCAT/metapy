---
layout: default
title: hill_climbing_01
grand_parent: Framework
parent: Metaheuristics
has_toc: false
nav_order: 1
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

```python
x_pop = initial_population_01(n_population, n_dimensions, x_lower, x_upper, seed=None)
```

<p align = "justify">
    Hill Climbing algorithm.
</p>

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
        <td>OF_FUNCTION</td>
        <td>External def user input this function in arguments</td>
        <td>Py function</td>
    </tr>
    <tr>
        <td>SETUP</td>
        <td>Algorithm setup</td>
        <td>Py dictionary</td>
    </tr>
    <tr>
        <td></td>
        <td>'N_REP' = Number of repetitions</td>
        <td>Integer</td>
    </tr>    
    <tr>
        <td></td>
        <td>'N_ITER' = Number of iterations</td>
        <td>Integer</td>
    </tr> 
    <tr>
        <td></td>
        <td>'N_POP' = Number of population</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td></td>
        <td>'D' = Problem dimension</td>
        <td>Integer</td>
    </tr>  
    <tr>
        <td></td>
        <td>'X_L' = Lower limit design variables</td>
        <td>Py list[D]</td>
    </tr> 
    <tr>
        <td></td>
        <td>'X_U' = Upper limit design variables</td>
        <td>Py list[D]</td>
    </tr>
    <tr>
        <td></td>
        <td>'NULL_DIC' = Empty variable for the user to use in the obj. function</td>
        <td>Py dictionary</td>
    </tr>
    <tr>
        <td></td>
        <td>'PARAMETERS' = Algorithm parameters</td>
        <td>Py dictionary</td>
    </tr>    
    <tr>
        <td>PARAMETERS</td>
        <td>Algorithm parameters</td>
        <td>Py dictionary</td>
    </tr> 
    <tr>
        <td></td>
        <td>'PERCENTAGE STD (SIGMA)' = Standard deviation the normal distribution in percentage (\(\sigma\))</td>
        <td>Float</td>
    </tr>
</table>

<h4>Output variables</h4>

<table style = "width:100%">
    <tr>
        <td>RESULTS_REP</td>
        <td>All results of population movement by repetition</td>
        <td>Py dictionary</td>
    </tr>
    <tr>
        <td></td>
        <td>'X_POSITION' = Design variables by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x D]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'OF' = Obj function value by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'FIT' = Fitness value by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'PARAMETERS' = Algorithm parameters</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'NEOF' = Number of objective function evaluations</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>
    <tr>
        <td></td>
        <td>'ID_PARTICLE' = ID particle</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td>BEST_REP</td>
        <td>Best population results by repetition</td>
        <td>Py dictionary</td>
    </tr>
    <tr>
        <td></td>
        <td>'X_POSITION' = Design variables by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x D]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'OF' = Obj function value by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'FIT' = Fitness value by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'PARAMETERS' = Algorithm parameters</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'NEOF' = Number of objective function evaluations</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>
    <tr>
        <td></td>
        <td>'ID_PARTICLE' = ID particle</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr> 
    <tr>
        <td>AVERAGE_REP</td>
        <td>Average OF and FIT results by repetition</td>
        <td>Py dictionary</td>
    </tr>
    <tr>
        <td></td>
        <td>'OF' = Obj function value by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'FIT' = Fitness value by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'NEOF' = Number of objective function evaluations</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>
    <tr>
        <td>WORST_REP</td>
        <td>Worst OF and FIT results by repetition</td>
        <td>Py dictionary</td>
    </tr>
    <tr>
        <td></td>
        <td>'X_POSITION' = Design variables by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x D]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'OF' = Obj function value by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'FIT' = Fitness value by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'PARAMETERS' = Algorithm parameters</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'NEOF' = Number of objective function evaluations</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>
    <tr>
        <td></td>
        <td>'ID_PARTICLE' = ID particle</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr> 
    <tr>
        <td>STATUS_PROCEDURE</td>
        <td>Process repetition ID - from lowest OF value to highest OF value</td>
        <td>Py list[N_REP]</td>
    </tr> 
</table>

Theory
{: .label .label-red }

<p align = "justify">
Hill Climbing was one of the first existing stochastic optimization algorithms in the literature. The Hill Climbing method is also known as a local search method <a href="#ref1">[1]</a>.
<br><br>
The iterative procedure is based on continuously improving the solution until the best solution is attained. The process consists of generating random neighbors of the current solution, according to the equation <a href="#eq1">(1)</a>, where \(\symbf{N}\) indicates a Gaussian or Uniform distribution where the mean \(\symbf{x}^{t}\) is the current solution and \(\sigma\) is the standard deviation input by the user. \(k\) is the kth component of the design variable vector \(\symbf{x}\).
</p>

<table border = "0" style = "width:100%">
    <tr>
        <td>\[\symbf{x}_{k}^{t+1} = \symbf{N}(\symbf{x}_{k}^{t}, \sigma)\]</td>
        <td><p align = "justify">random neighbour</p></td>
        <td><p align = "right" id = "eq1">(1)</p></td>
    </tr>
</table>

<h3><i>Algorithm</i></h3>

```python
1:  Input initial parameters (SIGMA)
2:  X = Initial solution
3:  Calculate OF and FIT
4:  for T in range(N_ITER):
5:      X_TEMP = neighbor solution equation (1)
6:      if f(X_TEMP) <= f(X):
7:         X(T+1) = X_TEMP
```

Reference list
{: .label .label-yellow }

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
