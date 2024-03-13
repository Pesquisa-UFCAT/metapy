---
layout: default
title: agent_selection
grand_parent: Framework
parent: Common Library functions
has_toc: false
nav_order: 7
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<h3>agent_selection</h3>

<br>

<p align = "justify">
This function selects a n agents from all population (uniform selection).
</p>

```python

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
       <td><code>n_population</code></td>
       <td>Number of population</td>
       <td>Integer</td>
   </tr>
    <tr>
       <td><code>n</code></td>
       <td>Number of agents to select</td>
       <td>Integer</td>
   </tr>
    <tr>
       <td><code>i_pop</code></td>
       <td>Default is False (Selects n agents among all population). i_pop=Integer Selects n agents among all population, excluding i_pop agent</td>
       <td>Integer or Boolean</td>
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
       <td>Selected dimensions</td>
       <td>List</td>
   </tr>
    <tr>
       <td><code>report</code></td>
       <td>Report about the selection process</td>
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
from metapy_toolbox import agent_selection # or import *

nPop = 5
n = 3
iPop = 2
selected, report = agent_selection(nPop, n, iPop)
print(selected)
```

```bash
[4 1 0]
```

<p align = "justify">
  To check the movement report just apply the following instruction.
</p>

```python
# Report details
arq = "report_example.txt"

# Writing report
with open(arq, "w") as file:
    file.write(report)
```

<p align = "justify">
  Open <code>report_example.txt</code>. 
</p>

```bash
    Selection population operator
    probs = [0.25, 0.25, 0.0, 0.25, 0.25]
    the selected agents = [4 1 0]
```
