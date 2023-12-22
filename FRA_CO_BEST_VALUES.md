---
title: best_values
layout: home
grand_parent: Framework
parent: Common Library
has_toc: false
nav_order: 5
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

```python
best_id, worst_id, x_best, x_worst, of_best, of_worst, \
            fit_best, fit_worst, of_avg, fit_avg = best_values(x_pop, of_pop, fit_pop)
```

<p align = "justify">
    This function determines the best, best id, worst particle and worst id. It also determines the average value (OF and FIT) of the population.
</p>

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
        <td>Population objective function values.</td>
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
        <td>Best id in population.</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>worst_id</code></td>
        <td>Worst id in population.</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>x_best</code></td>
        <td>Best design variables in population.</td>
        <td>Lits</td>
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

Example 7
{: .label .label-blue }

<p align = "justify">
  <i>
    Use the <code>best_values</code> function to find the best and worst values in the array <code>[[1, 2, 3], [4, 5, 6], [7, 8, 9]]</code>.
  </i>
</p>

```python
xValues = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ofValues = [10, 5, 8]
fitValues = [0.1, 0.5, 0.3]

bestPos, worstPos, xBest, xWorst, ofBest, ofWorst, fitBest, fitWorst, ofAverage, fitAverage = best_values(xValues, ofValues, fitValues)

print("Best position in the population:", bestPos)
print("Worst position in the population:", worstPos)
print("Best value of X:", xBest)
print("Worst value of X:", xWorst)
print("Best value of OF:", ofBest)
print("Worst value of OF:", ofWorst)
print("Best value of FIT:", fitBest)
print("Worst value of FIT:", fitWorst)
print("Average OF value:", ofAverage)
print("Average FIT value:", fitAverage)
```

```bash
Best position in the population: 1
Worst position in the population: 0
Best value of X: [4, 5, 6]
Worst value of X: [1, 2, 3]
Best value of OF: 5
Worst value of OF: 10
Best value of FIT: 0.5
Worst value of FIT: 0.1
Average OF value: 7.666666666666667
Average FIT value: 0.3
```
