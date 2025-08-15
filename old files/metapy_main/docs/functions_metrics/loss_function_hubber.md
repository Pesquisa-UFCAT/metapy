---
layout: default
title: loss_function_hubber
grand_parent: Framework
parent: Common Library functions
nav_order: 4
has_toc: false
---

<h3>loss_function_hubber</h3>

<br>

<p align = "justify">
    Loss function: Smooth Mean Absolute Error or Hubber Loss.
</p>

```python
loss_function_hubber(y_true, y_pred, delta)
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
        <td><code>y_true</code></td>
        <td>True values.</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>y_pred</code></td>
        <td>Predicted values.</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>delta</code></td>
        <td>Threshold.</td>
        <td>Float</td>
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
        <td><code>smae</code></td>
        <td>Hubber Loss.</td>
        <td>Float</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>loss_function_hubber</code> function to perform a task.
    </i>
</p>

```python
# Example code goes here
```

```bash
# Example output goes here
```

