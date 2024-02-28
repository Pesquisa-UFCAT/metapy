---
layout: default
title: de_movement_01
grand_parent: Framework
parent: Differential Evolution functions
has_children: false
has_toc: false
nav_order: 2
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>de_movement_01</h3>

<br>

<p align = "justify">
    This function performs the differential evolution movement.
</p>

```python
x_i_new, of_i_new, fit_i_new, neof, report_move = de_movement_01(obj_function, f, p_c, x_i_old, x_ii_old, x_iii_old, of_i_old, 0, n_dimensions, x_lower, x_upper)
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
        <td><code>obj_function</code></td>
        <td>The Metapy user defined this function.</td>
        <td>Py function (<code>def</code>)</td>
    </tr>
    <tr>
        <td><code>f</code></td>
        <td>Scale factor.</td>
        <td>Float</td>
    </tr>
      <tr>
        <td><code>p_c</code></td>
        <td>Crossover rate.</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>x_i_old</code></td>
        <td>Current design variables of the x_1 agent.</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>x_ii_old</code></td>
        <td>Current design variables of the x_2 agent.</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>x_iii_old</code></td>
        <td>Current design variables of the x_3 agent.</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>of_i_old</code></td>
        <td>Old function return.</td>
        <td>Float or Int</td>
    </tr>
    <tr>
        <td><code>fit_i_old</code></td>
        <td>Fitness of the x_0 agent.</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>n_dimensions</code></td>
        <td>Problem dimension.</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>x_lower</code></td>
        <td>Lower limit of the design variables.</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>x_upper</code></td>
        <td>Upper limit of the design variables.</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>none_variable</code></td>
        <td>None variable. Default is None. Use in objective function.</td>
        <td>Object or None</td>
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
        <td><code>x_i_new</code></td>
        <td>Update variables of the \(i\) agent</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>of_i_new</code></td>
        <td>Update objective function value of the i agent</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>fit_i_new</code></td>
        <td>Update fitness value of the i agent</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>neof</code></td>
        <td>Number of evaluations of the objective function</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>report</code></td>
        <td>Report about the mutation process</td>
        <td>String</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>de_movement_01</code> function to calculate the differential movement with the sum objective function.
    </i>

</p>

```python
# Objective function
def obj_function(x):
    return sum(x)

#DE parameters
f = 0.5
p_c = 0.7
n_dimensions = 3
x_lower = [-5, -5, -5]
x_upper = [5, 5, 5]

# Initial values
x_i_old = [1, 2, 3]
x_ii_old = [4, 5, 6]
x_iii_old = [7, 8, 9]
of_i_old = obj_function(x_i_old)

# Call DE movement
x_i_new, of_i_new, fit_i_new, neof, report_move = de_movement_01(obj_function, f, p_c, x_i_old, x_ii_old, x_iii_old, of_i_old, 0, n_dimensions, x_lower, x_upper)

print(f"Before DE Movement:\n x_i_old = {x_i_old}, of_i_old = {of_i_old}\n")
print(report_move)
print(f"After DE Movement:\n x_i_new = {x_i_new}, of_i_new = {of_i_new}\n")
```

```bash
Before DE Movement:
    x_i_old = [1, 2, 3], of_i_old = 6

    Mutation movement
    Dimension 0: rij = -3, neighbor = -0.5
    Dimension 1: rij = -3, neighbor = 0.5
    Dimension 2: rij = -3, neighbor = 1.5
    Crossover movement - DEd
    random_number 0.9509577325762715 > p_c
    dont update x = [1, 2, 3], of = 6, fit = 0

After DE Movement:
 x_i_new = [1, 2, 3], of_i_new = 6
```
