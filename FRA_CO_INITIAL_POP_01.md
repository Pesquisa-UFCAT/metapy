---
layout: default
title: initial_population_01
grand_parent: Framework
parent: Common Library functions
nav_order: 1
has_toc: false
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>initial_population_01</h3>

<br>

<p align = "justify">
    The function generates a random population with defined limits. Continuum variables generator.
</p>

```python
x_pop = initial_population_01(n_population, n_dimensions, x_lower, x_upper, seed=None)
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
        <td><code>n_population</code></td>
        <td>Number of population</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>n_dimensions</code></td>
        <td>Problem dimension</td>
        <td>Integer</td>
    </tr>  
    <tr>
        <td><code>x_lower</code></td>
        <td>Lower limit of the design variables</td>
        <td>List</td>
    </tr>  
    <tr>
        <td><code>x_upper</code></td>
        <td>Upper limit of the design variables</td>
        <td>List</td>
    </tr>    
    <tr>
        <td><code>seed</code></td>
        <td>Random seed. Default is None. Use None for random seed</td>
        <td>Integer or None</td>
    </tr>
</table>

Output variables
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
        <td><code>x_pop</code></td>
        <td>Population design variables</td>
        <td>List</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>initial_population_01</code> function to generate a new population (five agents) considering the limits \(\mathbf{x}_L = \left[1,\;1,\;2\right]\) and \(\mathbf{x}_U = \left[4,\;4,\;4\right]\).
    </i>
</p>

```python
# Import 
from metapy_toolbox import initial_population_01 # or import *

# Data
nPop = 5
xL = [1, 1, 2]
xU = [4, 4, 4]
d = len(xU) # or d = len(xL) or d = 3

# Call function
population = initial_population_01(nPop, d, xL, xU)

# Output details
print('particle 0: ', population[0])
print('particle 1: ', population[1])
print('particle 2: ', population[2])
print('particle 3: ', population[3])
print('particle 4: ', population[4])
```

```bash
particle 0:  [1.206696599676488, 3.6333795997730505, 2.7582027384444903]
particle 1:  [3.855855075161193, 2.387614157515121, 3.8073442405085656]
particle 2:  [1.7440060596179356, 3.4575301813292656, 3.384486502730728]
particle 3:  [2.487564137048481, 1.901279961962405, 2.146462080650636]
particle 4:  [2.8747948841114437, 3.253980082218285, 3.7593344650584686]
```
