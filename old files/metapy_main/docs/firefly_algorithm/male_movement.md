---
layout: default
title: male_movement
grand_parent: Framework
parent: Common Library functions
nav_order: 4
has_toc: false
---

<h3>male_movement</h3>

<br>

<p align = "justify">
    This function movement an male firefly.
</p>

```python
male_movement(obj_function, beta_0, gamma, x_i_old, fit_i_old, y_j_old, fit_j_old, y_k_old, fit_k_old, n_dimensions, x_lower, x_upper, none_variable=None)
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
    <tr>
        <td><code>x_i_old</code></td>
        <td>Design variables i (male) Firefly</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>fit_i_old</code></td>
        <td>Fitness of the i firefly</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>y_j_old</code></td>
        <td>Design variables j (female) Firefly</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>fit_j_old</code></td>
        <td>Fitness of the j firefly</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>y_k_old</code></td>
        <td>Design variables k (female) Firefly</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>fit_k_old</code></td>
        <td>Fitness of the k firefly</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>n_dimensions</code></td>
        <td>Problem dimension</td>
        <td>Integer</td>
    </tr>
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
        <td><code>none_variable</code></td>
        <td>None variable. Default is None. User can use this variable in objective function.</td>
        <td>None, list, float, dictionary, str or any</td>
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
        <td><code>report</code></td>
        <td>Report about the male movement process.</td>
        <td>string</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>male_movement</code> function to perform a task.
    </i>
</p>

```python
# Example code goes here
```

```bash
# Example output goes here
```

