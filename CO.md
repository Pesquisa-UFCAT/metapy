<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h1>COMMON LIBRARY</h1>

<p align = "justify">
This section describes the documentation of the file functions <code>META_CO_LIBRARY.py</code>.
</p>

<h2><code>INITIAL_POPULATION_01</code></h2>
<p align = "justify">
This function initializes the population randomically between the limits \(\symbf{x_l}\) and \(\symbf{x_u}\). Numerical values are continuous.
</p>

<h4>Input variables</h4>

<table style = "width:100%">
<tr>
<td>N_POP</td>
<td>Number of population</td>
<td>Integer</td>
</tr>
<tr>
<td>D</td>
<td>Problem dimension</td>
<td>Integer</td>
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
<td>X</td>
<td>Empty design variables</td>
<td>Py Numpy array[N_POP x D]</td>
</tr>
</table>

<h4>Output variables</h4>

<table style = "width:100%">
<tr>
<td>X</td>
<td>Initial design variables</td>
<td>Py Numpy array[N_POP x D]</td>
</tr>
</table>

#### Example 01

```python 
import numpy as np
from META_TOOLBOX import INITIAL_POPULATION_01

X_L = [1, 2, 3]
X_U = [5, 5, 5]
X = np.zeros((5, 3))
D = 3
N_POP = 5

X = INITIAL_POPULATION_01(N_POP, D, X, X_L, X_U)
X

Out: array([[1.81080776, 4.60365055, 3.87531294],
              [4.12197605, 3.53183507, 3.05786934],
              [3.93710947, 2.64617967, 4.74376385],
              [3.02342665, 2.34148094, 4.60085533],
              [4.63074404, 4.50925082, 4.50872698]])
```

<h2><code>CHECK_INTERVAL_01</code></h2>
<p align = "justify">
This function checks if a design variable is out of the limits established X_L and X_U.
</p>

<h4>Input variables</h4>

<table style = "width:100%">
<tr>
<td>X_IOLD</td>
<td>Design variable I particle before check</td>
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
</table>

<h4>Output variables</h4>

<table style = "width:100%">
<tr>
<td>X_INEW</td>
<td>Design variable I particle after check</td>
<td>Py list[D]</td>
</tr>
</table>

#### Example 01

```python 
from META_TOOLBOX import CHECK_INTERVAL_01

X_L = [1, 2, 3]
X_U = [5, 5, 5]
X_IOLD = [6, -1, 2.5] 
D = 3

X_INEW = CHECK_INTERVAL_01(X_IOLD, X_L, X_U)
X_INEW

Out: array([5., 2., 3.])
```

#### Example 02

```python 
from META_TOOLBOX import CHECK_INTERVAL_01

X_L = [1, 2, 3]
X_U = [5, 5, 5]
X_OLD = np.array([[6, -1, 2.5],[1, 1, 1],[-2, 2.5, -2]]) 
X_TEM = X_OLD.copy()
D = 3
N_POP = 3

for I in range(N_POP):
    X_TEM[I, :] = CHECK_INTERVAL_01(X_TEM[I, :], X_L, X_U)
X_TEM

Out: array([[5. , 2. , 3. ],
              [1. , 2. , 3. ],
              [1. , 2.5, 3. ]])
```