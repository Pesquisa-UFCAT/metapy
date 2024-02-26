---
layout: default
title: Powell
grand_parent: Benchmark
parent: Mathematical Functions
has_children: false
has_toc: true
nav_order: 11
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

```python
of = powell(x)
```

<p align="justify">
     The Powell function has several local minima <a href="#ref1">[1]</a>.
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
        <td>This is a list or array representing the input vector to the Powell function. It is the point at which the function is evaluated.</td>
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
        <td>It represents the result of evaluating the Powell function at the given input x.</td>
        <td>float</td>
    </tr>
</table>

<h3>Problem</h3>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[ f(\mathbf{x}) =  \sum^{d/4}_{i=1} \left [   \left ( x_{4i-3} + 10x_{4i-2} \right )^2 + 5\left ( x_{4i-2} -  2x_{4i-1} \right )^4 + 10\left ( x_{4i-3} 
 -x_{4i}  \right )^4  \right ]    \]</td>
        <td style="width: 10%;"><p align = "right">(1)</p></td>
    </tr>
    <tr>
        <td style="width: 90%;">\[x_{i} \in [-4, 5], i=1, ... ,d; \;...\; f(\mathbf{x}^*) = 0, \; \mathbf{x}^* = \left ( 0, ... , 0 \right ) \]</td>
        <td style="width: 10%;"><p align = "right">(2)</p></td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
      Considering the design variable \(\mathbf{x} = [0, 0]\), what value does the objective function expect?
  </i>
</p>

```python
# Data
x = [0, 0]

# Call function
of_powell = powell(x)

# Output details
print("of_best powell: of = {:.4f}".format(of_powell))
```

```bash
of_best powell: of = 0.0000
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
            <td><p align = "left"><a href="https://www.sfu.ca/~ssurjano/powell.html" target="_blank" rel="noopener noreferrer">Sonja Surjanovic, Derek Bingham. Virtual Library os Simulation Experiments, Simon Fraser University, accessed 20 February 2024, <www.sfu.ca/~ssurjano/optimization>.</a></p></td>
        </tr>
    </tbody>
</table>
