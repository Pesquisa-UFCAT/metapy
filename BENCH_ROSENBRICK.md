---
layout: default
title: Rosenbrick
grand_parent: Benchmark
parent: Mathematical Functions
has_children: false
has_toc: true
nav_order: 2
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

```python
of = rosenbrock(x=x)
```

<p align="justify">
The Rosenbrock function is unimodal, and the global minimum lies in a narrow, parabolic valley. However, even though  this valley is easy to find, convergence to the minimum is  difficult (Picheny et al., 2012).
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
        <td>This parameter represents the input vector for which the Rosenbrock function is evaluated. It's expected to be a list or array-like object containing numerical values.</td>
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
        <td> Objective function value, representing the result of evaluating the Rosenbrock function for the given input vector x.</td>
        <td>float</td>
    </tr>
</table>

<h3>Problem</h3>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[f(\mathbf{x}) = \sum_{i=1}^{d-1}\left [  100 \left ( x_{i+1} - x_{i}^{2} \right )_{}^{2}  + \left ( x_{i} + 1 \right )_{}^{2}  \right ]  \]</td>
        <td style="width: 10%;"><p align = "right">(1)</p></td>
    </tr>
    <tr>
        <td style="width: 90%;">\[f(\mathbf{x}^*) = 0, \; \mathbf{x}^* = (1,...,1) \]</td>
        <td style="width: 10%;"><p align = "right">(2)</p></td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
      Considering the design variable \(\mathbf{x} = [1,1]\), what value does the objective function expect?
  </i>
</p>

```python
# Data
  x_rosenbrock = [1, 1]

  # Call function
  of_rosenbrock = rosenbrock(x_rosenbrock, None)

  # Output details
  print("of_best rosenbrock: of = {:.4f}".format(of_rosenbrock))
```

```bash
of_best rosenbrock: of = 0.0000
```
