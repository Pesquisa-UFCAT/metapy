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

{: .note }
> The METApy is available for installation and use in Google Collaboratoy, Jupyter Notebook or other Python development environments.

<h2>Files structure</h2>

<p align="justify">
Let's build an example optimization problem using the METApy framework. The basic file structure of the library should be as follows:
</p>

```cmd
 .
 └── problem_directory
       └── of_file.py          # Contain objective function def
       └── your_problem.ipynb  # Metapy function (can use .py file too)
       └── other files
```

{: .warning }
> Build objective function in another .py file for good algorithm work. METApy uses parallel processing, and Python documntation recommends separating files when using a .ipynb file.

<h2>Quick start</h2>

<p align="justify">
The purpose of this example is the optimization (minimization) of the well-known sphere function.
</p>

your_problem
{: .label .label-green }

```python
# import libray
# pip install metapy-toolbox
from metapy_toolbox import metaheuristic_optimizer
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
            'algorithm parameters': {'sigma': 20, 'pdf': 'gaussian'},
            'type code': 'real code',
            'seed control': [None] * 3
        }

# Run algorithm
df_all_reps, df_resume_all_reps, reports, status = metaheuristic_optmizer(setup)
```

of_file
{: .label .label-green }

```bash
def my_function(x, none_variable):
    x_0 = x[0]
    x_1 = x[1]
    of = x_0 ** 2 + x_1 ** 2
    return of
```

Analysis
<h3>Analysis</h3>

<p align="justify">See the details repetition \(id = 0\). <code>df_resume_all_reps</code> contains history details the best particle in \(id = 0\) repetition.</p>

```python
print(df_resume_all_reps[0])
```

<p align="justify">To see all population history in repetition \(id = 0\) use:</p>

```python
print(df_all_reps[0])
```

<p align="justify">See best repetition \(id\):</p>

```python
print(status)
```

<p align="justify">See complete report about best repetition:</p>

```python
# Report details
arq = "report_example.txt"

# Writing report
with open(arq, "w") as file:
    file.write(report[status])
```

<p align="justify">
  See section <a href="https://wmpjrufg.github.io/METAPY/FRA_ALG_.html" target="_blank">Metaheuristic</a> for more detail.
</p>
