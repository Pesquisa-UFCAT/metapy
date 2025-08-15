---
layout: default
title: gender_firefly_01
grand_parent: Framework
parent: Common Library functions
nav_order: 6
has_toc: false
---

<h3>gender_firefly_01</h3>

<br>

<p align = "justify">
    Gender firefly algorithm.
</p>

```python
gender_firefly_01(settings)
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
        <td>[0] setup (dict), [1] initial population (List), [2] seeds (Integer).</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>gamma</code></td>
        <td>Light absorption coefficient  1 / (x_lower - x_upper) ** m.</td>
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
        <td><code>df_all</code></td>
        <td>All data of the population.</td>
        <td>dataframe</td>
    </tr>
    <tr>
        <td><code>df_best</code></td>
        <td>Best data of the population.</td>
        <td>dataframe</td>
    </tr>
    <tr>
        <td><code>delta_time</code></td>
        <td>Time of the algorithm execution in seconds.</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>report</code></td>
        <td>Report of the algorithm execution.</td>
        <td>string</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>gender_firefly_01</code> function to perform a task.
    </i>
</p>

```python
# Example code goes here
```

```bash
# Example output goes here
```

