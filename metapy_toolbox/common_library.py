"""Module has functions that are used in all metaheuristic algorithms"""
import numpy as np
import pandas as pd
from sklearn.model_selection import ParameterGrid
from copy import deepcopy

def initial_population_01(n_population, n_dimensions, x_lower, x_upper, seed=None):
    """  
    Generates a random population with defined limits. Continuum variables generator.
    
    Args:
        n_population (Integer): Number of population
        n_dimensions (Integer): Problem dimension
        x_lower (List): Lower limit of the design variables
        x_upper (List): Upper limit of the design variables
        seed (Integer or None): Random seed. Default is None. Use None for random seed
    
    Returns:
        x_pop (List): Population design variables
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


def initial_population_02(n_population, n_dimensions, seed=None):
    """  
    The function generates a random population. Combinatorial variables generator.
    
    Args:
        n_population (Integer): Number of population
        n_dimensions (Integer): Problem dimension
        seed (Integer or None): Random seed. Default is None
    
    Returns:
        x_pop (List): Population design variables
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


def initial_pops(n_repetitions, n_population, n_dimensions, x_lower, x_upper, type_pop, seeds):
    """
    This function randomly initializes a population of the metaheuristic algorithm for a given number of repetitions.
    
    Args:
        n_repetitions (Integer): Number of repetitions
        n_population (Integer): Number of population
        n_dimensions (Integer): Problem dimension
        x_lower (List or None): Lower limit of the design variables. Use None for combinatorial variables
        x_upper (List or None): Upper limit of the design variables. Use None for combinatorial variables
        type_pop (String): Type of population. Options: 'real code' or 'combinatorial code'. 'real code' call function initial_population_01 and 'combinatorial code' call function initial_population_02
        seeds (List or None): Random seed. Use None for random seed
    
    Returns:
        population (List): Population design variables. All repetitions
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


def fit_value(of_i_value):
    """ 
    This function calculates the fitness of the i agent.
    
    Args:
        of_i_value (Float): Object function value of the i agent
    
    Returns:
        fit_i_value (Float): Fitness value of the i agent
    """

    # Positive or zero OF value
    if of_i_value >= 0:
        fit_i_value = 1 / (1 + of_i_value)
    # Negative OF value
    elif of_i_value < 0:
        fit_i_value = 1 + abs(of_i_value)

    return fit_i_value


def check_interval_01(x_i_old, x_lower, x_upper):
    """
    This function checks if a design variable is out of the limits established x_ lower and x_ upper and updates the variable if necessary.
    
    Args:
        x_i_old (List): Current design variables of the i agent
        x_lower (List): Lower limit of the design variables
        x_upper (List): Upper limit of the design variables
    
    Returns:
        x_i_new (List): Update variables of the i agent
    """

    aux = np.clip(x_i_old, x_lower, x_upper)
    x_i_new = aux.tolist()

    return x_i_new


def best_values(x_pop, of_pop, fit_pop):
    """ 
    This function determines the best, best id, worst particle and worst id. It also determines the average value (OF and FIT) of the population.

    Args:
        x_pop (List): Population design variables
        of_pop (List): Population objective function values
        fit_pop (List): Population fitness values

    Returns:
        best_id (Integer): Best id in population
        worst_id (Integer): Worst id in population
        x_best (List): Best design variables in population
        x_worst (List): Worst design variables in population
        of_best (Float): Best objective function value in population
        of_worst (Float): Worst objective function value in population
        fit_best (Float): Best fitness value in population
        fit_worst (Float): Worst fitness value in population
        of_avg (Float): Average objective function value
        fit_avg (Float): Average fitness value
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


def id_selection(n_dimensions, n, k_dimension=False):
    """
    This function selects a k dimension from the all dimensions (uniform selection).
    
    Args:
        n_dimensions (Integer): Problem dimension
        n (Integer): Number of dimensions to select
        k_dimension (Integer or Boolean): Default is False (Selects n dimensions among all dimensions). k_dimension=Integer Selects n dimensions among all dimensions, excluding k dimension

    Returns:
        selected (List): selected dimensions
        report (String): Report about the selection process
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


def agent_selection(n_population, n, i_pop=False):
    """
    This function selects a n agents from all population (uniform selection).
    
    Args:
        n_population (Integer): Number of population
        n (Integer): Number of agents to select
        i_pop (Integer or Boolean): Default is False (Selects n agents among all population). i_pop=Integer Selects n agents among all population, excluding i_pop agent

    Returns:
        selected (List): Selected agents.
        report (String): Report about the selection process.
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


def convert_continuous_discrete(x, discrete_dataset):
    """
    This function converts a continuous variable into a discrete variable according to a discrete dataset.

    Args:
        x (List): Continuous design variables of the i agent
        discrete_dataset (Dictionary): Discrete dataset. Include the key 'x_k' where k is the dimension of the variable that the user wants to be assigned a value from a discrete list

    Returns:
        x_converted (List): Converted variables of the i agent
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


def mutation_01_hill_movement(obj_function, x_i_old, x_lower, x_upper, n_dimensions, pdf, cov, none_variable=None):
    """ 
    This function mutates a solution using a Gaussian or Uniform distribution. Hill Climbing movement.

    Args:
        obj_function (Py function (def)): Objective function. The Metapy user defined this function
        x_i_old (List): Current design variables of the i agent
        x_lower (List): Lower limit of the design variables
        x_upper (List): Upper limit of the design variables
        n_dimensions (Integer): Problem dimension
        pdf (String): Probability density function. Options: 'gaussian' or 'uniform'
        cov (Float): Coefficient of variation in percentage
        none_variable (None, list, float, dictionary, str or any): None variable. User can use this variable in objective function

    Returns:
        x_i_new (List): Update variables of the i agent
        of_i_new (Float): Update objective function value of the i agent
        fit_i_new (Float): Update fitness value of the i agent
        neof (Integer): Number of evaluations of the objective function.
        report_move (String): Report about the mutation process
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


def mutation_02_chaos_movement(obj_function, x_i_old, of_i_old, fit_i_old, x_lower, x_upper, n_dimensions, alpha, n_tries, iteration, n_iter, none_variable=None):
    """ 
    This function mutates a solution using a chaotic maps.
    
    Args:
        obj_function (Py function (def)): Objective function. The Metapy user defined this function
        x_i_old (List): Current design variables of the i agent
        of_i_old (Float): Current objective function value of the i agent
        fit_i_old (Float): Current fitness value of the i agent
        x_lower (List): Lower limit of the design variables
        x_upper (List): Upper limit of the design variables
        n_dimensions (Integer): Problem dimension
        alpha (Float): Chaotic map control parameter
        n_tries (Integer): Number of tries to find a better solution
        iteration (Integer): Current iteration number
        n_iter (Integer): Total number of iterations
        none_variable (None, list, float, dictionary, str or any): None variable. User can use this variable in objective function   

    Returns:
        x_i_new (List): Update variables of the i agent
        of_i_new (Float): Update objective function value of the i agent
        fit_i_new (Float): Update fitness value of the i agent
        neof (Integer): Number of evaluations of the objective function
        report_move (String): Report about the mutation process
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


def mutation_03_de_movement(obj_function, x_r0_old, x_r1_old, x_r2_old, x_lower, x_upper, n_dimensions, f, none_variable=None):
    """ 
    This function mutates a solution using a differential evolution mutation (rand/1).
    https://sci-hub.se/https://doi.org/10.1007/978-3-319-07173-2_32
    
    Args:
        obj_function (Py function (def)): Objective function. The Metapy user defined this function
        x_r0_old (List): Current design variables of the random r0 agent
        x_r1_old (List): Current design variables of the random r1 agent
        x_r2_old (List): Current design variables of the random r2 agent
        x_lower (List): Lower limit of the design variables
        x_upper (List): Upper limit of the design variables
        n_dimensions (Integer): Problem dimension
        f (Float): Scaling factor
        none_variable (None, list, float, dictionary, str or any): None variable. User can use this variable in objective function
    
    Returns:
        x_i_new (List): Update variables of the i agent
        of_i_new (Float): Update objective function value of the i agent
        fit_i_new (Float): Update fitness value of the i agent
        neof (Integer): Number of evaluations of the objective function
        report_move (String): Report about the mutation process
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


def mutation_04_de_movement(obj_function, x_r0_old, x_r1_old, x_r2_old, x_r3_old, x_r4_old, x_lower, x_upper, n_dimensions, f, none_variable=None):
    """ 
    This function mutates a solution using a differential evolution mutation (rand/2).
    
    Args:
        obj_function (Py function (def)): Objective function. The Metapy user defined this function
        x_r0_old (List): Current design variables of the random r0 agent
        x_r1_old (List): Current design variables of the random r1 agent
        x_r2_old (List): Current design variables of the random r2 agent
        x_r3_old (List): Current design variables of the random r3 agent
        x_r4_old (List): Current design variables of the random r4 agent
        x_lower (List): Lower limit of the design variables
        x_upper (List): Upper limit of the design variables
        n_dimensions (Integer): Problem dimension
        f (Float): Scaling factor
        none_variable (None, list, float, dictionary, str or any): None variable. User can use this variable in objective function

    Returns:
        x_i_new (List): Update variables of the i agent
        of_i_new (Float): Update objective function value of the i agent
        fit_i_new (Float): Update fitness value of the i agent
        neof (Integer): Number of evaluations of the objective function
        report_move (String): Report about the mutation process
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


def mutation_05_de_movement(obj_function, x_r0_old, x_r1_old, x_best, x_lower, x_upper, n_dimensions, f, none_variable=None):
    """ 
    This function mutates a solution using a differential evolution mutation (best/1).
    
    Args:
        obj_function (Py function (def)): Objective function. The Metapy user defined this function
        x_r0_old (List): Current design variables of the random r0 agent
        x_r1_old (List): Current design variables of the random r1 agent
        x_best (List): Best design variables from the population
        x_lower (List): Lower limit of the design variables
        x_upper (List): Upper limit of the design variables
        n_dimensions (Integer): Problem dimension
        f (Float): Scaling factor
        none_variable (None, list, float, dictionary, str or any): None variable. User can use this variable in objective function
    
    Returns:
        x_i_new (List): Update variables of the i agent
        of_i_new (Float): Update objective function value of the i agent
        fit_i_new (Float): Update fitness value of the i agent
        neof (Integer): Number of evaluations of the objective function
        report_move (String): Report about the mutation process
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


def mutation_06_de_movement(obj_function, x_r0_old, x_r1_old, x_r2_old, x_r3_old, x_best, x_lower, x_upper, n_dimensions, f, none_variable=None):
    """ 
    This function mutates a solution using a differential evolution mutation (best/2).
    
    Args:
        obj_function (Py function (def)): Objective function. The Metapy user defined this function
        x_r0_old (List): Current design variables of the random r0 agent
        x_r1_old (List): Current design variables of the random r1 agent
        x_r2_old (List): Current design variables of the random r2 agent
        x_r3_old (List): Current design variables of the random r3 agent
        x_best (List): Best design variables from the population
        x_lower (List): Lower limit of the design variables
        x_upper (List): Upper limit of the design variables
        n_dimensions (Integer): Problem dimension
        f (Float): Scaling factor
        none_variable (None, list, float, dictionary, str or any): None variable. User can use this variable in objective function

    Returns:
        x_i_new (List): Update variables of the i agent
        of_i_new (Float): Update objective function value of the i agent
        fit_i_new (Float): Update fitness value of the i agent
        neof (Integer): Number of evaluations of the objective function
        report_move (String): Report about the mutation process
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


def mutation_07_de_movement(obj_function, x_i_old, x_r0_old, x_r1_old, x_r2_old, x_best, x_lower, x_upper, n_dimensions, f, none_variable=None):
    """ 
    This function mutates a solution using a differential evolution mutation (current-to-best/1).
    
    Args:
        obj_function (Py function (def)): Objective function. The Metapy user defined this function
        x_i_old (List): Current design variables of the i agent
        x_r0_old (List): Current design variables of the random r0 agent
        x_r1_old (List): Current design variables of the random r1 agent
        x_r2_old (List): Current design variables of the random r2 agent
        x_best (List): Best design variables from the population
        x_lower (List): Lower limit of the design variables
        x_upper (List): Upper limit of the design variables
        n_dimensions (Integer): Problem dimension
        f (Float): Scaling factor
        none_variable (None, list, float, dictionary, str or any): None variable. User can use this variable in objective function

    Returns:
        x_i_new (List): Update variables of the i agent
        of_i_new (Float): Update objective function value of the i agent
        fit_i_new (Float): Update fitness value of the i agent
        neof (Integer): Number of evaluations of the objective function
        report_move (String): Report about the mutation process
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


def parametrizer_grid(param_grid, algorithm_setup):
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


def resume_all_data_in_dataframe(x_i_pop, of_i_pop, fit_i_pop, columns, iteration):
    """
    This function creates a dataframme with all values of the population.
    
    Args:
        x_i_pop (List): Design variables of the i agent
        of_i_pop (Float): Objective function value of the i agent
        fit_i_pop (Float): Fitness value of the i agent
        columns (List): Columns names about dataset results
        iteration (Integer): Current iteration number
    
    Returns:
        i_pop_data (Dataframe): Dataframe with all values of the i agent in j iteration
    """

    # Dataframe creation
    aux = x_i_pop.copy()
    aux.append(of_i_pop)
    aux.append(fit_i_pop)
    aux.append(iteration)
    solution_list = [aux]
    i_pop_data = pd.DataFrame(solution_list, columns=columns)

    return i_pop_data


def resume_best_data_in_dataframe(x_pop, of_pop, fit_pop, column_best, column_worst, other_columns, neof_count, iteration):
    """
    This function creates a dataframe with the best, worst and average values of the population.
    
    Args:
        x_pop (List): Population design variables
        of_pop (List): Population objective function values
        fit_pop (List): Population fitness values
        column_best (List): Columns names about dataset results
        column_worst (List): Columns names about dataset results
        other_columns (List): Columns names about dataset results
        neof_count (Integer): Number of evaluations of the objective function
        iteration (Integer): Current iteration number
    
    Returns:
        data_resume (Dataframe): Dataframe with the best, worst and average values of in j iteration 
        best_id (Integer): Best id in population
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


def summary_analysis(df_best_results):
    """
    This function searches for the best result in result list.

    Args:
        df_best_results (List): List with the best results of each repetition
    
    Returns:
        id_min_of (Integer): Best result id
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


def quasi_oppositional_population_initialization(obj_function, n_pop, n_dimension, initial_pop,  x_lower, x_upper, none_variable = None):
    """
    This function creates a diverse and balanced starting population.

    Args:
        obj_function (Py function (def)): Objective function. The Metapy user defined this function
        n_pop: population size
        n_dimension: dimension
        initial_pop: initial population
        x_lower: lower limit
        x_upper: upper limit

    Returns:
        of_quasi_oppositional (Float): Update objective function value
        
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



