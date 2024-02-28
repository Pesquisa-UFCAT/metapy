---
layout: default
title: start_temperature
grand_parent: Framework
parent: Simulated Annealing functions
has_toc: false
nav_order: 2
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>simulated_annealing_01</h3>

<br>

<p align = "justify">
This function calculates the initial temperature with an acceptance rate greater than 80% of the initial solutions. Fixed at 500 attempts.
</p>

```python
t_0mean, report = start_temperature(n_population, obj_function, x_pop, of_pop, x_lower, x_upper, n_dimensions, pdf, cov, none_variable = None)
```

Input variables
{: .label .label-yellow }

<table style="width:100%">
    <thead>
        <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Type</th>
        </tr>
    </thead>
    <tr>
        <td><code>n_population</code></td>
        <td>Number of population.</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>obj_function</code></td>
        <td>Objective function. The Metapy user defined this function.</td>
        <td>Python function (<code>def</code>)</td>
    </tr>
    <tr>
        <td><code>x_pop</code></td>
        <td>Population design variables.</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>of_pop</code></td>
        <td>Population objective function values.</td>
        <td>List</td>
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
        <td><code>n_dimensions</code></td>
        <td>Problem dimension.</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>pdf</code></td>
        <td>Probability density function. Options: 'gaussian' or 'uniform'.</td>
        <td>String</td>
    </tr>
    <tr>
        <td><code>cov</code></td>
        <td>Coefficient of variation in percentage.</td>
        <td>Float</td>
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
        <td><code>t_0mean</code></td>
        <td>Initial temperature</td>
        <td>Float</td>
    </tr>  
    <tr>
        <td><code>report</code></td>
        <td>Report of the algorithm execution</td>
        <td>String</td>
    </tr>  
</table>

<table style = "width:100%">
    <thead>
      <tr>
        <th>Name</th>
        <th>Description</th>
        <th>Type</th>
      </tr>
    </thead>
    <tr>
        <td><code>population</code></td>
        <td>Population design variables. All repetitions</td>
        <td>List</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>    
    </i>
</p>

```python

```

```bash

```
