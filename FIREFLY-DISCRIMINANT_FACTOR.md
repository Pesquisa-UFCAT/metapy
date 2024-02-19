---
layout: default
title: Discriminant factor
grand_parent: Framework
parent: Firefly functions
has_children: false
has_toc: true
nav_order: 1
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

```python
result = ff.discriminant_factor(1.1, 0.9)
```

<p align="justify">
Calculation of the discriminating factor of the male and female fireflies population
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
        <td><code>fit_male</code></td>
        <td>Fitness of the i firefly</td>
        <td>float</td>
    </tr>
    <tr>
        <td><code>fit_female</code></td>
        <td>Fitness of the k firefly.</td>
        <td>float</td>
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
        <td><code>d_1</code></td>
        <td>Discriminating factor.</td>
        <td>int</td>
    </tr>
</table>
