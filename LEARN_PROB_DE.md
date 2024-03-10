---
layout: default
title: Differential Evolution
parent: Probabilistic
grand_parent: Learning
nav_order: 4
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
Differential Evolution (DE) is a global optimization technique introduced in the late 1990s by Storn and Price <a href="#ref1">[1]</a>. DE works in two phases: initialization and evolution. In the first phase, population is generated randomly, and in the second phase, which is evolution, the generated population goes through mutation, crossover and selection processes, which are repeated until the termination criteria is met <a href="#ref2">[2]</a>.
</p>

<h4><i>Mutation</i></h4>

<p align = "justify">
Mutation specifies how a DE makes small random changes in the individuals in the population to create mutated children (\(\symbf{v}\)). Mutation provides genetic diversity and enables DE algorithm to search a broader space. A mutant vector is generated using one of following five most popular mutation strategies <a href="#ref3">[3]</a>. \(\symbf{x}_{r}\) is a random vector selected into the population, \(f\) is a parameter called the scale factor that controls the magnitude of the difference vector and \(k\) is the \(k\)th component of the design variable vector.
</p>

<table style = "width:100%">
    <tr>
        <td style="width: 80%;">\[ v_{k} = x_{r0,k}^{t} + f \cdot \left( x_{r1,k}^{t} - x_{r2,k}^{t} \right) \]</td>
        <td style="width: 10%;">rand/1</td>
        <td style="width: 10%;"><p align = "right" id = "eq1">(1)</p></td>
    </tr>
    <tr>
        <td style="width: 80%;">\[ v_{k} = x_{r0,k}^{t} + f \cdot \left( x_{r1,k}^{t} - x_{r2,k}^{t} \right) + f \cdot \left( x_{r3,k}^{t} - x_{r4,k}^{t} \right) \]</td>
        <td style="width: 10%;">rand/2</td>
        <td style="width: 10%;"><p align = "right" id = "eq2">(2)</p></td>
    </tr>
    <tr>
        <td style="width: 80%;">\[ v_{k} = x_{best,k}^{t} + f \cdot \left( x_{r0,k}^{t} - x_{r1,k}^{t} \right) \]</td>
        <td style="width: 10%;">best/1</td>
        <td style="width: 10%;"><p align = "right" id = "eq3">(3)</p></td>
    </tr>
    <tr>
        <td style="width: 80%;">\[ v_{k} = x_{best,k}^{t} + f \cdot \left( x_{r0,k}^{t} - x_{r1,k}^{t} \right) + f \cdot \left( x_{r2,k}^{t} - x_{r3,k}^{t} \right) \]</td>
        <td style="width: 10%;">best/2</td>
        <td style="width: 10%;"><p align = "right" id = "eq4">(4)</p></td>
    </tr>
    <tr>
        <td style="width: 80%;">\[ v_{k} = x_{i,k}^{t} + f \cdot \left( x_{best,k}^{t} - x_{r0,k}^{t} \right) + f \cdot \left( x_{r1,k}^{t} - x_{r2,k}^{t} \right) \]</td>
        <td style="width: 10%;">current-to-best/1</td>
        <td style="width: 10%;"><p align = "right" id = "eq5">(5)</p></td>
    </tr>
</table>

<p align = "justify">
In the equations above, \(r_0\), \(r_1\), \(r_2\), \(r_3\) and \(r_4\) and exclusive integer numbers ranging from 1 to number of population and they are different from current solution \(i\). \(\symbf{x_{best}}\) is the best individual in the current population and \(t\) is a current iteration.
</p>

<h4><i>Crossover</i></h4>

<p align = "justify">
After mutation, crossover is executed based on current solution (\(\symbf{x}_i^{t}\)); and mutation solution (\(\symbf{v}\)) to generate trial vectors (\(\symbf{u}\)). The binomial crossover operator is mostly used and it is defined as <a href="#ref3">[3,4]</a>:
</p>

<h5><u>Binomial crossover</u></h5>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[ u_k = \left\{\begin{matrix}
                                    v_k \;\; if \;rand(0,1)\leq p_c\\ 
                                    x_{i,k}^t \; \; otherwise
                                    \end{matrix}\right. \]</td>
        <td style="width: 10%;"><p align = "right" id = "eq1">(6)</p></td>
    </tr>
</table>

<p align = "justify">
\(p_c\) is the crossover rate (\(p_c \in \left[0,1\right] \)).
<br><br>
Once the trial vector is produced, the selection operator will make comparison between the target vector \(\symbf{x}_i\) and the
trial vector \(\symbf{u}\) and choose the superior one to survive to the next generation. The selection operator is performed as
below <a href="#ref3">[3]</a>:
</p>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[ \symbf{x}_i^{t+1} = \left\{\begin{matrix}
                                    \symbf{x}_i^{t} \;\; if \;f(\symbf{x}_i^{t})\leq f(\symbf{u})\\ 
                                    \symbf{u} \; \; otherwise
                                    \end{matrix}\right. \]</td>
        <td style="width: 10%;"><p align = "right" id = "eq1">(7)</p></td>
    </tr>
</table>

<h3>Algorithm</h3>

```python
1:  Input initial parameters (p_c, p_m, n_population,n_iteration, x_lower, x_upper, fit_function, obj_function, n_dimensions)
2:  Input initial guess (x_pop)
3:  Calculate of and fit (initial population)
4:  for iter in range(n_iterations):
5:      Apply selection operator
6:      r = random number [0,1]
7:      if r <=p_c: 
8:         Apply crossover operator
9:      r = random number [0,1]
10:     if r <= p_m:              
11:        Apply mutation operator
12:     if fit(x_temp) > fit(x_pop):
13:        x_pop(iter+1) = x_temp
14:     else:
15:        x_pop(iter+1) = x_pop(iter)
```

<p align = "justify">
See <a href="https://wmpjrufg.github.io/METAPY/FRA_GA_GA.html" target="_blank">GA algorithm</a> in METApy Framework.
</p>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
      Use the Genetic Algorithm optimization method to optimize the 2D sphere function. Use a total of 2 iterations to perform the optimization. Consider the limits \(\mathbf{x}_L = [-5.0, -5.0]\) and \(\mathbf{x}_U = [5.0, 5.0]\) for the problem design variables. Consider the initial guess (Three agents) \(\mathbf{pop}_0 = [-0.74, 1.25]\), \(\mathbf{pop}_1 = [3.58, -3.33]\) and \(\mathbf{pop}_2 = [1.50, 1.50]\). Use roulette wheel for selection procedure, linear crossover for crossover (82% rate) and hill climbing mutation (12% rate, \(cov=15\%\) and Gaussian generator).
  </i>
</p>


<h5>Solution</h5>

```
Genetic Algorithm 01- report 

Initial population
x0 = [-0.74, 1.25], of_pop 2.1101, fit 0.3215330696762162 - best solution
x1 = [3.58, -3.33], of_pop 23.9053, fit 0.040152096140179 
x2 = [1.5, 1.5], of_pop 4.5, fit 0.18181818181818182 

Iterations

Iteration: 1
Pop id: 0 - particle movement
    Selection operator
    sum(fit) = 0.22197027795836083
    probs(fit) = [0.0, 0.18088951597254424, 0.8191104840274557]
    selected agent id = 1
    Crossover operator - Linear crossover
    offspring a = [1.42, -1.04], of_a 3.098
    offspring b = [-2.9, 3.54], of_b 20.9416
    offspring c = [5.0, -5.0], of_c 50.0
    update x = [1.42, -1.04], of = 3.098, fit = 0.2440214738897023
    Mutation operator
    Dimension 0: mean = 1.42, sigma = 0.21299999999999997, neighbor = 1.4985129991098818
    Dimension 1: mean = -1.04, sigma = 0.15600000000000003, neighbor = -1.0535911109506693
    update x = [1.4985129991098818, -1.0535911109506693], of = 3.355595437575558, fit = 0.22958973447649375
    fit_i_temp < fit_pop[pop] - not accept this solution
Pop id: 1 - particle movement
    Selection operator
    sum(fit) = 0.5033512514943981
    probs(fit) = [0.6387846831047258, 0.0, 0.36121531689527414]
    selected agent id = 2
    Crossover operator - Linear crossover
    offspring a = [2.54, -0.915], of_a 7.288825
    offspring b = [4.62, -5.0], of_b 46.3444
    offspring c = [0.45999999999999996, 3.915], of_c 15.538825000000001
    update x = [2.54, -0.915], of = 7.288825, fit = 0.12064436153495822
    No mutation 0.9041777148613984 > p_m = 0.12 
    fit_i_temp > fit_pop[pop] - accept this solution
Pop id: 2 - particle movement
    Selection operator
    sum(fit) = 0.4421774312111744
    probs(fit) = [0.7271584820498423, 0.2728415179501576, 0.0]
    selected agent id = 0
    Crossover operator - Linear crossover
    offspring a = [0.38, 1.375], of_a 2.035025
    offspring b = [2.62, 1.625], of_b 9.505025
    offspring c = [-1.8599999999999999, 1.125], of_c 4.725225
    update x = [0.38, 1.375], of = 2.035025, fit = 0.32948657754054744
    No mutation 0.6805018349694458 > p_m = 0.12 
    fit_i_temp > fit_pop[pop] - accept this solution
update solutions
x0 = [-0.74, 1.25], of_pop 2.1101, fit 0.3215330696762162 
x1 = [2.54, -0.915], of_pop 7.288825, fit 0.12064436153495822 
x2 = [0.38, 1.375], of_pop 2.035025, fit 0.32948657754054744 - best solution

Iteration: 2
Pop id: 0 - particle movement
    Selection operator
    sum(fit) = 0.45013093907550566
    probs(fit) = [0.0, 0.2680205937026718, 0.7319794062973282]
    selected agent id = 2
    No crossover 0.8211070296158199 > p_c = 0.82 
    No mutation 0.2091585539994938 > p_m = 0.12 
    fit_i_temp < fit_pop[pop] - not accept this solution
Pop id: 1 - particle movement
    Selection operator
    sum(fit) = 0.6510196472167636
    probs(fit) = [0.4938914993592482, 0.0, 0.5061085006407519]
    selected agent id = 2
    No crossover 0.931387636116316 > p_c = 0.82 
    Mutation operator
    Dimension 0: mean = 2.54, sigma = 0.381, neighbor = 1.8273474406304766
    Dimension 1: mean = -0.915, sigma = 0.13725, neighbor = -1.071939271796121
    update x = [1.8273474406304766, -1.071939271796121], of = 4.488252471197551, fit = 0.18220736113143812
    fit_i_temp > fit_pop[pop] - accept this solution
Pop id: 2 - particle movement
    Selection operator
    sum(fit) = 0.5037404308076543
    probs(fit) = [0.6382911714287011, 0.361708828571299, 0.0]
    selected agent id = 0
    Crossover operator - Linear crossover
    offspring a = [-0.18, 1.3125], of_a 1.75505625
    offspring b = [0.9400000000000001, 1.4375], of_b 2.9500062500000004
    offspring c = [-1.2999999999999998, 1.1875], of_c 3.1001562499999995
    update x = [-0.18, 1.3125], of = 1.75505625, fit = 0.3629689956421035
    No mutation 0.964612378290656 > p_m = 0.12 
    fit_i_temp > fit_pop[pop] - accept this solution
update solutions
x0 = [-0.74, 1.25], of_pop 2.1101, fit 0.3215330696762162 
x1 = [1.8273474406304766, -1.071939271796121], of_pop 4.488252471197551, fit 0.18220736113143812 
x2 = [-0.18, 1.3125], of_pop 1.75505625, fit 0.3629689956421035 - best solution
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
            <td><p align = "left"><a href="https://doi.org/10.1023/A:1008202821328" target="_blank" rel="noopener noreferrer">Storn, R., Price, K. (1997) Differential Evolution – A Simple and Efficient Heuristic for global Optimization over Continuous Spaces. Journal of Global Optimization 11, 341–359.</a></p></td>
        </tr>
        <tr>
            <td><p align = "center" id = "ref2">[2]</p></td>
            <td><p align = "left"><a href="https://doi.org/10.1016/j.engappai.2020.103479" target="_blank" rel="noopener noreferrer">Bilal, Pant, M., Zaheer, H., Garcia-Hernandez, L., & Abraham, A. (2020). Differential Evolution: A review of more than two decades of research. Engineering Applications of Artificial Intelligence, 90, 103479.</a></p></td>
        </tr>
        <tr>
            <td><p align = "center" id = "ref3">[3]</p></td>
            <td><p align = "left"><a href="https://doi.org/10.1016/j.ins.2017.09.053" target="_blank" rel="noopener noreferrer">Wu, Guohua; Shen, Xin; Li, Haifeng; Chen, Huangke; Lin, Anping; Suganthan, P.N. (2018). Ensemble of differential evolution variants. Information Sciences, 423.</a></p></td>
        </tr>
        <tr>
            <td><p align = "center" id = "ref4">[4]</p></td>
            <td><p align = "left"><a href="https://doi.org/10.1016/j.ins.2017.09.053" target="_blank" rel="noopener noreferrer">Juan Yao,Zhe Chen ,Zhenling Liu (2020). Improved ensemble of differential evolution variants. PLoS ONE 16(8): e02562.</a></p></td>
        </tr>
    </tbody>
</table>
