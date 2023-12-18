---
title: Fit value
layout: home
grand_parent: Framework
parent: Common Library
has_children: true
nav_order: 4
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<!--

FIT_VALUE
{: .label .label-green }
-->

```python
fitI = FIT_VALUE(ofI)
```

<p align = "justify">
    This function calculates the fitness of the fitness of the \(i\) agent.
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
        <td><code>OF_I_VALUE</code></td>
        <td>Object function value of the \(i\) agent</td>
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
        <td><code>FIT_I_VALUE</code></td>
        <td>Fitness value of the \(i\) agent</td>
        <td>float</td>
    </tr>
</table>

Theory
{: .label .label-red }

<p align = "justify">
        The fitness function, in simple terms, is a function that takes a potential solution to a problem as input and produces an output indicating how "fit" or how "good" the solution is concerning the specific problem under consideration. Equation <a href="#eq1">(1)</a> presents the fitness function implemented in the METApy framework.
</p>

<table border = "0" style = "width: 100%;">
  <tr>
    <td align = "left" style = "width: 95%;">\[\begin{cases} fit_i = \frac{1}{1+of_i} & \: \text{if} \: of_i \leq 0 \\ fit_i = 1+\lvert of_{i}\rvert & \: \text{if} \: of_i > 0 \end{cases}\]</td>
    <td align = "right" style = "width: 5%;"><p id = "eq1">(1)</p></td>
  </tr>
</table>

Example 4
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>FIT_VALUE</code> function to generate the fitness of the \(i\) agent. 
    </i>
</p>

```python
# Data
nPop = 3
ofI = 1

# Call function
fitI = FIT_VALUE(ofI)

# Output details
print(f'fit value i agent when OF = {ofI} is ', fitI)
```

```bash
fit value i agent when OF = 1 is  0.5
```
