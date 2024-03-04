---
layout: default
title: blxalpha_crossover
grand_parent: Framework
parent: Genetic Algorithm functions
has_children: false
has_toc: false
nav_order: 4
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>blxalpha_crossover</h3>
<br>

```python
blxalpha_crossover(my_obj_function, father_1, father_2, n_dimensions, x_upper, x_lower, none_variable)
```

<p align = "justify">BLX alpha crossover operator.

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
       <td><code>of_function</code></td>
       <td>Objective function</td>
       <td>Py function (<code>def</code>)</td>
   </tr> 
   <tr>
       <td><code>father_1</code></td>
       <td>First parent</td>
       <td>List</td>
   </tr>
   <tr>
       <td><code>father_2</code></td>
       <td>Second parent</td>
       <td>List</td>
   </tr> 
   <tr>
       <td><code>n_dimensions</code></td>
       <td>Problem dimension</td>
       <td>Int</td>
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
       <td>Update variables of the i agent</td>
       <td>L'ist</td>
   </tr>
   <tr>
       <td><code>of_i_new</code></td>
       <td> Update objective function value of the i agent</td>
       <td>Float</td>
   </tr>
   <tr>
       <td><code>fit_i_new</code></td>
       <td>Update fitness value of the i agent</td>
       <td>Float</td>
   </tr>
   <tr>
       <td><code>neof</code></td>
       <td>New solution indicator. It is a Boolean value (1 to indicate a new solution)</td>
       <td>Int</td>
   </tr>
   <tr>
       <td><code>report</code></td>
       <td>Report about the male movement process</td>
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
from metapy_toolbox import blxalpha_crossover
from my_example import my_obj_function

father_1 = [1, 1, 1, 1, 1]
father_2 = [10, 10, 10, 10, 10]
n_dimensions = 5
x_upper = [10, 10, 10, 10, 10]
x_lower = [1, 1, 1, 1, 1]
none_variable = None


x_i_new, of_i_new, fit_i_new, neof, report_move = blxalpha_crossover(my_obj_function, father_1, father_2, n_dimensions, x_upper, x_lower, none_variable)

print(x_i_new)
print(of_i_new)
print(fit_i_new)
print(neof)
print(report_move)
```

```bash
[1, 1, 1, 1, 10]
2
0.3333333333333333
2
    Crossover operator - uniform crossover
    current p0 = [1, 1, 1, 1, 1]
    current p1 = [10, 10, 10, 10, 10]
    random number = 0.8064253519886561 >= 0.50
    cut parent_1 -> of_a 10
    cut parent_0 -> of_b 1
    random number = 0.8598725452151063 >= 0.50
    cut parent_1 -> of_a 10
    cut parent_0 -> of_b 1
    random number = 0.586172882088994 >= 0.50
    cut parent_1 -> of_a 10
    cut parent_0 -> of_b 1
    random number = 0.605892666755684 >= 0.50
    cut parent_1 -> of_a 10
    cut parent_0 -> of_b 1
    random number = 0.4394649418366411 < 0.50
    cut parent_0 -> of_a 1
    cut parent_1 -> of_b 10
    offspring a = [10, 10, 10, 10, 1], of_a = 200
    offspring b = [1, 1, 1, 1, 10], of_b = 2
    update pos = [1, 1, 1, 1, 10], of = 2, fit = 0.3333333333333333

[1, 1, 10, 10, 10]
2
0.3333333333333333
2
    Crossover operator - Single point
    current p0 = [1, 1, 1, 1, 1]
    current p1 = [10, 10, 10, 10, 10]
    cut position 2
    cut parent_0 -> of_a [1, 1]
    cut parent_1 -> of_a [10, 10, 10]
    cut parent_1 -> of_b [10, 10]
    cut parent_0 -> of_b [1, 1, 1]
    offspring a = [1, 1, 10, 10, 10], of_a = 2
    offspring b = [10, 10, 1, 1, 1], of_b = 200
    update n_dimensions = [1, 1, 10, 10, 10], of = 2, fit = 0.3333333333333333

[1.0, 1.0, 1.0, 1.0, 1.0]
2.0
0.3333333333333333
3
    Crossover operator - Linear crossover
    current p0 = [1, 1, 1, 1, 1]
    current p1 = [10, 10, 10, 10, 10]
    Dimension 0: alpha_a = 0.5, beta_a = 5.0, neighbor_a = 5.5
    Dimension 0: alpha_b = 1.5, beta_b = 5.0, neighbor_b = -3.5
    Dimension 0: alpha_c = 0.5, beta_c = 15.0, neighbor_c = 14.5
    Dimension 1: alpha_a = 0.5, beta_a = 5.0, neighbor_a = 5.5
    Dimension 1: alpha_b = 1.5, beta_b = 5.0, neighbor_b = -3.5
    Dimension 1: alpha_c = 0.5, beta_c = 15.0, neighbor_c = 14.5
    Dimension 2: alpha_a = 0.5, beta_a = 5.0, neighbor_a = 5.5
    Dimension 2: alpha_b = 1.5, beta_b = 5.0, neighbor_b = -3.5
    Dimension 2: alpha_c = 0.5, beta_c = 15.0, neighbor_c = 14.5
    Dimension 3: alpha_a = 0.5, beta_a = 5.0, neighbor_a = 5.5
    Dimension 3: alpha_b = 1.5, beta_b = 5.0, neighbor_b = -3.5
    Dimension 3: alpha_c = 0.5, beta_c = 15.0, neighbor_c = 14.5
    Dimension 4: alpha_a = 0.5, beta_a = 5.0, neighbor_a = 5.5
    Dimension 4: alpha_b = 1.5, beta_b = 5.0, neighbor_b = -3.5
    Dimension 4: alpha_c = 0.5, beta_c = 15.0, neighbor_c = 14.5
    offspring a = [1.0, 1.0, 1.0, 1.0, 1.0], of_a 2.0
    offspring b = [1.0, 1.0, 1.0, 1.0, 1.0], of_b 2.0
    offspring c = [1.0, 1.0, 1.0, 1.0, 1.0], of_c 2.0
    update x = [1.0, 1.0, 1.0, 1.0, 1.0], of = 2.0, fit = 0.3333333333333333

[1.0, 1.0, 1.0, 1.0, 1.0]
2.0
0.3333333333333333
2
    Crossover operator - BLX-alpha
    current p0 = [1, 1, 1, 1, 1]
    current p1 = [10, 10, 10, 10, 10]
    Dimension 0: min_val = 1, max_val = 10, r_ij = 9
    neighbor_a = -0.06942439549618662, neighbor_b = 11.069424395496187
    Dimension 1: min_val = 1, max_val = 10, r_ij = 9
    neighbor_a = -0.06942439549618662, neighbor_b = 11.069424395496187
    Dimension 2: min_val = 1, max_val = 10, r_ij = 9
    neighbor_a = -0.06942439549618662, neighbor_b = 11.069424395496187
    Dimension 3: min_val = 1, max_val = 10, r_ij = 9
    neighbor_a = -0.06942439549618662, neighbor_b = 11.069424395496187
    Dimension 4: min_val = 1, max_val = 10, r_ij = 9
    neighbor_a = -0.06942439549618662, neighbor_b = 11.069424395496187
    offspring a = [1.0, 1.0, 1.0, 1.0, 1.0], of_a 2.0
    offspring b = [1.0, 1.0, 1.0, 1.0, 1.0], of_b 2.0
    update x = [1.0, 1.0, 1.0, 1.0, 1.0], of = 2.0, fit = 0.3333333333333333
```
