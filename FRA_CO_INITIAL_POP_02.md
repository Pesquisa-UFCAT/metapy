---
layout: default
title: initial_population_02
grand_parent: Framework
parent: Common Library functions
nav_order: 2
has_toc: false
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>initial_population_02</h3>

<br>

<p align = "justify">
    The function generates a random population. Combinatorial variables generator.
</p>

```python
initial_population_02(n_population, n_dimensions, seed=None)
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
        <td><code>seed</code></td>
        <td>Random seed. Default is None</td>
        <td>Integer or None</td>
    </tr>
    <tr>
        <td><code>x_pop</code></td>
        <td>Population design variables</td>
        <td>List</td>
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
    Use the <code>initial_population_02</code> function to generate a new population (five agents) considering the three dimensional combinatorial problem. 
    </i>
</p>

```python
# Import
# pip install metapy-toolbox or pip install --upgrade metapy-toolbox
from metapy_toolbox import initial_population_02 # or import *

# Data
nPop = 5
d = 3

# Call function
population = initial_population_02(nPop, d)

# Output details
print('particle 0: ', population[0])
print('particle 1: ', population[1])
print('particle 2: ', population[2])
print('particle 3: ', population[3])
print('particle 4: ', population[4])
```

```bash
particle 0:  [1, 0, 2]
particle 1:  [2, 1, 0]
particle 2:  [2, 1, 0]
particle 3:  [2, 0, 1]
particle 4:  [2, 1, 0]
```
