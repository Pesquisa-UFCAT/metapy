---
layout: default
title: best_values
grand_parent: Framework
parent: Common Library functions
has_toc: false
nav_order: 5
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>best_values</h3>

<br>

<p align = "justify">
    This function determines the best, best id, worst particle and worst id. It also determines the average value (OF and FIT) of the population.
</p>

```python
best_id, worst_id,\
    x_best, x_worst,\
    of_best, of_worst,\
    fit_best, fit_worst,\
    of_avg, fit_avg = best_values(x_pop, of_pop, fit_pop)
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
        <td><code>fit_pop</code></td>
        <td>Population fitness values</td>
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
        <td><code>best_id</code></td>
        <td>Best id in population</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>worst_id</code></td>
        <td>Worst id in population</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>x_best</code></td>
        <td>Best design variables in population</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>x_worst</code></td>
        <td>Worst design variables in population</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>of_best</code></td>
        <td>Best objective function value in population</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>of_worst</code></td>
        <td>Worst objective function value in population</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>fit_best</code></td>
        <td>Best fitness value in population</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>fit_worst</code></td>
        <td>Worst fitness value in population</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>of_avg</code></td>
        <td>Average objective function value</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>fit_avg</code></td>
        <td>Average fitness value</td>
        <td>Float</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
    Use the <code>best_values</code> function to find the best and worst values in the pop array:
    <br>
    \(\mathbf{x}_0 = \left[1,\;2,\;3\right]\), \(of_0 = 10\) and \(fit_0 = 0.09\)
    <br>
    \(\mathbf{x}_1 = \left[4,\;5,\;6\right]\), \(of_1 = 5\) and \(fit_1 = 0.17\)
    <br>
    \(\mathbf{x}_2 = \left[7,\;8,\;9\right]\), \(of_2 = 8\) and \(fit_2 = 0.11\)
  </i>
</p>

```python
# Import 
from metapy_toolbox import best_values # or import *

# Data
xValues = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ofValues = [10, 5, 8]
fitValues = [0.09, 0.17, 0.11]

# Call function
bestPos, worstPos, xBest, xWorst, ofBest, ofWorst, fitBest, fitWorst, \
    ofAverage, fitAverage = best_values(xValues, ofValues, fitValues)

# Output details
print("Best position in the population:", bestPos)
print("Worst position in the population:", worstPos)
print("Best value of X:", xBest)
print("Worst value of X:", xWorst)
print("Best OF:", ofBest)
print("Worst OF:", ofWorst)
print("Best FIT:", fitBest)
print("Worst FIT:", fitWorst)
print("Average OF:", ofAverage)
print("Average FIT:", fitAverage)
```

```bash
Best position in the population: 1
Worst position in the population: 0
Best value of X: [4, 5, 6]
Worst value of X: [1, 2, 3]
Best OF: 5
Worst OF: 10
Best FIT: 0.17
Worst FIT: 0.09
Average OF: 7.666666666666667
Average FIT: 0.12333333333333334
```
