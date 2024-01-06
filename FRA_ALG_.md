---
layout: default
title: Metaheuristics
parent: Framework
has_children: true
nav_order: 2
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<p align = "justify">
    This section describes the metaheuristic algorithms implemented in framework. This sections contains main optimization functions about probabilistic methods.
    <br><br>
    The instructions below will guide you through the process of optimzation using the metapy framework.
</p>


```python
df_all_reps, df_resume_all_reps, reports, status = metaheuristic_optmizer(setup)
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
        <td><code>setup</code></td>
        <td>Algorithm settings</td>
        <td>Dictionary</td>
    </tr>
    <tr>
        <td><code>setup</code> keys</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><code>'number of repetitions'</code></td>
        <td>number of repetitions</td>
        <td>Integer</td>
    </tr>
    <tr>
        <td><code>'number of iterations'</code></td>
        <td>number of iterations</td>
        <td>Integer</td>
    </tr> 
    <tr>
        <td><code>'number of population'</code></td>
        <td>number of population</td>
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
        <td><code>'algorithm'</code></td>
        <td>See algorithms were that implemeted</td>
        <td>Dictionary</td>
    </tr>   
    <tr>
        <td><code>'algorithm parameters'</code></td>
        <td>See parameters necessary to perform your algorithm</td>
        <td>Dictionary</td>
    </tr>   
        <td><code>'type code'</code></td>
        <td>Type of population. Options: <code>'real code'</code> or <code>'combinatorial code'</code></td>
        <td>String</td>
    <tr>
        <td><code>'seed control'</code></td>
        <td>Random seed. Use <code>None</code> in list for random seed</td>
        <td>List</td>
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
        <td><code>reports</code></td>
        <td>Report about the repetition process</td>
        <td>String</td>
    </tr>  
    <tr>
        <td><code>status</code></td>
        <td>Best repetition \(id\)</td>
        <td>Integer</td>
    </tr>  
</table>


Example 1
{: .label .label-blue }

```python
# import libray
# pip install metapy-toolbox
from metapy_toolbox import metaheuristic_optmizer
from obj_function import my_function # External .py file with your objective function

# Setup and call function
setup = {   
            'number of repetitions': 30,
            'number of iterations': 250,
            'number of population': 3,
            'number of dimensions': 2,
            'x pop lower limit': [-5, -5],
            'x pop upper limit': [5, 5],
            'none variable': None,
            'objective function': my_function,
            'algorithm': 'hill_climbing_01',
            'algorithm parameters': {'sigma': 20, 'pdf': 'gaussian'},
            'type code': 'real code',
            'seed control': [None] * 30
        }
df_all_reps, df_resume_all_reps, reports, status = metaheuristic_optmizer(setup)
```

```bash
 Optimization results: 

 - Best repetition id:  28
 - Best of:             5.3042292250e-16
 - Design variables:    [2.100789251887419e-08, 9.438822723774955e-09]
 - Process time (s):    3.779469
```

Analysis
{: .label .label-yellow }

<p align="justify">See the details repetition \(id = 0\). <code>df_resume_all_reps</code> contains history details the best particle in \(id = 0\) repetition.</p>

```python
df_resume_all_reps[0]
```

<p align="justify">To see all population history in repetition \(id = 0\) use:</p>

```python
df_all_reps[0]
```

<p align="justify">See best\(id\) in repetitions:</p>

```python
status
```
<p align="justify">See best repetition:</p>

```python
df_resume_all_reps[status]
```

<p align="justify">See complete report about best repetition:</p>

```python
# Report details
arq = "report_example.txt"

# Writing report
with open(arq, "w") as file:
    file.write(report[status])
```
