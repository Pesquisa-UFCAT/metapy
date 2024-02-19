---
layout: default
title: Roulete Wheel Selection
grand_parent: Framework
parent: Genetic Algorithm functions
has_children: false
has_toc: true
nav_order: 1
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

ROULETE_WHEEL_SELECTION
{: .label .label-green }

```python
selected_index = meta.roulete_wheel_selection(fitness, n_pop, 2)
```

<p align = "justify">This function selects a position from the population using the roulette wheel selection method.</p>

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
       <td><code>fit</code></td>
       <td>It represents the fitness of the individuals in the population. It is supplied as input to the function.</td>
       <td>NumPy list</td>
   </tr>
   <tr>
       <td><code>n_pop</code></td>
       <td>Indicates the size of the population, i.e. the total number of individuals.</td>
       <td>Int</td>
   </tr> 
   <tr>
       <td><code>i</code></td>
       <td>Represents the index of the individual who will be excluded during the roulette wheel selection process.</td>
       <td>Int</td>
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
       <td><code>selected</code></td>
       <td>Stores the index of the individual selected after the roulette method.</td>
       <td>Int</td>
   </tr>
 
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
 <i>
Use the <code>ROULETE_WHEEL_SELECTION</code> function to select an individual based on probabilities proportional to their fitness. In this example, fitness is a list of aptitudes for each individual in the population. The number 2 passed as the third argument to the function indicates that you want to exclude the third individual when performing the roulette wheel selection. 
 </i>
</p>

```python
import meta_ga_library as meta
import numpy as np

n_pop = 10
fitness = np.random.rand(n_pop)
selected_index = meta.roulete_wheel_selection(fitness, n_pop, 2)

print(f"Selected index: {selected_index}")
```

```bash
Selected index: 7
```
