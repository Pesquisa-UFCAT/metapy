---
layout: default
title: Simulated Annealing
parent: Probabilistic
grand_parent: Learning
nav_order: 2
has_children: true
has_toc: true
---
<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>Theory</h3>

<p align = "justify">
The Simulated Annealing method was introduced by Kirkpatrick et al. <a href="#ref1">[1,2]</a> in 1983. This algorithm is inspired by the annealing process of metals during the manufacturing process. The Simulated Annealing model is based on the generation of random neighbors from a starting point, similar to what occurs in the Hill Climbing Algorithm (see <a href="https://wmpjrufg.github.io/METAPY/FRA_ALG_HILL_01.html" target="_blank">HC algorithm</a>).
<br><br>
In the Simulated Annealing algorithm, the acceptance of the new solution (see new solution procedure in see <a href="https://wmpjrufg.github.io/METAPY/FRA_ALG_HILL_01.html" target="_blank">HC algorithm</a>) is given by a criterion that compares the energy of the system given by equation (1). In this algorithm, the values of \(E_{i}\) are relative to the value of the objective function to \(i\) particle, i.e., \(E_{i}=OF_{i}\).
</p>

<table style = "width:100%">
    <tr>
        <td>\[\Delta E = E_{cur}-E_{new}\]</td>
        <td><p align = "right">(1)</p></td>
    </tr>
</table>

<p align = "justify">
The value \(E_{new}\) is the value of the objective function for the newly generated neighbor and \(E_{cur}\) is the value of the objective function for the current particle. 
<br><br>
The solution will be accepted if \(E_{cur} > E_{new}\) (\(P(\Delta E)=1.00\)). For solutions of type \(E_{cur} < E_{new}\) the acceptance will follow a certain probability given by equation (2) where \(T\) the annealing temperature.
</p>

<table style = "width:100%">
    <tr>
        <td>\[P(\Delta E) = e^{\frac{-\Delta E}{T}}\]</td>
        <td><p align = "right">(2)</p></td>
    </tr>
</table>

<h3>Algorithm</h3>

```python
1:  Input initial parameters (temp, pdf, cov)
2:  X = Initial solution
3:  Calculate OF and FIT
4:  for I in range(N_ITER):
5:      X_TEMP = new neighbor solution
6:      DELTA_E = equation(1)
7:      if DELTA_E > 0:
8:         PROB = 1
9:      else:
10:        PROB = equation(2)
11:     R = random number [0,1]
12:     if PROB > R:
13:        X(I+1) = X_NEW # Accept new solution
14:     else:
15:        X(I+1) = X(I)  # Ignore new solution
16:     Update temperature     
```

<p align = "justify">
At the end of the algorithm, the temperature is updated. \(\alpha\) is the cooling temperature adjustment factor. The methods for updating the temperature are:

<ul>
  <li>Geometric: See equation (3);</li>
  <li>Lundy: See equation (4);</li>
  <li>Linear: See equation (5);</li>
  <li>Logarithmic: See equation (6);</li>
</ul>
</p>

<table style = "width:100%">
    <tr>
        <td>\[T_{i+1} = T_{i}.\alpha\]</td>
        <td><code>'GEOMETRIC'</code></td>
        <td><p align = "right">(3)</p></td>
    </tr>
    <tr>
        <td>\[T_{i+1} = \frac{T_{i}}{1+\alpha.T}\]</td>
        <td><code>'LUNDY'</code></td>
        <td><p align = "right">(4)</p></td>
    </tr>
    <tr>
        <td>\[T_{i+1} = T_{i} - \alpha\]</td>
        <td><code>'LINEAR'</code></td>
        <td><p align = "right">(5)</p></td>
    </tr>
    <tr>
        <td>\[T_{i+1} = \frac{T_{i}}{\ln(i+\alpha)}\]</td>
        <td><code>'LOGARITHMIC'</code></td>
        <td><p align = "right">(6)</p></td>
    </tr>
</table>
