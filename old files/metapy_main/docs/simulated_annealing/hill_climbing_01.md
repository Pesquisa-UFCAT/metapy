---
layout: default
title: hill_climbing_01
grand_parent: Framework
parent: Common Library functions
nav_order: 2
has_toc: false
---

<h3>hill_climbing_01</h3>

<br>

<p align = "justify">
    Hill Climbing algorithm 01.
</p>

```python
hill_climbing_01(settings)
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
        <td><code>settings</code></td>
        <td>[0] setup (Dictionary), [1] initial population (List or METApy function), [2] seeds (None or integer)</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>population</code></td>
        <td>Users can inform the initial population or use initial population functions</td>
        <td>List or METApy function</td>
    </tr>
    <tr>
        <td><code>seed</code></td>
        <td>Random seed. Use None for random seed</td>
        <td>None or integer</td>
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
        <td><code>df_all</code></td>
        <td>All data of the population.</td>
        <td>Dataframe</td>
    </tr>
    <tr>
        <td><code>df_best</code></td>
        <td>Best data of the population.</td>
        <td>Dataframe</td>
    </tr>
    <tr>
        <td><code>delta_time</code></td>
        <td>Time of the algorithm execution in seconds.</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>report</code></td>
        <td>Report of the algorithm execution.</td>
        <td>String</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>hill_climbing_01</code> function to perform a task.
    </i>
</p>

```python
# Example code goes here
```

```bash
# Example output goes here
```

