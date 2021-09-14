<h1><i>How to use</i></h1>

<p align="justify">To use one of the library's functions, it is necessary to import.</p>

<h3><i>Optimization functions</i></h3>

Example: Call optimization algorithm and benchmark function.
```python
# import standard Simulated Annealing Optimization Algorithm
from META_TOOLBOX import SA_ALGORITHM_0001

# import sphere function (n-dimensional)
from META_TOOLBOX import SPHERE
```

Example: Using the optimization method after import of the funtcion
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

<p align="justify"> Optimization functions input. In the following all output variables are explained.</p>

- SETUP   
- OF_FUNCTION  

```SETUP```: Algorithm setup - Python dictionary 
> Tag contents in dictionary  
- ```N_REP```: Number of repetitions    
- ```N_ITER```: Number of iterations  
- ```N_POP```: Number of population   
- ```D```: Problem dimension   
- ```X_L```: Lower limit design variables  
- ```X_U```: Upper limit design variables  
- ```NULL_DIC```: Empty variable for the user to use in the obj. function 

```OF_FUNCTION```: External ```def``` user input this function in arguments 


Obs.: The algorithm's internal control parameters vary by method. Before using, check the example parameters of each optimization method. 

Choose the documentation for which algorithm you want to consul:
- [Standard Simulated Annealing Algorithm](https://wmpjrufg.github.io/META_TOOLBOX/CAP_3-1.html)
- Standard Firefly Algorithm **under development**


<p align="justify"> Optimization functions return results from the repetition / iterative process. In the following all output variables are explained.</p>

- xlsx repetition procedure in current folder  
- xlsx resume all repetitions in current folder  
- RESULTS_REP  
- BEST_REP  
- AVERAGE_REP  
- WORST_REP  
- STATUS 
  
```RESULTS_REP```: All results of the population movement - Python dictionary 
> Tag contents in dictionary  
- ```ID_PARTICLE```: i particle, 0 unitil (*N_POP - 1*)   
- ```X_POSITION```: *X* design variables movement of *i* particle (equals ID Partcile) per iteration  
- ```OF```: OF values of *i* particle (equals ID Partcile) per iteration 
- ```FIT```: Fitness values of *i* particle (equals ID Partcile) per iteration  
- ```???_PARAMETERS```: Internal parameters of the optimization method (In **SA** for example this tag stores temperature annealing schedule) per iteration  
- ```NEOF```: Number of objective function evaluations per iteration 

View results of second particle (**id: 1**):   
```python
print(RESULTS_REP[1])
```
Obs.: In Pyhton the internal counter start in zero value!   
  
```BEST_REP```: Best population results - Python dictionary 
> Tag contents in dictionary  
- ```ID_PARTICLE```: id best particle, 0 unitil (N_POP - 1)   
- ```X_POSITION```: *X* design variables movement of *i* particle (equals ID Partcile) per iteration
- ```OF```: OF values of *i* particle (equals ID Partcile) per iteration  
- ```FIT```: Fitness values of *i* particle (equals ID Partcile) per iteration  
- ```???_PARAMETERS```: Internal parameters of the optimization method (In **SA** for example this TAG stores Temperature annealing schedule) per iteration  
- ```NEOF```: Number of objective function evaluations per iteration  

View results of first repetition (**id: 0**):   
```python
print(BEST_REP[0])
```

```AVERAGE_REP```: Average OF and FIT results (Python dictionary) 
> Tag contents in dictionary  
- ```OF```: OF values of *i* particle (equals ID Partcile) per iteration  
- ```FIT```: Fitness values of *i* particle (equals ID Partcile) per iteration  
- ```NEOF```: Number of objective function evaluations per iteration  

View results of first repetition (**id: 0**):    
```python
print(AVERAGE_REP[0])
```

```WORST_REP```: Worst OF and FIT results - Python dictionary
> Tag contents in dictionary  
- ```OF```: OF values of *i* particle (equals ID Partcile) per iteration  
- ```FIT```: Fitness values of *i* particle (equals ID Partcile) per iteration  
- ```NEOF```: Number of objective function evaluations per iteration  

View results of first repetition (**id: 0**):    
```python
print(WORST_REP[0])
```

```STATUS```: Process repetition ID - from lowest OF value to highest OF value - Python list

View results:    
```python
print(STATUS)
```


