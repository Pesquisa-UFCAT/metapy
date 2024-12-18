---
layout: default
title: resume_best_data_in_dataframe
grand_parent: Framework
parent: Common Library functions
nav_order: 18
has_toc: false
---

<h3>resume_best_data_in_dataframe</h3>

<br>

<p align = "justify">
    This function creates a dataframe with the best, worst and average values of the population.
</p>

```python
resume_best_data_in_dataframe(x_pop, of_pop, fit_pop, column_best, column_worst, other_columns, neof_count, iteration)
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
    <tr>
        <td><code>column_best</code></td>
        <td>Columns names about dataset results</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>column_worst</code></td>
        <td>Columns names about dataset results</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>other_columns</code></td>
        <td>Columns names about dataset results</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>neof_count</code></td>
        <td>Number of evaluations of the objective function</td>
        <td>Integer</td>
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
        <td><code>data_resume</code></td>
        <td>Dataframe with the best, worst and average values of in j iteration</td>
        <td>Dataframe</td>
    </tr>
    <tr>
        <td><code>best_id</code></td>
        <td>Best id in population</td>
        <td>Integer</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>resume_best_data_in_dataframe</code> function to perform a task.
    </i>
</p>

```python
# Example code goes here
```

```bash
# Example output goes here
```

