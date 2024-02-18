---
layout: default
title: Simulated Annealing
parent: Probabilistic
grand_parent: Learning
nav_order: 2
has_children: false
has_toc: false
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>Theory</h3>
<br>
<p align = "justify">
The Simulated Annealing method was introduced by Kirkpatrick et al. <a href="#ref1">[1]</a> in 1983. This algorithm is inspired by the annealing process of metals during the manufacturing process. The Simulated Annealing model is based on the generation of random neighbors from a starting point, similar to what occurs in the Hill Climbing Algorithm (see <a href="https://wmpjrufg.github.io/METAPY/LEARN_PROB_HILL.html" target="_blank">HC algorithm</a>).
<br><br>
In the Simulated Annealing algorithm, the acceptance of the new solution (see new solution procedure in see <a href="https://wmpjrufg.github.io/METAPY/LEARN_PROB_HILL.html" target="_blank">HC algorithm</a>) is given by a criterion that compares the energy of the system given by equation <a href="#eq1">(1)</a>. In this algorithm, the values of \(E_{i}\) are relative to the value of the objective function to \(i\) particle, i.e., \(E_{i}=of_{i}\).
</p>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[\Delta E = E_{new} - E_{cur}\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq1">(1)</p></td>
    </tr>
</table>

<p align = "justify">
The value \(E_{new}\) is the value of the objective function for the newly generated neighbor and \(E_{cur}\) is the value of the objective function for the current particle. 
<br><br>
The solution will be accepted if \(E_{cur} > E_{new}\) (\(P(\Delta E)=1.00\)). For solutions of type \(E_{cur} < E_{new}\) the acceptance will follow a certain probability given by equation <a href="#eq2">(2)</a> where \(T\) the annealing temperature.
</p>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[P(\Delta E) = e^{\frac{-\Delta E}{T}}\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq2">(2)</p></td>
    </tr>
</table>

<p align = "justify">
At the end of the algorithm, the temperature is updated. \(\alpha\) is the cooling temperature adjustment factor. The methods for updating the temperature are:

<ul>
  <li>Geometric <a href="#ref3">[3]</a>: See equation <a href="#eq3">(3)</a>;</li>
  <li>Lundy <a href="#ref4">[5]</a>: See equation <a href="#eq4">(4)</a>;</li>
  <li>Linear <a href="#ref4">[4]</a>: See equation <a href="#eq5">(5)</a>;</li>
  <li>Logarithmic <a href="#ref2">[2]</a>: See equation <a href="#eq6">(6)</a>;</li>
</ul>
</p>

<table style = "width:100%">
    <tr>
        <td>\[T_{i+1} = \alpha \cdot T_{i} \]</td>
        <td><code>'GEOMETRIC'</code></td>
        <td><p align = "right" id = "eq3">(3)</p></td>
    </tr>
    <tr>
        <td>\[T_{i+1} = \frac{T_{i}}{1+ \alpha \cdot T}\]</td>
        <td><code>'LUNDY'</code></td>
        <td><p align = "right" id = "eq4">(4)</p></td>
    </tr>
    <tr>
        <td>\[T_{i+1} = T_{i} - \alpha \cdot T_{i} \]</td>
        <td><code>'LINEAR'</code></td>
        <td><p align = "right" id = "eq5">(5)</p></td>
    </tr>
    <tr>
        <td>\[T_{i+1} = \frac{T_{i}}{\log_2(i+\alpha)}\]</td>
        <td><code>'LOGARITHMIC'</code></td>
        <td><p align = "right" id = "eq6">(6)</p></td>
    </tr>
</table>

<h3>Start temperature</h3>

<h3>Algorithm</h3>

```python
1:  Input initial parameters (temp, cov, n_population, x_lower, x_upper, obj_function, n_dimensions)
2:  Input initial guess (x_pop)
3:  Calculate of and fit (initial population)
4:  for iter in range(n_iterations):
5:      x_temp = neighbor solution equation hill climbing
6:      delta_e = equation (1)
7:      if delta_e > 0:
8:         prob = 1
9:      else:
10:        prob = equation (2)
11:     r = random number [0,1]
12:     if r <= prob:
13:        x_pop(iter+1) = x_temp
14:     else:
15:        x_pop(iter+1) = x_pop(iter)
16:     temp_update = 
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
            <td><p align = "left"><a href="https://www.science.org/doi/10.1126/science.220.4598.671" target="_blank" rel="noopener noreferrer">Kirkpatrick S, Gelatt CD, Vecchiai MP. Optimization by Simulated Annealing. Science 1983; 220: 671-680.</a></p></td>
        </tr>
        <tr>
            <td><p align = "center" id = "ref2">[2]</p></td>
            <td><p align = "left"><a href="https://www.sciencedirect.com/science/article/abs/pii/S0960077921004021?via%3Dihub" target="_blank" rel="noopener noreferrer">        Honglin Lv;Xueye Chen;Xiangwei Zeng; (2021). Optimization of micromixer with Cantor fractal baffle based on simulated annealing algorithm . Chaos, Solitons &amp; Fractals.</a></p></td>
        </tr>
        <tr>
            <td><p align = "center" id = "ref3">[3]</p></td>
            <td><p align = "left"><a href="https://www.sciencedirect.com/science/article/abs/pii/S0301420721000337" target="_blank" rel="noopener noreferrer">Abid Ali Khan Danish;Asif Khan;Khan Muhammad;Waqas Ahmad;Saad Salman; (2021). A simulated annealing based approach for open pit mine production scheduling with stockpiling option. Resources Policy.</a></p></td>
        </tr>
        <tr>
            <td><p align = "center" id = "ref4">[4]</p></td>
            <td><p align = "left"><a href="https://www.scirp.org/pdf/AM_2017083014324828.pdf" target="_blank" rel="noopener noreferrer">Peprah, A.K., Appiah, S.K. and Amponsah, S.K. (2017) An Optimal Cooling Schedule Using a Simulated Annealing Based Approach. Applied Mathematics, 8, 1195-1210.</a></p></td>
        </tr>
        <tr>
            <td><p align = "center" id = "ref5">[5]</p></td>
            <td><p align = "left"><a href="https://link.springer.com/article/10.1007/BF01582166" target="_blank" rel="noopener noreferrer">M. Lundy; A. Mees (1986). Convergence of an annealing algorithm. Mathematical Programming, 34(1), 111–124.</a></p></td>
        </tr>
    </tbody>
</table>
