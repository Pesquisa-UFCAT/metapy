
<h2><b>Simulated Annealing</b></h2>

Function: _**SA_ALGORITHM_0001**_

<p align="justify">The user must always inform the method setup and the Objective Function that he wants to minimize. The OBJ function should always have an X list (design variables X = [1, 2, 3, 4, ..., N - 1, N) and a dictionary as input.</p>

Example:
```python
from META_TOOLBOX import SA_ALGORITHM_0001

# Data
nrep = 1                            # Number of repetitions
niter = 200                         # Number of iterations
npop = 1                            # Number of population
d = 2                               # Number of dimensions
sigma = 0.30                        # Standard deviation (SA internal parameter)
alpha = 0.98                        # Annealing schedule (linear decay)
typeboot = 'UNIFORM'                # Initial population distribution
xinf = [-1, -1]                     # Lower bound
xsup = [1, 1]                       # Upper bound

# Objective Function setup 
def OBJ(X, NULL_DIC):
    X_0 = X[0]
    X_1 = X[1]
    of = X_0 ** 2 + X_1 ** 2
    # restrição
    return of

RESULTS_REP, BEST_REP, MEAN_REP, WORST_REP = META.SA_ALGORITHM_0001(OBJ, nrep, niter, npop, d, typeboot, xinf, xsup, sigma, alpha, STOP_CONTROL_TEMP = 100)
```
