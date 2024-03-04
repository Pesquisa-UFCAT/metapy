---
layout: default
title: differential_evolution_01
grand_parent: Framework
parent: Differential Evolution functions
has_children: false
has_toc: false
nav_order: 1
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>differential_evolution_01</h3>

<br>

<p align = "justify">
    Differential Evolution algorithm 01 (see <a target="_blank" rel="noopener" href="https://wmpjrufg.github.io/METAPY/LEARN_PROB_DE.html">theory</a>).
</p>

```python
df_all, df_best, delta_time, report = differential_evolution_01(settings)
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
        <td>Algorithm settings: [0] setup, [1] initial population, [2] seeds</td>
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
        <td>None variable. Default is None. User can use this variable in objective function</td>
        <td>None, list, float, dictionary, str or any</td>
    </tr>  
    <tr>
        <td><code>'objective function'</code></td>
        <td>Objective function. The Metapy user defined this function</td>
        <td>Py function (def)</td>
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
        <td><code>'crossover</code></td>
        <td><a href="#cro">Crossover parameters</a></td>
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

<p align = "justify" id = "cro">
    See examples of crossover operator.
</p>

<h4><i>de/rand/1</i></h4>

```python
'crossover': {'crossover rate (%)': 85, 'type': 'de/rand/1', 'scale factor (F)'}
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
        <td><code>'crossover rate (%)'</code></td>
        <td>Crossover rate in percentage</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>'type'</code></td>
        <td>Crossover type</td>
        <td>String</td>
    </tr>
    <tr>
        <td><code>'scale factor (F)'</code></td>
        <td>Scale factor</td>
        <td>Float</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
      Use the Differential Evolution Algorithm optimization method to optimize the 2D sphere function. Use a total of 100 iterations to perform the optimization. Consider the limits \(\mathbf{x}_L = [-5.0, -5.0]\) and \(\mathbf{x}_U = [5.0, 5.0]\) for the problem design variables. Consider the initial guess (Four agents) \(\mathbf{pop}_0 = [-0.74, 1.25]\), \(\mathbf{pop}_1 = [3.58, -3.33]\), \(\mathbf{pop}_2 = [1.50, 1.50]\) and \(\mathbf{pop}_3 = [1.0, 4.00]\). Use de/rand/1 for crossover (85% rate) and scale factor \(F=0.70\).
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
from metapy_toolbox import differential_evolution_01
from my_example import my_obj_function

# Algorithm setup
setup = {   
            'number of iterations': 100,
            'number of population': 4,
            'number of dimensions': 2,
            'x pop lower limit': [-5, -5],
            'x pop upper limit': [5, 5],
            'none variable': None,
            'objective function': my_obj_function,
            'algorithm parameters': {
                                        'crossover': {
                                                      'crossover rate (%)': 90, 
                                                      'type': 'de/rand/1', 
                                                      'scale factor (F)': 0.70
                                                     }
                                    }
        }

# Initial guess
init_pop = [[-0.74, 1.25],
            [3.58, -3.33],
            [1.50, 1.50],
            [1.00, 4.00]]
"""
or # random guess
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
df_all_results, df_resume, time_cost, report = differential_evolution_01(settings)
```

<ol>
    <li>
    Download <a href="https://github.com/wmpjrufg/METAPY/blob/gh-pages/Table%20test/report_genetic_algorithm_01.xlsx" target="_blank">table test</a>.
    </li>
    <li>
    Download <a href="https://github.com/wmpjrufg/METAPY/blob/gh-pages/Notebooks/00_example_genetic_algorithm_01.zip" target="_blank">notebook</a>.
    </li>
</ol>
