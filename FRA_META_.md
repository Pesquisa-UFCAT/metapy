---
layout: default
title: metaheuristic_optimizer
parent: Framework
has_children: false
has_toc: false
nav_order: 1
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>metaheuristic_optimizer</h3>

<br>

<p align = "justify">
    This function is responsible for the metaheuristic optimization process. It is a general function that calls the specific algorithm functions.
</p>


```python
df_all_reps, df_resume_all_reps,\
            reports, status = metaheuristic_optimizer(algorithm_setup,
                                                        general_setup)
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
        <td><code>algorithm_setup</code></td>
        <td><p align = "justify">Metaheuristic optimization setup. See algorithms documentation for more details. <a href="#alg">Use the same setup dictionary as the desired optimization method here</a></p></td>
        <td>Dictionary</td>
    </tr>
    <tr>
        <td><code>general_setup</code></td>
        <td>Optimization process setup</td>
        <td>Dictionary</td>
    </tr>
    <tr>
        <td><code>general_setup</code> keys</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><code>'number of repetitions'</code></td>
        <td>Number of repetitions</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>'type code'</code></td>
        <td>Type of population. Options: 'real code' or 'combinatorial code'</td>
        <td>String</td>
    </tr>
    <tr>   
        <td><code>'initial pop. seed'</code></td>
        <td>Random seed. Use None in list for random seed</td>
        <td>List</td>
    </tr>
    <tr>   
        <td><code>'algorithm'</code></td>
        <td>Optimization algorithm. See the <a href="#alg">available metaheuristic algorithms</a></td>
        <td>String</td>
    </tr> 
</table>

Output variables
{: .label .label-yellow }

<table style = "width:100%">
    <tr>
        <td><code>df_all</code></td>
        <td>All data on the population</td>
        <td>Dataframe</td>
    </tr>
    <tr>
        <td><code>df_best</code></td>
        <td>Best data on the population</td>
        <td>Dataframe</td>
    </tr>  
    <tr>
        <td><code>reports</code></td>
        <td>Report about the repetition process</td>
        <td>String</td>
    </tr>  
    <tr>
        <td><code>status</code></td>
        <td>Best repetition \(id\)</td>
        <td>Integer</td>
    </tr>  
</table>

<p align = "justify"  id = "alg">
Metaheuristic algorithms.
</p>

<table style = "width:100%">
    <thead>
      <tr>
        <th>Function</th>
        <th>Name</th>
      </tr>
    </thead> 
    <tr>
        <td><code>'hill_climbing_01'</code></td>
        <td><a href="https://wmpjrufg.github.io/METAPY/FRA_SA_HILL.html" target="_blank" rel="noopener noreferrer">Hill Climbing algorithm 01</a></td>
    </tr>
    <tr>
        <td><code>'simulated_annealing_01'</code></td>
        <td><a href="https://wmpjrufg.github.io/METAPY/FRA_SA_SA.html" target="_blank" rel="noopener noreferrer">Simulated Annealing algorithm 01</a></td>
    </tr>
    <tr>
        <td><code>'genetic_algorithm_01'</code></td>
        <td><a href="https://wmpjrufg.github.io/METAPY/FRA_GA_GA.html" target="_blank" rel="noopener noreferrer">Genetic Algorithm 01</a></td>
    </tr>
    <!-- <tr>
        <td><code>'differential_evolution_01'</code></td>
        <td>Differential Evolution algorithm 01</td>
    </tr> -->
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
      Use the hill climbing optimization method to optimize the 2D sphere function. Use a total of 100 iterations to perform the optimization. Consider the limits \(\mathbf{x}_L = [-5.0, -5.0]\) and \(\mathbf{x}_U = [5.0, 5.0]\) for the problem design variables. Use \(cov = 20%\), Gaussian random generator, and random initial guess. Run this complete process 30 times. Consider a population of 10 agents.
  </i>
</p>

```python
"""Object Function: my_example.py"""
def my_obj_function(x, none_variable):
    return x[0]**2 + x[1]**2
```

```python
# import libray
# pip install metapy-toolbox
from metapy_toolbox import metaheuristic_optimizer
from my_example import my_obj_function # External .py file with your objective function

# Algorithm settings
algorithm_setup = {   
            'number of iterations': 100,
            'number of population': 2,
            'number of dimensions': 2,
            'x pop lower limit': [-5, -5],
            'x pop upper limit': [5, 5],
            'none variable': None,
            'objective function': my_obj_function,
            'algorithm parameters': {
                                        'mutation': {
                                                     'cov (%)': 20,
                                                     'pdf': 'gaussian'
                                                    }
                                    },
        }

# METApy settings
general_setup = {   
            'number of repetitions': 30,
            'type code': 'real code',
            'initial pop. seed': [None] * 30,
            'algorithm': 'hill_climbing_01',
        }

# Run algorithm
df_all_reps, df_resume_all_reps, reports, status = metaheuristic_optimizer(algorithm_setup, general_setup)
```

```bash
 Optimization results: 

 - Best repetition id:  28
 - Best of:             5.3042292250e-16
 - Design variables:    [2.100789251887419e-08, 9.438822723774955e-09]
 - Process time (s):    3.779469
```

Analysis
{: .label .label-yellow }

<p align="justify">See the details repetition \(id = 0\). <code>df_resume_all_reps</code> contains history details the best particle in \(id = 0\) repetition.</p>

```python
print(df_resume_all_reps[0])
```

<p align="justify">To see all population history in repetition \(id = 0\) use:</p>

```python
print(df_all_reps[0])
```

<p align="justify">See best\(id\) in repetitions:</p>

```python
print(status)
```
<p align="justify">See best repetition:</p>

```python
print(df_resume_all_reps[status])
```

<p align="justify">See complete report about best repetition:</p>

```python
# Report details
arq = "report_example.txt"

# Writing report
with open(arq, "w") as file:
    file.write(report[status])
```
