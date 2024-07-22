---
layout: default
title: check_interval_01
grand_parent: Framework
parent: Common Library functions
has_toc: false
nav_order: 6
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>check_interval_01</h3>

<br>

<p align = "justify">
    This function checks if a design variable is out of the limits established x_ lower and x_ upper and updates the variable if necessary.
</p>

```python
check_interval_01(x_i_old, x_lower, x_upper)
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
        <td><code>x_i_old</code></td>
        <td>Current design variables of the i agent</td>
        <td>List</td>
    <tr>
        <td><code>x_lower</code></td>
        <td>Lower limit of the design variables</td>
        <td>List</td>
    <tr>
        <td><code>x_upper</code></td>
        <td>Upper limit of the design variables</td>
        <td>List</td>
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
        <td><code>x_i_new</code></td>
        <td>Update variables of the i agent</td>
        <td>List</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

Use the `check_interval_01` function to generate a new list with the values inside the range $\mathbf{x}_L = [1, 2, 3]$ and $\mathbf{x}_U = [5, 5, 5]$. Consider current solution $\mathbf{x}_i = [6, -1, 2.5]$.

```python
# Import
# pip install metapy-toolbox or pip install --upgrade metapy-toolbox 
from metapy_toolbox import check_interval_01 # or import *

# Data
xL = [1, 2, 3]
xU = [5, 5, 5]
xI = [6, -1, 2.5]

# Call function
xINew = check_interval_01(xI, xL, xU)

# Output details
print(xINew, type(xINew))
```

```bash
[5.0, 2.0, 3.0] <class 'list'>
```

Example 2
{: .label .label-blue }

Use the `check_interval_01` function to generate a new list with the values inside the range $\mathbf{x}_L = [1, 2, 3]$ and $\mathbf{x}_U = [5, 5, 5]$. Consider current solution $\mathbf{x}_i = [6, 6, 6]$.

```python
# Import
# pip install metapy-toolbox or pip install --upgrade metapy-toolbox 
from metapy_toolbox import check_interval_01 # or import *

# Data
xL = [1, 2, 3]
xU = [5, 5, 5]
xI = [6, 6, 6]

# Call function
xINew = check_interval_01(xI, xL, xU)

# Output details
print(xINew, type(xINew))
```

```bash
[5, 5, 5] <class 'list'>
```

Example 3
{: .label .label-blue }

Use the `check_interval_01` function to generate a new list with the values inside the range $\mathbf{x}_L = [1, 2, 3]$ and $\mathbf{x}_U = [5, 5, 5]$. Consider current solution $\mathbf{x}_i = [-1, -1, -1]$.

```python
# Import
# pip install metapy-toolbox or pip install --upgrade metapy-toolbox 
from metapy_toolbox import check_interval_01 # or import *

# Data
xL = [1, 2, 3]
xU = [5, 5, 5]
xI = [-1, -1, -1]

# Call function
xINew = check_interval_01(xI, xL, xU)

# Output details
print(xINew, type(xINew))
```

```bash
[1, 2, 3] <class 'list'>
```