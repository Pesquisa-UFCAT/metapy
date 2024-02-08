---
layout: default
title: Goldstein Price function
grand_parent: Benchmark
parent: Mathematical Functions
has_children: false
has_toc: true
nav_order: 10
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

```python

result = benchmark.goldsteinPrice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
```

<p align="justify">
     The Goldstein-Price function has several local minima.
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
        <td>This is a list or array representing the input vector to the Goldstein Price function. It is the point at which the function is evaluated.</td>
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
        <td>It represents the result of evaluating the Goldstein Price function at the given input x.</td>
        <td>float</td>
    </tr>
</table>
