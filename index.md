---
title: Home
layout: home
nav_order: 1
---

<!--Don't delete ths script-->
<script src = "https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id = "MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!--Don't delete ths script-->

<table>
  <tr>
    <td style="width:70%;">
      <p align="justify">
        The METApy optimization toolbox is an easy-to-use environment for applying metaheuristic optimization methods. The platform has several optimization methods and functions for generating charts and statistical analysis of the results.
      </p>
    </td>
    <td style="width:30%;"><img src="assets/images/logo.png"/></td>  
  </tr>
</table>  

{: .note }
> If you have any suggestions or error reports regarding the algorithm's functioning, please inform us by email: `wanderlei_junior@ufcat.edu.br`. We will be happy to improve the framework.

<h2>Requirements and install</h2>

<p align = "justify">
  Use the command below to install the framework.
</p>

```python
pip install metapy-toolbox
```

{: .Important }
> The METApy is available for installation and use in Google Collaboratoy, Jupyter Notebook or other Python development environments.

<h1>Files structure</h1>

<p align="justify">Let's build an example optimization problem using the METApy framework. The basic file structure of the library should be as follows:</p>

```cmd
 .
 .
 └── problem_directory
       └── of_file.py          # Contain objective function def
       └── example_main.ipynb  # Metapy function (can use .py file too)
       └── other files
```

{: .warning }
> Build objective function in another .py file for good algorithm work. METApy uses parallel processing, and Python recommends separating files when using a .ipynb file.

<h2>Quick start</h2>

Run metaheuristic_optmizer
{: .label .label-yellow }

```python
# import libray
# pip install metapy-toolbox
from metapy_toolbox import metaheuristic_optmizer
from obj_function import my_function # External .py file with your objective function

# Settings
setup = {   
            'number of repetitions': 3,
            'number of iterations': 5,
            'number of population': 1,
            'number of dimensions': 2,
            'x pop lower limit': [-5, -5],
            'x pop upper limit': [5, 5],
            'none variable': None,
            'objective function': my_function,
            'algorithm': 'hill_climbing_01',
            'algorithm parameters': {'sigma': 20, 'pdf': 'GAUSSIAN'},
            'type code': 'real code',
            'seed control': [None] * 3
        }

df_all_reps, df_resume_all_reps, reports, status = metaheuristic_optmizer(setup)
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

<p align="justify">See best \(id\) in repetitions:</p>

```python
status
```

<p align="justify">See complete report about best repetition:</p>

```python
# Report details
arq = "report_example.txt"

# Writing report
with open(arq, "w") as file:
    file.write(report[status])
```

of_file structure
{: .label .label-yellow }

<p align="justify">Use the structure presents bellow to assembly your objective function. Example Sphere function.</p>

```python
def my_function(x, none_variable):
    x_0 = x[0]
    x_1 = x[1]
    obj_fun = x_0 ** 2 + x_1 ** 2
    return obj_fun
```

<p align="justify">
  See section <a href="https://wmpjrufg.github.io/METAPY/FRA_ALG_.html" target="_blank">Metaheuristic</a> for more detail.
</p>
