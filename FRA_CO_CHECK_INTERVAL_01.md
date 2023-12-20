---
title: Check Interval 01
layout: home
grand_parent: Framework
parent: Common Library
has_children: true
nav_order: 6
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<!--
check_interval_01
{: .label .label-green }

-->

```python
xINew = check_interval_01(xI, xL, xU)
```

<p align = "justify">
    This function checks if a design variable is out of the limits established \(\mathbf{x}_L\) and \(\mathbf{x}_U\).
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
        <td><code>x_i_old</code></td>
        <td>The design variables that will be checked</td>
        <td>Py list [D]</td>
    </tr>
    <tr>
        <td><code>x_l</code></td>
        <td>X Lower or lower limit</td>
        <td>Py list [D]</td>
    </tr>
    <tr>
        <td><code>x_u</code></td>
        <td>X Upper or Upper limit</td>
        <td>Py list [D]</td>
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
        <td><code>x_i_new</code></td>
        <td>The new design variable values, that are inside the limit defined by lower and upper</td>
        <td>Py list [D]</td>
    </tr>
</table>

Example 5
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>check_interval_01</code> function to generate a new list with the values inside the range \(\mathbf{x}_L = [1, 2, 3]\) and \(\mathbf{x}_L = [5, 5, 5]\). Consider current solution \(\mathbf{x}_i = [6, -1, 2.5]\)
    </i>
</p>

```python
# Data
xL = [1, 2, 3]
xU = [5, 5, 5]
xI = [6, -1, 2.5]

# Call function
xINew = check_interval_01(xI, xL, xU)

# Output details
print(xINew)
```

```bash
update solution:  [5.0, 2.0, 3.0]
```
