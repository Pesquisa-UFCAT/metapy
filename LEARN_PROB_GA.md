---
layout: default
title: Genetic Algorithm
parent: Probabilistic
grand_parent: Learning
nav_order: 3
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
A Genetic Algorithm (GA) functions as a search metaheuristic, drawing inspiration from Charles Darwin's evolutionary theory. This algorithm reflects the process of natural selection, where the fittest individuals are selected for reproduction to produce offspring of the next generation <a href="#ref1">[1]</a>. Genetic Algorithm was developed by J. Holland <a href="#ref2">[2]</a>.
<br><br>
According to Darwin's theory of evolution, generations with characteristics of superiority over the other generations will have a greater chance of survival. Therefore, their superior characteristics will be transferred to the next generations. On the other hand, the second part of Darwin's theory states that when multiplying children, an event occurs that changes the characteristics of the children. If these changes benefit the children, it will increase the probability of survival for those children <a href="#ref3">[3,4]</a>.
<br><br>
In GA, the new populations are produced by iterative use of genetic operators on agents present in the population. These are the genetic operators considered in this algorithm <a href="#ref5">[5]</a>: 
</p>

<h3>Genetic operators</h3>

<h4><i>Selection</i></h4>

<p align = "justify">
    The selection function specifies how the Genetic algorithm chooses parents for the next generation.
</p>

<h5><u>Roulette Wheel</u></h5>

<p align = "justify">
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
</p>

<h4><i>Crossover</i></h4>

<p align = "justify">
The crossover function specifies how the Genetic Algorithm combines two individuals, or parents, to form a crossover child for the next generation.
</p>

<!-- Deletar após finalizar documentação 
https://sci-hub.wf/10.1007/978-3-319-52156-5

https://sci-hub.wf/10.1016/j.amc.2006.10.047

https://sci-hub.wf/10.1109/CEC.2001.934452

https://www.researchgate.net/publication/201976658_Simulated_Crossover_in_Genetic_Algorithms

https://medium.com/geekculture/crossover-operators-in-ga-cffa77cdd0c8

https://www.linkedin.com/pulse/crossovers-genetic-algorithms-ali-karazmoodeh-tthjf/

https://sci-hub.wf/10.1016/j.ijepes.2014.04.031-->

<h5><u>Linear crossover</u> <a href="#ref6">[6]</a></h5>

<p aling = "justify">
From the two parent points \(\symbf{p_1}\) and \(\symbf{p_2}\) three new points are generated. See equations <a href="#eq1">[1]</a> to <a href="#eq3">[3]</a>. \(k\) is the kth component of the design variable vector \(\symbf{ch}\).
</p>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[ ch_{0,k} = 0.50 \cdot p_{1,k}^{t} + 0.50 \cdot p_{2,k}^{t}\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq1">(1)</p></td>
    </tr>
    <tr>
        <td style="width: 90%;">\[ ch_{1,k} = 1.50 \cdot p_{1,k}^{t} - 0.50 \cdot p_{2,k}^{t}\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq2">(2)</p></td>
    </tr>
    <tr>
        <td style="width: 90%;">\[ ch_{2,k} = -0.50 \cdot p_{1,k}^{t} + 1.50 \cdot p_{2,k}^{t}\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq3">(3)</p></td>
    </tr>
</table>

<p aling = "justify">
The best one of the three points (offspring 0 - (\(\mathbf{ch}_{0}\)), offspring 1 - (\(\mathbf{ch}_{1}\)) and offspring 2 - (\(\mathbf{ch}_{2}\))) are selected. See equation <a href="#eq4">(4)</a>.
</p>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[min(of_{ch_{0}}, of_{ch_{1}}, of_{ch_{2}}) \; \Rightarrow \; \symbf{x}^{t+1} = best(\symbf{ch}_0, \symbf{ch}_1, \symbf{ch}_2)\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq4">(4)</p></td>
    </tr>
</table>

<h5><u>Blend crossover (BLX- \(\alpha\))</u> <a href="#ref7">[7]</a></h5>

<p aling = "justify">
From the two parent points \(\symbf{p_1}\) and \(\symbf{p_2}\) one new point are generated <a href="#ref8">[8]</a>. See equations <a href="#eq5">[5]</a> to <a href="#eq7">[7]</a>. \(k\) is the kth component of the design variable vector \(\symbf{ch}\) and \(\alpha\) be a uniformly distributed random number such that \(\alpha \in \left[0, 1 \right]\).
</p>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[ ch_{0,k} = min( p_{1,k}^{t}, p_{2,k}^{t} ) - \alpha \cdot d_{k}^{t}\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq5">(5)</p></td>
    </tr>
    <tr>
        <td style="width: 90%;">\[ ch_{1,k} = max( p_{1,k}^{t}, p_{2,k}^{t} ) + \alpha \cdot d_{k}^{t}\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq6">(6)</p></td>
    </tr>
    <tr>
        <td style="width: 90%;">\[ d_{k}^{t} = \left| p_{1,k}^{t} - p_{2,k}^{t} \right| \]</td>
        <td style="width: 10%;"><p align = "right" id = "eq7">(7)</p></td>
    </tr>
</table>

<p aling = "justify">
The best one of the two points (offspring 0 - (\(\mathbf{ch}_{0}\)) and offspring 1 - (\(\mathbf{ch}_{1}\))) are selected. See equation <a href="#eq8">(8)</a>.
</p>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[min(of_{ch_{0}}, of_{ch_{1}}) \; \Rightarrow \; \symbf{x}^{t+1} = best(\symbf{ch}_0, \symbf{ch}_1)\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq8">(8)</p></td>
    </tr>
</table>

<h4><i>Mutation</i></h4>

<p align = "justify">
Mutation specifies how a Genetic Algorithm makes small random changes in the individuals in the population to create mutated children. Mutation provides genetic diversity and enables Genetic Algorithm to search a broader space. See one mutation example in <a href="https://wmpjrufg.github.io/METAPY/LEARN_PROB_HILL.html" target="_blank">HC algorithm</a> theory. All formats of the mutation procedure are present in the <a href="https://wmpjrufg.github.io/METAPY/FRA_GA_GA.html" target="_blank">GA framework</a>.
</p>

<h5><u>Hill Climbing mutation</u></h5>

<p aling = "justify">
    See one mutation example in <a href="https://wmpjrufg.github.io/METAPY/LEARN_PROB_HILL.html" target="_blank">HC algorithm</a> theory.
</p>

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
            <td><p align = "left"><a href="https://doi.org/10.1007/s11042-020-10139-6" target="_blank" rel="noopener noreferrer">Katoch, S., Chauhan, S.S. & Kumar, V  (2021). A review on genetic algorithm: past, present, and future. Multimed Tools Appl 80, 8091–8126.</a></p></td>
        </tr>
        <tr>
            <td><p align = "center" id = "ref2">[2]</p></td>
            <td><p align = "left"><a href="https://mitpress.mit.edu/9780262581110/adaptation-in-natural-and-artificial-systems/" target="_blank" rel="noopener noreferrer">John H. Holland (1992). Adaptation in Natural and Artificial Systems
An Introductory Analysis with Applications to Biology, Control, and Artificial Intelligence. The MIT Press.</a></p></td>
        </tr>
        <tr>
            <td><p align = "center" id = "ref3">[3]</p></td>
            <td><p align = "left"><a href="https://doi.org/10.1016/j.energy.2020.117064" target="_blank" rel="noopener noreferrer">Masoumi, A.P.; Tavakolpour-Saleh, A.R. (2020). Experimental assessment of damping and heat transfer coefficients in an active free piston Stirling engine using genetic algorithm. Energy.</a></p></td>
        </tr>
        <tr>
            <td><p align = "center" id = "ref4">[4]</p></td>
            <td><p align = "left"><a href="https://doi.org/10.1016/j.engappai.2010.01.005" target="_blank" rel="noopener noreferrer">Ali Reza Tavakolpour; Intan Z. Mat Darus; Osman Tokhi; Musa Mailah (2010). Genetic algorithm-based identification of transfer function parameters for a rectangular flexible plate system. , 23(8), 1388–1397.</a></p></td>
        </tr>
        <tr>
            <td><p align = "center" id = "ref5">[5]</p></td>
            <td><p align = "left"><a href="https://doi.org/10.1016/j.istruc.2020.09.066" target="_blank" rel="noopener noreferrer">Alhaddad, Wael; Halabi, Yahia; Meree, Hani; Yu, Zhixiang (2020). Optimum design method for simplified model of outrigger and ladder systems in tall buildings using genetic algorithm. Structures, 28(), 2467–2487.</a></p></td>
        </tr>
        <tr>
            <td><p align = "center" id = "ref6">[6]</p></td>
            <td><p align = "left"><a href="https://doi.org/10.1016/B978-0-08-050684-5.50016-1" target="_blank" rel="noopener noreferrer">Wright, Alden H. (1991). Genetic Algorithms for Real Parameter Optimization. Foundations of Genetic Algorithms, Volume 1, 1991, Pages 205-218.</a></p></td>
        </tr>
        <tr>
            <td><p align = "center" id = "ref7">[7]</p></td>
            <td><p align = "left"><a href="https://doi.org/10.1016/B978-0-08-094832-4.50018-0" target="_blank" rel="noopener noreferrer">Eshelman, L. J., & Schaffer, J. D. (1993). Real-Coded Genetic Algorithms and Interval-Schemata. Foundations of Genetic Algorithms, 187–202.</a></p></td>
        </tr>
        <tr>
            <td><p align = "center" id = "ref8">[8]</p></td>
            <td><p align = "left"><a href="https://ieeexplore.ieee.org/document/934452" target="_blank" rel="noopener noreferrer">Takahashi, M.; Kita, H. (2001). IEEE 2001 Congress on Evolutionary Computation - Seoul, South Korea (27-30 May 2001). Proceedings of the 2001 Congress on Evolutionary Computation (IEEE Cat. No.01TH8546) - A crossover operator using independent component analysis for real-coded genetic algorithms. , 1, 643–649.</a></p></td>
        </tr>
    </tbody>
</table>
