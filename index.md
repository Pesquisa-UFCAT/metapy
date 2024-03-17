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
    └── of_file.py          # Contain objective function (format Python def)
    └── your_problem.ipynb  # Metapy function (or can use .py file too)
    └── other files
```

{: .warning }
> Build objective function in another .py file for good algorithm work. METApy uses parallel processing, and Python documentation recommends separating files when using a .ipynb file.

<h2>Quick start</h2>

<p align="justify">
The purpose of this example is the optimization (minimization) of the well-known sphere function.
</p>

your_problem
{: .label .label-green }

```python
"""Run optimization: your_problem.py or your_problem.ipynb"""
# import libray
# pip install metapy-toolbox or pip install --upgrade metapy-toolbox
from metapy_toolbox import metaheuristic_optimizer
from of_file import my_function # External .py file with your objective function

# Algorithm settings
algorithm_setup = {   
                    'number of iterations': 100,
                    'number of population': 2,
                    'number of dimensions': 2,
                    'x pop lower limit': [-5, -5],
                    'x pop upper limit': [5, 5],
                    'none variable': None,
                    'objective function': my_obj_function,
                    'algorithm parameters': {
                                                'mutation': {
                                                                'cov (%)': 20,
                                                                'pdf': 'gaussian'
                                                            }
                                            },
                  }

# METApy settings
general_setup = {   
            'number of repetitions': 30,
            'type code': 'real code',
            'initial pop. seed': [None] * 30,
            'algorithm': 'hill_climbing_01',
        }

# Run algorithm
df_all_reps, df_resume_all_reps, reports, status = metaheuristic_optimizer(algorithm_setup, general_setup)
```

of_file
{: .label .label-green }

```python
"""Object Function: of_file.py"""  
def my_function(x, none_variable):
    x_0 = x[0]
    x_1 = x[1]
    of = x_0 ** 2 + x_1 ** 2
    return of
```

<h3>Analysis of results</h3>

<p align="justify">See the details repetition \(id = 0\). <code>df_resume_all_reps</code> contains history details the best particle in \(id = 0\) repetition.</p>

```python
print(df_resume_all_reps[0])
```

<p align="justify">To see all population history in repetition \(id = 0\) use:</p>

```python
print(df_all_reps[0])
```

<p align="justify">See best repetition \(id\) and best dataset:</p>

```python
print(status)
print(df_resume_all_reps[status])
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
  See section <a href="https://wmpjrufg.github.io/METAPY/FRA_META_.html" target="_blank">metaheuristic_optimizer</a> for more details.
</p>
