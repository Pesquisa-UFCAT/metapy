---
layout: default
title: id_selection
grand_parent: Framework
parent: Common Library functions
nav_order: 7
has_toc: false
---

<h3>id_selection</h3>

<br>

<p align = "justify">
    This function selects a k dimension from the all dimensions (uniform selection).
</p>

```python
id_selection(n_dimensions, n, k_dimension=False)
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
        <td><code>n_dimensions</code></td>
        <td>Problem dimension</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>n</code></td>
        <td>Number of dimensions to select</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>k_dimension</code></td>
        <td>Default is False (Selects n dimensions among all dimensions). k_dimension=Integer Selects n dimensions among all dimensions, excluding k dimension</td>
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
        <td>selected dimensions</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>report</code></td>
        <td>Report about the selection process</td>
        <td>String</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>id_selection</code> function to perform a task.
    </i>
</p>

```python
# Example code goes here
```

```bash
# Example output goes here
```

