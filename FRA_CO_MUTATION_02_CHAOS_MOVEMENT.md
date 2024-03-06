---
layout: default
title: mutation_02_chaos_movement
grand_parent: Framework
parent: Common Library functions
has_toc: false
nav_order: 7
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>mutation_02_chaos_movement</h3>

<br>

<p align = "justify">
  This function mutates a solution using a chaotic maps.
</p>

```python
x_i_new, of_i_new,\
    fit_i_new, neof = mutation_02_chaos_movement(obj_function,
                                                    x_i_old, fit_i_old,
                                                    x_lower, x_upper,
                                                    n_dimensions, ch,
                                                    alpha, n_tries,
                                                    iteration, n_iter,
                                                    none_variable=None)
```

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
        <td><code>obj_function</code></td>
        <td>Objective function. The Metapy user defined this function</td>
        <td>Py function (def)</td>
    </tr>
    <tr>
        <td><code>x_i_old</code></td>
        <td>Current design variables of the \(i\) agent</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>fit_i_old</code></td>
        <td>Current fitness value of the \(i\) agent</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>x_lower</code></td>
        <td>Lower limit of the design variables</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>x_upper</code></td>
        <td>Upper limit of the design variables</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>n_dimensions</code></td>
        <td>Problem dimension</td>
        <td>Int</td>
    </tr>
    <tr>
        <td><code>ch</code></td>
        <td>Initial value of chaotic map</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>alpha</code></td>
        <td>Chaotic map control parameter</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>n_tries</code></td>
        <td>Number of tries to find a better solution</td>
        <td>Int</td>
    </tr>
    <tr>
        <td><code>iteration</code></td>
        <td>Current iteration number</td>
        <td>Int</td>
    </tr>
    <tr>
        <td><code>n_iter</code></td>
        <td>Total number of iterations</td>
        <td>Int</td>
    </tr>
    <tr>
        <td><code>none_variable</code></td>
        <td>None variable. Default is None. Use in objective function</td>
        <td>Object or None</td>
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
        <td><code>x_i_new</code></td>
        <td>Update variables of the \(i\) agent</td>
        <td>List</td>
    </tr>
    <tr>
        <td><code>of_i_new</code></td>
        <td>Update objective function value of the \(i\) agent</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>fit_i_new</code></td>
        <td>Update fitness value of the \(i\) agent</td>
        <td>Float</td>
    </tr>
    <tr>
        <td><code>neof</code></td>
        <td>Number of evaluations of the objective function</td>
        <td>Int</td>
    </tr>
    <tr>
        <td><code>report</code></td>
        <td>Report about the mutation process</td>
        <td>String</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
  <i>
      
  </i>
</p>

```python
# Import
from metapy_toolbox import mutation_02_chaos_movement # or import *

# Data
xIOLD = [2, 2]
fitIOld = 0.5
xLower = [1, 1]
xUpper = [5, 5]
nDimensions = len(xLower)
ch = 0.80
alpha = 0.5
nTries = 5
iteration = 1
nIter = 10
noneVariable = None

# Objective function
def objFunction(x, _):
    """Example objective function"""
    x0 = x[0]
    x1 = x[1]
    of = x0 ** 2 + x1 ** 2
    return of

# Call function
xNew, ofNew, fitNew, neof, report = mutation_02_chaos_movement(objFunction, xIOLD, fitIOld, xLower, xUpper, nDimensions, ch, alpha, nTries, iteration, nIter, noneVariable)

# Output details
print('x New: ', xNew)
print('of New: ', ofNew)
print('fit New: ', fitNew)
print('number of evalutions objective function: ', neof)
print(report)
```

```bash
particle 0:  [0, 1, 2]
particle 1:  [1, 2, 0]
particle 2:  [2, 0, 1]
particle 3:  [1, 0, 2]
particle 4:  [2, 1, 0]
particle 0:  [3.8153230169089265, 1.9848354089962532, 2.450452219785369]
particle 1:  [2.259678570212208, 2.9985982933894864, 3.0448438282032217]
particle 2:  [3.8429316660847683, 2.6790897803261204, 3.4065822516097475]
particle 3:  [3.713141184010253, 3.9005925613641423, 2.6841743386681323]
particle 4:  [2.1170005613166114, 2.514410798888015, 2.449554323176514]
population repetition ID = 0:  [[2.1522944830727098, 1.4204806736930837, 1.484535069446151], [2.4353419066354984, 2.326333035092053, 1.0525705231667497]]
population repetition ID = 1:  [[2.9092424648909816, 2.5955086055916903, 2.65634590083977], [1.6698328920546859, 1.0302235634684915, 1.8573942792584803]]
population repetition ID = 2:  [[2.73776793829576, 2.385361212661906, 1.8816912211795804], [2.074566697630532, 1.1260402554313869, 2.767127226625485]]
population repetition ID = 3:  [[1.9960690883455705, 1.8053989355012685, 1.0895528482082497], [1.1386531462704574, 2.155905272871008, 2.867402253986409]]

 Agent example:
init. population rep. ID = 0 - pop = 0:  [2.1522944830727098, 1.4204806736930837, 1.484535069446151]
init. population rep. ID = 0 - pop = 1:  [2.4353419066354984, 2.326333035092053, 1.0525705231667497]
population repetition ID = 0:  [[2.5426412865334918, 1.041503898718803, 2.2672964698525506], [2.4976077650772237, 1.9970140246051808, 1.4495932910616953]]
population repetition ID = 1:  [[1.3605393777535384, 1.0389504829752492, 1.9264370529966892], [2.4498678583842954, 1.8404072091754549, 1.9708541963355648]]
population repetition ID = 2:  [[1.3083256847593447, 2.4800993930308097, 1.5266300303702693], [2.0674787867605957, 1.0291499249708393, 2.83749401619977]]
population repetition ID = 3:  [[2.5554048211476403, 1.4750824400698246, 2.648557065322737], [2.9314983960859995, 2.9452022278097867, 1.9068984948346244]]

 Agent example:
init. population rep. ID = 0 - pop = 0:  [2.5426412865334918, 1.041503898718803, 2.2672964698525506]
init. population rep. ID = 0 - pop = 1:  [2.4976077650772237, 1.9970140246051808, 1.4495932910616953]
population repetition ID = 0:  [[3, 9, 0, 1, 8, 5, 7, 6, 2, 4], [4, 9, 2, 1, 7, 6, 8, 5, 3, 0]]
population repetition ID = 1:  [[7, 9, 0, 1, 3, 5, 4, 2, 6, 8], [9, 6, 4, 3, 2, 7, 0, 1, 5, 8]]
population repetition ID = 2:  [[1, 4, 2, 5, 0, 8, 6, 7, 9, 3], [8, 2, 7, 1, 0, 5, 3, 9, 4, 6]]
population repetition ID = 3:  [[6, 5, 0, 7, 8, 1, 2, 3, 4, 9], [4, 7, 9, 6, 3, 2, 0, 8, 1, 5]]

 Agent example:
init. population rep. ID = 0 - pop = 0:  [3, 9, 0, 1, 8, 5, 7, 6, 2, 4]
init. population rep. ID = 0 - pop = 1:  [4, 9, 2, 1, 7, 6, 8, 5, 3, 0]
fit value i agent when OF = 1 is  0.5
[5.0, 2.0, 3.0] <class 'list'>
Best position in the population: 1
Worst position in the population: 0
Best value of X: [4, 5, 6]
Worst value of X: [1, 2, 3]
Best OF: 5
Worst OF: 10
Best FIT: 0.17
Worst FIT: 0.09
Average OF: 7.666666666666667
Average FIT: 0.12333333333333334
x New:  [2.2555966876941307, 2.1080630093627852]
of New:  9.531646068980415
fit New:  0.09495191857475814
number of evalutions objective function:  1
x New:  [1.0348175590490112, 1.0348175590490112]
of New:  2.1416947610323076
fit New:  0.31829954087309775
number of evalutions objective function:  5
    Try 0 fit best = 0.5
    Dimension 0: epsilon = 1.0, ch = 4.2, neighbor = 4.2
    Dimension 1: epsilon = 1.0, ch = 4.2, neighbor = 4.2
    temporary move x = [4.2, 4.2], of = 35.28, fit = 0.027563395810363836
    fit_i_temp 0.027563395810363836 < fit_pop[pop] 0.5 - not accept this solution
    Try 1 fit best = -1000
    Dimension 0: epsilon = 1.0, ch = 1.3199999999999998, neighbor = 1.3199999999999998
    Dimension 1: epsilon = 1.0, ch = 1.3199999999999998, neighbor = 1.3199999999999998
    temporary move x = [1.3199999999999998, 1.3199999999999998], of = 3.484799999999999, fit = 0.2229753835176597
    fit_i_temp 0.2229753835176597 > fit_pop[pop] -1000 - accept this solution
    update x = [1.3199999999999998, 1.3199999999999998], of = 3.484799999999999, fit = 0.2229753835176597
    Try 2 fit best = 0.2229753835176597
    Dimension 0: epsilon = 1.0, ch = 1.1472, neighbor = 1.1472
    Dimension 1: epsilon = 1.0, ch = 1.1472, neighbor = 1.1472
    temporary move x = [1.1472, 1.1472], of = 2.63213568, fit = 0.27532011138967144
    fit_i_temp 0.27532011138967144 > fit_pop[pop] 0.2229753835176597 - accept this solution
    update x = [1.1472, 1.1472], of = 2.63213568, fit = 0.27532011138967144
    Try 3 fit best = 0.27532011138967144
    Dimension 0: epsilon = 1.0, ch = 1.07089152, neighbor = 1.07089152
    Dimension 1: epsilon = 1.0, ch = 1.07089152, neighbor = 1.07089152
    temporary move x = [1.07089152, 1.07089152], of = 2.293617295215821, fit = 0.3036175458067216
    fit_i_temp 0.3036175458067216 > fit_pop[pop] 0.27532011138967144 - accept this solution
    update x = [1.07089152, 1.07089152], of = 2.293617295215821, fit = 0.3036175458067216
    Try 4 fit best = 0.3036175458067216
    Dimension 0: epsilon = 1.0, ch = 1.0348175590490112, neighbor = 1.0348175590490112
    Dimension 1: epsilon = 1.0, ch = 1.0348175590490112, neighbor = 1.0348175590490112
    temporary move x = [1.0348175590490112, 1.0348175590490112], of = 2.1416947610323076, fit = 0.31829954087309775
    fit_i_temp 0.31829954087309775 > fit_pop[pop] 0.3036175458067216 - accept this solution
    update x = [1.0348175590490112, 1.0348175590490112], of = 2.1416947610323076, fit = 0.31829954087309775
```
