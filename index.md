---
title: Home
layout: home
nav_order: 1
---

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
> If you have any suggestions or error reports regarding the algorithm's functioning, please inform us by email: `wanderlei_junior@ufcat.edu.br`. We will be happy to improve the platform.

<h2>Requirements and install</h2>

<p align = "justify">
  Use the command below to install the framework.
</p>

```python
pip install metapy-toolbox
```

<p align="justify">The METApy is available for installation and use in <b>Google Collaboratoy</b>, <b>Jupyter Notebook</b> or other <b>Python development environments</b>.</p>

<h2>Quick start</h2>

Run metaheuristic optmizer {: .label .label-yellow }

```python
# pip install metapy-toolbox
from metapy_toolbox import metaheuristic_optmizer

from obj_function import * # External .py file with your objective function

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
            'algorithm parameters': {'std (%)': 20, 'pdf': 'GAUSSIAN'},
            'type code': 'real code',
            'seed control': None
        }

df_all_reps, df_resume_all_reps = metaheuristic_optmizer(setup)
```
Analysis{: .label .label-yellow }

<p align="justify">See the details repetition \(id\ = 0\). <code>df_resume_all_reps</code> contains history details the best particle in \(id\ = 0\) repetition.</p>

```python
df_resume_all_reps[0]
```

<p align="justify">To see all population history in repetition \(id\ = 0\) use:</p>

```python
df_all_reps[0]
```

of_file structure{: .label .label-yellow }

<p align="justify">Use the structure presents bellow to assembly your objective function. Example sphere function.</p>

```python
def my_function(x, none_variable):
    x_0 = x[0]
    x_1 = x[1]
    obj_fun = x_0 ** 2 + x_1 ** 2
    return obj_fun
```
