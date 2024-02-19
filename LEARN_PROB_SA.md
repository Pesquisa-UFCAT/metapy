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
The Simulated Annealing method was introduced by Kirkpatrick et al. <a href="#ref1">[1]</a> in 1983. The annealing process of metals inspires this algorithm during the manufacturing process. The Simulated Annealing model is based on generating random neighbors from a starting point, similar to what occurs in the Hill Climbing Algorithm (see <a href="https://wmpjrufg.github.io/METAPY/LEARN_PROB_HILL.html" target="_blank">HC algorithm</a>).
<br><br>
In the Simulated Annealing algorithm, the acceptance of the new solution (see new solution procedure in see <a href="https://wmpjrufg.github.io/METAPY/LEARN_PROB_HILL.html" target="_blank">HC algorithm</a>) is given by a criterion that compares the system's energy given by equation <a href="#eq1">(1)</a>. In this algorithm, the values of \(E_{i}\) are relative to the value of the objective function to \(i\) particle, i.e., \(E_{i}=of_{i}\).
</p>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[\Delta E = E_{new} - E_{cur}\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq1">(1)</p></td>
    </tr>
</table>

<p align = "justify">
The value \(E_{new}\) is the value of the objective function for the newly generated neighbor, and \(E_{cur}\) is the value of the objective function for the current particle. 
<br><br>
The solution will be accepted if \( E_{cur} > E_{new} \left( P(\Delta E,T)=1.00 \right) \). For solutions of type \(E_{cur} < E_{new}\) the acceptance will follow a certain probability given by equation <a href="#eq2">(2)</a> where \(T\) the annealing temperature.
</p>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[P(\Delta E,T) = e^{\frac{-\Delta E}{T}}\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq2">(2)</p></td>
    </tr>
</table>

<p align = "justify">
At the end of the algorithm, the temperature is updated. \(\alpha\) is the cooling temperature adjustment factor. The methods for updating the temperature are (see Figure <a href="#fig01">1</a>):
</p>

<ul>
  <li>Geometric <a href="#ref3">[3]</a>: See equation <a href="#eq3">(3)</a>;</li>
  <li>Lundy <a href="#ref4">[5]</a>: See equation <a href="#eq4">(4)</a>;</li>
  <li>Linear <a href="#ref4">[4]</a>: See equation <a href="#eq5">(5)</a>;</li>
  <li>Exponential <a href="#ref2">[2]</a>: See equation <a href="#eq6">(6)</a>;</li>
</ul>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[T_{i+1} = \alpha \cdot T_{i} \]</td>
        <td style="width: 10%;"><p align = "right" id = "eq3">(3)</p></td>
    </tr>
    <tr>
        <td style="width: 90%;">\[T_{i+1} = \frac{T_{i}}{1+ \alpha \cdot T_{i}}\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq4">(4)</p></td>
    </tr>
    <tr>
        <td style="width: 90%;">\[T_{i+1} = T_{i} - \alpha \cdot T_{i} \]</td>
        <td style="width: 10%;"><p align = "right" id = "eq5">(5)</p></td>
    </tr>
    <tr>
        <td style="width: 90%;">\[T_{i+1} = T_{i} \cdot e^{-\alpha \cdot i}\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq6">(6)</p></td>
    </tr>
</table>

<center><img src="./imgs/sa/fig01.svg" width="70%"></center>
<p align = "center" id = "fig01"><b>Figure 1.</b> Colling schema.</p>

<h3>Start temperature</h3>

<p align = "justify">
The initial temperature \(T_0\) should be high enough large enough so that nearly all transitions are accepted at the first iterations. The initial probability of acceptance must not be close to one, neither must be close to zero. The probability of accepting a higher-cost solution was set to 0.80 <a href="#ref1">[6,7,8]</a>. The initial temperature is given by equation <a href="#eq7">(7)</a>:
</p>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[T_0 = \frac{-\Delta E^+}{\ln{0.80}}\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq7">(7)</p></td>
    </tr>
</table>

<p align = "justify">
\(\Delta E^+\) represents the energy of strictly positive transitions, i.e. \(\Delta E > 0 \).
</p>

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
16:     temp_update = equation (3) - (6)
```

{: .note }
> The Simulated Annealing algorithm can accept unfavorable moves. This characteristic depends on temperature and change in objective value ΔE.

<p align = "justify">
See <a href="https://wmpjrufg.github.io/METAPY/FRA_ALG_SA_01.html" target="_blank">SA algorithm</a> in METApy Framework.
</p>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
      Use the Simulated Annealing optimization method to optimize the 2D sphere function. Use a total of 2 iterations to perform the optimization. Consider the limits \(\mathbf{x}_L = [-5.0, -5.0]\) and \(\mathbf{x}_U = [5.0, 5.0]\) for the problem design variables. Consider the initial guess (two agents) \(\mathbf{pop}_0 = [-0.74, 1.25]\) and \(\mathbf{pop}_1 = [3.58, -3.33]\). Use \(cov = 20%\), Gaussian random generator, \(T_0 = 15\) and geometric schedule (\(\alpha = 0.90\)).
  </i>
</p>


<h5>Solution</h5>

```
Simulated Annealing 01 - report 

Initial population
x0 = [-0.74, 1.25], of_pop 2.1101 - best solution
x1 = [3.58, -3.33], of_pop 23.9053 

Iterations

Iteration: 1
Temperature: 15
Pop id: 0 - particle movement - mutation procedure
    current x = [-0.74, 1.25], of = 2.1101, fit = 0.3215330696762162
    Dimension 0: mean = -0.74, sigma = 0.14800000000000002, neighbor = -1.0351744807425902
    Dimension 1: mean = 1.25, sigma = 0.25, neighbor = 1.5447852100500892
    update x = [-1.0351744807425902, 1.5447852100500892], of = 3.4579475507701893, fit = 0.22431847584820336
    energy = 1.3478475507701893, prob. state = 0.9140623407129066
    prob. state 0.9140623407129066 >= random number 0.6630641248277662 - accept this solution
Pop id: 1 - particle movement - mutation procedure
    current x = [3.58, -3.33], of = 23.9053, fit = 0.040152096140179
    Dimension 0: mean = 3.58, sigma = 0.716, neighbor = 3.9447170160318668
    Dimension 1: mean = -3.33, sigma = 0.6659999999999999, neighbor = -3.7756500200969305
    update x = [3.9447170160318668, -3.7756500200969305], of = 29.816325410829307, fit = 0.03245033230498615
    energy = 5.911025410829307, prob. state = 0.674307958485963
    prob. state 0.674307958485963 >= random number 0.11118541366280277 - accept this solution
update solutions
x0 = [-1.0351744807425902, 1.5447852100500892], of_pop 3.4579475507701893 - best solution
x1 = [3.9447170160318668, -3.7756500200969305], of_pop 29.816325410829307 

Iteration: 2
Temperature: 13.5
Pop id: 0 - particle movement - mutation procedure
    current x = [-1.0351744807425902, 1.5447852100500892], of = 3.4579475507701893, fit = 0.22431847584820336
    Dimension 0: mean = -1.0351744807425902, sigma = 0.20703489614851806, neighbor = -0.9559782630786865
    Dimension 1: mean = 1.5447852100500892, sigma = 0.30895704201001783, neighbor = 1.0793006180821911
    update x = [-0.9559782630786865, 1.0793006180821911], of = 2.078784263671542, fit = 0.3248035309909861
    energy = -1.3791632870986472, prob. state = 1
    prob. state 1 >= random number 0.40559404312719416 - accept this solution
Pop id: 1 - particle movement - mutation procedure
    current x = [3.9447170160318668, -3.7756500200969305], of = 29.816325410829307, fit = 0.03245033230498615
    Dimension 0: mean = 3.9447170160318668, sigma = 0.7889434032063734, neighbor = 3.3478221189294404
    Dimension 1: mean = -3.7756500200969305, sigma = 0.7551300040193861, neighbor = -3.871949506115549
    update x = [3.3478221189294404, -3.871949506115549], of = 26.199905917901653, fit = 0.03676483304825877
    energy = -3.6164194929276547, prob. state = 1
    prob. state 1 >= random number 0.5368960666312674 - accept this solution
update solutions
x0 = [-0.9559782630786865, 1.0793006180821911], of_pop 2.078784263671542 - best solution
x1 = [3.3478221189294404, -3.871949506115549], of_pop 26.199905917901653   
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
            <td><p align = "left"><a href="https://www.science.org/doi/10.1126/science.220.4598.671" target="_blank" rel="noopener noreferrer">Kirkpatrick, S.; Gelatt, C. D.; Vecchi, M. P. (1983). Optimization by Simulated Annealing. , 220(4598), 671–680.</a></p></td>
        </tr>
        <tr>
            <td><p align = "center" id = "ref2">[2]</p></td>
            <td><p align = "left"><a href="https://doi.org/10.1063/5.0018725" target="_blank" rel="noopener noreferrer">Karabin, M., & Stuart, S. J. (2020). Simulated annealing with adaptive cooling rates. The Journal of Chemical Physics, 153(11).</a></p></td>
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
        <tr>
            <td><p align = "center" id = "ref6">[6]</p></td>
            <td><p align = "left"><a href="https://doi.org/10.1007/978-3-319-91086-4_1" target="_blank" rel="noopener noreferrer">Delahaye, D., Chaimatanan, S., Mongeau, M. (2019). Simulated Annealing: From Basics to Applications. In: Gendreau, M., Potvin, JY. (eds) Handbook of Metaheuristics. International Series in Operations Research & Management Science, vol 272. Springer, Cham.</a></p></td>
        </tr>
        <tr>
            <td><p align = "center" id = "ref7">[7]</p></td>
            <td><p align = "left"><a href="https://doi.org/10.1007/978-3-540-24767-8_41" target="_blank" rel="noopener noreferrer">Atiqullah, M.M. (2004). An Efficient Simple Cooling Schedule for Simulated Annealing. In: Laganá, A., Gavrilova, M.L., Kumar, V., Mun, Y., Tan, C.J.K., Gervasi, O. (eds) Computational Science and Its Applications – ICCSA 2004. ICCSA 2004. Lecture Notes in Computer Science, vol 3045. Springer, Berlin, Heidelberg.</a></p></td>
        </tr>
        <tr>
            <td><p align = "center" id = "ref8">[8]</p></td>
            <td><p align = "left"><a href="https://ieeexplore.ieee.org/document/5164685" target="_blank" rel="noopener noreferrer">Shakouri G., H.; Shojaee, Kambiz; Behnam T., M. (2009). [IEEE 2009 17th Mediterranean Conference on Control and Automation (MED) - Thessaloniki, Greece (2009.06.24-2009.06.26)] 2009 17th Mediterranean Conference on Control and Automation - Investigation on the choice of the initial temperature in the Simulated Annealing: A mushy state SA for TSP. , (), 1050–1055.</a></p></td>
        </tr>
    </tbody>
</table>


