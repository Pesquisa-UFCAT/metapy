---
layout: default
title: gamma_parameter
grand_parent: Framework
parent: Common Library functions
nav_order: 1
has_toc: false
---

<h3>gamma_parameter</h3>

<br>

<p align = "justify">
    This function calculates the light absorption coefficient.
</p>

```python
gamma_parameter(x_lower, x_upper, n_dimension, m=2)
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
        <td><code>x_lower</code></td>
        <td>Lower limit of the problem</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>x_upper</code></td>
        <td>Upper limit of the problem</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>n_dimensions</code></td>
        <td>Problem dimension</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>m</code></td>
        <td>Light absorption factor. Default is 2</td>
        <td>Integer</td>
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
        <td><code>gamma</code></td>
        <td>Light absorption coefficient  1 / (x_upper - x_lower) ** m</td>
        <td>List</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>gamma_parameter</code> function to perform a task.
    </i>
</p>

```python
# Example code goes here
```

```bash
# Example output goes here
```

