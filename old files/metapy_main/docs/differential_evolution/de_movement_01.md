---
layout: default
title: de_movement_01
grand_parent: Framework
parent: Common Library functions
nav_order: 1
has_toc: false
---

<h3>de_movement_01</h3>

<br>

<p align = "justify">
    This function performs the differential evolution movement (binomial crossover).
</p>

```python
de_movement_01(obj_function, p_c, x_i_old, x_i_mutation, n_dimensions, x_lower, x_upper, none_variable=None)
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
        <td><code>p_c</code></td>
        <td>Crossover rate.</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>x_i_old</code></td>
        <td>Current design variables of the i agent.</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>x_i_mutation</code></td>
        <td>Current design variables of the mutation agent.</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>n_dimensions</code></td>
        <td>Problem dimension.</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>x_lower</code></td>
        <td>Lower limit of the design variables.</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>x_upper</code></td>
        <td>Upper limit of the design variables.</td>
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
        <td>String</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>de_movement_01</code> function to perform a task.
    </i>
</p>

```python
# Example code goes here
```

```bash
# Example output goes here
```

