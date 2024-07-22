---
layout: default
title: id_selection
grand_parent: Framework
parent: Common Library functions
has_toc: false
nav_order: 7
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>id_selection</h3>

<br>

<p align = "justify">
    This function selects a k dimension from the all dimensions (uniform selection).
</p>

```python
id_selection(n_dimensions, n, k_dimension=False)
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
        <td><code>n_dimensions</code></td>
        <td>Problem dimension</td>
        <td>Integer</td>
    <tr>
        <td><code>n</code></td>
        <td>Number of dimensions to select</td>
        <td>Integer</td>
    <tr>
        <td><code>k_dimension</code></td>
        <td>Default is False (Selects n dimensions among all dimensions). k_dimension=Integer Selects n dimensions among all dimensions, excluding k dimension</td>
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
        <td>selected dimensions</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>report</code></td>
        <td>Report about the selection process</td>
        <td>String</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

Select three dimension from five dimensions, except dimension 2 ($k=2$).

```python
# Import
# pip install metapy-toolbox or pip install --upgrade metapy-toolbox 
from metapy_toolbox import id_selection # or import *

# Data
nDimensions = 5 
n = 3
excludedDimension = 2

# Call function
selected, report = id_selection(nDimensions, n, excludedDimension)
print(f'selected ids from dimensions: {selected} \n')
print(report)
```

```bash
selected ids from dimensions: [4 3 0] 

    Selection dimension operator
    probs = [0.25, 0.25, 0.0, 0.25, 0.25]
    the selected dimensions = [4 3 0]
```

Example 2
{: .label .label-blue }

Select three dimension from five dimensions.

```python
# Import
# pip install metapy-toolbox or pip install --upgrade metapy-toolbox
from metapy_toolbox import id_selection # or import *

# Data
nDimensions = 5 
n = 3

# Call function
selected, report = id_selection(nDimensions, n)
print(f'selected ids from dimensions: {selected} \n')
print(report)
```

```bash
selected ids from dimensions: [2 0 4] 

    Selection dimension operator
    probs = [0.2, 0.2, 0.2, 0.2, 0.2]
    the selected dimensions = [2 0 4]
```