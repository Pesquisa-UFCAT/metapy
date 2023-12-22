---
layout: default
title: hill_climbing_01
grand_parent: Framework
parent: Algorithms
has_toc: false
nav_order: 1
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h2>Theory</h2>

<p align = "justify">
Hill Climbing was one of the first existing stochastic optimization algorithms in the literature. The Hill Climbing method is also known as a local search method [1].
<br><br>
The iterative procedure is based on continuously improving the solution until the best solution is attained. The process consists of generating random neighbors of the current solution, according to the equation (1), where \(\symbf{N}\) indicates a Gaussian distribution where the mean \(\symbf{x}^{t}\) is the current solution and \(\sigma\) is the standard deviation input by the user. \(k\) is the kth component of the design variable vector \(\symbf{x}\).
</p>

<table style = "width:100%">
    <tr>
        <td>\[\symbf{x}_{k}^{t+1} = \symbf{N}(\symbf{x}_{k}^{t}, \sigma)\]</td>
        <td><p align = "justify">random neighbour</p></td>
        <td><p align = "right">(1)</p></td>
    </tr>
</table>

<h3><i>Algorithm</i></h3>

```python
1:  Input initial parameters (SIGMA)
2:  X = Initial solution
3:  Calculate OF and FIT
4:  for T in range(N_ITER):
5:      X_TEMP = neighbor solution equation (1)
6:      if f(X_TEMP) <= f(X):
7:         X(T+1) = X_TEMP
```
<h3><i>References</i></h3>
<p align = "justify">
    [1]	Al-Betar MA. β -Hill climbing: an exploratory local search. Neural Comput & Applic 2017;28:153–68. https://doi.org/10.1007/s00521-016-2328-2.
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
        <td>'PERCENTAGE STD (SIGMA)' = Standard deviation the normal distribution in percentage (\(\sigma\))</td>
        <td>Float</td>
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
from META_TOOLBOX import HILL_CLIMBING_001 # or from META_TOOLBOX import *

# Input
PARAMETERS = {'PERCENTAGE STD (SIGMA)': 10.0} # equal 10%

SETUP = {
        'N_REP': 10,
        'N_ITER': 100,
        'N_POP': 1,
        'D': 3,
        'X_L': [-2, -2, -2],
        'X_U': [2, 2, 2],
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
RESULTS_REP, BEST_REP, AVERAGE_REP, WORST_REP, STATUS_PROCEDURE = HILL_CLIMBING_001(OF_FUNCTION, SETUP)
```
```console
Output:
Progress: |██████████████████████████████████████████████████| 100.0% Complete
Process Time: 3.02 Seconds 
 Seconds per repetition: 0.30
META_HC001_REP_0_BEST_0_20221027 211711.xlsx
META_HC001_REP_1_BEST_1_20221027 211711.xlsx
META_HC001_REP_2_BEST_2_20221027 211712.xlsx
META_HC001_REP_3_BEST_3_20221027 211712.xlsx
META_HC001_REP_4_BEST_4_20221027 211712.xlsx
META_HC001_REP_5_BEST_5_20221027 211712.xlsx
META_HC001_REP_6_BEST_6_20221027 211712.xlsx
META_HC001_REP_7_BEST_7_20221027 211712.xlsx
META_HC001_REP_8_BEST_8_20221027 211712.xlsx
META_HC001_REP_9_BEST_9_20221027 211713.xlsx
META_HC001_RESUME_20221027 211713.xlsx
```

<!--
<p align = "justify">
This section describes the documentation of the file functions <code>META_HC_LIBRARY.py</code>.
</p>


<h2>Dependences</h2>

<ul>
    <li><a href="https://numpy.org/install/" target="_blank">Numpy</a></li>
</ul>

<h2><b><code>HC_MOVEMENT</code></b></h2>
<p align = "justify">
This function creates a new solution using Hill Climbing movement.
</p>

<h4>Input variables</h4>

<table style = "width:100%">
    <tr>
        <td>OF_FUNCTION</td>
        <td>External def user input this function in arguments</td>
        <td>Py function</td>
    </tr>
    <tr>
        <td>NULL_DIC</td>
        <td>Empty variable for the user to use in the obj. function</td>
        <td>Py dictionary</td>
    </tr>
    <tr>
        <td>X_IOLD</td>
        <td>Design variable I particle before movement</td>
        <td>Py list[D]</td>
    </tr>
    <tr>
        <td>X_L</td>
        <td>Lower limit design variables</td>
        <td>Py list[D]</td>
    </tr>
    <tr>
        <td>X_U</td>
        <td>Upper limit design variables</td>
        <td>Py list[D]</td>
    </tr>
    <tr>
        <td>D</td>
        <td>Problem dimension</td>
        <td>Integer</td>
    </tr>  
    <tr>
        <td>SIGMA</td>
        <td>Standard deviation in percentage</td>
        <td>Float</td>
    </tr>
</table>

<h4>Output variables</h4>

<table style = "width:100%">
    <tr>
        <td>X_INEW</td>
        <td>Design variable I particle after movement</td>
        <td>Py list[D]</td>
    </tr>
    <tr>
        <td>OF_INEW</td>
        <td>Objective function X_INEW (new particle)</td>
        <td>Float</td>
    </tr>
    <tr>
        <td>FIT_INEW</td>
        <td>Fitness X_INEW (new particle)</td>
        <td>Float</td>
    </tr>
    <tr>
        <td>NEOF</td>
        <td>Number of objective function evaluations</td>
        <td>Integer</td>
    </tr>
</table>

#### Example 01

```python 
from META_TOOLBOX import HC_MOVEMENT

# Input
X_L = [1, 2, 3]
X_U = [5, 5, 5]
D = 3
N_POP = 5
X_IOLD = [1, 2, 3]
NULL_DIC = None
SIGMA = 20 / 100  # 20%

# OF statement
def OF_FUNCTION(X, NULL_DIC):
    X_0 = X[0]
    X_1 = X[1]
    X_2 = X[2]
    OF = X_0 ** 2 + X_1 ** 2 + X_2 ** 2
    return OF

# Call function
X_INEW, OF_INEW, FIT_INEW, NEOF = HC_MOVEMENT(OF_FUNCTION, NULL_DIC, X_IOLD, X_L, X_U, D, SIGMA)
print(X_INEW, '\n', OF_INEW, '\n', FIT_INEW, '\n', NEOF)
```

```console
Output:
[1.44464707 2.         3.55896412] 
    18.753230789868464 
    0.05062462999788902 
    1
```
-->
