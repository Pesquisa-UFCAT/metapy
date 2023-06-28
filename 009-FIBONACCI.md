<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h1>FIBONACCI</h1>

<h2>Theory</h2>

<p align = "justify">
The Fibonacci method is a classical unconstrained optimization method for determining the minimum value of unidimensional functions. This specific method does not use derivatives in the iterative process. The search for the function's minimum point is given within a user-specified interval \(\left[x_{lower}, x_{upper}\right]\). We emphasize that the optimal point of the function (\(x^*\)) is contained within the reference interval \(\left[x_{lower}, x_{upper}\right]\).
<br><br>
The Fibonacci method originates from the Fibonacci sequence, which was discovered by the Italian mathematician Leonardo Fibonacci. He used a logical sequence of numbers to describe the population growth of rabbits in 1202.
<br><br>
The rule of the Fibonacci sequence is that the values \(F_{1} = 1\), and \(F_{2} = 1\), and the subsequent numbers follow the recursive equation.
</p>

$$
F_{n} = F_{n-1} + F_{n-2}
\tag{1}
$$

<p align = "justify">
    Thus the Fibonacci numbers are \(1, 1, 2, 3, 5, 8, 13, 21, 34, ...\).
    <br><br>
    The Fibonacci method differs from the golden ratio method in that the ratio for the reduction of intervals is not constant. The closed-form expression of \(n^{th}\) Fibonacci number is thus given by:
</p>

$$
F_{n} = \frac{1}{\sqrt{5}}.\left [ \left ( \frac{1+\sqrt{5}}{2} \right )^n-\left ( \frac{1-\sqrt{5}}{2} \right )^n\right]
\tag{2}
$$

<p align = "justify">
    This method is an elimination technique or interval reduction method. For any iteration $i$ the new interval of uncertainty \([u,v]\) \((u, v \in \left[x_{lower}, x_{upper}\right])\) is defined according to the equations (3) and (4):
</p>

$$
u_i = x_{upper} - L_i
\tag{3}
$$

$$
v_i = x_{lower} + L_i
\tag{4}
$$

$$
L_i = \frac{F_{n-i-1}}{F_{n-i}}.\left(x_{upper} - x_{lower} \right)
\tag{5}
$$

<p align = "justify">
    if \(\theta\left(u\right) \leq \theta\left(v\right)\) the minimum value is contained in the interval \(\left[x_{lower}, v\right]\). if \(\theta\left(u\right) > \theta\left(v\right)\) the minimum value is contained in the interval \(\left[u, x_{upper}\right]\). Where \(\theta\left(\cdot\right)\) indicates the value of the objective function.
</p>

<h3><i>Algorithm</i></h3>

```python
1: # Initialize X_L, X_U, N_ITER, THETA(X)
2: for I in range(N_ITER):
3:     U_I = EQ(3); V_I = EQ(4)
4:     THETA_U = THETA(U_I); THETA_V = THETA(V_I)
5:     if THETA_U <= THETA_V:
6:        X_L = X_L; X_U = V_I
7:     elif THETA_U > THETA_V:
8:        X_L = U_I; X_U = X_U    
```
<h2>Example</h2>

<p align = "justify">
    Determine the minimum point of the function \(f(x) = x^5 - 5.x^3 - 20.x + 5\) with Fibonacci search method, if the first uncertainty interval is \(\left[x_{lower}, x_{upper}\right] = [-2.5, 2.5]\).  
</p>

<p align = "justify"></p>
Using \(n_{inter} = 25\) iterations  
</p>

<b>1. Iteration \(i = 0\):</b>

$$  
n-i-1 = 25 - 0 - 1 = 24
$$   
$$   
n-i = 25 - 0 = 25
$$   
$$  
F_{24} = \frac{1}{\sqrt{5}}.\left [ \left ( \frac{1+\sqrt{5}}{2} \right )^24-\left ( \frac{1-\sqrt{5}}{2} \right )^24\right] = 46368
$$  
$$  
F_{25} = \frac{1}{\sqrt{5}}.\left [ \left ( \frac{1+\sqrt{5}}{2} \right )^25-\left ( \frac{1-\sqrt{5}}{2} \right )^25\right] = 75025
$$  
$$  
L_1 = \frac{46368}{75025}.\left(2.5 - (-2.5)\right) = 3.0902
$$  
$$  
u_1 = 2.5 - 3.0902 = -0.5902
$$  
$$  
v_1 = -2.5 + 3.0902 = 0.5902
$$  
$$  
\theta(u_1) = (-0.5902)^5 - 5.(-0.5902)^3 - 20.(-0.5902) + 5 = 17.76
$$  
$$  
\theta(v_1) = (0.5902)^5 - 5.(0.5902)^3 - 20.(0.5902) + 5 = -7.76
$$  
$$  
\theta(u_1) > \theta(v_1) \therefore x_{lower} = u_1 = -0.5902, x_{upper} = x_{upper} = 2.50
$$  
$$  
\left[-2.5000, 2.5000\right] \to \left[-0.5902, 2.5000\right]
$$  
$$  
x^* = \frac{x_l + x_u}{2} = \frac{-0.5902 + 2.5}{2} = 0.95 \therefore \theta(x^*) = 0.95^5 - 5.0.95^3 - 20.0.95 + 5 = -17.51 
$$  

<b>2. Iteration \(i = 1\):</b>

$$
n-i-1 = 25 - 1 - 1 = 23
$$
$$
n-i = 25 - 1 = 24
$$
$$
F_{23} = \frac{1}{\sqrt{5}}.\left [ \left ( \frac{1+\sqrt{5}}{2} \right )^23-\left ( \frac{1-\sqrt{5}}{2} \right )^23\right] = 28567
$$
$$
F_{24} = \frac{1}{\sqrt{5}}.\left [ \left ( \frac{1+\sqrt{5}}{2} \right )^24-\left ( \frac{1-\sqrt{5}}{2} \right )^24\right] = 46368
$$
$$
L_1 = \frac{28657}{46368}.\left(2.5 - (-0.5902)\right) = 1.9098
$$
$$
u_1 = 2.5 - 1.9098 = 0.5902
$$
$$
v_1 = -0.5902 + 1.9098 = 1.3196
$$
$$
\theta(u_1) = (0.5902)^5 - 5.(0.5902)^3 - 20.(0.5902) + 5 = -7.76
$$
$$
\theta(v_1) = (1.3196)^5 - 5.(1.3196)^3 - 20.(1.3196) + 5 = -28.88
$$
$$
\theta(u_1) > \theta(v_1) \therefore x_{lower} = u_1 = 0.5902, x_{upper} = x_{upper} = 2.50
$$
$$
\left[-0.5902, 2.5000\right] \to \left[0.5902, 2.5000\right]
$$
$$
x^* = \frac{x_l + x_u}{2} = \frac{0.5902 + 2.50}{2} = 1.54 \therefore \theta(x^*) = 1.54^5 - 5.1.54^3 - 20.1.54 + 5 = -35.39 
$$

<b>3. Iteration \(i = 1\):</b>

$$
n-i-1 = 25 - 2 - 1 = 22
$$
$$
n-i = 25 - 2 = 23
$$
$$
F_{22} = \frac{1}{\sqrt{5}}.\left [ \left ( \frac{1+\sqrt{5}}{2} \right )^22-\left ( \frac{1-\sqrt{5}}{2} \right )^22\right] = 17711
$$
$$
F_{23} = \frac{1}{\sqrt{5}}.\left [ \left ( \frac{1+\sqrt{5}}{2} \right )^23-\left ( \frac{1-\sqrt{5}}{2} \right )^23\right] = 28657
$$
$$
L_1 = \frac{17711}{28657}.\left(2.5 - (0.5902)\right) = 1.1803
$$
$$
u_1 = 2.5 - 1.1803 = 1.3197
$$
$$
v_1 = 0.5902 + 1.1803 = 1.7705
$$
$$
\theta(u_1) = (1.3197)^5 - 5.(1.3197)^3 - 20.(1.3197) + 5 = -28.88
$$
$$
\theta(v_1) = (1.7705)^5 - 5.(1.7705)^3 - 20.(1.7705) + 5 = -40.76
$$
$$
\theta(u_1) > \theta(v_1) \therefore x_{lower} = u_1 = 1.3197, x_{upper} = x_{upper} = 2.50
$$
$$
\left[0.5902, 2.5000\right] \to \left[1.3197, 2.5000\right]
$$
$$
x^* = \frac{x_l + x_u}{2} = \frac{1.3197 + 2.50}{2} = 1.91 \therefore \theta(x^*) = 1.91^5 - 5.1.91^3 - 20.1.91 + 5 = -42.61
$$

<h3><i>References</i></h3>
<p align = "justify">
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
        <td><code>'N_ITER'</code> = Number of iterations</td>
        <td>Integer</td>
    </tr> 
    <tr>
        <td></td>
        <td><code>'X_L'</code> = Lower limit design variables</td>
        <td>Float</td>
    </tr> 
    <tr>
        <td></td>
        <td><code>'X_U'</code> = Upper limit design variables</td>
        <td>Float</td>
    </tr>
    <tr>
        <td></td>
        <td><code>'NULL_DIC'</code> = Empty variable for the user to use in the obj. function</td>
        <td>Py dictionary</td>
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
        <td><code>'X_POSITION'</code> = Design variables by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td><code>'OF'</code> = Obj function value by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td><code>'FIT'</code> = Fitness value by iteration</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td><code>'PARAMETERS'</code> = Algorithm parameters</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
    <tr>
        <td></td>
        <td><code>'NEOF'</code> = Number of objective function evaluations</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>
    <tr>
        <td></td>
        <td><code>'ID_PARTICLE'</code> = ID particle</td>
        <td>Py Numpy array[N_ITER + 1 x 1]</td>
    </tr>  
</table>

<h3><i>Notebook</i></h3>

<p align = "justify">See Jupyter notebook example:</p>

```python
# Library
from META_TOOLBOX import FIBONACCI_ALGORITHM

# Input
X_L = -2.5
X_U = 2.5

SETUP = {
        'N_ITER': 25,
        'X_L': X_L,
        'X_U': X_U,
        'NULL_DIC': None,
        }

# OF statement
def OF_FUNCTION(X, NULL_DIC):
    OF = X ** 5 - 5 * X ** 3 - 20 * X + 5
    return OF

# Call algorithm
BEST_REP = FIBONACCI_ALGORITHM(OF_FUNCTION, SETUP)
```
```console
Progress: |██████████████████████████████████████████████████| 100.0% Complete
Process Time: 0.01 Seconds 
 Seconds per repetition: 0.01
META_FIBONACCI_REP_0_BEST_0_20230628 171718.xlsx
META_FIBONACCI_RESUME_20230628 171718.xlsx
```
<p align = "justify">
Download <a href="https://github.com/wmpjrufg/METAPY/blob/gh-pages/009-FIBONACCI.ipynb" target="_blank">notebook</a>
</p>
