---
layout: default
title: Dixon Price
grand_parent: Benchmark
parent: Mathematical Functions
has_children: false
has_toc: true
nav_order: 9
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

```python
of = dixonPrice(x)
```

<p align="justify">    
The Dixon prince function is a multimodal minimization <a href="#ref1">[1]</a>.
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
        <td>This is a list or array representing the input vector to the Dixon Price function. It is the point at which the function is evaluated.</td>
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
        <td>It represents the result of evaluating the Dixon Price function at the given input x.</td>
        <td>float</td>
    </tr>
</table>

<h3>Problem</h3>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[ f(\mathbf{x}) =   \left ( x_{1} - 1 \right )^2 + \sum^d_{i=2} i \left ( 2x^2_{i} - x_{i-1} \right )^2\]</td>
        <td style="width: 10%;"><p align = "right">(1)</p></td>
    </tr>
    <tr>
        <td style="width: 90%;">\[x_{i} \in [-10, 10], i=1, ... , d; \;f(\mathbf{x}^*) = 0, \; \mathbf{x}_{i} = 2^{-\frac{2^i - 2}{2^i}},  i = 1, ... , d    \]</td>
        <td style="width: 10%;"><p align = "right">(2)</p></td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
      Considering the design variable \(\mathbf{x} = [0, -1]\), what value does the objective function expect?
  </i>
</p>

```python
# Data
x = [0, -1]

# Call function
of_dixonPrice = dixonPrice(x)

# Output details
print("of_best dixon-Price: of = {:.4f}".format(of_dixonPrice))
```

```bash
of_best dixon-Price: of = 0.0000
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
            <td><p align = "left"><a href="https://www.sfu.ca/~ssurjano/dixonpr.html" target="_blank" rel="noopener noreferrer">Sonja Surjanovic, Derek Bingham. Virtual Library os Simulation Experiments, Simon Fraser University, accessed 20 February 2024, <www.sfu.ca/~ssurjano/optimization>.</a></p></td>
        </tr>
    </tbody>
</table>
