---
layout: default
title: Initial pops
grand_parent: Framework
parent: Common Library
has_toc: false
nav_order: 3
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

```python
population = initial_pops(n_repetitions, n_populationulation, n_dimensions,
                            x_lowerower, x_upper, type_pop, seeds)
```

<p align = "justify">
    This function randomly initializes a population of procedures for a given number of repetitions.
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
        <td><code>n_repetitions</code></td>
        <td>Number of repetitions</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>n_population</code></td>
        <td>Number of population.</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>n_dimensions</code></td>
        <td>Problem dimension</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>x_lower</code></td>
        <td>Lower limit of the design variables. Use <code>None</code> for combinatorial variables.</td>
        <td>List or None</td>
    </tr>
    <tr>
        <td><code>x_upper</code></td>
        <td>Upper limit of the design variables. Use <code>None</code> for combinatorial variables.</td>
        <td>List or None</td>
    </tr>
    <tr>
        <td><code>type_pop</code></td>
        <td>Type of population. Options: <code>'real code'</code> or <code>'combinatorial code'</code>.</td>
        <td>String</td>
    </tr>
    <tr>
        <td><code>seeds</code></td>
        <td>Random seed. Use <code>None</code> for random seed.</td>
        <td>List or None</td>
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
        <td>Population design variables. All repetitions.</td>
        <td>List</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>initial_pops</code> function to randomly initialize the population required for four repetitions of the optimization procedure, where each solution set has two agents, and each has three dimensions. Generation values ​​are between \(\mathbf{x}_L = \left[1,\;1,\;1\right]\) and \(\mathbf{x}_U = \left[3,\;3,\;3\right]\). Use "seed without control" in your setup.
    </i>
</p>

```python
# Data
nRep = 4
nPop = 2
d = 3
xL = [1, 1, 1]
xU = [3, 3, 3]
typeCode = 'real code'
seeds = None

# Call function
pops = initial_pops(nRep, nPop, d, xL, xU, typeCode, seeds)

# Output details
print('population repetition ID = 0: ', pops[0])
print('population repetition ID = 1: ', pops[1])
print('population repetition ID = 2: ', pops[2])
print('population repetition ID = 3: ', pops[3])
print('\n Agent example:')
print('init. population rep. ID = 0 - agent id = 0: ', pops[0][0])
print('init. population rep. ID = 0 - agent id = 1: ', pops[0][1])
```

```bash
population repetition ID = 0:  [[2.2196326014139323, 1.3840517317205192, 2.6116781074286313], [1.3403223273226081, 1.1674717842974527, 2.2436660854022747]]
population repetition ID = 1:  [[2.254591881105598, 1.1077574733049664, 1.9129032401629404], [2.5519888813800913, 2.1522163950561666, 2.54366540526461]]
population repetition ID = 2:  [[2.283743242030489, 2.284006259927572, 2.454720419092418], [1.5915597454398382, 1.0423599148278597, 1.8482867884497962]]
population repetition ID = 3:  [[1.8937748864434991, 1.5110123109265392, 2.8229927611822845], [2.7585766165646697, 2.8376271268544357, 2.127148509873788]]

 Agent example:
init. population rep. ID = 0 - agent id = 0:  [2.2196326014139323, 1.3840517317205192, 2.6116781074286313]
init. population rep. ID = 0 - agent id = 1:  [1.3403223273226081, 1.1674717842974527, 2.2436660854022747]
```

Example 2
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>initial_pops</code> function to randomly initialize the population required for four repetitions of the optimization procedure, where each solution set has two agents, and each has three dimensions. Generation values ​​are between \(\mathbf{x}_L = \left[1,\;1,\;1\right]\) and \(\mathbf{x}_U = \left[3,\;3,\;3\right]\). Use "seed control" in your setup. Suggest: \(\mathbf{seeds} = \left[10,\;11,\;10,\;11\right]\).
    </i>
</p>

```python
# Data
nRep = 4
nPop = 2
d = 3
xL = [1, 1, 1]
xU = [3, 3, 3]
typeCode = 'real code'
seeds = [10, 11, 10, 11]

# Call function
pops = initial_pops(nRep, nPop, d, xL, xU, typeCode, seeds)

# Output details
print('population repetition ID = 0: ', pops[0])
print('population repetition ID = 1: ', pops[1])
print('population repetition ID = 2: ', pops[2])
print('population repetition ID = 3: ', pops[3])
print('\n Agent example:')
print('init. population rep. ID = 0 - agent id = 0: ', pops[0][0])
print('init. population rep. ID = 0 - agent id = 1: ', pops[0][1])
```

```bash
population repetition ID = 0:  [[2.5426412865334918, 1.041503898718803, 2.2672964698525506], [2.4976077650772237, 1.9970140246051808, 1.4495932910616953]]
population repetition ID = 1:  [[1.3605393777535384, 1.0389504829752492, 1.9264370529966892], [2.4498678583842954, 1.8404072091754549, 1.9708541963355648]]
population repetition ID = 2:  [[2.5426412865334918, 1.041503898718803, 2.2672964698525506], [2.4976077650772237, 1.9970140246051808, 1.4495932910616953]]
population repetition ID = 3:  [[1.3605393777535384, 1.0389504829752492, 1.9264370529966892], [2.4498678583842954, 1.8404072091754549, 1.9708541963355648]]

 Agent example:
init. population rep. ID = 0 - agent id = 0:  [2.5426412865334918, 1.041503898718803, 2.2672964698525506]
init. population rep. ID = 0 - agent id = 1:  [2.4976077650772237, 1.9970140246051808, 1.4495932910616953]
```
