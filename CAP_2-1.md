<h2>Simulated Annealing</h2>

Function: _**SA_ALGORITHM_0001**_

Example:
```python
import META


# Dados do problema
nrep = 1 # número de repetições
niter = 200 # número de iterações
npop = 1 # número de pop.
d = 2 # dimensões
sigma = 0.30 # desvio padrão
alpha = 0.98 # decaimento da temp
typeboot = 'UNIFORM'
xinf = [-1, -1] # lower bound
xsup = [1, 1] # upper bound

# função objetivo
def funcao_obj(X, NULL_DIC):
    X_0 = X[0]
    X_1 = X[1]
    of = X_0 ** 2 + X_1 ** 2
    # restrição
    return of

RESULTS_REP, BEST_REP, MEAN_REP, WORST_REP = META.SA_ALGORITHM_0001(funcao_obj, nrep, niter, npop, d, typeboot, xinf, xsup, sigma, alpha, STOP_CONTROL_TEMP = 100)


```
