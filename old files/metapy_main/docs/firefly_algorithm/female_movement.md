---
layout: default
title: female_movement
grand_parent: Framework
parent: Common Library functions
nav_order: 5
has_toc: false
---

<h3>female_movement</h3>

<br>

<p align = "justify">
    This function movement an female firefly.
</p>

```python
female_movement(obj_function, beta_0, gamma, x_i_old_best, y_j_old, n_dimensions, x_lower, x_upper, none_variable=None)
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
        <td><code>of_function</code></td>
        <td>Objective function. The Metapy user defined this function.</td>
        <td>Py function (def)</td>
    </tr>
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
        <td><code>y_i_new</code></td>
        <td>Update variables of the i agent.</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>of_i_new</code></td>
        <td>Update objective function value of the i agent.</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>fit_i_new</code></td>
        <td>Update fitness value of the i agent.</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>neof</code></td>
        <td>Number of evaluations of the objective function.</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>report_move</code></td>
        <td>Report about the male movement process.</td>
        <td>string</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>female_movement</code> function to perform a task.
    </i>
</p>

```python
# Example code goes here
```

```bash
# Example output goes here
```

