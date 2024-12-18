---
layout: default
title: convert_continuous_discrete
grand_parent: Framework
parent: Common Library functions
nav_order: 9
has_toc: false
---

<h3>convert_continuous_discrete</h3>

<br>

<p align = "justify">
    This function converts a continuous variable into a discrete variable according to a discrete dataset.
</p>

```python
convert_continuous_discrete(x, discrete_dataset)
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
        <td><code>x</code></td>
        <td>Continuous design variables of the i agent</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>discrete_dataset</code></td>
        <td>Discrete dataset. Include the key 'x_k' where k is the dimension of the variable that the user wants to be assigned a value from a discrete list</td>
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
        <td><code>x_converted</code></td>
        <td>Converted variables of the i agent</td>
        <td>List</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>convert_continuous_discrete</code> function to perform a task.
    </i>
</p>

```python
# Example code goes here
```

```bash
# Example output goes here
```

