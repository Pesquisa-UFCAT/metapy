---
layout: default
title: best_values
grand_parent: Framework
parent: Common Library functions
nav_order: 6
has_toc: false
---

<h3>best_values</h3>

<br>

<p align = "justify">
    This function determines the best, best id, worst particle and worst id. It also determines the average value (OF and FIT) of the population.
</p>

```python
best_values(x_pop, of_pop, fit_pop)
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
        <td><code>x_pop</code></td>
        <td>Population design variables</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>of_pop</code></td>
        <td>Population objective function values</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>fit_pop</code></td>
        <td>Population fitness values</td>
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
        <td><code>best_id</code></td>
        <td>Best id in population</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>worst_id</code></td>
        <td>Worst id in population</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>x_best</code></td>
        <td>Best design variables in population</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>x_worst</code></td>
        <td>Worst design variables in population</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>of_best</code></td>
        <td>Best objective function value in population</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>of_worst</code></td>
        <td>Worst objective function value in population</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>fit_best</code></td>
        <td>Best fitness value in population</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>fit_worst</code></td>
        <td>Worst fitness value in population</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>of_avg</code></td>
        <td>Average objective function value</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>fit_avg</code></td>
        <td>Average fitness value</td>
        <td>Float</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>best_values</code> function to perform a task.
    </i>
</p>

```python
# Example code goes here
```

```bash
# Example output goes here
```

