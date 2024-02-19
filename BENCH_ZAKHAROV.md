---
layout: default
title: Zakharov
grand_parent: Benchmark
parent: Mathematical Functions
has_children: false
has_toc: true
nav_order: 6
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

```python
result = zakharov(x)
```

<p align="justify">
The Zakharov function has no local minima except the global one.
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
        <td>This is a list or array representing the input vector to the Zakharov function. It is the point at which the function is evaluated.</td>
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
        <td>It represents the result of evaluating the Zakharov function at the given input x.</td>
        <td>float</td>
    </tr>
</table>

<h3>Problem</h3>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[ f(\mathbf{x}) =  \sum_{i=1}^{d}  x^2_{i} + \left ( \sum_{i=1}^{d}  0.5ix_{i} \right )^2  + \left ( \sum_{i=1}^{d}  0.5ix_{i} \right )^4   \]</td>
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
of_zakharov = zakharov(x)

# Output details
print("of_best zakharov: of = {:.4f}".format(of_zakharov))
```

```bash
of_best zakharov: of = 0.0000
```
