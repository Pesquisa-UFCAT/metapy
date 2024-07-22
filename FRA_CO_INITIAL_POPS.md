---
layout: default
title: initial_pops
grand_parent: Framework
parent: Common Library functions
has_toc: false
nav_order: 3
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>initial_pops</h3>

<br>

<p align = "justify">
    This function randomly initializes a population of the metaheuristic algorithm for a given number of repetitions.
</p>

```python
initial_pops(n_repetitions, n_population, n_dimensions, x_lower, x_upper, type_pop, seeds)
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
        <td><code>n_repetitions</code></td>
        <td>Number of repetitions</td>
        <td>Integer</td>
    <tr>
        <td><code>n_population</code></td>
        <td>Number of population</td>
        <td>Integer</td>
    <tr>
        <td><code>n_dimensions</code></td>
        <td>Problem dimension</td>
        <td>Integer</td>
    <tr>
        <td><code>x_lower</code></td>
        <td>Lower limit of the design variables. Use None for combinatorial variables</td>
        <td>List or None</td>
    <tr>
        <td><code>x_upper</code></td>
        <td>Upper limit of the design variables. Use None for combinatorial variables</td>
        <td>List or None</td>
    <tr>
        <td><code>type_pop</code></td>
        <td>Type of population. Options: 'real code' or 'combinatorial code'. 'real code' call function initial_population_01 and 'combinatorial code' call function initial_population_02</td>
        <td>String</td>
    <tr>
        <td><code>seeds</code></td>
        <td>Random seed. Use None for random seed</td>
        <td>List or None</td>
    <tr>
        <td><code>population</code></td>
        <td>Population design variables. All repetitions</td>
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
        <td><code>population</code></td>
        <td>Population design variables. All repetitions</td>
        <td>List</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

Use the `initial_pops` function to randomly initialize the population required for four repetitions of the optimization procedure, where each solution set has two agents, and each has three dimensions. The design variables limits are $\mathbf{x}_L = \left[1,\;1,\;1\right]$ and $\mathbf{x}_U = \left[3,\;3,\;3\right]$. Use "seed without control" in your setup.

```python
# Import
# pip install metapy-toolbox or pip install --upgrade metapy-toolbox
from metapy_toolbox import initial_pops # or import *

# Data
nRep = 4
nPop = 2
d = 3
xL = [1, 1, 1]
xU = [3, 3, 3]
typeCode = 'real code'
seeds = [None, None, None, None]

# Call function
pops = initial_pops(nRep, nPop, d, xL, xU, typeCode, seeds)

# Output details
print('population repetition ID = 0: ', pops[0])
print('population repetition ID = 1: ', pops[1])
print('population repetition ID = 2: ', pops[2])
print('population repetition ID = 3: ', pops[3])
print('\nAgent example:')
print('init. population rep. ID = 0 - pop = 0: ', pops[0][0])
print('init. population rep. ID = 0 - pop = 1: ', pops[0][1])
```

```bash
population repetition ID = 0:  [[1.7569870977744084, 1.042806656388939, 2.9574518690911633], [2.516871253402986, 1.0623716942485755, 2.1845178409922843]]
population repetition ID = 1:  [[2.1662762308582373, 2.66090910550537, 2.474471453333295], [2.8198256171594864, 2.570566076401062, 1.7930497331754311]]
population repetition ID = 2:  [[1.66330938269935, 1.870843964868756, 1.5196732590734792], [2.8295716904027115, 1.4195645627391247, 1.6252392995992408]]
population repetition ID = 3:  [[1.418822142851461, 2.083824683419757, 1.717224896458115], [2.795448903059947, 2.242610136700492, 1.1159414911258083]]

Agent example:
init. population rep. ID = 0 - pop = 0:  [1.7569870977744084, 1.042806656388939, 2.9574518690911633]
init. population rep. ID = 0 - pop = 1:  [2.516871253402986, 1.0623716942485755, 2.1845178409922843]
```

Example 2
{: .label .label-blue }

Use the `initial_pops` function to randomly initialize the population required for four repetitions of the optimization procedure, where each solution set has two agents, and each has three dimensions. The design variables limits are $\mathbf{x}_L = \left[1,\;1,\;1\right]$ and $\mathbf{x}_U = \left[3,\;3,\;3\right]$. Use "seed control" in your setup. Suggest: $\mathbf{seed} = \left[ 10,\;11,\;12,\;13 \right]$.

```python
# Import
# pip install metapy-toolbox or pip install --upgrade metapy-toolbox 
from metapy_toolbox import initial_pops # or import *

# Data
nRep = 4
nPop = 2
d = 3
xL = [1, 1, 1]
xU = [3, 3, 3]
typeCode = 'real code'
seeds = [10, 11, 12, 13]

# Call function
pops = initial_pops(nRep, nPop, d, xL, xU, typeCode, seeds)

# Output details
print('population repetition ID = 0: ', pops[0])
print('population repetition ID = 1: ', pops[1])
print('population repetition ID = 2: ', pops[2])
print('population repetition ID = 3: ', pops[3])
print('\nAgent example:')
print('init. population rep. ID = 0 - pop = 0: ', pops[0][0])
print('init. population rep. ID = 0 - pop = 1: ', pops[0][1])
```

```bash
population repetition ID = 0:  [[2.5426412865334918, 1.041503898718803, 2.2672964698525506], [2.4976077650772237, 1.9970140246051808, 1.4495932910616953]]
population repetition ID = 1:  [[1.3605393777535384, 1.0389504829752492, 1.9264370529966892], [2.4498678583842954, 1.8404072091754549, 1.9708541963355648]]
population repetition ID = 2:  [[1.3083256847593447, 2.4800993930308097, 1.5266300303702693], [2.0674787867605957, 1.0291499249708393, 2.83749401619977]]
population repetition ID = 3:  [[2.5554048211476403, 1.4750824400698246, 2.648557065322737], [2.9314983960859995, 2.9452022278097867, 1.9068984948346244]]

Agent example:
init. population rep. ID = 0 - pop = 0:  [2.5426412865334918, 1.041503898718803, 2.2672964698525506]
init. population rep. ID = 0 - pop = 1:  [2.4976077650772237, 1.9970140246051808, 1.4495932910616953]
```

Example 3
{: .label .label-blue }

Use the `initial_pops` function to randomly initialize the population required for four repetitions of the optimization procedure, where each solution set has two agents, and each has three dimensions. Use the combinatorial process to generate an initial guess. Use "seed without control" in your setup.

```python
# Import
# pip install metapy-toolbox or pip install --upgrade metapy-toolbox 
from metapy_toolbox import initial_pops # or import *

# Data
nRep = 4
nPop = 2
d = 10
xL = None
xU = None
typeCode = 'combinatorial code'
seeds = [None, None, None, None]

# Call function
pops = initial_pops(nRep, nPop, d, xL, xU, typeCode, seeds)

# Output details
print('population repetition ID = 0: ', pops[0])
print('population repetition ID = 1: ', pops[1])
print('population repetition ID = 2: ', pops[2])
print('population repetition ID = 3: ', pops[3])
print('\n Agent example:')
print('init. population rep. ID = 0 - pop = 0: ', pops[0][0])
print('init. population rep. ID = 0 - pop = 1: ', pops[0][1])
```

```bash
population repetition ID = 0:  [[3, 9, 0, 1, 8, 5, 7, 6, 2, 4], [4, 9, 2, 1, 7, 6, 8, 5, 3, 0]]
population repetition ID = 1:  [[7, 9, 0, 1, 3, 5, 4, 2, 6, 8], [9, 6, 4, 3, 2, 7, 0, 1, 5, 8]]
population repetition ID = 2:  [[1, 4, 2, 5, 0, 8, 6, 7, 9, 3], [8, 2, 7, 1, 0, 5, 3, 9, 4, 6]]
population repetition ID = 3:  [[6, 5, 0, 7, 8, 1, 2, 3, 4, 9], [4, 7, 9, 6, 3, 2, 0, 8, 1, 5]]

 Agent example:
init. population rep. ID = 0 - pop = 0:  [3, 9, 0, 1, 8, 5, 7, 6, 2, 4]
init. population rep. ID = 0 - pop = 1:  [4, 9, 2, 1, 7, 6, 8, 5, 3, 0]
```
