---
layout: default
title: initial_pops
grand_parent: Framework
parent: Common Library functions
nav_order: 3
has_toc: false
---

<h3>initial_pops</h3>

<br>

<p align = "justify">
    This function randomly initializes a population of the metaheuristic algorithm for a given number of repetitions.
</p>

```python
initial_pops(n_repetitions, n_population, n_dimensions, x_lower, x_upper, type_pop, seeds)
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
        <td><code>n_repetitions</code></td>
        <td>Number of repetitions</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>n_population</code></td>
        <td>Number of population</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>n_dimensions</code></td>
        <td>Problem dimension</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>x_lower</code></td>
        <td>Lower limit of the design variables. Use None for combinatorial variables</td>
        <td>List or None</td>
    </tr>
    <tr>
        <td><code>x_upper</code></td>
        <td>Upper limit of the design variables. Use None for combinatorial variables</td>
        <td>List or None</td>
    </tr>
    <tr>
        <td><code>type_pop</code></td>
        <td>Type of population. Options: 'real code' or 'combinatorial code'. 'real code' call function initial_population_01 and 'combinatorial code' call function initial_population_02</td>
        <td>String</td>
    </tr>
    <tr>
        <td><code>seeds</code></td>
        <td>Random seed. Use None for random seed</td>
        <td>List or None</td>
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
        <td><code>population</code></td>
        <td>Population design variables. All repetitions</td>
        <td>List</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>initial_pops</code> function to perform a task.
    </i>
</p>

```python
# Example code goes here
```

```bash
# Example output goes here
```

