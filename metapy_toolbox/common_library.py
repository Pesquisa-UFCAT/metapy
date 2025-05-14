"""Module has functions that are used in all metaheuristic algorithms"""
import numpy as np
import pandas as pd

from sklearn.model_selection import ParameterGrid
from copy import deepcopy
from typing import Any, Callable, List, Dict, Optional, Tuple, Union

def initial_population_01(n_population: int, n_dimensions: int, x_lower: List[float], x_upper: List[float], seed: Optional[int] = None) -> List[List[float]]:
    """  
    Generates a random population with defined limits. Continuum variables generator.
    
    :param n_population: Number of individuals in the population.
    :param n_dimensions: Number of dimensions (design variables).
    :param x_lower: Lower bounds for each variable.
    :param x_upper: Upper bounds for each variable.
    :param seed: Random seed. Use None for a random seed.

    :return: List of individuals, each represented as a list of real values.
    """
    # Set random seed
    if seed is None:
        pass
    else:
        np.random.seed(seed)

    # Random variable generator
    x_pop = []
    for _ in range(n_population):
        aux = []
        for j in range(n_dimensions):
            random_number = np.random.random()
            value_i_dimension = x_lower[j] + (x_upper[j] - x_lower[j]) * random_number
            aux.append(value_i_dimension)
        x_pop.append(aux)

    return x_pop


def initial_population_02(n_population: int, n_dimensions: int, seed: Optional[int] = None) -> List[List[int]]:
    """  
    The function generates a random population. Combinatorial variables generator.
    
    :param n_population: Number of individuals in the population.
    :param n_dimensions: Number of elements in each permutation.
    :param seed: Random seed. Use None for a random seed.

    :return: List of individuals, each represented as a list of integers (permutation).
    """
    # Set random seed
    if seed is None:
        pass
    else:
        np.random.seed(seed)

    # Random variable generator
    nodes = list(range(n_dimensions))
    x_pop = [list(np.random.permutation(nodes)) for _ in range(n_population)]

    return x_pop


def initial_pops(n_repetitions: int, n_population: int, n_dimensions: int, x_lower: Optional[List[float]], x_upper: Optional[List[float]], type_pop: str, seeds: Optional[List[Optional[int]]]) -> List[List[List[float]]]:
    """
    This function randomly initializes a population of the metaheuristic algorithm for a given number of repetitions.
    
    :param n_repetitions: Number of repetitions to generate populations.
    :param n_population: Number of individuals per population.
    :param n_dimensions: Number of dimensions or problem size.
    :param x_lower: Lower bounds for real-coded variables. Use None for combinatorial problems.
    :param x_upper: Upper bounds for real-coded variables. Use None for combinatorial problems.
    :param type_pop: Type of encoding. Options: 'real code' or 'combinatorial code'.
    :param seeds: List of seeds (one per repetition). Use None for random seed.

    :return: List of populations for each repetition.
    """
    # Set random seed
    population = []
    # Random variable generator
    if type_pop.upper() == 'REAL CODE':
        for i in range(n_repetitions):
            if seeds[i] is None:
                population.append(initial_population_01(n_population, n_dimensions,
                                                        x_lower, x_upper))
            else:
                population.append(initial_population_01(n_population, n_dimensions,
                                                        x_lower, x_upper,
                                                        seed=seeds[i]))
    elif type_pop.upper() == 'COMBINATORIAL CODE':
        for i in range(n_repetitions):
            if seeds[i] is None:
                population.append(initial_population_02(n_population, n_dimensions))
            else:
                population.append(initial_population_02(n_population, n_dimensions,
                                                        seed=seeds[i]))

    return population


def fit_value(of_i_value: float) -> float:
    """ 
    This function calculates the fitness of the i agent.
    
    :param of_i_value: Objective function value of the i-th agent.

    :return: Fitness value of the i-th agent.
    """

    # Positive or zero OF value
    if of_i_value >= 0:
        fit_i_value = 1 / (1 + of_i_value)
    # Negative OF value
    elif of_i_value < 0:
        fit_i_value = 1 + abs(of_i_value)

    return fit_i_value


def check_interval_01(x_i_old: List[float], x_lower: List[float], x_upper: List[float]) -> List[float]:
    """
    This function checks if a design variable is out of the limits established x_ lower and x_ upper and updates the variable if necessary.
    
    :param x_i_old: Current design variables of the i-th agent.
    :param x_lower: Lower bounds for the design variables.
    :param x_upper: Upper bounds for the design variables.

    :return: Corrected design variables within specified bounds.
    """

    aux = np.clip(x_i_old, x_lower, x_upper)
    x_i_new = aux.tolist()

    return x_i_new


def best_values(x_pop: List[List[float]], of_pop: List[float], fit_pop: List[float]) -> tuple:
    """ 
    This function determines the best, best id, worst particle and worst id. It also determines the average value (OF and FIT) of the population.

    :param x_pop: Population of design variables.
    :param of_pop: Objective function values for each individual.
    :param fit_pop: Fitness values for each individual.

    :return: Tuple containing:

        - best_id: Index of the best individual.
        - worst_id: Index of the worst individual.
        - x_best: Design variables of the best individual.
        - x_worst: Design variables of the worst individual.
        - of_best: Best objective function value.
        - of_worst: Worst objective function value.
        - fit_best: Best fitness value.
        - fit_worst: Worst fitness value.
        - of_avg: Average objective function value.
        - fit_avg: Average fitness value.
    """

    # Best and worst ID in population
    best_id = of_pop.index(min(of_pop))
    worst_id = of_pop.index(max(of_pop))

    # Global best values
    x_best = x_pop[best_id].copy()
    of_best = of_pop[best_id]
    fit_best = fit_pop[best_id]

    # Global worst values
    x_worst = x_pop[worst_id].copy()
    of_worst = of_pop[worst_id]
    fit_worst = fit_pop[worst_id]

    # Average values
    of_avg = sum(of_pop) / len(of_pop)
    fit_avg = sum(fit_pop) / len(fit_pop)

    return best_id, worst_id, x_best, x_worst, of_best, of_worst, \
            fit_best, fit_worst, of_avg, fit_avg


def id_selection(n_dimensions: int, n: int, k_dimension: Union[int, bool] = False) -> Tuple[np.ndarray, str]:
    """
    This function selects a k dimension from the all dimensions (uniform selection).
    
    :param n_dimensions: Total number of dimensions in the problem.
    :param n: Number of dimensions to select.
    :param k_dimension: Index to exclude from selection (default is False, meaning no exclusion).

    :return: Tuple containing:
    
        - selected: Array of selected dimension indices.
        - report: String report describing the selection process.
    """

    if k_dimension > 0:
        # Sum of the fitness values
        report_move = "    Selection dimension operator\n"
        pos = [int(c) for c in range(n_dimensions)]
        selection_probs = []

        # Fit probabilities
        tam = n_dimensions - 1
        for j in range(n_dimensions):
            if j == k_dimension:
                selection_probs.append(0.0)
            else:
                selection_probs.append(100/tam/100)

        # Selection
        report_move += f"    probs = {selection_probs}\n"
        selected = np.random.choice(pos, n, replace = False, p = selection_probs)
        report_move += f"    the selected dimensions = {selected}\n"
    else:
        # Sum of the fitness values
        report_move = "    Selection dimension operator\n"
        pos = [int(c) for c in range(n_dimensions)]
        selection_probs = []

        # Fit probabilities
        for j in range(n_dimensions):
            selection_probs.append(100/n_dimensions/100)

        # Selection
        report_move += f"    probs = {selection_probs}\n"
        selected = np.random.choice(pos, n, replace = False, p = selection_probs)
        report_move += f"    the selected dimensions = {selected}\n"

    return selected, report_move


def agent_selection(n_population: int, n: int, i_pop: Union[int, bool] = False) -> Tuple[np.ndarray, str]:
    """
    Selects `n` agents from a population using uniform selection, optionally excluding one agent.

    :param n_population: Total number of individuals in the population.
    :param n: Number of agents to select.
    :param i_pop: Index to exclude from selection. If False, no exclusion.

    :return: Tuple containing:

        - selected: Array of selected agent indices.
        - report: Textual report of the selection process.
    """

    if i_pop > 0:
        # Sum of the fitness values
        report_move = "    Selection population operator\n"
        pos = [int(c) for c in range(n_population)]
        selection_probs = []

        # Probabilities
        tam = n_population - 1
        for j in range(n_population):
            if j == i_pop:
                selection_probs.append(0.0)
            else:
                selection_probs.append(100/tam/100)

        # Selection
        report_move += f"    probs = {selection_probs}\n"
        selected = np.random.choice(pos, n, replace = False, p = selection_probs)
        report_move += f"    the selected agents = {selected}\n"
    else:
        # Sum of the fitness values
        report_move = "    Selection population operator\n"
        pos = [int(c) for c in range(n_population)]
        selection_probs = []

        # Probabilities
        for j in range(n_population):
            selection_probs.append(100/n_population/100)

        # Selection
        report_move += f"    probs = {selection_probs}\n"
        selected = np.random.choice(pos, n, replace = False, p = selection_probs)
        report_move += f"    the selected agents = {selected}\n"

    return selected, report_move


def convert_continuous_discrete(x: List[float], discrete_dataset: Dict[str, List[Union[int, float]]]) -> List[Union[int, float]]:
    """
    This function converts a continuous variable into a discrete variable according to a discrete dataset.

    :param x: Continuous design variables of the i-th agent.
    :param discrete_dataset: Dictionary containing discrete mappings (e.g., {'x_0': [...], 'x_1': [...]}).

    :return: List of converted design variables.
    """

    # Converting variables
    x_converted = []
    for k, x_k in enumerate(x):
        key = f'x_{k}'
        if key in discrete_dataset:
            aux = round(x_k)
            x_converted.append(discrete_dataset[key][aux])
        else:
            x_converted.append(x_k)

    return x_converted


def mutation_01_hill_movement(obj_function: Callable, x_i_old: List[float], x_lower: List[float], x_upper: List[float], n_dimensions: int, pdf: str, cov: float, none_variable: Optional[object] = None) -> Tuple[List[float], float, float, int, str]:
    """ 
    This function mutates a solution using a Gaussian or Uniform distribution. Hill Climbing movement.

    :param obj_function: Objective function defined by the user.
    :param x_i_old: Current design variables of the i-th agent.
    :param x_lower: Lower bounds for each variable.
    :param x_upper: Upper bounds for each variable.
    :param n_dimensions: Problem dimensionality.
    :param pdf: Probability density function. Options: 'gaussian' or 'uniform'.
    :param cov: Coefficient of variation (in %).
    :param none_variable: Optional variable to pass to the objective function.

    :return: Tuple containing:

        - x_i_new: Mutated design variables.
        - of_i_new: Objective function value of the new solution.
        - fit_i_new: Fitness value of the new solution.
        - neof: Number of function evaluations (1).
        - report_move: Mutation process report string.
    """
    # Start internal variables
    x_i_new = []

    # Particle movement - Gaussian distribution or Uniform distribution
    report_move = ""
    report_move += f"    current x = {x_i_old}\n"
    for i in range(n_dimensions):
        mean_value = x_i_old[i]
        sigma_value = abs(mean_value * cov / 100)
        if pdf.upper() == 'GAUSSIAN' or pdf.upper() == 'NORMAL':
            s = np.random.normal(0, sigma_value, 1)
        elif pdf.upper() == 'UNIFORM':
            s = np.random.uniform(0 - sigma_value, 0 + sigma_value, 1)
        neighbor = x_i_old[i] + s[0]
        x_i_new.append(neighbor)
        report_move += f"    Dimension {i}: mean = {mean_value}, sigma = {sigma_value}, neighbor = {neighbor}\n"

    # Check bounds
    x_i_new = check_interval_01(x_i_new, x_lower, x_upper)

    # Evaluation of the objective function and fitness
    of_i_new = obj_function(x_i_new, none_variable)
    fit_i_new = fit_value(of_i_new)
    report_move += f"    update x = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"
    neof = 1

    return x_i_new, of_i_new, fit_i_new, neof, report_move


def mutation_02_chaos_movement(obj_function: Callable, x_i_old: List[float], of_i_old: float, fit_i_old: float, x_lower: List[float], x_upper: List[float], n_dimensions: int, alpha: float, n_tries: int, iteration: int, n_iter: int, none_variable: Optional[object] = None) -> Tuple[List[float], float, float, int, str]:
    """ 
    This function mutates a solution using a chaotic maps.
    
    :param obj_function: User-defined objective function.
    :param x_i_old: Current design variables of the i-th agent.
    :param of_i_old: Objective function value of the current solution.
    :param fit_i_old: Fitness value of the current solution.
    :param x_lower: Lower bounds for each variable.
    :param x_upper: Upper bounds for each variable.
    :param n_dimensions: Number of design variables.
    :param alpha: Chaos control parameter (commonly 4 for full chaos).
    :param n_tries: Number of attempts to generate better solutions.
    :param iteration: Current iteration number.
    :param n_iter: Total number of iterations.
    :param none_variable: Optional input to be passed to the objective function.

    :return: Tuple containing:

        - x_i_new: Updated design variables.
        - of_i_new: Updated objective function value.
        - fit_i_new: Updated fitness value.
        - neof: Number of objective function evaluations.
        - report_move: Textual report of the mutation process.
    """

    # Start internal variables
    fit_i_new = -1000
    report_move = ""

    # Particle movement - Chaotic map
    ch = np.random.uniform(low=0, high=1)
    for j in range(n_tries):
        if j == 0:
            fit_best = fit_i_old
            x_i_new = x_i_old.copy()
            of_i_new = of_i_old
        else:
            fit_best = fit_i_new
        x_i_temp = []
        report_move += f"    Try {j} -> current x = {x_i_new}, fit best = {fit_best}\n"
        for i in range(n_dimensions):
            chaos_value = x_lower[i] + (x_upper[i] - x_lower[i]) * ch
            epsilon = (n_iter-iteration+1) / n_iter
            g_best = (1-epsilon)*x_i_old[i] + epsilon*chaos_value
            x_i_temp.append(g_best)
            report_move += f"    Dimension {i}: epsilon = {epsilon}, ch = {ch}, chaos value = {chaos_value}, neighbor = {g_best}\n"

        # Check bounds
        x_i_temp = check_interval_01(x_i_temp, x_lower, x_upper)

        # Evaluation of the objective function and fitness
        of_i_temp = obj_function(x_i_temp, none_variable)
        fit_i_temp = fit_value(of_i_temp)
        report_move += f"    temporary move x = {x_i_temp}, of = {of_i_temp}, fit = {fit_i_temp}\n"

        # New design variables
        if fit_i_temp > fit_best:
            report_move += f"    fit_i_temp {fit_i_temp} > fit_pop[pop] {fit_best} - accept this solution\n"
            x_i_new = x_i_temp.copy()
            of_i_new = of_i_temp
            fit_i_new = fit_i_temp
            report_move += f"    update x = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"
        else:
            report_move += f"    fit_i_temp {fit_i_temp} < fit_pop[pop] {fit_best} - not accept this solution\n"
            report_move += f"    update x = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"

        # Update chaos map
        ch = alpha*ch*(1-ch)

    # Update number of evaluations of the objective function
    neof = n_tries

    return x_i_new, of_i_new, fit_i_new, neof, report_move


def mutation_03_de_movement(obj_function: Callable, x_r0_old: List[float], x_r1_old: List[float], x_r2_old: List[float], x_lower: List[float], x_upper: List[float], n_dimensions: int, f: float, none_variable: Optional[object] = None) -> Tuple[List[float], float, float, int, str]:
    """ 
    This function mutates a solution using a differential evolution mutation (rand/1).
    
    See the `original documentation for more details <https://sci-hub.se/https://doi.org/10.1007/978-3-319-07173-2_32>`_.
    
    
    :param obj_function: User-defined objective function.
    :param x_r0_old: Design variables of the base (r0) vector.
    :param x_r1_old: Design variables of the r1 vector.
    :param x_r2_old: Design variables of the r2 vector.
    :param x_lower: Lower bounds for each variable.
    :param x_upper: Upper bounds for each variable.
    :param n_dimensions: Number of design variables.
    :param f: Scaling factor.
    :param none_variable: Optional input to be passed to the objective function.

    :return: Tuple containing:

        - x_i_new: New mutated solution.
        - of_i_new: Objective function value of the new solution.
        - fit_i_new: Fitness value of the new solution.
        - neof: Number of objective function evaluations (1).
        - report_move: Mutation log text.
    """

    # Start internal variables
    x_i_new = []

    # Particle movement - DE mutation movement (rand/1)
    report_move = ""
    report_move += f"    current xr0 = {x_r0_old}\n"
    report_move += f"    current xr1 = {x_r1_old}\n"
    report_move += f"    current xr2 = {x_r2_old}\n"
    for i in range(n_dimensions):
        r_ij = x_r1_old[i]-x_r2_old[i]
        v = x_r0_old[i] + f*r_ij
        x_i_new.append(v)
        report_move += f"    Dimension {i}: rij = {r_ij}, neighbor = {v}\n"

    # Check bounds
    x_i_new = check_interval_01(x_i_new, x_lower, x_upper)

    # Evaluation of the objective function and fitness
    of_i_new = obj_function(x_i_new, none_variable)
    fit_i_new = fit_value(of_i_new)
    report_move += f"    update x = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"
    neof = 1

    return x_i_new, of_i_new, fit_i_new, neof, report_move    


def mutation_04_de_movement(obj_function: Callable, x_r0_old: List[float], x_r1_old: List[float], x_r2_old: List[float], x_r3_old: List[float], x_r4_old: List[float], x_lower: List[float], x_upper: List[float], n_dimensions: int, f: float, none_variable: Optional[object] = None) -> Tuple[List[float], float, float, int, str]:
    """ 
    This function mutates a solution using a differential evolution mutation (rand/2).
    
    :param obj_function: User-defined objective function.
    :param x_r0_old: Design variables of the base (r0) vector.
    :param x_r1_old: Design variables of the r1 vector.
    :param x_r2_old: Design variables of the r2 vector.
    :param x_r3_old: Design variables of the r3 vector.
    :param x_r4_old: Design variables of the r4 vector.
    :param x_lower: Lower bounds for each variable.
    :param x_upper: Upper bounds for each variable.
    :param n_dimensions: Number of design variables.
    :param f: Scaling factor.
    :param none_variable: Optional input to be passed to the objective function.

    :return: Tuple containing:

        - x_i_new: New mutated solution.
        - of_i_new: Objective function value of the new solution.
        - fit_i_new: Fitness value of the new solution.
        - neof: Number of objective function evaluations (1).
        - report_move: Mutation log text.
    """

    # Start internal variables
    x_i_new = []

    # Particle movement - DE mutation movement (rand/2)
    report_move = ""
    report_move += f"    current xr0 = {x_r0_old}\n"
    report_move += f"    current xr1 = {x_r1_old}\n"
    report_move += f"    current xr2 = {x_r2_old}\n"
    report_move += f"    current xr3 = {x_r3_old}\n"
    report_move += f"    current xr4 = {x_r4_old}\n"
    for i in range(n_dimensions):
        r_ij_1 = x_r1_old[i] - x_r2_old[i]
        r_ij_2 = x_r3_old[i] - x_r4_old[i]
        v = x_r0_old[i] + f*r_ij_1 + f*r_ij_2
        x_i_new.append(v)
        report_move += f"    Dimension {i}: rij_1 = {r_ij_1}, rij_2 = {r_ij_2}, neighbor = {v}\n"

    # Check bounds
    x_i_new = check_interval_01(x_i_new, x_lower, x_upper)

    # Evaluation of the objective function and fitness
    of_i_new = obj_function(x_i_new, none_variable)
    fit_i_new = fit_value(of_i_new)
    report_move += f"    update x = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"
    neof = 1

    return x_i_new, of_i_new, fit_i_new, neof, report_move


def mutation_05_de_movement(obj_function: Callable, x_r0_old: List[float], x_r1_old: List[float], x_best: List[float], x_lower: List[float], x_upper: List[float], n_dimensions: int, f: float, none_variable: Optional[object] = None) -> Tuple[List[float], float, float, int, str]:
    """ 
    This function mutates a solution using a differential evolution mutation (best/1).
    
    :param obj_function: User-defined objective function.
    :param x_r0_old: Design variables of random agent r0.
    :param x_r1_old: Design variables of random agent r1.
    :param x_best: Best design variables in the population.
    :param x_lower: Lower bounds for design variables.
    :param x_upper: Upper bounds for design variables.
    :param n_dimensions: Problem dimensionality.
    :param f: Scaling factor.
    :param none_variable: Optional argument passed to the objective function.

    :return: Tuple with:

        - x_i_new: New mutated solution.
        - of_i_new: Objective function value.
        - fit_i_new: Fitness value.
        - neof: Number of function evaluations.
        - report_move: Mutation process report.
    """

    # Start internal variables
    x_i_new = []

    # Particle movement - DE mutation movement (best/1)
    report_move = ""
    report_move += f"    current xr0 = {x_r0_old}\n"
    report_move += f"    current xr1 = {x_r1_old}\n"
    report_move += f"    current x_best = {x_best}\n"

    for i in range(n_dimensions):
        r_ij = x_r0_old[i] - x_r1_old[i]
        v = x_best[i] + f*r_ij
        x_i_new.append(v)
        report_move += f"    Dimension {i}: rij = {r_ij}, neighbor = {v}\n"

    # Check bounds
    x_i_new = check_interval_01(x_i_new, x_lower, x_upper)

    # Evaluation of the objective function and fitness
    of_i_new = obj_function(x_i_new, none_variable)
    fit_i_new = fit_value(of_i_new)
    report_move += f"    update x = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"
    neof = 1

    return x_i_new, of_i_new, fit_i_new, neof, report_move    


def mutation_06_de_movement(obj_function: Callable, x_r0_old: List[float], x_r1_old: List[float], x_r2_old: List[float], x_r3_old: List[float], x_best: List[float], x_lower: List[float], x_upper: List[float], n_dimensions: int, f: float, none_variable: Optional[object] = None) -> Tuple[List[float], float, float, int, str]:
    """ 
    This function mutates a solution using a differential evolution mutation (best/2).
    
    :param obj_function: User-defined objective function.
    :param x_r0_old: Design variables of random agent r0.
    :param x_r1_old: Design variables of random agent r1.
    :param x_r2_old: Design variables of random agent r2.
    :param x_r3_old: Design variables of random agent r3.
    :param x_best: Best design variables in the population.
    :param x_lower: Lower bounds for design variables.
    :param x_upper: Upper bounds for design variables.
    :param n_dimensions: Problem dimensionality.
    :param f: Scaling factor.
    :param none_variable: Optional argument passed to the objective function.

    :return: Tuple with:

        - x_i_new: New mutated solution.
        - of_i_new: Objective function value.
        - fit_i_new: Fitness value.
        - neof: Number of function evaluations.
        - report_move: Mutation process report.
    """

    # Start internal variables
    x_i_new = []

    # Particle movement - DE mutation movement (best/2)
    report_move = ""
    report_move += f"    current xr0 = {x_r0_old}\n"
    report_move += f"    current xr1 = {x_r1_old}\n"
    report_move += f"    current xr2 = {x_r2_old}\n"
    report_move += f"    current xr3 = {x_r3_old}\n"
    report_move += f"    current x_best = {x_best}\n"
    for i in range(n_dimensions):
        r_ij_1 = x_r0_old[i] - x_r1_old[i]
        r_ij_2 = x_r2_old[i] - x_r3_old[i]
        v = x_best[i] + f*r_ij_1 + f*r_ij_2
        x_i_new.append(v)
        report_move += f"    Dimension {i}: rij_1 = {r_ij_1}, rij_2 = {r_ij_2}, neighbor = {v}\n"

    # Check bounds
    x_i_new = check_interval_01(x_i_new, x_lower, x_upper)

    # Evaluation of the objective function and fitness
    of_i_new = obj_function(x_i_new, none_variable)
    fit_i_new = fit_value(of_i_new)
    report_move += f"    update x = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"
    neof = 1

    return x_i_new, of_i_new, fit_i_new, neof, report_move  


def mutation_07_de_movement(obj_function: Callable, x_i_old: List[float], x_r0_old: List[float], x_r1_old: List[float], x_r2_old: List[float], x_best: List[float], x_lower: List[float], x_upper: List[float], n_dimensions: int, f: float, none_variable: Optional[object] = None) -> Tuple[List[float], float, float, int, str]:
    """ 
    This function mutates a solution using a differential evolution mutation (current-to-best/1).
    
    :param obj_function: User-defined objective function.
    :param x_i_old: Current solution to mutate.
    :param x_r0_old: Design variables of random agent r0.
    :param x_r1_old: Design variables of random agent r1.
    :param x_r2_old: Design variables of random agent r2.
    :param x_best: Best design variables in the population.
    :param x_lower: Lower bounds for design variables.
    :param x_upper: Upper bounds for design variables.
    :param n_dimensions: Problem dimensionality.
    :param f: Scaling factor.
    :param none_variable: Optional argument passed to the objective function.

    :return: Tuple with:

        - x_i_new: New mutated solution.
        - of_i_new: Objective function value.
        - fit_i_new: Fitness value.
        - neof: Number of function evaluations.
        - report_move: Mutation process report.
    """

    # Start internal variables
    x_i_new = []

    # Particle movement - DE mutation movement (current-to-best/1)
    report_move = ""
    report_move += f"    current xi = {x_i_old}\n"
    report_move += f"    current xr0 = {x_r0_old}\n"
    report_move += f"    current xr1 = {x_r1_old}\n"
    report_move += f"    current xr2 = {x_r2_old}\n"
    report_move += f"    current x_best = {x_best}\n"
    for i in range(n_dimensions):
        r_ij_1 = x_best[i] - x_r0_old[i]
        r_ij_2 = x_r1_old[i] - x_r2_old[i]
        v = x_i_old[i] + f*r_ij_1 + f*r_ij_2 
        x_i_new.append(v)
        report_move += f"    Dimension {i}: rij_1 = {r_ij_1}, rij_2 = {r_ij_2}, neighbor = {v}\n"

    # Check bounds
    x_i_new = check_interval_01(x_i_new, x_lower, x_upper)

    # Evaluation of the objective function and fitness
    of_i_new = obj_function(x_i_new, none_variable)
    fit_i_new = fit_value(of_i_new)
    report_move += f"    update x = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"
    neof = 1

    return x_i_new, of_i_new, fit_i_new, neof, report_move  


def parametrizer_grid(param_grid: Dict[str, List[Any]], algorithm_setup: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Generates a list of algorithm setups by expanding the parameter grid into all combinations.

    :param param_grid: Dictionary with parameter names as keys and lists of values to try.
    :param algorithm_setup: Template dictionary where 'parametrizer' placeholders will be replaced.

    :return: List of algorithm setups with all parameter combinations applied.
    """
    # Generate all possible combinations of parameters
    param_combinations = list(ParameterGrid(param_grid))
    algorithm_setups_with_params = []
    
    for params in param_combinations:
        setup_copy = deepcopy(algorithm_setup)
        
        # Function to replace 'parametrizer' by the actual value
        def replace_parametrizer(obj, params):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if v == 'parametrizer' and k in params:
                        obj[k] = params[k] # Replace 'parametrizer' by the actual value
                    elif isinstance(v, (dict, list)):
                        replace_parametrizer(v, params)
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    if item == 'parametrizer' and i in params:
                        obj[i] = params[i]
                    elif isinstance(item, (dict, list)):
                        replace_parametrizer(item, params)

        replace_parametrizer(setup_copy, params)
        
        # Add the setup to the list
        if setup_copy not in algorithm_setups_with_params:
            algorithm_setups_with_params.append(setup_copy)
    
    return algorithm_setups_with_params


def resume_all_data_in_dataframe(x_i_pop: List[float], of_i_pop: float, fit_i_pop: float, columns: List[str], iteration: int) -> pd.DataFrame:
    """
    This function creates a dataframme with all values of the population.
    
    :param x_i_pop: Design variables of the agent.
    :param of_i_pop: Objective function value.
    :param fit_i_pop: Fitness value.
    :param columns: Column names for the resulting DataFrame.
    :param iteration: Iteration number.

    :return: DataFrame with solution and performance information.
    """
    # Dataframe creation
    aux = x_i_pop.copy()
    aux.append(of_i_pop)
    aux.append(fit_i_pop)
    aux.append(iteration)
    solution_list = [aux]
    i_pop_data = pd.DataFrame(solution_list, columns=columns)

    return i_pop_data


def resume_best_data_in_dataframe(x_pop: List[List[float]], of_pop: List[float], fit_pop: List[float], column_best: List[str], column_worst: List[str], other_columns: List[str], neof_count: int, iteration: int) -> tuple[pd.DataFrame, int]:
    """
    This function creates a dataframe with the best, worst and average values of the population.
    
    :param x_pop: List of design variables for the population.
    :param of_pop: Objective function values.
    :param fit_pop: Fitness values.
    :param column_best: Column names for the best individual.
    :param column_worst: Column names for the worst individual.
    :param other_columns: Column names for average and iteration tracking.
    :param neof_count: Number of function evaluations so far.
    :param iteration: Current iteration number.

    :return: Tuple containing:

        - data_resume: DataFrame with best, worst, and average data.
        - best_id: Index of the best individual.
    """

    # Best, average and worst values
    best_id, worst_id, x_best, x_worst, of_best, of_worst, fit_best,\
    fit_worst, of_avg, fit_avg = best_values(x_pop, of_pop, fit_pop)

    # Dataframe creation
    aux = x_best.copy()
    aux.append(of_best)
    aux.append(fit_best)
    aux.append(best_id)
    best_solution = pd.DataFrame([aux], columns = column_best)
    aux = x_worst.copy()
    aux.append(of_worst)
    aux.append(fit_worst)
    aux.append(worst_id)
    worst_solution = pd.DataFrame([aux], columns = column_worst)
    avg_solution = pd.DataFrame([[of_avg, fit_avg, iteration, neof_count]], columns = other_columns)
    data_resume = pd.concat([best_solution, worst_solution, avg_solution], axis = 1)

    return data_resume, best_id


def summary_analysis(df_best_results: List[pd.DataFrame]) -> int:
    """
    This function searches for the best result in result list.

    :param df_best_results: List of DataFrames containing best results for each repetition.

    :return: Index of the repetition with the lowest final objective function value.
    """
    min_of = float('inf')
    id_min_of = None
    for index, df in enumerate(df_best_results):
        last_line = df.iloc[-1]
        min_of_atual = last_line['OF BEST']
        if min_of_atual < min_of:
            min_of = min_of_atual
            id_min_of = index

    return id_min_of


def quasi_oppositional_population_initialization(obj_function: Callable, n_pop: int, n_dimension: int, initial_pop: np.ndarray, x_lower: List[float], x_upper: List[float], none_variable: Optional[object] = None) -> np.ndarray:
    """
    Generates a quasi-oppositional population and selects the fittest individuals for the initial population.

    :param obj_function: User-defined objective function that evaluates a population matrix.
    :param n_pop: Number of individuals to select for the new population.
    :param n_dimension: Number of design variables (problem dimensionality).
    :param initial_pop: Initial population array (n_pop x n_dimension).
    :param x_lower: Lower bounds for each dimension.
    :param x_upper: Upper bounds for each dimension.
    :param none_variable: Optional additional argument passed to the objective function.

    :return: New population array (n_pop x n_dimension) containing the fittest individuals from the combined set.
    """
    quasi_oppositional = np.zeros((n_pop,n_dimension))
    
    for i in range(n_pop):
        for j in range(n_dimension):
            opo_ij = x_lower[j] + x_upper[j] - initial_pop[i][j]
            m_ij = (x_lower[j] + x_upper[j])/2
            
            if initial_pop[i][j] < m_ij:
                quasi_oppositional[i][j] = m_ij + (opo_ij - m_ij) * np.random.rand()
            
            else:
                quasi_oppositional[i][j] = opo_ij + (m_ij - opo_ij) * np.random.rand()
    
    # Check bounds
    quasi_oppositional = check_interval_01(quasi_oppositional, x_lower, x_upper)

    # Combines the initial population and the quasi-opposing populations 
    combined_population = np.concatenate((initial_pop, quasi_oppositional))

    # Evaluates the objective function for all individuals in the combined population    
    obj_values = obj_function(combined_population, none_variable)

    # Calculate fitness values ​​for all individuals in the combined population
    fit_new_pop = fit_value(obj_values)

    # Sorts the indices of individuals in the combined population based on fitness values ​​(in descending order)
    sorted_indices = np.argsort(fit_new_pop)[::-1]

    # Select the fittest individuals
    selected_indices = sorted_indices[:n_pop]

    # Use the selected indices to extract the fittest Np individuals as the new population P0
    new_pop = combined_population[selected_indices]

    
    return new_pop



