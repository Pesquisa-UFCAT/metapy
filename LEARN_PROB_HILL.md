---
layout: default
title: Hill Climbing
parent: Probabilistic
grand_parent: Learning
nav_order: 1
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
Hill Climbing was one of the literature's first existing probabilistic optimization algorithms. The Hill Climbing method is also known as a local search method <a href="#ref1">[1]</a>.
<br><br>
The iterative procedure continuously improves the solution until the best solution is attained. The process consists of generating random neighbors of the current solution \left(\symbf{x}_i\right\), according to equation <a href="#eq1">(1)</a>, where \(\symbf{N}\) indicates a Gaussian or Uniform distribution where the mean \(\symbf{x}^{t}\) is the current solution and \(cov\) is the coefficient of variation input by the user. \(k\) is the \(k\)th component of the design variable vector \(\symbf{x}\) and \(t\) is a current iteration.
</p>

<table border = "0" style = "width:100%">
    <tr>
        <td style="width: 90%;">\[x_{i,k}^{t+1} \sim \symbf{N}(x_{i,k}^{t}, \sigma)\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq1">(1)</p></td>
    </tr>
    <tr>
        <td style="width: 90%;">\[\sigma = x_{i,k}^{t} \cdot \frac{cov}{100}\]</td>
        <td style="width: 10%;"><p align = "right" id = "eq2">(2)</p></td>
    </tr>
</table>

<p align = "justify">
A small value of \(\sigma\) gives a higher probability for creating ‘near-parent’ solutions and a large value of \(\sigma\) allows distant solutions.
</p>

<h3>Algorithm</h3>

```python
1:  Input initial parameters (cov, n_population, x_lower, x_upper, obj_function, n_dimensions)
2:  Input initial guess (x_pop)
3:  Calculate of and fit (initial population)
4:  for iter in range(n_iterations):
5:      x_temp = equation (1)
6:      if fit(x_temp) > fit(x_pop):
7:         x_pop(iter+1) = x_temp
8:      else:
9:         x_pop(iter+1) = x_pop(iter)
```

{: .note }
> The Hill Climbing algorithm saves a new solution when a new candidate improves the current best solution.

<p align = "justify">
See <a href="https://wmpjrufg.github.io/METAPY/FRA_SA_HILL.html" target="_blank">HC algorithm</a> in METApy Framework.
</p>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
      Use the Hill Climbing optimization method to optimize the 2D sphere function. Use a total of 2 iterations to perform the optimization. Consider the limits \(\mathbf{x}_L = [-5.0, -5.0]\) and \(\mathbf{x}_U = [5.0, 5.0]\) for the problem design variables. Consider the initial guess (two agents) \(\mathbf{pop}_0 = [-0.74, 1.25]\) and \(\mathbf{pop}_1 = [3.58, -3.33]\). Use \(cov = 20%\) and Gaussian random generator.
  </i>
</p>


<h3>Solution - (Report)</h3>
<ul>
  <li>\( \mathbf{x}_0 = (-0.74, 1.25) \), \( \text{of}_{\text{pop}} = 2.1101 \)</li>
  <li>\( \mathbf{x}_1 = (3.58, -3.33) \), \( \text{of}_{\text{pop}} = 23.9053 \)</li>
</ul>

<br>

<!-- 
ITERACAO 1 - X0 EM MOVIMENTO
-->

<h4><strong>ITERATION: 1</strong></h4>
<p> 
   <strong> Particle Movement - \( \mathbf{x}_0 \)  </strong><br><br>
    <strong> Current \( \mathbf{x}_0 \) </strong> = [-0.74, 1.25]

<ul>
  <li><strong>  Dimension 0: </strong></li>
      <ul>
          <li>Mean = -0.74</li> 
          <li>Sigma = 0.14800000000000002</li>
          <li>Neighbor = -0.9023477757469192</li>
      </ul>    
  <li><strong>  Dimension 1: </strong></li>
      <ul>
          <li>Mean = 1.25</li> 
          <li>Sigma =  0.25</li>
          <li>Neighbor = 1.2619927898303909</li>
      </ul>    
</ul>

<!-- 
ITERACAO 1 - UPDATE X0
-->
<strong> Update \( \mathbf{x}_0 \) </strong>
    <ul>
        <li>\( \mathbf{x}_0 \)  = [-0.9023477757469192, 1.2619927898303909] </li>
        <li>\( \text{of}_{\text{pop}}\) = 2.4068573099793054 </li>
        <li>\( \text{fit}\) = 0.29352564813055654</li>
    </ul>
</p>


<br>

<!-- 
ITERACAO 1 - X1 EM MOVIMENTO
-->
<p> 
   <strong> Particle Movement - \( \mathbf{x}_1 \)  </strong><br><br>
    <strong> Current \( \mathbf{x}_1 \) </strong> = [3.58, -3.33]

<ul>
  <li><strong>  Dimension 0: </strong></li>
      <ul>
          <li>Mean = 3.58</li> 
          <li>Sigma = 0.716</li>
          <li>Neighbor = 3.6241680241318215</li>
      </ul>    
  <li><strong>  Dimension 1: </strong></li>
      <ul>
          <li>Mean = -3.33</li> 
          <li>Sigma =  0.6659999999999999</li>
          <li>Neighbor = -3.2320736729816724</li>
      </ul>    
</ul>


<!--
ITERACAO 1 - UPDATE X1
-->
<strong> Update \( \mathbf{x}_1 \) </strong>
    <ul>
        <li>\( \mathbf{x}_1 \)  = [3.6241680241318215, -3.2320736729816724] </li>
        <li>\( \text{of}_{\text{pop}}\) = 23.58089409472079 </li>
        <li>\( \text{fit}\) = 0.040682002702854034</li> <br>
    </ul>


<!--
ITERACAO 1 - UPDATE SOLUTION
-->
<strong> Update Solution </strong>
    <ul>
        <li> \( \mathbf{x}_0 \) = [-0.74, 1,.25] ,  \( \text{of}_{\text{pop}}\) = 2.1101 - <strong>Best Solution</strong></li>
        <li> \( \mathbf{x}_1 \) = [3.6241680241318215, -3.2320736729816724] ,  \( \text{of}_{\text{pop}}\) = 23.58089409472079  </li>
    </ul>
<br>
</p>
<!-- 
FIM ITERACAO 1
-->

<!--
ITERACAO 2 - X0 EM MOVIMENTO
-->

<h4><strong>ITERATION: 2</strong></h4>
<p> 
   <strong> Particle Movement - \( \mathbf{x}_0 \)  </strong><br><br>
    <strong> Current \( \mathbf{x}_0 \) </strong> = [-0.74, 1.25]

<ul>
  <li><strong>  Dimension 0: </strong></li>
      <ul>
          <li>Mean = -0.74</li> 
          <li>Sigma = 0.14800000000000002</li>
          <li>Neighbor = -0.6839602767380419</li>
      </ul>    
  <li><strong>  Dimension 1: </strong></li>
      <ul>
          <li>Mean = 1.25</li> 
          <li>Sigma =  0.25</li>
          <li>Neighbor = 0.9611420858210487</li>
      </ul>    
</ul>

<!-- 
ITERACAO 2 - UPDATE X0
-->
<strong> Update \( \mathbf{x}_0 \) </strong>
    <ul>
        <li>\( \mathbf{x}_0 \)  = [-0.6839602767380419, 0.9611420858210487] </li>
        <li>\( \text{of}_{\text{pop}}\) = 1.391595769292015 </li>
        <li>\( \text{fit}\) = 0.41813086176182296 </li>
    </ul>
</p>


<br>

<!--
ITERACAO 2 - X1 EM MOVIMENTO
-->
<p> 
   <strong> Particle Movement - \( \mathbf{x}_1 \)  </strong><br><br>
    <strong> Current \( \mathbf{x}_1 \) </strong> = [3.6241680241318215, -3.2320736729816724]

<ul>
  <li><strong>  Dimension 0: </strong></li>
      <ul>
          <li>Mean = 3.6241680241318215</li> 
          <li>Sigma = 0.7248336048263643</li>
          <li>Neighbor = 2.9304941843959953</li>
      </ul>    
  <li><strong>  Dimension 1: </strong></li>
      <ul>
          <li>Mean = -3.2320736729816724</li> 
          <li>Sigma =  0.6464147345963345</li>
          <li>Neighbor = -3.1041458794450945</li>
      </ul>    
</ul>


<!-- 
ITERACAO 2 - UPDATE X1
-->
<strong> Update \( \mathbf{x}_1 \) </strong>
    <ul>
        <li>\( \mathbf{x}_1 \)  = [2.9304941843959953, -3.1041458794450945] </li>
        <li>\( \text{of}_{\text{pop}}\) = 18.22351780565471</li>
        <li>\( \text{fit}\) = 0.05201961524991249</li> <br>
    </ul>


<!--
ITERACAO 2 - UPDATE SOLUTION
-->
<strong> Update Solution </strong>
    <ul>
        <li> \( \mathbf{x}_0 \) = [-0.6839602767380419, 0.9611420858210487] ,  \( \text{of}_{\text{pop}}\) = 1.391595769292015 - <strong>Best Solution</strong></li>
        <li> \( \mathbf{x}_1 \) = [2.9304941843959953, -3.1041458794450945] ,  \( \text{of}_{\text{pop}}\) = 18.22351780565471  </li>
    </ul>
<br>
</p>
<!-- 
FIM ITERACAO 2
-->

<h2>Guia de Cálculo Manual - Hill Climbing</h2>

<h3>População Inicial</h3>
<p>A solução inicial é definida a partir do vetor de design fornecido. A seguir, apresentamos a população inicial com o respectivo valor da função objetivo (\( \text{of} \)):</p>
<ul>
    <li>\( \mathbf{x}_0 = [88.25395326699595], \ \text{of}_{\text{pop}} = -7.5079 \) - <strong>melhor solução inicial</strong></li>
</ul>

<h3>Exploração da Vizinhança</h3>

<p>O algoritmo Hill Climbing explora a vizinhança da solução atual para gerar um novo candidato. Este processo é realizado utilizando uma distribuição normal \( \text{N}(\mu, \sigma) \), onde:</p>

<ul>
    <li>\( \mu \) é o valor atual da variável (\( \mathbf{x}_i^t \)).</li>
    <li>\( \sigma \) é definido por \( \sigma = \mu \cdot \frac{cov}{100} \), conforme a equação (2).</li>
</ul>

<p> Os cálculos detalhados para a geração do novo candidato são apresentados abaixo:</p>

<h5>Cálculo de \( \sigma \):</h5>


<p>\( \sigma = 88.25395326699595 \cdot \frac{20}{100} = 17.65079065339919 \)</p>

<h5>Amostragem da nova solução (\( \mathbf{x}_i^{t+1} \)):</h5>
<p>\( \mathbf{x}_i^{t+1} \sim \text{N}(88.25395326699595, 17.65079065339919) \)</p>
<p>Valor gerado: \( \mathbf{x}' = [145.67723926735943] \)</p>

<hr>

<h3>Avaliação da Nova Solução</h3>

<p>A nova solução gerada, \( \mathbf{x}' = [145.67723926735943] \), é avaliada com base na função objetivo (\( \text{of} \)). Calculamos também o fitness para comparar a qualidade das soluções:</p>
<table>
    <tr>
        <th>Parâmetro</th>
        <th>Valor</th>
    </tr>
    <tr>
        <td>Função objetivo para a solução mutada (\( \mathbf{x}' \))</td>
        <td>\( \text{of}_{\text{mutado}} = -6.3297 \)</td>
    </tr>
    <tr>
        <td>Fitness para a solução mutada</td>
        <td>\( \text{fit}_{\text{mutado}} = 6.3297 \)</td>
    </tr>
    <tr>
        <td>Fitness para a solução atual (\( \mathbf{x}_i^t \))</td>
        <td>\( \text{fit}_{\text{atual}} = 7.5079 \)</td>
    </tr>
</table>

<hr>

<h3>Atualização da Solução</h3>
<p>O algoritmo Hill Climbing aceita apenas soluções que melhoram o fitness da solução atual. Neste caso:</p>
<ul>
    <li>\( \text{fit}_{\text{mutado}} = 6.3297 \) é <strong>menor</strong> que \( \text{fit}_{\text{atual}} = 7.5079 \).</li>
    <li>Portanto, a solução mutada \( \mathbf{x}' \) <strong>não é aceita</strong>, e a solução atual permanece inalterada.</li>
</ul>

<hr>

<h3>Atualização Após a Iteração</h3>
<p>Após a conclusão da primeira iteração, a melhor solução permanece como:</p>
<ul>
    <li>\( \mathbf{x}_0 = [88.25395326699595], \ \text{of}_{\text{pop}} = -7.5079 \)</li>
</ul>

<hr>


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
            <td><p align = "left"><a href="https://doi.org/10.1007/s00521-016-2328-2" target="_blank" rel="noopener noreferrer">Al-Betar, Mohammed Azmi (2016). β-Hill climbing: an exploratory local search. Neural Computing and Applications.</a></p></td>
        </tr>
    </tbody>
</table>
