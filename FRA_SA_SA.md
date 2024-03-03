---
layout: default
title: simulated_annealing_01
grand_parent: Framework
parent: Simulated Annealing functions
has_toc: false
nav_order: 2
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>simulated_annealing_01</h3>

<br>

<p align = "justify">
Simulated Annealing algorithm (see <a target="_blank" rel="noopener" href="https://wmpjrufg.github.io/METAPY/LEARN_PROB_SA.html">theory</a>).
</p>

```python
df_all, df_best, delta_time, report = simulated_annealing_01(settings)
```

{: .warning }

> This function does not perform more than one repetition. To perform multiple repetitions, use the [metaheuristic_optimizer](https://wmpjrufg.github.io/METAPY/FRA_META_.html) function.

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
        <td><code>settings</code></td>
        <td>Algorithm settings: <code>[0]</code> setup, <code>[1]</code> initial population, <code>[2]</code> seeds</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>settings[0]</code> \(=\) setup</td>
        <td>Algorithm setup</td>
        <td>Dictionary</td>
    </tr>
    <tr>
        <td><code>setup</code> keys</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><code>'number of population'</code></td>
        <td>Number of population</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>'number of iterations'</code></td>
        <td>Number of iterations</td>
        <td>Integer</td>
    </tr> 
    <tr>
        <td><code>'number of dimensions'</code></td>
        <td>Problem dimension</td>
        <td>Integer</td>
    </tr> 
    <tr>
        <td><code>'x pop lower limit'</code></td>
        <td>Lower limit of the design variables</td>
        <td>List</td>
    </tr>  
    <tr>
        <td><code>'x upper lower limit'</code></td>
        <td>Upper limit of the design variables</td>
        <td>List</td>
    </tr>  
    <tr>
        <td><code>'none variable'</code></td>
        <td>None variable. Default is <code>None</code>. User can use this variable in objective function</td>
        <td>None, list, float, dictionary, str or any</td>
    </tr>  
    <tr>
        <td><code>'objective function'</code></td>
        <td>Objective function. The Metapy user defined this function</td>
        <td>Py function (<code>def</code>)</td>
    </tr>  
    <tr>
        <td><code>'algorithm parameters'</code></td>
        <td>Algorithm parameters</td>
        <td>Dictionary</td>
    </tr>   
    <tr>
        <td><code>'algorithm parameters'</code> keys</td>
        <td></td>
        <td></td>
    </tr> 
    <tr>
        <td><code>'mutation'</code></td>
        <td><a href="#mut">Mutation parameters</a></td>
        <td>Dictionary</td>
    </tr>   
    <tr>
        <td><code>'temp. control'</code></td>
        <td><a href="#temp">Temperature parameters</a></td>
        <td>Dictionary</td>
    </tr>  
    <tr>
        <td><code>settings[1]</code> \(=\) initial population</td>
        <td>Users can inform the initial population or use <a target="_blank" rel="noopener" href="https://wmpjrufg.github.io/METAPY/FRA_CO_.html">initial population functions</a></td>
        <td>List or METApy function</td>
    </tr>
    <tr>
        <td><code>settings[2]</code> \(=\) seed</td>
        <td>Random seed. Use <code>None</code> for random seed</td>
        <td>None or Integer</td>
    </tr> 
</table>

Output variables
{: .label .label-yellow }

<table style = "width:100%">
    <tr>
        <td><code>df_all</code></td>
        <td>All data of the population</td>
        <td>Dataframe</td>
    </tr>
    <tr>
        <td><code>df_best</code></td>
        <td>Best data of the population</td>
        <td>Dataframe</td>
    </tr>  
    <tr>
        <td><code>delta_time</code></td>
        <td>Time of the algorithm execution in seconds</td>
        <td>Float</td>
    </tr>  
    <tr>
        <td><code>report</code></td>
        <td>Report of the algorithm execution</td>
        <td>String</td>
    </tr>  
</table>

<h4><p align = "justify"  id = "mut">Mutation parameters</p></h4>

```python
'mutation': {
             'cov (%)': 20,
             'pdf': 'gaussian'
            }
```

<table style = "width:100%">
    <thead>
      <tr>
        <th>Name</th>
        <th>Description</th>
        <th>Type</th>
      </tr>
    </thead> 
    <tr>
        <td><code>'cov (%)'</code></td>
        <td>Coefficient of variation in percentage</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>'pdf'</code></td>
        <td>Probability density function used in random generator. Options: <code>'gaussian'</code> or <code>'uniform'</code></td>
        <td>String</td>
    </tr>
</table>

{: .note }

> In no original algorithm the mutation rate is 100% for all iterations. The type is also `hill_climbing` only.

<h4><p align = "justify"  id = "temp">Temperature parameters</p></h4>

```python
'temp. control': {
                  'temperature t_0': 15,
                  'temperature update': 'geometric',
                  'alpha': 0.9
                 }
```

<table style = "width:100%">
    <thead>
      <tr>
        <th>Name</th>
        <th>Description</th>
        <th>Type</th>
      </tr>
    </thead> 
    <tr>
        <td><code>'temperature t_0'</code></td>
        <td>Initial temperature. <code>'auto'</code>: Automatic starts cooling temperature. For specific value, use a float number (see <a target="_blank" rel="noopener" href="https://wmpjrufg.github.io/METAPY/LEARN_PROB_SA.html#temp">theory</a>)</td>
        <td>Float or String</td>
    </tr>
    <tr>
        <td><code>'temperature update'</code></td>
        <td>Cooling schema (see <a target="_blank" rel="noopener" href="https://wmpjrufg.github.io/METAPY/LEARN_PROB_SA.html#colling">theory</a>):<br>
        <ul>
        <li><code>'geometric'</code></li>
        <li><code>'lundy'</code></li>
        <li><code>'linear'</code></li>
        <li><code>'exponential'</code></li>
        </ul>
        </td>
        <td>String</td>
    </tr>
    <tr>
        <td><code>'alpha'</code></td>
        <td>Cooling control (see <a target="_blank" rel="noopener" href="https://wmpjrufg.github.io/METAPY/LEARN_PROB_SA.html#colling">theory</a>)</td>
        <td>Float</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
      Use the Simulated Annealing optimization method to optimize the 2D sphere function. Use a total of 100 iterations to perform the optimization. Consider the limits \(\mathbf{x}_L = [-5.0, -5.0]\) and \(\mathbf{x}_U = [5.0, 5.0]\) for the problem design variables. Consider the initial guess (two agents) \(\mathbf{pop}_0 = [-0.74, 1.25]\) and \(\mathbf{pop}_1 = [3.58, -3.33]\). Use \(cov = 20\%\), Gaussian random generator, \(T_0 = 15\) and geometric schedule (\(\alpha = 0.90\)).
  </i>
</p>

```python
"""Object Function: my_example.py"""
def my_obj_function(x, none_variable):
    return x[0]**2 + x[1]**2
```

```python
"""Run optimization"""
# Import Library
from metapy_toolbox import simulated_annealing_01
from my_example import my_obj_function

# Algorithm setup
setup = {
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
                                                    },
                                        'temp. control': {
                                                          'temperature t_0': 15,
                                                          'temperature update': 'geometric',
                                                          'alpha': 0.9
                                                         }
                                    },
        }

# Initial guess
init_pop = [[-0.74, 1.25],
            [3.58, -3.33]]
"""
# or random initial guess (real design variables)
from metapy_toolbox import initial_population_01
init_pop = initial_population_01(setup['number of population'],
                                setup['number of dimensions'],
                                setup['x pop lower limit'],
                                setup['x pop upper limit'])
"""

# Seed
seed = None

# Call function
settings = [setup, init_pop, seed]
df_all_results, df_resume, time_cost, report = simulated_annealing_01(settings)
```
<!-- 
<ol>
    <li>
    Download <a href="https://github.com/wmpjrufg/METAPY/blob/gh-pages/Table%20test/report_simulated_annealing_01.xlsx" target="_blank">table test</a>.
    </li>
    <li>
    Download <a href="https://github.com/wmpjrufg/METAPY/blob/gh-pages/Notebooks/00_example_simulated_annealing_01.zip" target="_blank">notebook</a>.
    </li>
</ol> -->
