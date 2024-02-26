---
layout: default
title: Michalewicz
grand_parent: Benchmark
parent: Mathematical Functions
has_children: false
has_toc: true
nav_order: 8
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

```python
of = michalewicz(x)
```

<p align="justify">
    The Michalewicz function has d! local minima, and it is multimodal. 
    The parameter m defines the steepness of they valleys and ridges; 
    a larger m leads to a more difficult search <a href="#ref1">[1]</a>.
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
        <td>This is a list or array representing the input vector to the Michalewicz function. It is the point at which the function is evaluated.</td>
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
        <td>It represents the result of evaluating the Michalewicz function at the given input x.</td>
        <td>Float</td>
    </tr>
</table>

<h3>Problem</h3>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[f(\mathbf{x}) =   -\cos{x_{1}} \cos{x_{2}} exp \left ( -\left ( x_{1} - \pi \right )^2  - ( -\left ( x_{2} - \pi \right )^2  \right ) \]</td>
        <td style="width: 10%;"><p align = "right">(1)</p></td>
    </tr>
    <tr>
        <td style="width: 90%;">\[ x_{i} \in [0, \pi], i=1, ... , d; \; d = 2: \;...\;  f(\mathbf{x}^*) = -1.8013, \; \mathbf{x}^* = (2.20, 1.57) \]</td>
        <td style="width: 10%;"><p align = "right">(2)</p></td>
    </tr>
    <tr>
      <td style="width: 90%;">\[x_{i} \in [0, \pi], i=1, ... , d; \; d = 5; \;...\;  f(\mathbf{x}^*) = -4.687658 \]</td>
      <td style="width: 10%;"><p align = "right">(3)</p></td>
    </tr>
    <tr>
      <td style="width: 90%;">\[x_{i} \in [0, \pi], i=1, ... , d; \; d = 10; \;...\;  f(\mathbf{x}^*) = -9.66015 \]</td>
      <td style="width: 10%;"><p align = "right">(4)</p></td>
    </tr>

</table>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
      Considering the design variable \(\mathbf{x} = [2.20, 1.57]\), what value does the objective function expect?
  </i>
</p>

```python
x = [2.20, 1.57]

# Call function
of_michalewicz = michalewicz(x)

# Output details
print("of_best michalewicz: of = {:.4f}".format(of_michalewicz))
```

```bash
of_best michalewicz: of = -0.0010
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
            <td><p align = "left"><a href="https://www.sfu.ca/~ssurjano/michal.html" target="_blank" rel="noopener noreferrer">Sonja Surjanovic, Derek Bingham. Virtual Library os Simulation Experiments, Simon Fraser University, accessed 20 February 2024, <www.sfu.ca/~ssurjano/optimization>.</a></p></td>
        </tr>
    </tbody>
</table>
