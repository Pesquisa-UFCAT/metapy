<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h1>Firefly Algorithm</h1>

<h2>Theory</h2>

<p align = "justify">
The Firefly Algorithm (FA) was introduced by Xin-Shen Yang [1] in 2008 based on the communication system of fireflies as a function of their bioluminescence [1]. For this purpose, Yang [1] simplified the procedure by defining the following assumptions: (a) Individuals are not distinguishable by gender, so they can interact by attractiveness (\(\beta\)); (b) Attractiveness is inversely proportional to Euclidean distance (\(r\)) and there is a permeability factor (\(\gamma\)) of luminosity in the medium, so as to reduce light intensity; (c) Luminosity is defined through the Objective Function (OF).
<br><br>
Therefore, each firefly behaves as a possible solution (of dimension \(k\)) to the problem within a previously defined search space. Thus, based on the factor’s attractiveness (\(\beta\)), permeability (\(\gamma\)), and randomness (\(\alpha\)), each new generation is defined based on equation (1):
</p>

<table style = "width:100%">
    <tr>
        <td>\[\symbf{x}^{t+1} = \symbf{x}^{t} + \symbf{\beta}.(\symbf{y}^{t} - \symbf{x}^{t}) + \alpha.(\symbf{rand} - 0.50)\]</td>
        <td><p align = "right">(1)</p></td>
    </tr>
</table>

<p align = "justify">
Where the attractiveness array (\(\beta\)), corresponding to the attractiveness of the firefly is understood as the degree of light perception that a particle \(i\) has of its peers (\(\symbf{y}\)), as a function of the Euclidean distance (\(\symbf{r}_{xy}\)) among individuals is provided by the equation (2), where \(\beta_0\) is the value for null distance. Therefore, a low value of \(\beta\), either due to a large distance or high light absorption by the medium (\(\gamma\)), will affect a model with a greater random character. \(\symbf{x}^{t}\) is the current solution and \(\symbf{y}^{t}\) is the current neighbor solution. 
</p>

<table style = "width:100%">
    <tr>
        <td>\[\beta = \frac{\beta_0}{1+\symbf{\gamma}.\symbf{r}_{xy}^2}\]</td>
        <td><p align = "right">(2)</p></td>
    </tr>
    <tr>
        <td>\[\symbf{\gamma} = \frac{1}{(\symbf{x}_{upper}-\symbf{x}_{lower})^2}\]</td>
        <td><p align = "right">(3)</p></td>
    </tr>
</table>

<p align = "justify">
Considering the random part of equation (1), the term \(\symbf{rand}\) is a array of random numbers between 0 and 1 [2]. Therefore, larger values of \(\alpha\) lead to expressive randomness in the generation of populations. Thus, Yang [1] proposes to use some function (see equation 4 and 5) that updates \(\alpha\) along the generations \(t\) in order to change the degree of randomness.
</p>

<table style = "width:100%">
    <tr>
        <td>\[\alpha^{t+1} = \alpha_{min} + (\alpha_{max} - \alpha_{min}).\theta^t\]</td>
        <td><p align = "right">(4)</p></td>
    </tr>
    <tr>
        <td>\[\alpha^{t+1} = \alpha_{max}.\theta^t\]</td>
        <td><p align = "right">(5)</p></td>
    </tr>
</table>

<h3><i>Algorithm</i></h3>

```python
1:  Input initial parameters (GAMMA, ALPHA_MAX, ALPHA_MIN, TETHA)
2:  X = Initial solution
3:  for T in range(N_ITER):
4:      Calculate OF and FIT      
5:      Sort population
6:      X(T+1) = update solution
7:      update ALPHA
```

<p align = "justify">
In standard Firefly, the attraction mechanism used is the full attraction model. See Figure 1.
</p>

<center><img src="/imgs/FAfig1.png" width="40%"></center>
<p align = "center">
<b>Figure 1.</b> The full attraction mechanism [3].</p>


<h3><i>References</i></h3>
<p align = "justify">
    [1]	X.-S. Yang, Nature-Inspired Metaheuristic Algorithms, Luniver Press, 2008.<br>
    [2] X.-S. Yang, Firefly Algorithm, Stochastic Test Functions and Design Optimisation, ArXiv:1003.1409 [Math]. (2010). http://arxiv.org/abs/1003.1409 (accessed September 5, 2019).<br>
    [3] W. Li, W. Li and Y. Huang, Enhancing Firefly Algorithm with Dual-Population Topology Coevolution, Mathematics 2022, 10, 1564. https://doi.org/10.3390/math10091564.

</p>

<h2>Framework</h2>

<h3><i>Algorithm functions</i></h3>

<h4>Input variables</h4>

<table style = "width:100%">
    <tr>
        <td>OF_FUNCTION</td>
        <td>External def user input this function in arguments</td>
        <td>Py function</td>
    </tr>
    <tr>
        <td>SETUP</td>
        <td>Algorithm setup</td>
        <td>Py dictionary</td>
    </tr>
    <tr>
        <td></td>
        <td>'N_REP' = Number of repetitions</td>
        <td>Integer</td>
    </tr>    
    <tr>
        <td></td>
        <td>'N_ITER' = Number of iterations</td>
        <td>Integer</td>
    </tr> 
    <tr>
        <td></td>
        <td>'N_POP' = Number of population</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td></td>
        <td>'D' = Problem dimension</td>
        <td>Integer</td>
    </tr>  
    <tr>
        <td></td>
        <td>'X_L' = Lower limit design variables</td>
        <td>Py list[D]</td>
    </tr> 
    <tr>
        <td></td>
        <td>'X_U' = Upper limit design variables</td>
        <td>Py list[D]</td>
    </tr>
    <tr>
        <td></td>
        <td>'NULL_DIC' = Empty variable for the user to use in the obj. function</td>
        <td>Py dictionary</td>
    </tr>
    <tr>
        <td></td>
        <td>'PARAMETERS' = Algorithm parameters</td>
        <td>Py dictionary</td>
    </tr>    
    <tr>
        <td>PARAMETERS</td>
        <td>Algorithm parameters</td>
        <td>Py dictionary</td>
    </tr> 
    <tr>
        <td></td>
        <td>'BETA_0' = attractiveness (\(\beta\))</td>
        <td>Float</td>
    </tr>
    <tr>
        <td></td>
        <td>'ALPHA_MIN' = minimal randomness (\(\beta\))</td>
        <td>Float</td>
    </tr>
    <tr>
        <td></td>
        <td>'ALPHA_MAX' = maximum randomness (\(\beta\))</td>
        <td>Float</td>
    </tr>
    <tr>
        <td></td>
        <td>'GAMMA' = light absorption (\(\gamma\)). See function <code>GAMMA_ASSEMBLY</code></td>
        <td>Py list[D]</td>
    </tr>
    <tr>
        <td></td>
        <td>'THETA' = randomness factor (\(\theta\))</td>
        <td>Float</td>
    </tr>
    <tr>
        <td></td>
        <td>'TYPE ALPHA UPDATE' = \(\alpha\) update see equation (4) 'YANG 0' and (5) 'YANG 1'</td>
        <td>String</td>
    </tr>
</table>

<h4>Output variables</h4>

<table style = "width:100%">
    <tr>
        <td>RESULTS_REP</td>
        <td>All results of population movement by repetition</td>
        <td>Py dictionary</td>
    </tr>
    <tr>
        <td></td>
        <td>'X_POSITION' = Design variables by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x D]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'OF' = Obj function value by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'FIT' = Fitness value by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'PARAMETERS' = Algorithm parameters</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'NEOF' = Number of objective function evaluations</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>
    <tr>
        <td></td>
        <td>'ID_PARTICLE' = ID particle</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td>BEST_REP</td>
        <td>Best population results by repetition</td>
        <td>Py dictionary</td>
    </tr>
    <tr>
        <td></td>
        <td>'X_POSITION' = Design variables by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x D]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'OF' = Obj function value by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'FIT' = Fitness value by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'PARAMETERS' = Algorithm parameters</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'NEOF' = Number of objective function evaluations</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>
    <tr>
        <td></td>
        <td>'ID_PARTICLE' = ID particle</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr> 
    <tr>
        <td>AVERAGE_REP</td>
        <td>Average OF and FIT results by repetition</td>
        <td>Py dictionary</td>
    </tr>
    <tr>
        <td></td>
        <td>'OF' = Obj function value by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'FIT' = Fitness value by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'NEOF' = Number of objective function evaluations</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>
    <tr>
        <td>WORST_REP</td>
        <td>Worst OF and FIT results by repetition</td>
        <td>Py dictionary</td>
    </tr>
    <tr>
        <td></td>
        <td>'X_POSITION' = Design variables by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x D]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'OF' = Obj function value by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'FIT' = Fitness value by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'PARAMETERS' = Algorithm parameters</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td>'NEOF' = Number of objective function evaluations</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>
    <tr>
        <td></td>
        <td>'ID_PARTICLE' = ID particle</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr> 
    <tr>
        <td>STATUS_PROCEDURE</td>
        <td>Process repetition ID - from lowest OF value to highest OF value</td>
        <td>Py list[N_REP]</td>
    </tr> 
</table>

<h3><i>Notebook</i></h3>

<p align = "justify">See Jupyter notebook example:</p>

```python
from META_TOOLBOX import FIREFLY_ALGORITHM_001 # or from META_TOOLBOX import *
from META_TOOLBOX import GAMMA_ASSEMBLY

# Input
X_L = [-2, -2, -2]
X_U = [2, 2, 2]
D = 3
GAMMA = GAMMA_ASSEMBLY(X_L, X_U, D, 2)

PARAMETERS = {
              'BETA_0': 0.98,
              'ALPHA_MIN': 0.20,
              'ALPHA_MAX': 0.95,
              'GAMMA': GAMMA,
              'THETA': 0.98,
              'TYPE ALPHA UPDATE': 'YANG 0'
             }

SETUP = {
        'N_REP': 10,
        'N_POP': 5,
        'N_ITER': 100,
        'X_L': X_L,
        'X_U': X_U,
        'D': D,
        'NULL_DIC': None,
        'PARAMETERS': PARAMETERS
        }

# OF statement
def OF_FUNCTION(X, NULL_DIC):
    X_0 = X[0]
    X_1 = X[1]
    X_2 = X[2]
    OF = X_0 ** 2 + X_1 ** 2 + X_2 ** 2
    return OF

# Call algorithm
RESULTS_REP, BEST_REP, AVERAGE_REP, WORST_REP, STATUS_PROCEDURE = FIREFLY_ALGORITHM_001(OF_FUNCTION, SETUP)
```
```console
Output:
Progress: |██████████████████████████████████████████████████| 100.0% Complete
Process Time: 0.80 Seconds 
 Seconds per repetition: 0.08
META_FA001_REP_0_BEST_0_20230210 214404.xlsx
META_FA001_REP_1_BEST_1_20230210 214404.xlsx
META_FA001_REP_2_BEST_2_20230210 214404.xlsx
META_FA001_REP_3_BEST_3_20230210 214404.xlsx
META_FA001_REP_4_BEST_4_20230210 214404.xlsx
META_FA001_REP_5_BEST_5_20230210 214404.xlsx
META_FA001_REP_6_BEST_6_20230210 214404.xlsx
META_FA001_REP_7_BEST_7_20230210 214404.xlsx
META_FA001_REP_8_BEST_8_20230210 214404.xlsx
META_FA001_REP_9_BEST_9_20230210 214404.xlsx
META_FA001_RESUME_20230210 214404.xlsx
```