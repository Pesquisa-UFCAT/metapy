---
layout: default
title: metaheuristic_optimizer
grand_parent: Framework
parent: Common Library functions
nav_order: 1
has_toc: false
---

<h3>metaheuristic_optimizer</h3>

<br>

<p align = "justify">
    This function is responsible for the metaheuristic optimization process. It is a general function that calls the specific algorithm functions.
</p>

```python
metaheuristic_optimizer(algorithm_setup, general_setup)
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
        <td><code>algorithm_setup</code></td>
        <td>Metaheuristic optimization setup. See algorithms documentation for more details.</td>
        <td>Dictionary</td>
    </tr>
    <tr>
        <td><code>general_setup</code></td>
        <td>Optimization process setup.</td>
        <td>Dictionary</td>
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
        <td><code>all_results_per_rep</code></td>
        <td>All results for each repetition.</td>
        <td>list</td>
    </tr>
    <tr>
        <td><code>best_population_per_rep</code></td>
        <td>Best population for each repetition.</td>
        <td>list</td>
    </tr>
    <tr>
        <td><code>reports</code></td>
        <td>Reports for each repetition.</td>
        <td>list</td>
    </tr>
    <tr>
        <td><code>status_procedure</code></td>
        <td>Best repetition id.</td>
        <td>integer</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>metaheuristic_optimizer</code> function to perform a task.
    </i>
</p>

```python
# Example code goes here
```

```bash
# Example output goes here
```

