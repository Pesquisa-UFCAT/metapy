<!-- ---
layout: default
title: Tournament Selection
grand_parent: Framework
parent: Genetic Algorithm functions
has_children: false
has_toc: true
nav_order: 2
--- -->

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

TOURNAMENT_SELECTION
{: .label .label-green }

```python
selected_index = meta.tournament_selection(fitness, n_pop, 2, 5)
```

<p align = "justify">This function selects a position from the population using the tournament selection method.</p>

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
       <td>A matrix that stores the fitness values for each individual in the population.</td>
       <td>NumPy list</td>
   </tr>
   <tr>
       <td><code>n_pop</code></td>
       <td>Indicates the size of the population, i.e. the total number of individuals.</td>
       <td>Int</td>
   </tr> 
   <tr>
       <td><code>i</code></td>
       <td>Index of the individual for whom tournament selection will be carried out. This is the index that will be temporarily removed during the selection process.</td>
       <td>Int</td>
   </tr>
      <tr>
       <td><code>runs</code></td>
       <td>Number of times the tournament will be run to choose the individual. Each run of the tournament involves randomly choosing two individuals from the population.</td>
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
       <td>Index of the selected individual in the population. This is the index of the individual who won the tournament.</td>
       <td>Int</td>
   </tr>
 
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
 <i>
 Use the <code>TOURNAMENT_SELECTION</code> function to select an individual based on probabilities proportional to their aptitude. In this example, the aptitude is a list of aptitudes for each individual in the population. The number 2 passed as the third argument to the function indicates that you want to exclude the third individual when performing the tournament selection. And 5 is the number of times the tournament will be played.
 </i>
</p>

```python
import numpy as np
import meta_ga_library as meta

n_pop = 10
fitness = np.random.rand(n_pop, 1)

selected_index = meta.tournament_selection(fitness, n_pop, 2, 5)

print("Selected individual:", selected_index)

```

```bash
Selected individual: 6
```
