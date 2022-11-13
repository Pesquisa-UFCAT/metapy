<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h1>HILL CLIMBING</h1>

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