---
layout: default
title: Griewank
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
of = griewank(x)
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

<h3>Problem</h3>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[ f(\mathbf{x}) = -\alpha \ exp \left( \sqrt[-b ]{\frac{1}{d}\sum*{i}^{d} x*{2}^{i}} \right ) -exp \left ( \frac{1}{d} \sum*{d}^{i=1} \cos (cx*{i}) \right ) + \alpha + exp(1) \]</td>
        <td style="width: 10%;"><p align = "right">(1)</p></td>
    </tr>
    <tr>
        <td style="width: 90%;">\[f(\mathbf{x}^*) = 0, \; \mathbf{x}^* = (0,...,0) \]</td>
        <td style="width: 10%;"><p align = "right">(2)</p></td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
      Considering the design variable \(\mathbf{x} = [0,0]\), what value does the objective function expect?
  </i>
</p>

```python
# Data
x = [0, 0]

# Call function
of_griewank = griewank(x)

# Output details
print("of_best griewank: of = {:.4f}".format(of_griewank))
```

```bash
of_best griewank: of = 0.0000
```
