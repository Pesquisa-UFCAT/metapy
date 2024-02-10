---
layout: default
title: Griewank function
grand_parent: Benchmark
parent: Mathematical Functions
has_children: false
has_toc: true
nav_order: 5
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

```python
result = benchmark.griewank([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
```

<p align="justify">
 The Griewank function has many widespread local minima, which are regularly distributed.
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
        <td><code>x</code></td>
        <td>A list or array of numeric values representing the coordinates in the search space. It represents the point in the n-dimensional space for which we want to evaluate the Griewank function.</td>
        <td>Py list </td>
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
        <td><code>of</code></td>
        <td>A float representing the value of the Griewank function evaluated at the given point x. This value is the objective function value.</td>
        <td>float</td>
    </tr>
</table>
