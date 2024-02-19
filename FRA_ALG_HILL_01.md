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

<h3>hill_climbing_01</h3>

<br>

<p align = "justify">
Hill Climbing algorithm (see <a target="_blank" rel="noopener" href="https://wmpjrufg.github.io/METAPY/LEARN_PROB_HILL.html">theory</a>).
</p>

```python
df_all, df_best, delta_time, report = hill_climbing_01(settings)
```

{: .warning }
> This function does not perform more than one repetition. To perform multiple repetitions, use the [metaheuristic_optimizer](https://wmpjrufg.github.io/METAPY/FRA_ALG_.html) function.

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
        <td>Algorithm settings: <code>[0]</code> setup (dict), <code>[1]</code> initial population (list), <code>[2]</code> seeds (int)</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>settings[0]</code> \(=\) <code>setup</code> (keys)</td>
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
        <td>Function - def</td>
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
        <td><code>'cov (%)'</code></td>
        <td>Coefficient of variation in percentage.</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>'pdf'</code></td>
        <td>Probability density function. Options: <code>'gaussian'</code> or <code>'uniform'</code></td>
        <td>String</td>
    </tr>
    <tr>
        <td><code>settings[1]</code> \(=\) initital population</td>
        <td>Users can inform the initial population or use <a target="_blank" rel="noopener" href="https://wmpjrufg.github.io/METAPY/FRA_CO_.html">initital population functions</a></td>
        <td>List or METApy function</td>
    </tr>
    <tr>
        <td><code>settings[2]</code> \(=\) seed</td>
        <td>Random seed. Use <code>None</code> for random seed</td>
        <td>None or Integer</td>
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