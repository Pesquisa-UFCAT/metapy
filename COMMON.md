---
title: Common Library
layout: home
parent: Framework
nav_order: 1
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

INITIAL_POPULATION_01
{: .label .label-green }

<p align = "justify">
    The function generates a random population with defined limits. Continuum variables generator.
</p>

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
        <td><code>N_POP</code></td>
        <td>Number of population</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>D</code></td>
        <td>Problem dimension</td>
        <td>Integer</td>
    </tr>  
    <tr>
        <td><code>X_L</code></td>
        <td>Lower limit design variables</td>
        <td>Py list [D]</td>
    </tr>  
    <tr>
        <td><code>X_U</code></td>
        <td>Upper limit design variables</td>
        <td>Py list [D]</td>
    </tr>    
    <tr>
        <td><code>SEED</code></td>
        <td>Control the seed for random numbers. It is used when you want to test the algorithm. Default <code>SEED = None</code>.</td>
        <td>Null or Integer</td>
    </tr>
</table>

Output variables
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
        <td><code>X_NEW</code></td>
        <td>All design variables</td>
        <td>Py list [N_POP] \( \times\) [D] </td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>INITIAL_POPULATION_01</code> function to generate a new population (five agents) considering the limits \(\mathbf{x}_L = \left[1,\;1,\;2\right]\) and \(\mathbf{x}_U = \left[4,\;4,\;4\right]\). 
    </i>
</p>

```python
# Data
nPop = 5
xL = [1, 1, 2]
xU = [4, 4, 4]
d = len(xU) # or d = len(xL) or d = 3

# Call function
population = INITIAL_POPULATION_01(nPop, d, xL, xU)

# Output details
print('particle 0: ', population[0])
print('particle 1: ', population[1])
print('particle 2: ', population[2])
print('particle 3: ', population[3])
print('particle 4: ', population[4])
```

```bash
particle 0:  [1.206696599676488, 3.6333795997730505, 2.7582027384444903]
particle 1:  [3.855855075161193, 2.387614157515121, 3.8073442405085656]
particle 2:  [1.7440060596179356, 3.4575301813292656, 3.384486502730728]
particle 3:  [2.487564137048481, 1.901279961962405, 2.146462080650636]
particle 4:  [2.8747948841114437, 3.253980082218285, 3.7593344650584686]
```

INITIAL_POPULATION_02
{: .label .label-green }

<p align = "justify">
    The function generates a random population. Combinatorial variables generator.
</p>

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
        <td><code>N_POP</code></td>
        <td>Number of population</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>D</code></td>
        <td>Problem dimension</td>
        <td>Integer</td>
    </tr>  
    <tr>
        <td><code>SEED</code></td>
        <td>Control the seed for random numbers. It is used when you want to test the algorithm. Default <code>SEED = None</code>.</td>
        <td>Null or Integer</td>
    </tr>
</table>

Output variables
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
        <td><code>X_NEW</code></td>
        <td>All design variables</td>
        <td>Py list [N_POP] \( \times\) [D] </td>
    </tr>
</table>

Example 2
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>INITIAL_POPULATION_02</code> function to generate a new population (five agents) considering the three dimensional combinatorial problem. 
    </i>
</p>

```python
# Data
nPop = 5
d = 3

# Call function
population = INITIAL_POPULATION_02(nPop, d)

# Output details
print('particle 0: ', population[0])
print('particle 1: ', population[1])
print('particle 2: ', population[2])
print('particle 3: ', population[3])
print('particle 4: ', population[4])
```

```bash
particle 0:  [0, 1, 2]
particle 1:  [0, 1, 2]
particle 2:  [0, 2, 1]
particle 3:  [0, 2, 1]
particle 4:  [1, 2, 0]
```

INITIAL_POPS
{: .label .label-green }

<p align = "justify">
    This function randomly initializes a population of procedures for a given number of repetitions.
</p>

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
        <td><code>N_REP</code></td>
        <td>Number of repetitions to initialize the population</td>
        <td>int</td>
    </tr>
    <tr>
        <td><code>N_POP</code></td>
        <td>Number of procedures in the population to be generated</td>
        <td>int</td>
    </tr>
    <tr>
        <td><code>D</code></td>
        <td>Size of the procedures in the population</td>
        <td>int</td>
    </tr>
    <tr>
        <td><code>X_L</code></td>
        <td>Lower limit for generating procedures in the case of 'REAL CODE'</td>
        <td>Py list [D]</td>
    </tr>
    <tr>
        <td><code>X_U</code></td>
        <td>Upper limit for generating procedures in the case of 'REAL CODE'</td>
        <td>Py list [D]</td>
    </tr>
    <tr>
        <td><code>TYPE_POP</code></td>
        <td>Type of code for the population (<code>'REAL CODE'</code> or <code>'COMBINATORIAL CODE'</code>). This parameter determines which population generation method will be used.</td>
        <td>String</td>
    </tr>

</table>

Output variables
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
        <td><code>POPS</code></td>
        <td>A list of populations of procedures, where each element in the list corresponds to a population of procedures.</td>
        <td>Py list [N_REP] \( \times\) [N_POP][D] </td>
    </tr>
</table>

Example 3
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>INITIAL_POPS</code> function to randomly initialize the population required for four repetitions of the optimization procedure, where each solution set has two agents, and each has three dimensions. Generation values ​​are between \(\mathbf{x}_L = \left[1,\;1,\;1\right]\) and \(\mathbf{x}_U = \left[3,\;3,\;3\right]\) 
    </i>
</p>

```python
# Data
setup = {
        'N_REP': 4,
        'N_POP': 2,
        'D': 3,
        'X_L': [1, 1, 1],
        'X_U': [3, 3, 3],
        'TYPE CODE': 'REAL CODE'
        }

# Call function
pops = INITIAL_POPS(setup['N_REP'], setup['N_POP'], setup['D'], setup['X_L'], setup['X_U'], setup['TYPE CODE'])

# Output details
print('population repetition ID = 0: ', pops[0])
print('population repetition ID = 1: ', pops[1])
print('population repetition ID = 2: ', pops[2])
print('population repetition ID = 3: ', pops[2])
print('\n Agent exemple:')
print('0 agent in population ID = 0: ', pops[0][0])
print('1 agent in population ID = 0: ', pops[0][1])
```

```bash
population repetition ID = 0:  [[2.862111952616406, 2.284517466837009, 2.0741217318333103], [1.6803996532703893, 1.6194312605496488, 2.7652733838433456]]
population repetition ID = 1:  [[2.408822694414611, 2.866968888723667, 1.9916222406959379], [2.8254541701093085, 2.4653213471948545, 2.7369968725507032]]
population repetition ID = 2:  [[2.8540657471191926, 2.642642845575371, 1.3530324239432858], [2.1787854602802144, 1.4197496397657159, 2.299558574899631]]
population repetition ID = 3:  [[2.8540657471191926, 2.642642845575371, 1.3530324239432858], [2.1787854602802144, 1.4197496397657159, 2.299558574899631]]

 Agent exemple:
0 agent in population ID = 0:  [2.862111952616406, 2.284517466837009, 2.0741217318333103]
1 agent in population ID = 0:  [1.6803996532703893, 1.6194312605496488, 2.7652733838433456]
```

FIT_VALUE
{: .label .label-green }

<p align = "justify">
    This function calculates the fitness of the fitness of the \(i\) agent.
</p>

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
        <td><code>OF_I_VALUE</code></td>
        <td>Object function value of the \(i\) agent</td>
        <td>float</td>
    </tr>
   
</table>

Output variables
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
        <td><code>FIT_I_VALUE</code></td>
        <td>Fitness value of the \(i\) agent</td>
        <td>float</td>
    </tr>
</table>

Theory
{: .label .label-red }
<p align = "justify">
        The fitness function, in simple terms, is a function that takes a potential solution to a problem as input and produces an output indicating how "fit" or how "good" the solution is concerning the specific problem under consideration. Equation <a href="#eq1">(1)</a> presents the fitness function implemented in the METApy framework.
</p>

<table border = "0" style = "width: 100%;">
  <tr>
    <td align = "left" style = "width: 95%;">\[\begin{cases} fit_i = \frac{1}{1+of_i} & \: \text{if} \: of_i \leq 0 \\ fit_i = 1+\lvert of_{i}\rvert & \: \text{if} \: of_i > 0 \end{cases}\]</td>
    <td align = "right" style = "width: 5%;"><p id = "eq1">(1)</p></td>
  </tr>
</table>


Example 4
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>FIT_VALUE</code> function to generate the fitness of the \(i\) agent. 
    </i>
</p>

```python
# Data
nPop = 3
ofI = 1

# Call function
fitI = FIT_VALUE(ofI)

# Output details
print(f'fit value i agent when OF = {ofI} is ', fitI)
```

```bash
fit value i agent when OF = 1 is  0.5
```

CHECK_INTERVAL_01
{: .label .label-green }

<p align = "justify">
    This function checks if a design variable is out of the limits established \(\mathbf{x}_L\) and \(\mathbf{x}_U\).
</p>

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
        <td><code>X_I_OLD</code></td>
        <td>The design variables that will be checked.</td>
        <td>Py list [D]</td>
    </tr>
    <tr>
        <td><code>X_L</code></td>
        <td>X Lower or lower limit</td>
        <td>Py list [D]</td>
    </tr>
    <tr>
        <td><code>X_U</code></td>
        <td>X Upper or Upper limit</td>
        <td>Py list [D]</td>
    </tr>
</table>

Output variables
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
        <td><code>X_I_NEW</code></td>
        <td>The new design variable values, that are inside the limit defined by lower and upper.</td>
        <td>Py list [D]</td>
    </tr>
</table>

Example 5
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>CHECK_INTERVAL_01</code> function to generate a new list with the values inside the range \(\mathbf{x}_L = [1, 2, 3]\) and \(\mathbf{x}_L = [5, 5, 5]\). Consider current solution \(\mathbf{x}_i = [6, -1, 2.5]\)
    </i>
</p>

```python
xL = [1, 2, 3]
xU = [5, 5, 5]
xI = [6, -1, 2.5]

xINew = CHECK_INTERVAL_01(xI, xL, xU)
print(xINew)
```

```bash
update solution:  [5.0, 2.0, 3.0]

```

MUTATION_01_MOVEMENT
{: .label .label-green }

<p align = "justify">This function mutates a solution using a Gaussian distribution.</p>

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
        <td><code>OF_FUNCTION</code></td>
        <td>Objective function to be optimized.</td>
        <td>Py function (<code>def</code>)</td>
    </tr>
    <tr>
        <td><code>NULL_DIC</code></td>
        <td>Dictionary of parameters, can be None</td>
        <td>Py dict</td>
    </tr>
    <tr>
        <td><code>X_IOLD</code></td>
        <td>List containing the values of the previous solution</td>
        <td>Py list</td>
    </tr>
    <tr>
        <td><code>X_L</code></td>
        <td>List containing the lower limits for each decision variable</td>
        <td>Py list</td>
    </tr>
    <tr>
        <td><code>X_U</code></td>
        <td>List containing the upper limits for each decision variable</td>
        <td>Py list</td>
    </tr>
    <tr>
        <td><code>D</code></td>
        <td>Dimension of the problem (number of variables)</td>
        <td>int</td>
    </tr>
    <tr>
        <td><code>SIGMA</code></td>
        <td>Control parameter for the Gaussian distribution</td>
        <td>float</td>
    </tr>
    <tr>
        <td><code>SEED</code></td>
        <td>Optional. Seed for generating random numbers</td>
        <td>int</td>
    </tr>
</table>

Output variables
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
        <td><code>X_INEW</code></td>
        <td>New solution generated by the mutation, containing the values of the decision variables after applying the Gaussian distribution and checking the limits</td>
        <td>Py list</td>
    </tr>
    <tr>
        <td><code>OF_INEW</code></td>
        <td>Value of the objective function associated with the new solution <code>X_INEW</code></td>
        <td>float</td>
    </tr>
    <tr>
        <td><code>FIT_INEW</code></td>
        <td>Fitness value associated with the new solution after applying an adjustment function to the objective function value</td>
        <td>float</td>
    </tr>
    <tr>
        <td><code>NEOF</code></td>
        <td>New solution indicator. It is a Boolean value (1 to indicate a new solution)</td>
        <td>int</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
    Use the <code>MUTATION_01_MOVEMENT</code> function to generate a new mutated solution from an existing solution, applying a 15 percent Gaussian distribution to mutate the decision variables within the specified limits, and then evaluate this new solution using a supplied objective function.  
  </i>
</p>

```python
from META_CO_LIBRARY import *

# Set variables
X_L = [1, 1, 1]
X_U = [3, 3, 3]
D = len(X_L)
NULL_DIC = None
SIGMA = 15 / 100 # 15%
SETUP_RANDOM_SEED = 10

# Objective function
def OF_FUNCTION(X, NULL_DIC):
    X_0 = X[0]
    X_1 = X[1]
    X_2 = X[2]
    OF = X_0 ** 2 + X_1 ** 2 + X_2 ** 2
    return OF

# Output
X_I = [2, 2, 2]
X_II, OF_INEW, FIT_INEW, NEOF = MUTATION_01_MOVEMENT(OF_FUNCTION, NULL_DIC, X_I, X_L, X_U, D, SIGMA, SEED = SETUP_RANDOM_SEED)

print('X_II',X_II, '\n')
print('OF_INEW',OF_INEW, '\n')
print('FIT_INEW', FIT_INEW, '\n')
print('NEOF',NEOF, '\n')
```

```bash
X_II [2.3994759512388555, 2.2145836923195215, 1.5363799123666195]

OF_INEW 13.022329005984838

FIT_INEW 0.07131482933920551

NEOF 1
```

BEST_VALUES
{: .label .label-green }

<p align = "justify"></p>

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
        <td><code>X</code></td>
        <td>It represents the population of particles, where each line is a particle and its characteristics</td>
        <td>Py list</td>
    </tr>
    <tr>
        <td><code>OF</code></td>
        <td>Objective function values for each particle in the population</td>
        <td>Py list</td>
    </tr>  
    <tr>
        <td><code>FIT</code></td>
        <td>Fitness values for each particle in the population</td>
        <td>Py list</td>
    </tr>  
    <tr>
        <td><code>N_POP</code></td>
        <td>Population size</td>
        <td>int</td>
    </tr>

</table>

Output variables
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
        <td><code>BEST_POSITION</code></td>
        <td>Index of the best particle in the population</td>
        <td>int</td>
    </tr>
    <tr>
        <td><code>WORST_POSITION</code></td>
        <td>Index of the worst particle in the population</td>
        <td>int</td>
    </tr>
    <tr>
        <td><code>X_BEST</code></td>
        <td>Representing the characteristics of the best particle</td>
        <td>Py list</td>
    </tr>
    <tr>
        <td><code>X_WORST</code></td>
        <td>Representing the characteristics of the worst particle</td>
        <td>Py list</td>
    </tr>
    <tr>
        <td><code>OF_BEST</code></td>
        <td>Objective function value of the best particle</td>
        <td>float</td>
    </tr>
    <tr>
        <td><code>OF_WORST</code></td>
        <td>Objective function value of the worst particle</td>
        <td>float</td>
    </tr>
    <tr>
        <td><code>FIT_BEST</code></td>
        <td>Fitness value of the best particle</td>
        <td>float</td>
    </tr>
    <tr>
        <td><code>FIT_WORST</code></td>
        <td>Fitness value of the worst particle</td>
        <td>float</td>
    </tr>
    <tr>
        <td><code>OF_AVERAGE</code></td>
        <td>Average value of the objective functions in the population</td>
        <td>float</td>
    </tr>
    <tr>
        <td><code>FIT_AVERAGE</code></td>
        <td>Average fitness value in the population.</td>
        <td>float</td>
    </tr>

</table>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
     
  </i>
</p>

```python

```

```bash

```
