---
layout: default
title: agent_selection
grand_parent: Framework
parent: Common Library functions
nav_order: 8
has_toc: false
---

<h3>agent_selection</h3>

<br>

<p align = "justify">
    This function selects a n agents from all population (uniform selection).
</p>

```python
agent_selection(n_population, n, i_pop=False)
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
        <td><code>n_population</code></td>
        <td>Number of population</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>n</code></td>
        <td>Number of agents to select</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>i_pop</code></td>
        <td>Default is False (Selects n agents among all population). i_pop=Integer Selects n agents among all population, excluding i_pop agent</td>
        <td>Integer or Boolean</td>
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
        <td><code>selected</code></td>
        <td>Selected agents.</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>report</code></td>
        <td>Report about the selection process.</td>
        <td>String</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>agent_selection</code> function to perform a task.
    </i>
</p>

```python
# Example code goes here
```

```bash
# Example output goes here
```

