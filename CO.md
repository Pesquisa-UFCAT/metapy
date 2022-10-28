<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h1>COMMON LIBRARY</h1>

<p align = "justify">
This section describes the documentation of the file functions <code>META_CO_LIBRARY.py</code>.
</p>

<h2>Dependences</h2>

<ul>
    <li>numpy</li>
    <li>pandas</li>
</ul>

<h2><b><code>INITIAL_POPULATION_01</code></b></h2>
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
</table>

<h4>Output variables</h4>

<table style = "width:100%">
    <tr>
        <td>X_NEW</td>
        <td>New design variables</td>
        <td>Py Numpy array[N_POP x D]</td>
    </tr>
</table>

#### Example 01

```python 
from META_TOOLBOX import INITIAL_POPULATION_01

# Input
X_L = [1, 2, 3]
X_U = [5, 5, 5]
D = 3
N_POP = 5

# Call function
X = INITIAL_POPULATION_01(N_POP, D, X_L, X_U)
X

Output: 
array([[1.81080776, 4.60365055, 3.87531294],
        [4.12197605, 3.53183507, 3.05786934],
        [3.93710947, 2.64617967, 4.74376385],
        [3.02342665, 2.34148094, 4.60085533],
        [4.63074404, 4.50925082, 4.50872698]])
```

<h2><b><code>CHECK_INTERVAL_01</code></b></h2>
<p align = "justify">
This function checks if a design variable is out of the limits established \(\symbf{x_l}\) and \(\symbf{x_u}\).
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

# Input
X_L = [1, 2, 3]
X_U = [5, 5, 5]
X_IOLD = [6, -1, 2.5] 
D = 3

# Call function
X_INEW = CHECK_INTERVAL_01(X_IOLD, X_L, X_U)
X_INEW

Output: 
array([5., 2., 3.])
```

#### Example 02

```python 
from META_TOOLBOX import CHECK_INTERVAL_01

# Input
X_L = [1, 2, 3]
X_U = [5, 5, 5]
X_OLD = np.array([[6, -1, 2.5],[1, 1, 1],[-2, 2.5, -2]]) 
X_TEM = X_OLD.copy()
D = 3
N_POP = 3

# Call function using for looping
for I in range(N_POP):
    X_TEM[I, :] = CHECK_INTERVAL_01(X_TEM[I, :], X_L, X_U)
X_TEM

Output: 
array([[5. , 2. , 3. ],
        [1. , 2. , 3. ],
        [1. , 2.5, 3. ]])
```

<h2><b><code>FIT_VALUE</code></b></h2>
<p align = "justify">
This function calculates the fitness of a value of the objective function.
</p>

<h4>Input variables</h4>

<table style = "width:100%">
    <tr>
        <td>OF_VALUEI</td>
        <td>Objective function I particle value</td>
        <td>Float</td>
    </tr>
</table>

<h4>Output variables</h4>

<table style = "width:100%">
    <tr>
        <td>FIT_VALUEI</td>
        <td>Fitness I particle value</td>
        <td>Float</td>
    </tr>
</table>

#### Example 01

```python 
from META_TOOLBOX import FIT_VALUE

# Input
N_POP = 3
FIT = np.zeros((N_POP, 1))
OF = np.array([[1], [2], [-3]])

# Call function
for I in range(N_POP):
    FIT[I, 0] = FIT_VALUE(OF[I, 0])
FIT

Output: 
array([[0.5       ],
        [0.33333333],
        [4.        ]])
```

<h2><b><code>BEST_VALUE</code></b></h2>
<p align = "justify">
This function determines the best and worst particle. It also determines the average value (OF and FIT) of the population.
</p>

<h4>Input variables</h4>

<table style = "width:100%">
    <tr>
        <td>X</td>
        <td>Design variables</td>
        <td>Py Numpy array[N_POP x D]</td>
    </tr>
    <tr>
        <td>OF</td>
        <td>All objective function values</td>
        <td>Py Numpy array[N_POP x 1]</td>
    </tr>
    <tr>
        <td>FIT</td>
        <td>All fitness values</td>
        <td>Py Numpy array[N_POP x 1]</td>
    </tr>
    <tr>
        <td>N_POP</td>
        <td>Number of population</td>
        <td>Integer</td>
    </tr>
</table>

<h4>Output variables</h4>

<table style = "width:100%">
    <tr>
        <td>BEST_POSITION</td>
        <td>ID best position</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td>WORST_POSITION</td>
        <td>ID worst position</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td>X_BEST</td>
        <td>Design variables best particle</td>
        <td>Py list[D]</td>
    </tr>
    <tr>
        <td>X_WORST</td>
        <td>Design variables worst particle</td>
        <td>Py list[D]</td>
    </tr>
    <tr>
        <td>OF_BEST</td>
        <td>Objective function best particle value</td>
        <td>Float</td>
    </tr>
    <tr>
        <td>OF_WORST</td>
        <td>Objective function worst particle value</td>
        <td>Float</td>
    </tr>
    <tr>
        <td>FIT_BEST</td>
        <td>Fitness best particle value</td>
        <td>Float</td>
    </tr>
    <tr>
        <td>FIT_WORST</td>
        <td>Fitness worst particle value</td>
        <td>Float</td>
    </tr>
    <tr>
        <td>OF_AVERAGE</td>
        <td>Average Objective function value</td>
        <td>Float</td>
    </tr>
    <tr>
        <td>FIT_AVERAGE</td>
        <td>Average Fitness value</td>
        <td>Float</td>
    </tr>
</table>

#### Example 01

```python 
from META_TOOLBOX import BEST_VALUES, FIT_VALUE

# Input
N_POP = 3
X = np.array([[0.895705592, 0.00602558, 0.968560594],
              [0.089570559, 0.00602558, 0.968560594],
              [0.848445242, 0.00540733, 0.090126453]])
NULL_DIC = None
OF = np.zeros((N_POP, 1))
FIT = np.zeros((N_POP, 1))

# OF statement
def OF_FUNCTION(X, NULL_DIC):
    X_0 = X[0]
    X_1 = X[1]
    X_2 = X[2]
    OF = X_0 ** 2 + X_1 ** 2 + X_2 ** 2
    return OF

# Evaluating Fitness and OF
for I in range(N_POP):
    POP = X[I, :]
    OF[I, 0] = OF_FUNCTION(POP, NULL_DIC)
    FIT[I, 0] = FIT_VALUE(OF[I, 0])

# Call function
BEST_ID, WORST_ID, X_BEST, X_WORST, OF_BEST, OF_WORST, FIT_BEST, FIT_WORST, OF_AVERAGE, FIT_AVERAGE = BEST_VALUES(X, OF, FIT, N_POP)

# Fit 
FIT 

Output: 
array([[0.36490565],
       [0.51383004],
       [0.5786999 ]])

# OF
OF

Output:
array([[1.74043444],
       [0.94616882],
       [0.72801135]])

# best ID
BEST_ID

Output:
2

# Best design variables
X_BEST

Output:
array([0.84844524, 0.00540733, 0.09012645])

# OF Best design variables
OF_BEST

Output:
0.7280113454205287
```