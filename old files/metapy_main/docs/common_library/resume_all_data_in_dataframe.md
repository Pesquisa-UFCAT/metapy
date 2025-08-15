---
layout: default
title: resume_all_data_in_dataframe
grand_parent: Framework
parent: Common Library functions
nav_order: 17
has_toc: false
---

<h3>resume_all_data_in_dataframe</h3>

<br>

<p align = "justify">
    This function creates a dataframme with all values of the population.
</p>

```python
resume_all_data_in_dataframe(x_i_pop, of_i_pop, fit_i_pop, columns, iteration)
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
        <td><code>x_i_pop</code></td>
        <td>Design variables of the i agent</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>of_i_pop</code></td>
        <td>Objective function value of the i agent</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>fit_i_pop</code></td>
        <td>Fitness value of the i agent</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>columns</code></td>
        <td>Columns names about dataset results</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>iteration</code></td>
        <td>Current iteration number</td>
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
        <td><code>i_pop_data</code></td>
        <td>Dataframe with all values of the i agent in j iteration</td>
        <td>Dataframe</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>resume_all_data_in_dataframe</code> function to perform a task.
    </i>
</p>

```python
# Example code goes here
```

```bash
# Example output goes here
```

