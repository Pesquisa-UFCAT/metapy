---
title: Initial pop. 2
layout: home
grand_parent: Framework
parent: Common Library
has_children: true
nav_order: 2
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

```python

population = initial_population_02(nPop, d)
```

<p align = "justify">
    The function generates a random population. Combinatorial variables generator.
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
        <td><code>n_pop</code></td>
        <td>Number of population</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>d</code></td>
        <td>Problem dimension</td>
        <td>Integer</td>
    </tr>  
    <tr>
        <td><code>seed</code></td>
        <td>Control the seed for random numbers. It is used when you want to test the algorithm. Default <code>seed = None</code></td>
        <td>Null or Integer</td>
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
        <td><code>x_new</code></td>
        <td>All design variables</td>
        <td>Py list [N_POP] \( \times\) [D] </td>
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
particle 0:  [0, 1, 2]
particle 1:  [0, 1, 2]
particle 2:  [0, 2, 1]
particle 3:  [0, 2, 1]
particle 4:  [1, 2, 0]
```
