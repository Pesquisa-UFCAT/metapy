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
    This section describes the metaheuristic algorithms implemented in framework. This sections contains main optimization functions.
    <br><br>
    The instructions below will guide you through the process of optimzation using the metapy framework.
</p>

<h1>Requirements and install</h1>

<p align="justify">To use the platform in an environment that interprets the Python language, simply use the following command:</p>

```python
pip install metapy-toolbox
```
<h1>Files structure</h1>

<p align="justify">Let's build an example optimization problem using the METApy framework. The basic file structure of the library should be as follows:</p>

```cmd
 .
 .
 └── problem_directory
       └── of_file.py          # contain objective function def
       └── example_main.ipynb  # Metapy function (can use .py file)
       └── other files
```

Example 
{: .label .label-blue }

```python
# Import
from obj_function import my_function
from metapy_toolbox import metaheuristic_optmizer

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
df_all_reps, df_resume_all_reps, status = metaheuristic_optmizer(setup)
```

```bash
 Optimization results: 

 - Best repetition id:  28
 - Best of:             5.3042292250e-16
 - Design variables:    [2.100789251887419e-08, 9.438822723774955e-09]
 - Process time (s):    3.779469
```
