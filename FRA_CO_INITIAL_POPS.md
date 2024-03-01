---
layout: default
title: initial_pops
grand_parent: Framework
parent: Common Library
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
population = initial_pops(n_repetitions, n_populatio, n_dimensions,
                            x_lower, x_upper, type_pop, seeds)
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
    </tr>
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
        <td>Lower limit of the design variables. Use <code>None</code> for combinatorial variables</td>
        <td>List or None</td>
    </tr>
    <tr>
        <td><code>x_upper</code></td>
        <td>Upper limit of the design variables. Use <code>None</code> for combinatorial variables</td>
        <td>List or None</td>
    </tr>
    <tr>
        <td><code>type_pop</code></td>
        <td>Type of population. Options: <code>'real code'</code> or <code>'combinatorial code'</code></td>
        <td>String</td>
    </tr>
    <tr>
        <td><code>seeds</code></td>
        <td>Random seed. Use <code>None</code> in list for random seed</td>
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

<p align = "justify">
    <i>
        Use the <code>initial_pops</code> function to randomly initialize the population required for four repetitions of the optimization procedure, where each solution set has two agents, and each has three dimensions. The design variables limits are \(\mathbf{x}_L = \left[1,\;1,\;1\right]\) and \(\mathbf{x}_U = \left[3,\;3,\;3\right]\). Use "seed without control" in your setup.
    </i>
</p>

```python
# Import 
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
print('\n Agent example:')
print('init. population rep. ID = 0 - pop = 0: ', pops[0][0])
print('init. population rep. ID = 0 - pop = 1: ', pops[0][1])
```

```bash
population repetition ID = 0:  [[1.1359865490814205, 1.9931752417282842, 1.0847618980701748], [2.832494224437009, 1.0308454714359216, 1.6084514693314158]]
population repetition ID = 1:  [[2.562529253197214, 1.335050948532941, 2.471126286418664], [1.7419058478442666, 1.9078061098864592, 1.9528020890071016]]
population repetition ID = 2:  [[2.348291662377105, 2.2466499984534245, 1.6412960829528787], [1.1203068212210328, 1.7563980550149785, 1.6043992339627355]]
population repetition ID = 3:  [[2.2405106223759903, 2.17166926457243, 1.9455074174195885], [2.932186892245638, 2.1583902072567573, 2.616713054507649]]

 Agent example:
init. population rep. ID = 0 - pop = 0:  [1.1359865490814205, 1.9931752417282842, 1.0847618980701748]
init. population rep. ID = 0 - pop = 1:  [2.832494224437009, 1.0308454714359216, 1.6084514693314158]
```

Example 2
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>initial_pops</code> function to randomly initialize the population required for four repetitions of the optimization procedure, where each solution set has two agents, and each has three dimensions. The design variables limits are \(\mathbf{x}_L = \left[1,\;1,\;1\right]\) and \(\mathbf{x}_U = \left[3,\;3,\;3\right]\). Use "seed control" in your setup. Suggest: \(\mathbf{seed} = \left[ 10,\;11,\;12,\;13 \right]\)
    </i>
</p>

```python
# Import 
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
print('\n Agent example:')
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

<p align = "justify">
    <i>
        Use the <code>initial_pops</code> function to randomly initialize the population required for four repetitions of the optimization procedure, where each solution set has two agents, and each has three dimensions. Use the combinatorial process to generate an initial guess. Use "seed without control" in your setup.
    </i>
</p>

```python
# Import 
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
