---
title: Common Library
layout: home
parent: Framework
has_children: true
nav_order: 1
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<p align = "justify">
    This section describes the documentation of the file functions <code>META_CO_LIBRARY.py</code>.
</p>

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
    <!--
    <tr>
        <td><code>N_POP</code></td>
        <td>Population size</td>
        <td>integer</td>
    </tr>
    -->
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
    Use the <code>BEST_VALUES</code> function to find the best and worst values in the array <code>[[1, 2, 3], [4, 5, 6], [7, 8, 9]]</code>.
  </i>
</p>

```python
xValues = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ofValues = [10, 5, 8]
fitValues = [0.1, 0.5, 0.3]

bestPos, worstPos, xBest, xWorst, ofBest, ofWorst, fitBest, fitWorst, ofAverage, fitAverage = BEST_VALUES(xValues, ofValues, fitValues)

print("Best position in the population:", bestPos)
print("Worst position in the population:", worstPos)
print("Best value of X:", xBest)
print("Worst value of X:", xWorst)
print("Best value of OF:", ofBest)
print("Worst value of OF:", ofWorst)
print("Best value of FIT:", fitBest)
print("Worst value of FIT:", fitWorst)
print("Average OF value:", ofAverage)
print("Average FIT value:", fitAverage)


```

```bash
Best position in the population: 1
Worst position in the population: 0
Best value of X: [4, 5, 6]
Worst value of X: [1, 2, 3]
Best value of OF: 5
Worst value of OF: 10
Best value of FIT: 0.5
Worst value of FIT: 0.1
Average OF value: 7.666666666666667
Average FIT value: 0.3
```
