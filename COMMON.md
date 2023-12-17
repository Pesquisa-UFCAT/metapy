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
        <td>Control the seed for random numbers. It is used when you want to test the algorithm. Default <code>SEED = None</code></td>
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
        Use the <code>INITIAL_POPULATION_01</code> function to generate a new population (five agents) considering the limits \(\mathbf{x}_L = \left[1,\;1,\;2\right]\) and \(\mathbf{x}_U = \left[4,\;4,\;4\right]\) 
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
        <td>Control the seed for random numbers. It is used when you want to test the algorithm. Default <code>SEED = None</code></td>
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
        <td>Type of code for the population (<code>'REAL CODE'</code> or <code>'COMBINATORIAL CODE'</code>). This parameter determines which population generation method will be used</td>
        <td>String</td>
    </tr>
    <tr>
        <td><code>SEEDS</code></td>
        <td>Seed control. <code>SEEDS</code> = <code>None</code> represents: "without control". <code>SEEDS</code> = <code>[??, ??, ??] represents "seed control".</code></td>
        <td>None or Py List [N_REP]</td>
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
        <td>Py list [N_REP] \( \times\) [N_POP][D]</td>
    </tr>
</table>

Example 3
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>INITIAL_POPS</code> function to randomly initialize the population required for four repetitions of the optimization procedure, where each solution set has two agents, and each has three dimensions. Generation values ​​are between \(\mathbf{x}_L = \left[1,\;1,\;1\right]\) and \(\mathbf{x}_U = \left[3,\;3,\;3\right]\). Use "seed without control" in your setup.
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
        'TYPE CODE': 'REAL CODE',
        'SEED CONTROL': None
        }

# Call function
pops = INITIAL_POPS(setup['N_REP'], setup['N_POP'], setup['D'], setup['X_L'], setup['X_U'], setup['TYPE CODE'], setup['SEED CONTROL'])

# Output details
print('population repetition ID = 0: ', pops[0])
print('population repetition ID = 1: ', pops[1])
print('population repetition ID = 2: ', pops[2])
print('population repetition ID = 3: ', pops[3])
print('\n Agent example:')
print('init. population rep. ID = 0 - agent id = 0: ', pops[0][0])
print('init. population rep. ID = 0 - agent id = 1: ', pops[0][1])
```

```bash
population repetition ID = 0:  [[2.2196326014139323, 1.3840517317205192, 2.6116781074286313], [1.3403223273226081, 1.1674717842974527, 2.2436660854022747]]
population repetition ID = 1:  [[2.254591881105598, 1.1077574733049664, 1.9129032401629404], [2.5519888813800913, 2.1522163950561666, 2.54366540526461]]
population repetition ID = 2:  [[2.283743242030489, 2.284006259927572, 2.454720419092418], [1.5915597454398382, 1.0423599148278597, 1.8482867884497962]]
population repetition ID = 3:  [[1.8937748864434991, 1.5110123109265392, 2.8229927611822845], [2.7585766165646697, 2.8376271268544357, 2.127148509873788]]

 Agent example:
init. population rep. ID = 0 - agent id = 0:  [2.2196326014139323, 1.3840517317205192, 2.6116781074286313]
init. population rep. ID = 0 - agent id = 1:  [1.3403223273226081, 1.1674717842974527, 2.2436660854022747]
```
Example 4
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>INITIAL_POPS</code> function to randomly initialize the population required for four repetitions of the optimization procedure, where each solution set has two agents, and each has three dimensions. Generation values ​​are between \(\mathbf{x}_L = \left[1,\;1,\;1\right]\) and \(\mathbf{x}_U = \left[3,\;3,\;3\right]\). Use "seed control" in your setup. Suggest: \(\mathbf{seeds} = \left[10,\;11,\;10,\;11\right]\).
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
        'TYPE CODE': 'REAL CODE',
        'SEED CONTROL': [10, 11, 10, 11]
        }

# Call function
pops = INITIAL_POPS(setup['N_REP'], setup['N_POP'], setup['D'], setup['X_L'], setup['X_U'], setup['TYPE CODE'], setup['SEED CONTROL'])

# Output details
print('population repetition ID = 0: ', pops[0])
print('population repetition ID = 1: ', pops[1])
print('population repetition ID = 2: ', pops[2])
print('population repetition ID = 3: ', pops[3])
print('\n Agent example:')
print('init. population rep. ID = 0 - agent id = 0: ', pops[0][0])
print('init. population rep. ID = 0 - agent id = 1: ', pops[0][1])
```

```bash
population repetition ID = 0:  [[2.5426412865334918, 1.041503898718803, 2.2672964698525506], [2.4976077650772237, 1.9970140246051808, 1.4495932910616953]]
population repetition ID = 1:  [[1.3605393777535384, 1.0389504829752492, 1.9264370529966892], [2.4498678583842954, 1.8404072091754549, 1.9708541963355648]]
population repetition ID = 2:  [[2.5426412865334918, 1.041503898718803, 2.2672964698525506], [2.4976077650772237, 1.9970140246051808, 1.4495932910616953]]
population repetition ID = 3:  [[1.3605393777535384, 1.0389504829752492, 1.9264370529966892], [2.4498678583842954, 1.8404072091754549, 1.9708541963355648]]

 Agent example:
init. population rep. ID = 0 - agent id = 0:  [2.5426412865334918, 1.041503898718803, 2.2672964698525506]
init. population rep. ID = 0 - agent id = 1:  [2.4976077650772237, 1.9970140246051808, 1.4495932910616953]
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
        <td>The design variables that will be checked</td>
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
        <td>The new design variable values, that are inside the limit defined by lower and upper</td>
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
# Data
xL = [1, 2, 3]
xU = [5, 5, 5]
xI = [6, -1, 2.5]

# Call function
xINew = CHECK_INTERVAL_01(xI, xL, xU)

# Output details
print(xINew)
```

```bash
update solution:  [5.0, 2.0, 3.0]
```

MUTATION_01_MOVEMENT
{: .label .label-green }

<p align = "justify">This function mutates a solution using a Gaussian or Uniform distribution.</p>

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
        <td>Objective function to be optimized</td>
        <td>Py function (<code>def</code>)</td>
    </tr>
    <tr>
        <td><code>X_I_OLD</code></td>
        <td>List containing the values of the current solution</td>
        <td>Py list [D]</td>
    </tr>
    <tr>
        <td><code>X_L</code></td>
        <td>List containing the lower limits for each decision variable</td>
        <td>Py list [D]</td>
    </tr>
    <tr>
        <td><code>X_U</code></td>
        <td>List containing the upper limits for each decision variable</td>
        <td>Py list [D]</td>
    </tr>
    <tr>
        <td><code>D</code></td>
        <td>Problem dimension</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>PDF</code></td>
        <td>Probability Density Function select</td>
        <td>string</td>
    </tr>
    <tr>
        <td><code>SIGMA</code></td>
        <td>Control parameter for the Gaussian or Uniform distribution in percentage. In Gaussian or Uniform distribution, \(\sigma\) equivalent to a standard deviation</td>
        <td>float</td>
    </tr>
    <tr>
        <td><code>SEED</code></td>
        <td>Optional. Seed for generating random numbers. Default <code>SEED = None</code></td>
        <td>Null or integer</td>
    </tr>
    <tr>
        <td><code>NULL_DIC</code></td>
        <td>Variable to use some external data you want in the objective function. When you use NULL_DIC, your data is already saved in memory. Default <code>NULL_DIC = None</code></td>
        <td>Py dict or None</td>
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
        <td>New solution generated by the mutation, containing the values of the decision variables after applying the Gaussian or Uniform distribution and checking the limits</td>
        <td>Py list [D]</td>
    </tr>
    <tr>
        <td><code>OF_I_NEW</code></td>
        <td>Value of the objective function associated with the new solution <code>X_I_NEW</code></td>
        <td>float</td>
    </tr>
    <tr>
        <td><code>FIT_I_NEW</code></td>
        <td>Fitness value associated with the new solution after applying an adjustment function to the objective function value</td>
        <td>float</td>
    </tr>
    <tr>
        <td><code>NEOF</code></td>
        <td>New solution indicator. It is a Boolean value (1 to indicate a new solution)</td>
        <td>int</td>
    </tr>
</table>

Theory
{: .label .label-red }
<p align = "justify">
    See Hill Climbing Theory.
</p>

Example 6
{: .label .label-blue }

<p align = "justify">
  <i>
    Use the <code>MUTATION_01_MOVEMENT</code> function to generate a new solution from an existing solution, applying a standard deviation 15% in current design variables. Use the range \(\mathbf{x}_L = [1.0, 1.0, 1.0]\) and \(\mathbf{x}_L = [3.0, 3.0, 3.0]\). Consider current solution \(\mathbf{x}_i = [2.0, 2.0, 2.0]\).
  </i>
</p>

```python
# Data
xL = [1, 1, 1]
xU = [3, 3, 3]
d = len(xL)
sigma = 15 / 100 # 15%
xI = [2, 2, 2]
pdf = 'UNIFORM'

# Objective function
def OF_FUNCTION(X, NULL_DIC):
    x0 = X[0]
    x1 = X[1]
    x2 = X[2]
    of = x0 ** 2 + x1 ** 2 + x2 ** 2
    return of

# Call function
xII, ofINew, fitINew, neof = MUTATION_01_MOVEMENT(OF_FUNCTION, xI, xL, xU, d, pdf, sigma, NULL_DIC = 1)

# Output details
print('x New: ', xII)
print('of New: ',ofINew)
print('fit New: ', fitINew)
print('number of evalutions objective function: ',neof)
```

```bash
x New:  [2.0532085664365676, 2.0237328790140405, 2.2571792918690035]
of New:  13.406018538533218
fit New:  0.06941543198248705
number of evalutions objective function:  1
```

BEST_VALUES
{: .label .label-green }

<p align = "justify">
    This function determines the best and worst particle. It also determines the average value (OF and FIT) of the population.
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
        <td><code>X</code></td>
        <td>It represents the population of particles, where each line is a particle and and list id is a dimension</td>
        <td>Py list [N_POP] \(\times\) [D]</td>
    </tr>
    <tr>
        <td><code>OF</code></td>
        <td>Objective function values for each particle in the population</td>
        <td>Py list [N_POP]</td>
    </tr>  
    <tr>
        <td><code>FIT</code></td>
        <td>Fitness values for each particle in the population</td>
        <td>Py list [N_POP]</td>
    </tr>  
    <tr>
        <td><code>N_POP</code></td>
        <td>Population size</td>
        <td>integer</td>
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
        <td>integer</td>
    </tr>
    <tr>
        <td><code>WORST_POSITION</code></td>
        <td>Index of the worst particle in the population</td>
        <td>integer</td>
    </tr>
    <tr>
        <td><code>X_BEST</code></td>
        <td>Design variables of the best particle</td>
        <td>Py list [D]</td>
    </tr>
    <tr>
        <td><code>X_WORST</code></td>
        <td>Design variables of the worst particle</td>
        <td>Py list [D]</td>
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

Example 7
{: .label .label-blue }

<p align = "justify">
  <i>
     
  </i>
</p>

```python

```

```bash

```
