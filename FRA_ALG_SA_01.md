---
layout: default
title: simulated_annealing_01
grand_parent: Framework
parent: Metaheuristics
has_toc: false
nav_order: 2
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

```python
df_all, df_best, delta_time, report = simulated_annealing_01(settings)
```

<p align = "justify">
    Simulated Annealing 01 algorithm.
</p>

{: .warning }
> This function does not perform more than one repetition. To perform multiple repetitions, use the `metaheuristic_optmizer` function.

Input variables
{: .label .label-yellow }

<table style = "width:100%">
    <thead>
      <tr>
        <th>Name</th>
        <th>Description</th>
        <th>Type</th>
      </tr>
    </thead>
    <tr>
        <td><code>settings</code></td>
        <td>Algorithm settings: <code>[0]</code> setup (dict), <code>[1]</code> initial population (list), <code>[2]</code> seeds (int)</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>setup</code> keys</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><code>'number of population'</code></td>
        <td>number of population</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>'number of iterations'</code></td>
        <td>number of iterations</td>
        <td>Integer</td>
    </tr> 
    <tr>
        <td><code>'number of dimensions'</code></td>
        <td>Problem dimension</td>
        <td>Integer</td>
    </tr> 
    <tr>
        <td><code>'x pop lower limit'</code></td>
        <td>Lower limit of the design variables</td>
        <td>List</td>
    </tr>  
    <tr>
        <td><code>'x upper lower limit'</code></td>
        <td>Upper limit of the design variables</td>
        <td>List</td>
    </tr>  
    <tr>
        <td><code>'none variable'</code></td>
        <td>None variable. Default is <code>None</code>. Use in objective function</td>
        <td>Object or None</td>
    </tr>  
    <tr>
        <td><code>'objective function'</code></td>
        <td>Objective function. The Metapy user defined this function</td>
        <td>Function (<code>def</code>)</td>
    </tr>  
    <tr>
        <td><code>'algorithm parameters'</code></td>
        <td>Algorithm parameters</td>
        <td>Dictionary</td>
    </tr>   
    <tr>
        <td><code>'algorithm parameters'</code> keys</td>
        <td></td>
        <td></td>
    </tr> 
    <tr>
        <td><code>'sigma'</code></td>
        <td>Control parameter for the Gaussian or Uniform distribution in percentage. In Gaussian or Uniform distribution, 
 \(\sigma\) equivalent to a standard deviation</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>'pdf'</code></td>
        <td>Probability density function. Options: <code>'gaussian'</code> or <code>'uniform'</code></td>
        <td>String</td>
    </tr>
    <tr>
        <td><code>'temperature'</code></td>
        <td>Initial temperature. Default is <code>'None'</code>. <code>'None'</code>: Automatic starts cooling temperature. See theory bellow</td>
        <td>Float or None</td>
    </tr>
    <tr>
        <td><code>'schedule'</code></td>
        <td>Cooling schema</td>
        <td>String</td>
    </tr>
    <tr>
        <td><code>'alpha'</code></td>
        <td>Cooling control</td>
        <td>Float</td>
    </tr>
</table>

Output variables
{: .label .label-yellow }

<table style = "width:100%">
    <tr>
        <td><code>df_all</code></td>
        <td>All data of the population</td>
        <td>Dataframe</td>
    </tr>
    <tr>
        <td><code>df_best</code></td>
        <td>Best data of the population</td>
        <td>Dataframe</td>
    </tr>  
    <tr>
        <td><code>delta_time</code></td>
        <td>Time of the algorithm execution in seconds</td>
        <td>Float</td>
    </tr>  
    <tr>
        <td><code>report</code></td>
        <td>Report of the algorithm execution</td>
        <td>String</td>
    </tr>  
</table>

Theory
{: .label .label-red }

<p align = "justify">
The Simulated Annealing method was introduced by Kirkpatrick et al. <a href="#ref1">[1,2]</a> in 1983. This algorithm is inspired by the annealing process of metals during the manufacturing process. The Simulated Annealing model is based on the generation of random neighbors from a starting point, similar to what occurs in the Hill Climbing Algorithm (see <a href="https://wmpjrufg.github.io/METAPY/FRA_ALG_HILL_01.html" target="_blank">HC algorithm</a>).
<br><br>
In the Simulated Annealing algorithm, the acceptance of the new solution (see new solution procedure in see <a href="https://wmpjrufg.github.io/METAPY/FRA_ALG_HILL_01.html" target="_blank">HC algorithm</a>) is given by a criterion that compares the energy of the system given by equation (1). In this algorithm, the values of \(E_{i}\) are relative to the value of the objective function to \(i\) particle, i.e., \(E_{i}=OF_{i}\).
</p>

<table style = "width:100%">
    <tr>
        <td>\[\Delta E = E_{cur}-E_{new}\]</td>
        <td><p align = "right">(1)</p></td>
    </tr>
</table>

<p align = "justify">
The value \(E_{new}\) is the value of the objective function for the newly generated neighbor and \(E_{cur}\) is the value of the objective function for the current particle. 
<br><br>
The solution will be accepted if \(E_{cur} > E_{new}\) (\(P(\Delta E)=1.00\)). For solutions of type \(E_{cur} < E_{new}\) the acceptance will follow a certain probability given by equation (2) where \(T\) the annealing temperature.
</p>

<table style = "width:100%">
    <tr>
        <td>\[P(\Delta E) = e^{\frac{-\Delta E}{T}}\]</td>
        <td><p align = "right">(2)</p></td>
    </tr>
</table>

Algorithm
{: .label .label-red }

```python
1:  Input initial parameters (T_0, SIGMA)
2:  X = Initial solution
3:  Calculate OF and FIT
4:  for I in range(N_ITER):
5:      X_TEMP = new neighbor solution
6:      DELTA_E = equation(1)
7:      if DELTA_E > 0:
8:         PROB = 1
9:      else:
10:        PROB = equation(2)
11:     R = random number [0,1]
12:     if PROB > R:
13:        X(I+1) = X_NEW # Accept new solution
14:     else:
15:        X(I+1) = X(I)  # Ignore new solution
16:     Update temperature     
```

<p align = "justify">
At the end of the algorithm, the temperature is updated. \(\alpha\) is the cooling temperature adjustment factor. The methods for updating the temperature are:

<ul>
  <li>Geometric: See equation (3);</li>
  <li>Lundy: See equation (4);</li>
  <li>Linear: See equation (5);</li>
  <li>Logarithmic: See equation (6);</li>
</ul>
</p>

<table style = "width:100%">
    <tr>
        <td>\[T_{i+1} = T_{i}.\alpha\]</td>
        <td><code>'GEOMETRIC'</code></td>
        <td><p align = "right">(3)</p></td>
    </tr>
    <tr>
        <td>\[T_{i+1} = \frac{T_{i}}{1+\alpha.T}\]</td>
        <td><code>'LUNDY'</code></td>
        <td><p align = "right">(4)</p></td>
    </tr>
    <tr>
        <td>\[T_{i+1} = T_{i} - \alpha\]</td>
        <td><code>'LINEAR'</code></td>
        <td><p align = "right">(5)</p></td>
    </tr>
    <tr>
        <td>\[T_{i+1} = \frac{T_{i}}{\ln(i+\alpha)}\]</td>
        <td><code>'LOGARITHMIC'</code></td>
        <td><p align = "right">(6)</p></td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
      Use the hill climbing optimization method to optimize the sphere function. Use a total of 100 iterations to perform the optimization. Consider the limits \(\mathbf{x}_L = [-5.0, -5.0]\) and \(\mathbf{x}_U = [5.0, 5.0]\) for the problem design variables.
  </i>
</p>

```python
# Import Library
from metapy_toolbox import simulated_annealing_01

# Optmization problem
def my_function(x, none_variable):
    return x[0]**2 + x[1]**2

# Algorithm setup
setup = {   
            'number of iterations': 100,
            'number of population': 5,
            'number of dimensions': 2,
            'x pop lower limit': [-5, -5],
            'x pop upper limit': [5, 5],
            'none variable': None,
            'objective function': my_function_test,
            'algorithm parameters': {'sigma': 20,
                                     'pdf': 'gaussian',
                                     'temperature': 100,
                                     'schedule': 'geometric',
                                     'alpha': 0.9}
        }

init_pop = [[-0.744296104431692, 1.2756394501594848],
                [3.584499004856184, -3.3267189715496515]]

seed = None

# Call function
settings = [setup, init_pop, seed]
df_all_results, df_resume, time_cost, report = simulated_annealing_01(settings)
```

<p align = "justify">
    Download <a href="https://wmpjrufg.github.io/METAPY/FRA_ALG_HILL_01.html" target="_blank">notebook</a>.
</p>

Reference list
{: .label .label-yellow }

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
            <td><p align = "left"><a href="https://doi.org/10.1126/science.220.4598.671" target="_blank" rel="noopener noreferrer">S. Kirkpatrick, C.D. Gelatt, M.P. Vecchi, Optimization by Simulated Annealing, Science. 220 (1983) 671–680.</a></p></td>
        </tr>
        <tr>
            <td><p align = "center" id = "ref1">[2]</p></td>
            <td><p align = "left"><a href="https://doi.org/10.1063/1.1699114" target="_blank" rel="noopener noreferrer">N. Metropolis, A.W. Rosenbluth, M.N. Rosenbluth, A.H. Teller, Equation of State Calculations by Fast Computing Machines, (n.d.) 7.</a></p></td>
        </tr>
    </tbody>
</table>
