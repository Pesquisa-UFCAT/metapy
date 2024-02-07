---
layout: default
title: Rosenbrick function
parent: Mathematical Functions
grandparent: Benchmark
has_children: false
nav_order: 2
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

ROSENBRICK
{: .label .label-green }

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
