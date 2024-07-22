---
layout: default
title: fit_value
grand_parent: Framework
parent: Common Library functions
has_toc: false
nav_order: 4
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>fit_value</h3>

<br>

<p align = "justify">
    This function calculates the fitness of the i agent.
</p>

```python
fit_value(of_i_value)
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
        <td><code>of_i_value</code></td>
        <td>Object function value of the i agent</td>
        <td>Float</td>
    <tr>
        <td><code>fit_i_value</code></td>
        <td>Fitness value of the i agent</td>
        <td>Float</td>
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
        <td><code>fit_i_value</code></td>
        <td>Fitness value of the i agent</td>
        <td>Float</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

Use the `fit_value` function to generate the fitness of the agent. The objective function value is 1.

```python
# Import
# pip install metapy-toolbox or pip install --upgrade metapy-toolbox 
from metapy_toolbox import fit_value # or import *

# Data
ofI = 1

# Call function
fitI = fit_value(ofI)

# Output details
print(f'fit value i agent when OF = {ofI} is {fitI}')
```

```bash
fit value i agent when OF = 1 is 0.5
```

Example 2
{: .label .label-blue }

Use the `fit_value` function to generate the fitness of the agent. The objective function value is -1.

```python
# Import
# pip install metapy-toolbox or pip install --upgrade metapy-toolbox 
from metapy_toolbox import fit_value # or import *

# Data
ofI = -1

# Call function
fitI = fit_value(ofI)

# Output details
print(f'fit value i agent when OF = {ofI} is {fitI}')
```

```bash
fit value i agent when OF = -1 is 2
```
