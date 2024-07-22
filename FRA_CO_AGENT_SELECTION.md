---
layout: default
title: agent_selection
grand_parent: Framework
parent: Common Library functions
has_toc: false
nav_order: 8
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>agent_selection</h3>

<br>

<p align = "justify">
    This function selects a n agents from all population (uniform selection).
</p>

```python
agent_selection(n_population, n, i_pop=False)
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
    <tr>
        <td><code>n</code></td>
        <td>Number of agents to select</td>
        <td>Integer</td>
    <tr>
        <td><code>i_pop</code></td>
        <td>Default is False (Selects n agents among all population). i_pop=Integer Selects n agents among all population, excluding i_pop agent</td>
        <td>Integer or Boolean</td>
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
        <td><code>selected</code></td>
        <td>Selected agents.</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>report</code></td>
        <td>Report about the selection process.</td>
        <td>String</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

Select three agents from population $n_{pop} = 5$, except agent $i=2$.

```python
# Import
# pip install metapy-toolbox or pip install --upgrade metapy-toolbox
from metapy_toolbox import agent_selection # or import *

# Data
nPop = 5
n = 3
excludedAgent = 2

# Call function
selected, report = agent_selection(nPop, n, excludedAgent)
print(f'selected ids from population: {selected} \n')
print(report)
```

```bash
selected ids from population: [1 0 3] 

    Selection population operator
    probs = [0.25, 0.25, 0.0, 0.25, 0.25]
    the selected agents = [1 0 3]
```

Example 2
{: .label .label-blue }

Select three agents from population $n_{pop} = 5$.

```python
# Import
# pip install metapy-toolbox or pip install --upgrade metapy-toolbox
from metapy_toolbox import agent_selection # or import *

# Data
nPop = 5
n = 3

# Call function
selected, report = agent_selection(nPop, n)
print(f'selected ids from population: {selected} \n')
print(report)
```

```bash
selected ids from population: [3 4 1] 

    Selection population operator
    probs = [0.2, 0.2, 0.2, 0.2, 0.2]
    the selected agents = [3 4 1]
```
