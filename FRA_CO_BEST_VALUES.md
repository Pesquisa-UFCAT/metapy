---
title: Best values
layout: home
grand_parent: Framework
parent: Common Library
has_children: true
nav_order: 4
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

BEST_VALUES
{: .label .label-green }

<p align = "justify">
    This function determines the best and worst particle. It also determines the average value (OF and FIT) of the population.
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
        <td><code>X</code></td>
        <td>It represents the population of particles, where each line is a particle and and list id is a dimension</td>
        <td>Py list [N_POP] \(\times\) [D]</td>
    </tr>
    <tr>
        <td><code>OF</code></td>
        <td>Objective function values for each particle in the population</td>
        <td>Py list [N_POP]</td>
    </tr>  
    <tr>
        <td><code>FIT</code></td>
        <td>Fitness values for each particle in the population</td>
        <td>Py list [N_POP]</td>
    </tr>  
    <!--
    <tr>
        <td><code>N_POP</code></td>
        <td>Population size</td>
        <td>integer</td>
    </tr>
    -->
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
        <td><code>BEST_POSITION</code></td>
        <td>Index of the best particle in the population</td>
        <td>integer</td>
    </tr>
    <tr>
        <td><code>WORST_POSITION</code></td>
        <td>Index of the worst particle in the population</td>
        <td>integer</td>
    </tr>
    <tr>
        <td><code>X_BEST</code></td>
        <td>Design variables of the best particle</td>
        <td>Py list [D]</td>
    </tr>
    <tr>
        <td><code>X_WORST</code></td>
        <td>Design variables of the worst particle</td>
        <td>Py list [D]</td>
    </tr>
    <tr>
        <td><code>OF_BEST</code></td>
        <td>Objective function value of the best particle</td>
        <td>float</td>
    </tr>
    <tr>
        <td><code>OF_WORST</code></td>
        <td>Objective function value of the worst particle</td>
        <td>float</td>
    </tr>
    <tr>
        <td><code>FIT_BEST</code></td>
        <td>Fitness value of the best particle</td>
        <td>float</td>
    </tr>
    <tr>
        <td><code>FIT_WORST</code></td>
        <td>Fitness value of the worst particle</td>
        <td>float</td>
    </tr>
    <tr>
        <td><code>OF_AVERAGE</code></td>
        <td>Average value of the objective functions in the population</td>
        <td>float</td>
    </tr>
    <tr>
        <td><code>FIT_AVERAGE</code></td>
        <td>Average fitness value in the population.</td>
        <td>float</td>
    </tr>
</table>

Example 7
{: .label .label-blue }

<p align = "justify">
  <i>
    Use the <code>BEST_VALUES</code> function to find the best and worst values in the array <code>[[1, 2, 3], [4, 5, 6], [7, 8, 9]]</code>.
  </i>
</p>

```python
xValues = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ofValues = [10, 5, 8]
fitValues = [0.1, 0.5, 0.3]

bestPos, worstPos, xBest, xWorst, ofBest, ofWorst, fitBest, fitWorst, ofAverage, fitAverage = BEST_VALUES(xValues, ofValues, fitValues)

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
