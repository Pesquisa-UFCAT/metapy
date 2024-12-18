---
layout: default
title: differential_evolution_01
grand_parent: Framework
parent: Common Library functions
nav_order: 2
has_toc: false
---

<h3>differential_evolution_01</h3>

<br>

<p align = "justify">
    Differential Evolution algorithm 01.
</p>

```python
differential_evolution_01(settings)
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
        <td>[0] setup, [1] initial population, [2] seeds.</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>function</code></td>
        <td>Objective function. The Metapy user defined this function.</td>
        <td>def)</td>
    </tr>
    <tr>
        <td><code>population</code></td>
        <td>Initial population.</td>
        <td>List or METApy function</td>
    </tr>
    <tr>
        <td><code>seed</code></td>
        <td>Random seed. Use None for random seed.</td>
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
        Use the <code>differential_evolution_01</code> function to perform a task.
    </i>
</p>

```python
# Example code goes here
```

```bash
# Example output goes here
```

