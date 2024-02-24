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

<p aling = "justify">
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
From the two parent points \(p_1\) and \(p_2\) three new points are generated.
</p>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[ ch_{1,k} = 0.50 \cdot p_{1,k}^{t} + 0.50 \cdot p_{2,k}^{t}\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq1">(1)</p></td>
    </tr>
    <tr>
        <td style="width: 90%;">\[ ch_{2,k} = 1.50 \cdot p_{1,k}^{t} - 0.50 \cdot p_{2,k}^{t}\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq2">(2)</p></td>
    </tr>
    <tr>
        <td style="width: 90%;">\[ ch_{3,k} = -0.50 \cdot p_{1,k}^{t} + 1.50 \cdot p_{2,k}^{t}\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq3">(3)</p></td>
    </tr>
</table>

<p aling = "justify">
The best one of the three points (offspring 0 \(\mathbf{ch}_{0}\), offspring 1 \(\mathbf{ch}_{1}\) and offspring 2 \(\mathbf{ch}_{2}\)) are selected. See equation <a href="#eq4">(4)</a>. \(k\) is the kth component of the design variable vector \(\symbf{ch}\).
</p>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[ min(of_{ch_{0}}, of_{ch_{1}}, of_{ch_{2}}) \]</td>
        <td style="width: 10%;"><p align = "right" id = "eq4">(1)</p></td>
    </tr>
</table>

<h5><u>Blend crossover (BLX-\(\alpha\))</u> <a href="#ref7">[7]</a></h5>

<p aling = "justify">
From the two parent points \(p_1\) and \(p_2\) one new point are generated <a href="#ref8">[8]</a>.
</p>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[ ch_{1,k}^{t+1} = min \letf( p_{1,k}^{t}, p_{2,k}^{t}\right) - \alpha \cdot d_{k}^{t}\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq5">(5)</p></td>
    </tr>
    <tr>
        <td style="width: 90%;">\[ ch_{2,k}^{t+1} = max \letf( p_{1,k}^{t}, p_{2,k}^{t}\right) + \alpha \cdot d_{k}^{t}\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq6">(6)</p></td>
    </tr>
    <tr>
        <td style="width: 90%;">\[ d_{k}^{t} = \left| p_{1,k}^{t} - p_{2,k}^{t} \right| \]</td>
        <td style="width: 10%;"><p align = "right" id = "eq7">(7)</p></td>
    </tr>
</table>

<p aling = "justify">
The best one of the two points (offspring 0 \(\mathbf{ch}_{0}\) and offspring 1 \(\mathbf{ch}_{1}\)) are selected. See equation <a href="#eq8">(8)</a>. \(k\) is the kth component of the design variable vector \(\symbf{ch}\) and Let \(\alpha\) be a uniformly distributed random number such that \(r \in \left[0, 1 \right]\).
</p>

<table style = "width:100%">
    <tr>
        <td style="width: 90%;">\[ min(of_{ch_{0}}, of_{ch_{1}}) \]</td>
        <td style="width: 10%;"><p align = "right" id = "eq8">(8)</p></td>
    </tr>
</table>

<h4><i>Mutation</i></h4>

<p align = "justify">
Mutation specifies how a Genetic Algorithm makes small random changes in the individuals in the population to create mutated children. Mutation provides genetic diversity and enables Genetic Algorithm to search a broader space. See one mutation example in <a href="https://wmpjrufg.github.io/METAPY/LEARN_PROB_HILL.html" target="_blank">HC algorithm</a> theory. All formats of the mutation procedure are present in the <a href="https://wmpjrufg.github.io/METAPY/LEARN_PROB_HILL.html" target="_blank">GA framework</a>.
</p>

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
See <a href="https://wmpjrufg.github.io/METAPY/FRA_ALG_SA_01.html" target="_blank">GA algorithm</a> in METApy Framework.
</p>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
      Use the Genetic algorithm optimization method to optimize the 2D sphere function. Use a total of 2 iterations to perform the optimization. Consider the limits \(\mathbf{x}_L = [-5.0, -5.0]\) and \(\mathbf{x}_U = [5.0, 5.0]\) for the problem design variables. Consider the initial guess (two agents) \(\mathbf{pop}_0 = [-0.74, 1.25]\) and \(\mathbf{pop}_1 = [3.58, -3.33]\). Use \(cov = 20%\), Gaussian random generator, \(T_0 = 15\) and geometric schedule (\(\alpha = 0.90\)).
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
            <td><p align = "left"><a href="10.1109/CEC.2001.934452" target="_blank" rel="noopener noreferrer">Takahashi, M.; Kita, H. (2001). IEEE 2001 Congress on Evolutionary Computation - Seoul, South Korea (27-30 May 2001). Proceedings of the 2001 Congress on Evolutionary Computation (IEEE Cat. No.01TH8546) - A crossover operator using independent component analysis for real-coded genetic algorithms. , 1, 643–649.</a></p></td>
        </tr>
    </tbody>
</table>
