---
layout: default
title: Sphere
grand_parent: Benchmark
parent: Mathematical Functions
has_children: false
has_toc: false
nav_order: 1
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

```python
of = sphere(x=x)
```

<p align="justify">
The sphere function has \(d\) local minima except for the global one. It is continuous, convex and unimodal.
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
        <td>This parameter represents the input point in the \(n\)-dimensional space for which the Sphere function value is to be computed.</td>
        <td>List</td>
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
        <td>The function returns the value of the Sphere function at the given design variable \(\mathbf{x}\).</td>
        <td>Float</td>
    </tr>
</table>

<h3>Problem</h3>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[f(\mathbf{x}) = \sum_{i=1}^{n} x_{i}^{2}\]</td>
        <td style="width: 10%;"><p align = "right">(1)</p></td>
    </tr>
    <tr>
        <td style="width: 90%;">\[f(\mathbf{x}^*) = (0,..,0), \; \mathbf{x}^* = [0,...,0] \]</td>
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
