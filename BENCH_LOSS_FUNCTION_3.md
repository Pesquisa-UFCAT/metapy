---
layout: default
title: Benchmark
has_children: true
nav_order: 13
---

<!--Don't delete this script-->
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete this script-->

```python
result = benchmark.LOSS_FUNCTION_3([5, 4, 8, 6, 9, 10, 11], [6, 5, 7, 7, 9, 9, 12])
```

<p align="justify">
Loss function d-dimensional: Square Error.
</p>

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
        <td><code>Y_EXP</code></td>
        <td>A list or array containing the experimental results.</td>
        <td>Py list</td>
    </tr>
    <tr>
        <td><code>Y_NUM</code></td>
        <td>A list or array containing the results obtained from numerical modeling from experimental data.</td>
        <td>Py list</td>
    </tr>
</table>

Output variables
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
        <td><code>OF</code></td>
        <td>The output value of the Square Error function.</td>
        <td>float</td>
    </tr>
</table>

