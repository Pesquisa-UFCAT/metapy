---
layout: default
title: Sphere function
grandparent: Benchmark
parent: Mathematical Functions
has_children: false
nav_order: 1
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

```python
result = benchmark.sphere([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
```

<p align="justify">
The Sphere function has d local minima except for the global one. It is continuous, convex and unimodal.
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
        <td>This parameter represents the input point in the n-dimensional space for which the Sphere function value is to be computed.</td>
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
        <td>The function returns the value of the Sphere function at the given point x. This value is a scalar, representing the output of the Sphere function for the input point.</td>
        <td>float</td>
    </tr>
</table>
