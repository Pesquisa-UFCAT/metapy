---
layout: default
title: genetic_algorithm_01
grand_parent: Framework
parent: Genetic Algorithm functions
has_children: false
has_toc: false
nav_order: 1
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>genetic_algorithm_01</h3>

<br>

<p align = "justify">
    Genetic Algorithm 01 (see <a target="_blank" rel="noopener" href="https://wmpjrufg.github.io/METAPY/LEARN_PROB_GA.html">theory</a>).
</p>

```python
df_all, df_best, delta_time, report = hill_climbing_01(settings)
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
        <td><code>'selection'</code></td>
        <td><a href="#sele">Selection parameters</a></td>
        <td>Dictionary</td>
    </tr>
    <tr>
        <td><code>'crossover</code></td>
        <td><a href="#cro">Crossover parameters</a></td>
        <td>Dictionary</td>
    </tr>
    <tr>
        <td><code>'mutation'</code></td>
        <td><a href="#mut">Mutation parameters</a></td>
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

<h4><p align = "justify" id = "sele">Selection operator</p></h4>

<h5>Roulete wheel</h5>

```python
'selection': {'type': 'roulette'}
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
        <td><code>'type'</code></td>
        <td>Selection type</td>
        <td>String</td>
    </tr>
</table>

<h4><p align = "justify" id = "cro">Crossover operator</p></h4>

<h5>Linear crossover</h5>

```python
'crossover': {'crossover rate (%)': 85, 'type': 'linear'}
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
</table>

<h5><i>BLX-alpha crossover</i></h5>

```python
'crossover': {'crossover rate (%)': 20, 'type': 'blx-alpha'}
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
</table>

<h5><i>Single point crossover</i></h5>

```python
'crossover': {'crossover rate (%)': 20, 'type': 'single point'}
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
</table>

{: .warning }
> This method only works for problems of dimension >= 3.

<h5><i>Multi point crossover</i></h5>

```python
'crossover': {'crossover rate (%)': 20, 'type': 'multi point'}
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
</table>

{: .warning }
> This method only works for problems of dimension >= 4.

<h5><i>Uniform crossover</i></h5>

```python
'crossover': {'crossover rate (%)': 20, 'type': 'uniform'}
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
</table>

<h5><i>Heuristic crossover</i></h5>

```python
'crossover': {'crossover rate (%)': 20, 'type': 'heuristic'}
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
</table>

<h5><i>Arithmetic crossover</i></h5>

```python
'crossover': {'crossover rate (%)': 20, 'type': 'arithmetic', 'alpha': 0.86}
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
        <td><code>'alpha'</code></td>
        <td>Arithmetic crossover parameter</td>
        <td>Float</td>
    </tr>
</table>

<h5><i>Simulated Binary crossover</i></h5>

```python
'crossover': {'crossover rate (%)': 20, 'type': 'sbc', 'eta_c': 2}
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
        <td><code>'eta_c'</code></td>
        <td>Distribution index</td>
        <td>Float</td>
    </tr>
</table>

<h5><i>Laplace crossover</i></h5>

```python
'crossover': {'crossover rate (%)': 20, 'type': 'laplace', 'loc': 0, 'scale': 0.5}
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
        <td><code>'loc'</code></td>
        <td>location parameter</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>'scale'</code></td>
        <td>scale parameter</td>
        <td>Float</td>
    </tr>
</table>


<h4><p align = "justify" id = "mut">Mutation operator</p></h4>

<h5>Hill Climbing</h5>

```python
'mutation': {'mutation rate (%)': 15, 'type': 'hill climbing', 'cov (%)': 20, 'pdf': 'gaussian'}
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
        <td><code>'mutation rate (%)'</code></td>
        <td>Mutation rate in percentage</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>'type'</code></td>
        <td>Mutation type</td>
        <td>String</td>
    </tr>
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

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
      Use the Genetic Algorithm optimization method to optimize the 2D sphere function. Use a total of 100 iterations to perform the optimization. Consider the limits \(\mathbf{x}_L = [-5.0, -5.0]\) and \(\mathbf{x}_U = [5.0, 5.0]\) for the problem design variables. Consider the initial guess (three agents) \(\mathbf{pop}_0 = [-0.74, 1.25]\), \(\mathbf{pop}_1 = [3.58, -3.33]\) and \(\mathbf{pop}_2 = [1.50, 1.50]\). Use roulette wheel for selection procedure, linear crossover for crossover (82% rate) and hill climbing mutation (12% rate, \(cov=15\%\) and Gaussian generator).
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
from metapy_toolbox import genetic_algorithm_01
from my_example import my_obj_function

# Algorithm setup
setup = {   
            'number of iterations': 100,
            'number of population': 3,
            'number of dimensions': 2,
            'x pop lower limit': [-5, -5],
            'x pop upper limit': [5, 5],
            'none variable': None,
            'objective function': my_obj_function,
            'algorithm parameters': {
                                     'selection': {'type': 'roulette'},
                                     'crossover': {'crossover rate (%)': 82, 'type':'linear'},
                                     'mutation': {'mutation rate (%)': 12, 'type': 'hill climbing', 'cov (%)': 15, 'pdf': 'gaussian'},
                                    }
        }

# Initial guess
init_pop = [[-0.74, 1.25],
            [3.58, -3.33],
            [1.50, 1.50]]
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
df_all_results, df_resume, time_cost, report = genetic_algorithm_01(settings)
```

<!-- 
<ol>
    <li>
    Download <a href="https://github.com/wmpjrufg/METAPY/blob/gh-pages/Table%20test/report_genetic_algorithm_01.xlsx" target="_blank">table test</a>.
    </li>
    <li>
    Download <a href="https://github.com/wmpjrufg/METAPY/blob/gh-pages/Notebooks/00_example_genetic_algorithm_01.zip" target="_blank">notebook</a>.
    </li>
</ol> -->