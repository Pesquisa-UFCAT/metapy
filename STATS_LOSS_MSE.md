---
layout: default
title: MSE
parent: Statistical
grand_parent: Loss
has_children: false
has_toc: false
nav_order: 1
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

```python
result = benchmark.LOSS_FUNCTION_1([5, 4, 8, 6, 9, 10, 11], [6, 5, 7, 7, 9, 9, 12])
```

<p align="justify">
texto..................
</p>

Input variables
{: .label .label-yellow }

<!--PAREI AQUI. COMO ADD DUAS LINHAS NA TABELA?-->
<table style = "width:100%">
    <thead>
      <tr>
        <th>Name</th>
        <th>Description</th>
        <th>Type</th>
      </tr>
    </thead>
    <tr>
        <td><code>Y_NUM</code></td>
        <td>A list or array containing the results obtained from numerical modeling from experimental data.</td>
        <td>Py list </td>
    </tr>
    
     <tr>
        <td><code>Y_EXP</code></td>
        <td>A list or array containing the experimental results.</td>
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
        <td>The output value of the Ackley function evaluated at the input coordinates x.</td>
        <td>float</td>
    </tr>
</table>
