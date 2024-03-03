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

<h3>start_temperature</h3>

<br>

<p align = "justify">
This function calculates the initial temperature with an acceptance rate greater than 80% of the initial solutions. Fixed at 500 attempts.
</p>

```python
t_0mean, report = start_temperature(n_population, obj_function, x_pop, of_pop, x_lower, x_upper,\
                                    n_dimensions, pdf, cov, none_variable=None)
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
        <td>Population design variables</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>of_pop</code></td>
        <td>Population objective function values</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>x_lower</code></td>
        <td>Lower limit of the design variables</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>x_upper</code></td>
        <td>Upper limit of the design variables</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>n_dimensions</code></td>
        <td>Problem dimension</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>pdf</code></td>
        <td>Probability density function. Options: 'gaussian' or 'uniform'</td>
        <td>String</td>
    </tr>
    <tr>
        <td><code>cov</code></td>
        <td>Coefficient of variation in percentage</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>none_variable</code></td>
        <td>None variable. Default is <code>None</code>. User can use this variable in objective function</td>
        <td>None, list, float, dictionary, str or any</td>
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

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>    
        Use the <code>start_temperature</code> function to calculate the initial temperature.
    </i>
</p>

```python
# Import 
from metapy_toolbox import initial_population_01, start_temperature # or import *

# Data
nPop = 10
xL = [-5, -5]
xU = [5, 5]
d = len(xU) # or d = len(xL) or d = 2
pdf = 'uniform'
cov = 20
none_variable = None

# Objective function
def obj_function(x, none_variable):
    """Example objective function"""
    x0 = x[0]
    x1 = x[1]
    of = x0 ** 2 + x1 ** 2
    return of

# Calculate initial temperature
xPop = initial_population_01(nPop, d, xL, xU)
ofPop = [obj_function(x, none_variable) for x in xPop]
t0Mean, report = start_temperature(nPop, obj_function, xPop, ofPop, xL, xU, d, pdf, cov, none_variable)

# Output details
print(f"t_0: {t0Mean}")
```

```bash
t_0: 11.075177109777801
```

<p align = "justify">
  To check the start temperature report just apply the following instruction.
</p>

```python
# Report details
arq = "report_example_start_temp_sa.txt"

# Writing report
with open(arq, "w") as file:
    file.write(report)
```

<p align = "justify">
  Open <code>report_example_start_temp_sa.txt</code>. 
</p>

```bash
Automotic initial temperature
    sum_t0 = 30120.743224553567, number of accepted moves (delta_e > 0) = 2510, t_mean = 12.000296105399828
```
