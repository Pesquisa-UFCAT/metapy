---
layout: default
title: ackley
grand_parent: Benchmark
parent: Mathematical Functions
has_children: false
has_toc: true
nav_order: 4
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>ackley</h3>

<br>

<p align="justify">
  The Ackley function is widely used for testing optimization algorithms. In its two-dimensional form, as shown in the plot above, it is characterized by a nearly flat outer region, and a large hole at the centre <a href="#ref1">[1]</a>.
</p>


```python
of = ackley(x)
```

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
        <td>A list or array containing the values for the dimensions of the input. This represents the point in the input space for which the Ackley function is being evaluated.</td>
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
of_ackley = ackley(x)

# Output details
print("of_best rastrigin: of = {:.4f}".format(of_rastrigin))
```

```bash
of_best ackley: of = 0.0000
```

<h3>Reference list</h3>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Reference</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><p align = "center" id = "ref1">[1]</p></td>
            <td><p align = "left"><a href="https://doi.org/10.1007/s00521-016-2328-2" target="_blank" rel="noopener noreferrer">Sonja Surjanovic, Derek Bingham. Virtual Library os Simulation Experiments, Simon Fraser University, accessed 20 February 2024, <https://www.dss.gov.au/>.</a></p></td>
        </tr>
    </tbody>
</table>