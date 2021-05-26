<h2><b>How to use</b></h2>

<p align="justify">To use one of the library's functions, it is necessary to import.</p>

Example:
```python
# import standard Simulated Annealing Optimization Algorithm
from META_TOOLBOX import SA_ALGORITHM_0001
```
Functions META_COMMON_LIBRARY:
- ```INITIAL_POPULATION```: This function initializes the population randomically between the limits X_L and X_U;
- ```FIT_VALUE```: This function calculates the fitness of a value of the Objective Function;
- ```CHECK_INTERVAL```: This function checks if a variable is out of the limits established X_L and X_U;
- ```BEST_VALUES```: This function determines the best and worst particle. it also determines the average value (OF and FIT) of the population;
- ```CONVERT_SI_TO_INCHES```: This function convert figure size meters to inches;
- ```SAVE_GRAPHIC```: This function save graphics on a specific path extensions options;
- ```META_PLOT_1```: This function print OF + FIT (2x1) chart about input dataset

Functions META:
- ```SA_ALGORITHM_0001```: Standard continuous simulated annealing algorithm;
