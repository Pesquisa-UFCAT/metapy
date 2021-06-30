<h1><b>Simulated Annealing</b></h1>

Function: _**SA_ALGORITHM_0001**_

<p align="justify">The user must always inform the method setup and the Objective Function that he wants to minimize. The OBJ function should always have an X list (design variables X = [0, 1, 2, 3, ..., N_POP - 2, N_POP - 1) and a dictionary as input.</p>

<h3><b>How to use</b></h3>

<p align="justify">The simulated annealing function has the following input variables.</p>

- ```OF_FUNCTION```: External _def_ user input this function in arguments (Python ```def```);
- ```N_REP```: Number of repetitions (integer);
- ```N_ITER```: Number of iterations (integer);
- ```N_POP```: Number of population (integer);
- ```D```: Dimension problem (integer);
- ```X_L```: Lower limit design variables (Python list[D], float);
- ```X_U```: Upper limit design variables (Python list[D], float);
- ```SIGMA```: Standard deviation the normal distribution in percentage (float);
- ```ALPHA```: Linear temperature reduction factor (float);  
_None Variables_:
- ```TEMP```: Initial temperature (float) or automatic temperature value that has an 80% probability of acceptance by the initial population (float)
- ```STOP_CONTROL_TEMP```: Stop criteria about initial temperature try (float) or automatic value = 1000 (float)
- ```NULL_DIC```: Empty dictionary for the user to use in the obj function (Python dictionary)

<p align="justify">The simulated annealing function has the following output variables.</p>
- ```RESULTS_REP```: Results movement all population (Python dictionary)
- ```BEST_REP```: Results movement best population (Python dictionary)
- ```AVERAGE_REP```: Results movement average of and fit (Python dictionary)
- ```WORST_REP```: Results movement worst population (Python dictionary)

Example:  
```python
# Method setup
SETUP = {'N_REP': 2,
         'N_ITER': 10,
         'N_POP': 1,
         'D': 5,
         'X_L': [-30] * 5,
         'X_U': [30] * 5,
         'SIGMA': 0.20,
         'ALPHA': 0.98,
         'TEMP': 100,
         'STOP_CONTROL_TEMP': 2,
         'NULL_DIC': None
        }

# Sphere
def SPHERE(X):
    """
    Sphere benchmark function D-dimension
    """
    DIM = len(X)
    SUM = 0
    for I_COUNT in range(DIM):
        X_I = X[I_COUNT]
        SUM += X_I ** 2
    Y = SUM
    return Y

# Obj. Function
def OF_FUNCTION(X, NULL_DIC):
    OF = SPHERE(X)
    return OF  
    
# Call function
RESULTS_REP, BEST_REP, AVERAGE_REP, WORST_REP = SA_ALGORITHM_0001(OF_FUNCTION, SETUP)
```
