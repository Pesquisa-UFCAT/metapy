---
layout: default
title: attractiveness_parameter
grand_parent: Framework
parent: Common Library functions
nav_order: 3
has_toc: false
---

<h3>attractiveness_parameter</h3>

<br>

<p align = "justify">
    This function calculates at attractiveness parameter between x_i and x_j fireflies.
</p>

```python
attractiveness_parameter(beta_0, gamma, x_i, x_j, n_dimensions)
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
        <td><code>beta_0</code></td>
        <td>Attractiveness at r = 0</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>gamma</code></td>
        <td>Light absorption coefficient  1 / (x_upper - x_lower) ** m</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>x_i</code></td>
        <td>Design variables i Firefly</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>x_j</code></td>
        <td>Design variables j Firefly</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>n_dimensions</code></td>
        <td>Problem dimension</td>
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
        <td><code>beta</code></td>
        <td>Attractiveness</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>r_ij</code></td>
        <td>Firefly distance</td>
        <td>Float</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>attractiveness_parameter</code> function to perform a task.
    </i>
</p>

```python
# Example code goes here
```

```bash
# Example output goes here
```

