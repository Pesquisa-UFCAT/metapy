<h1><b>Simulated Annealing</b></h1>

Function: _**SA_ALGORITHM_0001**_

<p align="justify">The user must always inform the method setup and the Objective Function that he wants to minimize. The OBJ function should always have an X list (design variables X = [0, 1, 2, 3, ..., N_POP - 2, N_POP - 1) and a dictionary as input.</p>

Syntax example:

```python
# Sphere optimization (4 dimensions)
SETUP = {'N_REP': 30,
         'N_ITER': 100,
         'N_POP': 1,
         'D': 4,
         'X_L': [-10] * D, # or [-10, -10, -10, -10]
         'X_U': [10] * D,  # or [10, 10, 10, 10]
         'SIGMA': 0.15,
         'ALPHA': 0.98,
         'TEMP': None,
         'STOP_CONTROL_TEMP': None,
         'NULL_DIC': None
        }

def OF_FUNCTION(X, NULL_DIC):
    OF = SPHERE(X)
    return OF

[RESULTS_REP, BEST_REP, AVERAGE_REP, WORST_REP, STATUS] = SA_ALGORITHM_0001(OF_FUNCTION, SETUP)
```

Internal parameters:
_Required filling_
- ```SIGMA```: Standard deviation the normal distribution in percentage (float);
- ```ALPHA```: Linear temperature reduction factor (float).     
  
_None Variables_
- ```TEMP```: Initial temperature (float) or automatic temperature value that has an 80% probability of acceptance by the initial population (float);  
- ```STOP_CONTROL_TEMP```: Stop criteria about initial temperature try (float) or automatic value = 1000 (float);  
- ```NULL_DIC```: Empty dictionary for the user to use in the obj function (Python dictionary).  

[Download the example](https://nbviewer.jupyter.org/github/wmpjrufg/META_TOOLBOX/blob/gh-pages/SA_example.ipynb)