<h2><b>Simulated Annealing</b></h2>

Function: _**SA_ALGORITHM_0001**_

<p align="justify">The user must always inform the method setup and the Objective Function that he wants to minimize. The OBJ function should always have an X list (design variables X = [0, 1, 2, 3, ..., N_POP - 2, N_POP - 1) and a dictionary as input.</p>

<h3><b>Theory</b></h3>

<p align="justify">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>


<h3><b>How to use</b></h3>

<p align="justify">The simulated annealing function has the following input variables.</p>

- ```OF_FUNCTION```: External _def_ user input this function in arguments (Python ```def```);
- ```N_REP```: Number of repetitions (integer);
- ```N_ITER```: Number of iterations (integer);
- ```N_POP```: Number of population (integer);
- ```D```: Dimension problem (integer);
- ```TYPE_BOOT```: Type distribution start (string). Only accepts the value ```'UNIFORM'```. Example: ```TYPE_BOOT = 'UNIFORM'```;
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
from META_TOOLBOX import SA_ALGORITHM_0001

# Algorithm Setup
N_REP = 1                               # Number of repetitions
N_ITER = 200                            # Number of iterations
N_POP = 1                               # Number of population
D = 2                                   # Number of dimensions
SIGMA = 0.30                            # Standard deviation (SA internal parameter)
ALPHA = 0.98                            # Annealing schedule (linear decay)
TYPE_BOOT = 'UNIFORM'                   # Initial population distribution
X_L = [-1, -1]                          # Lower bound [X_0, X_1, X_2, ..., X_NPOP-2, X_NPOP-1]
X_U = [1, 1]                            # Upper bound [X_0, X_1, X_2, ..., X_NPOP-2, X_NPOP-1]

# Objective Function setup 
def OBJ(X, NULL_DIC):
    # Assigning X Design Variables
    X_0 = X[0]                          # Assigning the value of X_0
    X_1 = X[1]                          # Assigning the value of X_1
    # Obj. Function
    OF = X_0 ** 2 + X_1 ** 2            # OBJ function
    return OF

# Call SA Algorithm 
RESULTS_REP, BEST_REP, MEAN_REP, WORST_REP = SA_ALGORITHM_0001(OBJ, N_REP, N_ITER, N_POP, D, TYPE_BOOT, X_L, X_U, SIGMA, ALPHA, STOP_CONTROL_TEMP = 100)
```
