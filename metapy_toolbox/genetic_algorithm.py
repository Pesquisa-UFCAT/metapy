"""Genetic algorithm functions"""
import time

import pandas as pd
import numpy as np
from tqdm import tqdm

import metapy_toolbox.common_library as metapyco


def roulette_wheel_selection(fit_pop, i_pop):
    """
    This function selects a position from the population using the roulette wheel selection method.

    Args:
        fit_pop (List): Population fitness values.
        i_pop (Integer):  agent id.
    
    Returns:
        i_selected (Integer): selected agent id.
        report (String): Report about the roulette wheel selection process.
    """

    # Sum of the fitness values
    report_move = "    Selection operator\n"
    fit_pop_aux = fit_pop.copy()
    pos = [int(c) for c in range(len(fit_pop))]
    fit_pop_aux.pop(i_pop)
    maximumm = sum(fit_pop_aux)
    report_move += f"    sum(fit) = {maximumm}\n"
    selection_probs = []

    # Fit probabilities
    for j, value in enumerate(fit_pop):
        if j == i_pop:
            selection_probs.append(0.0)
        else:
            selection_probs.append(value/maximumm)

    # Selection
    report_move += f"    probs(fit) = {selection_probs}\n"
    selected = np.random.choice(pos, 1, replace=False, p=selection_probs)
    i_selected = list(selected)[0]
    report_move += f"    selected agent id = {i_selected}\n"

    return i_selected, report_move


def tournament_selection(fit, n_pop, i, runs):
    """
    This function selects a position from the population using the tournament selection method.

    Under construction
    """
    fit_new = list(fit.flatten())
    pos = [int(c) for c in list(np.arange(0, n_pop, 1, dtype=int))]
    del pos[i]
    del fit_new[i]
    points = [0 for c in range(n_pop)]
    for j in range(runs):
        selected_pos = np.random.choice(pos, 2, replace=False)
        selected_fit = [fit[selected_pos[0]], fit[selected_pos[1]]]
        if selected_fit[0][0] <= selected_fit[1][0]:
            win = selected_pos[1]
        elif selected_fit[0][0] > selected_fit[1][0]:
            win = selected_pos[0]
        points[win] += 1
    m = max(points)
    poss = [k for k in range(len(points)) if points[k] == m]
    selected = np.random.choice(poss, 1, replace=False)
    return selected[0]


def linear_crossover(of_function, parent_0, parent_1,\
                     n_dimensions, x_lower, x_upper, none_variable=None):
    """
    This function performs the linear crossover operator. 
    Three new points are generated from the two parent points (offspring).

    Args: 
        of_function (Py function (def)): Objective function. The Metapy user defined this function.
        parent_0 (List): First parent (Current design variables).
        parent_1 (List): Second parent (Current design variables).
        n_dimensions (Integer): Problem dimension.
        x_lower (List): Lower limit of the design variables.
        x_upper (List): Upper limit of the design variables.
        none_variable (None, list, float, dictionary, str or any): None variable. Default is None. 
                                        User can use this variable in objective function.

    Returns:
        x_i_new (List): Update variables of the i agent.
        of_i_new (Float): Update objective function value of the i agent.
        fit_i_new (Float): Update fitness value of the i agent.
        neof (Integer): Number of evaluations of the objective function.
        report (String): Report about the male movement process.    
    """

    # Start internal variables
    report_move = "    Crossover operator - Linear crossover\n"
    report_move += f"    current p0 = {parent_0}\n"
    report_move += f"    current p1 = {parent_1}\n"
    offspring_a = []
    offspring_b = []
    offspring_c = []

    # Movement
    for i in range(n_dimensions):
        alpha_a = 0.5*parent_0[i]
        beta_a = 0.5*parent_1[i]
        report_move += f"    Dimension {i}: alpha_a = {alpha_a}, beta_a = {beta_a}, neighbor_a = {alpha_a + beta_a}\n"
        offspring_a.append(alpha_a + beta_a)
        alpha_b = 1.5*parent_0[i]
        beta_b = 0.5*parent_1[i]
        report_move += f"    Dimension {i}: alpha_b = {alpha_b}, beta_b = {beta_b}, neighbor_b = {alpha_b - beta_b}\n"
        offspring_b.append(alpha_b - beta_b)
        alpha_c = 0.5*parent_0[i]
        beta_c = 1.5*parent_1[i]
        report_move += f"    Dimension {i}: alpha_c = {alpha_c}, beta_c = {beta_c}, neighbor_c = {-alpha_c + beta_c}\n"
        offspring_c.append(-alpha_c + beta_c)

    # Check bounds
    offspring_a = metapyco.check_interval_01(offspring_a, x_lower, x_upper)
    offspring_b = metapyco.check_interval_01(offspring_b, x_lower, x_upper)
    offspring_c = metapyco.check_interval_01(offspring_c, x_lower, x_upper)

    # Evaluation of the objective function and fitness
    of_offspring_a = of_function(offspring_a, none_variable)
    of_offspring_b = of_function(offspring_b, none_variable)
    of_offspring_c = of_function(offspring_c, none_variable)
    report_move += f"    offspring a = {offspring_a}, of_a {of_offspring_a}\n"
    report_move += f"    offspring b = {offspring_b}, of_b {of_offspring_b}\n"
    report_move += f"    offspring c = {offspring_c}, of_c {of_offspring_c}\n"
    neof = 3

    # min of the offspring
    list_of = [of_offspring_a, of_offspring_b, of_offspring_c]
    min_value = min(list_of)
    pos_min = list_of.index(min_value)
    if pos_min == 0:
        x_i_new = offspring_a.copy()
        of_i_new = of_offspring_a
    elif pos_min == 1:
        x_i_new = offspring_b.copy()
        of_i_new = of_offspring_b
    else:
        x_i_new = offspring_c.copy()
        of_i_new = of_offspring_c
    fit_i_new = metapyco.fit_value(of_i_new)
    report_move += f"    update x = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"

    return x_i_new, of_i_new, fit_i_new, neof, report_move


def blxalpha_crossover(of_function, parent_0, parent_1,\
                       n_dimensions, x_lower, x_upper, none_variable=None):
    """
    This function performs the blx-alpha crossover operator. 
    Two new points are generated from the two parent points (offspring).

    Args: 
        of_function (Py function (def)): Objective function. The Metapy user defined this function.
        parent_0 (List): Current design variables of the first parent.
        parent_1 (List): Current design variables of the second parent.
        n_dimensions (Integer): Problem dimension.
        x_lower (List): Lower limit of the design variables.
        x_upper (List): Upper limit of the design variables.
        none_variable (None, list, float, dictionary, str or any): None variable. Default is None. 
                                        User can use this variable in objective function.

    Returns:
        x_i_new (List): Update variables of the i agent.
        of_i_new (Float): Update objective function value of the i agent.
        fit_i_new (Float): Update fitness value of the i agent.
        neof (Integer): Number of evaluations of the objective function.
        report (String): Report about the male movement process.    
    """

    # Start internal variables
    report_move = "    Crossover operator - BLX-alpha\n"
    report_move += f"    current p0 = {parent_0}\n"
    report_move += f"    current p1 = {parent_1}\n"
    offspring_a = []
    offspring_b = []

    # Movement
    for i in range(n_dimensions):
        alpha = np.random.uniform(low=0, high=1)
        max_val = max(parent_0[i], parent_1[i])
        min_val = min(parent_0[i], parent_1[i])
        r_ij = np.abs(parent_0[i] - parent_1[i])
        report_move += f"    Dimension {i}: min_val = {min_val}, max_val = {max_val}, r_ij = {r_ij}\n"
        report_move += f"    neighbor_a = {min_val - alpha*r_ij}, neighbor_b = {max_val + alpha*r_ij}\n"
        offspring_a.append(min_val - alpha*r_ij)
        offspring_b.append(max_val + alpha*r_ij)

    # Check bounds
    offspring_a = metapyco.check_interval_01(offspring_a, x_lower, x_upper)
    offspring_b = metapyco.check_interval_01(offspring_b, x_lower, x_upper)

    # Evaluation of the objective function and fitness
    of_offspring_a = of_function(offspring_a, none_variable)
    of_offspring_b = of_function(offspring_b, none_variable)
    report_move += f"    offspring a = {offspring_a}, of_a {of_offspring_a}\n"
    report_move += f"    offspring b = {offspring_b}, of_b {of_offspring_b}\n"
    neof = 2

    # min of the offspring
    list_of = [of_offspring_a, of_offspring_b]
    min_value = min(list_of)
    pos_min = list_of.index(min_value)
    if pos_min == 0:
        x_i_new = offspring_a.copy()
        of_i_new = of_offspring_a
    elif pos_min == 1:
        x_i_new = offspring_b.copy()
        of_i_new = of_offspring_b
    fit_i_new = metapyco.fit_value(of_i_new)
    report_move += f"    update x = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"

    return x_i_new, of_i_new, fit_i_new, neof, report_move


def heuristic_crossover(of_function, parent_0, parent_1,\
                        n_dimensions, x_upper, x_lower, none_variable=None):
    """
    This function performs the heuristic crossover operator. 
    Two new points are generated from the two parent points (offspring).

    Args: 
        of_function (Py function (def)): Objective function. The Metapy user defined this function.
        parent_0 (List): Current design variables of the first parent.
        parent_1 (List): Current design variables of the second parent.
        n_dimensions (Integer): Problem dimension.
        x_lower (List): Lower limit of the design variables.
        x_upper (List): Upper limit of the design variables.
        none_variable (None, list, float, dictionary, str or any): None variable. Default is None. 
                                        User can use this variable in objective function.

    Returns:
        x_i_new (List): Update variables of the i agent.
        of_i_new (Float): Update objective function value of the i agent.
        fit_i_new (Float): Update fitness value of the i agent.
        neof (Integer): Number of evaluations of the objective function.
        report (String): Report about the male movement process.
    """

    # Start internal variables
    report_move = "    Crossover operator - Heuristic crossover\n"
    report_move += f"    current p0 = {parent_0}\n"
    report_move += f"    current p1 = {parent_1}\n"    
    offspring_a = []
    offspring_b = []

    # Movement
    for i in range(n_dimensions):
        r = np.random.uniform(low=0, high=1)
        offspring_a.append(parent_0[i] + r*(parent_0[i] - parent_1[i]))
        offspring_b.append(parent_1[i] + r*(parent_1[i] - parent_0[i]))
        report_move += f"    random number = {r}\n"
        report_move += f"    neighbor_a = {parent_0[i] + r*(parent_0[i] - parent_1[i])}, neighbor_b = {parent_1[i] + r*(parent_1[i] - parent_0[i])}\n"

    # Check bounds
    offspring_a = metapyco.check_interval_01(offspring_a, x_lower, x_upper)
    offspring_b = metapyco.check_interval_01(offspring_b, x_lower, x_upper)

    # Evaluation of the objective function and fitness
    of_offspring_a = of_function(offspring_a, none_variable)
    of_offspring_b = of_function(offspring_b, none_variable)
    report_move += f"    offspring a = {offspring_a}, of_a = {of_offspring_a}\n"
    report_move += f"    offspring b = {offspring_b}, of_b = {of_offspring_b}\n"
    neof = 2

    # min of the offspring
    list_of = [of_offspring_a, of_offspring_b]
    min_value = min(list_of)
    pos_min = list_of.index(min_value)
    if pos_min == 0:
        x_i_new = offspring_a.copy()
        of_i_new = of_offspring_a
    else:
        x_i_new = offspring_b.copy()
        of_i_new = of_offspring_b
    fit_i_new = metapyco.fit_value(of_i_new)
    report_move += f"    update pos = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"

    return x_i_new, of_i_new, fit_i_new, neof, report_move


def simulated_binary_crossover(of_function, parent_0, parent_1,\
                                eta_c, n_dimensions, x_upper, x_lower, none_variable=None):
    """
    This function performs the simulated binary crossover operator. 
    Two new points are generated from the two parent points (offspring).
        
    Args: 
        of_function (Py function (def)): Objective function. The Metapy user defined this function.
        parent_0 (List): Current design variables of the first parent.
        parent_1 (List): Current design variables of the second parent.
        eta_c (Float): Distribution index.
        n_dimensions (Integer): Problem dimension.
        x_lower (List): Lower limit of the design variables.
        x_upper (List): Upper limit of the design variables.
        none_variable (None, list, float, dictionary, str or any): None variable. Default is None. 
                                        User can use this variable in objective function.

    Returns:
        x_i_new (List): Update variables of the i agent.
        of_i_new (Float): Update objective function value of the i agent.
        fit_i_new (Float): Update fitness value of the i agent.
        neof (Integer): Number of evaluations of the objective function.
        report (String): Report about the male movement process.    
    """

    # Start internal variables
    report_move = "    Crossover operator - simulated binary crossover\n"
    report_move += f"    current p0 = {parent_0}\n"
    report_move += f"    current p1 = {parent_1}\n"    
    offspring_a = []
    offspring_b = []

    # Movement
    for i in range(n_dimensions):
        r = np.random.uniform(low=0, high=1)
        if r <= 0.5:
            beta = (2*r)**(1/(eta_c+1))
            report_move += f"    random number = {r} <= 0.50, beta = {beta}\n"
        else:
            beta = (1/(2*(1-r)))**(1/(eta_c+1))
            report_move += f"    random number = {r} > 0.50, beta = {beta}\n"
        neighbor_a = 0.5*((1+beta)*parent_0[i] + (1-beta)*parent_1[i])
        neighbor_b = 0.5*((1-beta)*parent_1[i] + (1+beta)*parent_0[i])
        offspring_a.append(neighbor_a)
        offspring_b.append(neighbor_b)
        report_move += f"    neighbor_a {neighbor_a}\n"
        report_move += f"    neighbor_b {neighbor_b}\n"

    # Check bounds
    offspring_a = metapyco.check_interval_01(offspring_a, x_lower, x_upper)
    offspring_b = metapyco.check_interval_01(offspring_b, x_lower, x_upper)

    # Evaluation of the objective function and fitness
    of_offspring_a = of_function(offspring_a, none_variable)
    of_offspring_b = of_function(offspring_b, none_variable)
    report_move += f"    offspring a = {offspring_a}, of_a = {of_offspring_a}\n"
    report_move += f"    offspring b = {offspring_b}, of_b = {of_offspring_b}\n"
    neof = 2

    # min of the offspring
    list_of = [of_offspring_a, of_offspring_b]
    min_value = min(list_of)
    pos_min = list_of.index(min_value)
    if pos_min == 0:
        x_i_new = offspring_a.copy()
        of_i_new = of_offspring_a
    else:
        x_i_new = offspring_b.copy()
        of_i_new = of_offspring_b
    fit_i_new = metapyco.fit_value(of_i_new)
    report_move += f"    update pos = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"

    return x_i_new, of_i_new, fit_i_new, neof, report_move


def arithmetic_crossover(of_function, parent_0, parent_1,\
                          n_dimensions, x_upper, x_lower, none_variable=None):
    """
    This function performs the arithmetic crossover operator. 
    Two new points are generated from the two parent points (offspring).

    Args: 
        of_function (Py function (def)): Objective function. The Metapy user defined this function.
        parent_0 (List): Current design variables of the first parent.
        parent_1 (List): Current design variables of the second parent.
        n_dimensions (Integer): Problem dimension.
        x_lower (List): Lower limit of the design variables.
        x_upper (List): Upper limit of the design variables.
        none_variable (None, list, float, dictionary, str or any): None variable. Default is None. 
                                        User can use this variable in objective function.

    Returns:
        x_i_new (List): Update variables of the i agent.
        of_i_new (Float): Update objective function value of the i agent.
        fit_i_new (Float): Update fitness value of the i agent.
        neof (Integer): Number of evaluations of the objective function.
        report (String): Report about the male movement process.    
    """

    # Start internal variables
    report_move = "    Crossover operator - Arithmetic crossover\n"
    report_move += f"    current p0 = {parent_0}\n"
    report_move += f"    current p1 = {parent_1}\n"    
    offspring_a = []
    offspring_b = []

    # Movement
    for i in range(n_dimensions):
        alpha = np.random.uniform(low=0, high=1)
        offspring_a.append(parent_0[i]*alpha + parent_1[i]*(1-alpha))
        offspring_b.append(parent_1[i]*alpha + parent_0[i]*(1-alpha))
        report_move += f"    neighbor_a = {parent_0[i]*alpha + parent_1[i]*(1-alpha)}, neighbor_b = {parent_1[i]*alpha + parent_0[i]*(1-alpha)}\n"

    # Check bounds
    offspring_a = metapyco.check_interval_01(offspring_a, x_lower, x_upper)
    offspring_b = metapyco.check_interval_01(offspring_b, x_lower, x_upper)

    # Evaluation of the objective function and fitness
    of_offspring_a = of_function(offspring_a, none_variable)
    of_offspring_b = of_function(offspring_b, none_variable)
    report_move += f"    offspring a = {offspring_a}, of_a = {of_offspring_a}\n"
    report_move += f"    offspring b = {offspring_b}, of_b = {of_offspring_b}\n"
    neof = 2
    # min of the offspring
    list_of = [of_offspring_a, of_offspring_b]
    min_value = min(list_of)
    pos_min = list_of.index(min_value)
    if pos_min == 0:
        x_i_new = offspring_a.copy()
        of_i_new = of_offspring_a
    else:
        x_i_new = offspring_b.copy()
        of_i_new = of_offspring_b
    fit_i_new = metapyco.fit_value(of_i_new)
    report_move += f"    update pos = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"

    return x_i_new, of_i_new, fit_i_new, neof, report_move


def laplace_crossover(of_function, parent_0, parent_1,\
                      mu, sigma, n_dimensions, x_upper,\
                      x_lower, none_variable=None):
    """
    This function performs the laplace crossover operator. 
    Two new points are generated from the two parent points (offspring).

    Args: 
        of_function (Py function (def)): Objective function. The Metapy user defined this function.
        parent_0 (List): Current design variables of the first parent.
        parent_1 (List): Current design variables of the second parent.
        mu (Float): location parameter.
        sigma (Float): scale parameter.
        n_dimensions (Integer): Problem dimension.
        x_lower (List): Lower limit of the design variables.
        x_upper (List): Upper limit of the design variables.
        none_variable (None, list, float, dictionary, str or any): None variable. Default is None. 
                                        User can use this variable in objective function.

    Returns:
        x_i_new (List): Update variables of the i agent.
        of_i_new (Float): Update objective function value of the i agent.
        fit_i_new (Float): Update fitness value of the i agent.
        neof (Integer): Number of evaluations of the objective function.
        report (String): Report about the male movement process.    
    """

    # Start internal variables
    report_move = "    Crossover operator - laplace crossover\n"
    report_move += f"    current p0 = {parent_0}\n"
    report_move += f"    current p1 = {parent_1}\n"    
    offspring_a = []
    offspring_b = []

    # Movement
    for i in range(n_dimensions):
        r = np.random.uniform(low=0, high=1)
        if r <= 0.5:
            beta = mu - sigma*np.log(r)
            report_move += f"    random number = {r} <= 0.50, beta = {beta}\n"
        else:
            beta = mu + sigma*np.log(r)
            report_move += f"    random number = {r} > 0.50, beta = {beta}\n"
        rij = np.abs(parent_0[i] - parent_1[i])
        neighbor_a = parent_0[i] + beta*rij
        neighbor_b = parent_1[i] + beta*rij
        offspring_a.append(neighbor_a)
        offspring_b.append(neighbor_b)
        report_move += f"    rij = {rij}, neighbor_a {neighbor_a}\n"
        report_move += f"    rij = {rij}, neighbor_b {neighbor_b}\n"

    # Check bounds
    offspring_a = metapyco.check_interval_01(offspring_a, x_lower, x_upper)
    offspring_b = metapyco.check_interval_01(offspring_b, x_lower, x_upper)

    # Evaluation of the objective function and fitness
    of_offspring_a = of_function(offspring_a, none_variable)
    of_offspring_b = of_function(offspring_b, none_variable)
    report_move += f"    offspring a = {offspring_a}, of_a = {of_offspring_a}\n"
    report_move += f"    offspring b = {offspring_b}, of_b = {of_offspring_b}\n"
    neof = 2

    # min of the offspring
    list_of = [of_offspring_a, of_offspring_b]
    min_value = min(list_of)
    pos_min = list_of.index(min_value)
    if pos_min == 0:
        x_i_new = offspring_a.copy()
        of_i_new = of_offspring_a
    else:
        x_i_new = offspring_b.copy()
        of_i_new = of_offspring_b
    fit_i_new = metapyco.fit_value(of_i_new)
    report_move += f"    update pos = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"

    return x_i_new, of_i_new, fit_i_new, neof, report_move


def uniform_crossover(of_function, parent_0, parent_1,\
                       n_dimensions, x_upper, x_lower, none_variable=None):
    """
    This function performs the uniform crossover operator. 
    Two new points are generated from the two parent points (offspring).

    Args: 
        of_function (Py function (def)): Objective function. The Metapy user defined this function.
        parent_0 (List): Current design variables of the first parent.
        parent_1 (List): Current design variables of the second parent.
        n_dimensions (Integer): Problem dimension.
        x_lower (List): Lower limit of the design variables.
        x_upper (List): Upper limit of the design variables.
        none_variable (None, list, float, dictionary, str or any): None variable. Default is None. 
                                        User can use this variable in objective function.

    Returns:
        x_i_new (List): Update variables of the i agent.
        of_i_new (Float): Update objective function value of the i agent.
        fit_i_new (Float): Update fitness value of the i agent.
        neof (Integer): Number of evaluations of the objective function.
        report (String): Report about the male movement process.    
    """

    # Start internal variables
    report_move = "    Crossover operator - uniform crossover\n"
    report_move += f"    current p0 = {parent_0}\n"
    report_move += f"    current p1 = {parent_1}\n"    
    offspring_a = []
    offspring_b = []

    # Movement
    for i in range(n_dimensions):
        r = np.random.uniform(low=0, high=1)
        if r < 0.5:
            offspring_a.append(parent_0[i])
            offspring_b.append(parent_1[i])
            report_move += f"    random number = {r} < 0.50\n"
            report_move += f"    cut parent_0 -> of_a {parent_0[i]}\n"
            report_move += f"    cut parent_1 -> of_b {parent_1[i]}\n"
        else:
            offspring_a.append(parent_1[i])
            offspring_b.append(parent_0[i])
            report_move += f"    random number = {r} >= 0.50\n"
            report_move += f"    cut parent_1 -> of_a {parent_1[i]}\n"
            report_move += f"    cut parent_0 -> of_b {parent_0[i]}\n"

    # Check bounds
    offspring_a = metapyco.check_interval_01(offspring_a, x_lower, x_upper)
    offspring_b = metapyco.check_interval_01(offspring_b, x_lower, x_upper)

    # Evaluation of the objective function and fitness
    of_offspring_a = of_function(offspring_a, none_variable)
    of_offspring_b = of_function(offspring_b, none_variable)
    report_move += f"    offspring a = {offspring_a}, of_a = {of_offspring_a}\n"
    report_move += f"    offspring b = {offspring_b}, of_b = {of_offspring_b}\n"
    neof = 2

    # min of the offspring
    list_of = [of_offspring_a, of_offspring_b]
    min_value = min(list_of)
    pos_min = list_of.index(min_value)
    if pos_min == 0:
        x_i_new = offspring_a.copy()
        of_i_new = of_offspring_a
    else:
        x_i_new = offspring_b.copy()
        of_i_new = of_offspring_b
    fit_i_new = metapyco.fit_value(of_i_new)
    report_move += f"    update pos = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"

    return x_i_new, of_i_new, fit_i_new, neof, report_move


def binomial_crossover(of_function, parent_0, parent_1,\
                       p_c, n_dimensions, x_upper, x_lower, none_variable=None):
    """
    This function performs the uniform crossover operator. 
    Two new points are generated from the two parent points (offspring).

    Args: 
        of_function (Py function (def)): Objective function. The Metapy user defined this function.
        parent_0 (List): Current design variables of the first parent.
        parent_1 (List): Current design variables of the second parent.
        p_c (Float): Crossover probability rate (% * 0.01).
        n_dimensions (Integer): Problem dimension.
        x_upper (List): Upper limit of the design variables.
        x_lower (List): Lower limit of the design variables.
        none_variable (None, list, float, dictionary, str or any): None variable. Default is None. 
                                        User can use this variable in objective function.

    Returns:
        x_i_new (List): Update variables of the i agent.
        of_i_new (Float): Update objective function value of the i agent.
        fit_i_new (Float): Update fitness value of the i agent.
        neof (Integer): Number of evaluations of the objective function.
        report (String): Report about movement process.    
    """

    # Start internal variables
    report_move = "    Crossover operator - uniform crossover\n"
    report_move += f"    current p0 = {parent_0}\n"
    report_move += f"    current p1 = {parent_1}\n"
    offspring_a = []
    offspring_b = []

    # Movement
    for i in range(n_dimensions):
        r = np.random.uniform(low=0, high=1)
        if r <= p_c:
            offspring_a.append(parent_0[i])
            offspring_b.append(parent_1[i])
            report_move += f"    random number = {r} < p_c = {p_c}\n"
            report_move += f"    cut parent_0 -> of_a {parent_0[i]}\n"
            report_move += f"    cut parent_1 -> of_b {parent_1[i]}\n"
        else:
            offspring_a.append(parent_1[i])
            offspring_b.append(parent_0[i])
            report_move += f"    random number = {r} >= 0.50\n"
            report_move += f"    cut parent_1 -> of_a {parent_1[i]}\n"
            report_move += f"    cut parent_0 -> of_b {parent_0[i]}\n"

    # Check bounds
    offspring_a = metapyco.check_interval_01(offspring_a, x_lower, x_upper)
    offspring_b = metapyco.check_interval_01(offspring_b, x_lower, x_upper)

    # Evaluation of the objective function and fitness
    of_offspring_a = of_function(offspring_a, none_variable)
    of_offspring_b = of_function(offspring_b, none_variable)
    report_move += f"    offspring a = {offspring_a}, of_a = {of_offspring_a}\n"
    report_move += f"    offspring b = {offspring_b}, of_b = {of_offspring_b}\n"
    neof = 2

    # min of the offspring
    list_of = [of_offspring_a, of_offspring_b]
    min_value = min(list_of)
    pos_min = list_of.index(min_value)
    if pos_min == 0:
        x_i_new = offspring_a.copy()
        of_i_new = of_offspring_a
    else:
        x_i_new = offspring_b.copy()
        of_i_new = of_offspring_b
    fit_i_new = metapyco.fit_value(of_i_new)
    report_move += f"    update pos = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"

    return x_i_new, of_i_new, fit_i_new, neof, report_move


def single_point_crossover(of_function, parent_0, parent_1, \
                            n_dimensions, x_upper, x_lower, none_variable=None):
    """
    This function performs the single point crossover operator. 
    Two new points are generated from the two parent points (offspring).

    Args: 
        of_function (Py function (def)): Objective function. The Metapy user defined this function.
        parent_0 (List): Current design variables of the first parent.
        parent_1 (List): Current design variables of the second parent.
        n_dimensions (Integer): Problem dimension.
        x_lower (List): Lower limit of the design variables.
        x_upper (List): Upper limit of the design variables.
        none_variable (None, list, float, dictionary, str or any): None variable. Default is None. 
                                        User can use this variable in objective function.

    Returns:
        x_i_new (List): Update variables of the i agent.
        of_i_new (Float): Update objective function value of the i agent.
        fit_i_new (Float): Update fitness value of the i agent.
        neof (Integer): Number of evaluations of the objective function.
        report (String): Report about the male movement process.    
    """

    # Start internal variables
    report_move = "    Crossover operator - Single point\n"
    report_move += f"    current p0 = {parent_0}\n"
    report_move += f"    current p1 = {parent_1}\n"

    # Movement
    pos = np.random.randint(1, n_dimensions)
    report_move += f"    cut position {pos}\n"
    offspring_a = np.append(parent_0[:pos], parent_1[pos:])
    report_move += f"    cut parent_0 -> of_a {parent_0[:pos]}\n"
    report_move += f"    cut parent_1 -> of_a {parent_1[pos:]}\n"
    offspring_b = np.append(parent_1[:pos], parent_0[pos:])
    report_move += f"    cut parent_1 -> of_b {parent_1[:pos]}\n"
    report_move += f"    cut parent_0 -> of_b {parent_0[pos:]}\n" 
    offspring_a = offspring_a.tolist()
    offspring_b = offspring_b.tolist()

    # Check bounds
    offspring_a = metapyco.check_interval_01(offspring_a, x_lower, x_upper)
    offspring_b = metapyco.check_interval_01(offspring_b, x_lower, x_upper)

    # Evaluation of the objective function and fitness
    of_offspring_a = of_function(offspring_a, none_variable)
    of_offspring_b = of_function(offspring_b, none_variable)
    report_move += f"    offspring a = {offspring_a}, of_a = {of_offspring_a}\n"
    report_move += f"    offspring b = {offspring_b}, of_b = {of_offspring_b}\n"
    neof = 2

    # min of the offspring
    list_of = [of_offspring_a, of_offspring_b]
    min_value = min(list_of)
    pos_min = list_of.index(min_value)
    if pos_min == 0:
        x_i_new = offspring_a.copy()
        of_i_new = of_offspring_a
    else:
        x_i_new = offspring_b.copy()
        of_i_new = of_offspring_b
    fit_i_new = metapyco.fit_value(of_i_new)
    report_move += f"    update n_dimensions = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"

    return x_i_new, of_i_new, fit_i_new, neof, report_move


def multi_point_crossover(of_function, parent_0, parent_1,\
                           n_dimensions, x_upper, x_lower, none_variable=None):
    """
    This function performs the multi point crossover operator. 
    Two new points are generated from the two parent points (offspring).

    Args: 
        of_function (Py function (def)): Objective function. The Metapy user defined this function.
        parent_0 (List): Current design variables of the first parent.
        parent_1 (List): Current design variables of the second parent.
        n_dimensions (Integer): Problem dimension.
        x_lower (List): Lower limit of the design variables.
        x_upper (List): Upper limit of the design variables.
        none_variable (None, list, float, dictionary, str or any): None variable. Default is None. 
                                        User can use this variable in objective function.

    Returns:
        x_i_new (List): Update variables of the i agent.
        of_i_new (Float): Update objective function value of the i agent.
        fit_i_new (Float): Update fitness value of the i agent.
        neof (Integer): Number of evaluations of the objective function.
        report (String): Report about the male movement process.    
    """

    # Start internal variables
    report_move = "    Crossover operator - multi point crossover\n"
    report_move += f"    current p0 = {parent_0}\n"
    report_move += f"    current p1 = {parent_1}\n"
    offspring_a = []
    offspring_b = []

    # Movement
    pos = [int(c+1) for c in range(n_dimensions)]
    probs = [100/n_dimensions/100 for c in range(n_dimensions)]
    number_cuts = np.random.choice(pos, 1, replace=False, p=probs)[0]
    point_cuts = np.random.choice(n_dimensions, size=number_cuts, replace=False)
    mask = [0 for _ in range(n_dimensions)]
    for p in point_cuts:
        mask[p] = 1
    report_move += f"    cut mask = {mask}\n"
    for j in mask:
        if j == 0:
            offspring_a.append(parent_0[j])
            offspring_b.append(parent_1[j])
        else:
            offspring_a.append(parent_1[j])
            offspring_b.append(parent_0[j])

    # Check bounds
    offspring_a = metapyco.check_interval_01(offspring_a, x_lower, x_upper)
    offspring_b = metapyco.check_interval_01(offspring_b, x_lower, x_upper)

    # Evaluation of the objective function and fitness
    of_offspring_a = of_function(offspring_a, none_variable)
    of_offspring_b = of_function(offspring_b, none_variable)
    report_move += f"    offspring a = {offspring_a}, of_a = {of_offspring_a}\n"
    report_move += f"    offspring b = {offspring_b}, of_b = {of_offspring_b}\n"
    neof = 2

    # min of the offspring
    list_of = [of_offspring_a, of_offspring_b]
    min_value = min(list_of)
    pos_min = list_of.index(min_value)
    if pos_min == 0:
        x_i_new = offspring_a.copy()
        of_i_new = of_offspring_a
    else:
        x_i_new = offspring_b.copy()
        of_i_new = of_offspring_b
    fit_i_new = metapyco.fit_value(of_i_new)
    report_move += f"    update pos = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"

    return x_i_new, of_i_new, fit_i_new, neof, report_move


def mp_crossover(chromosome_a, chromosome_b, seed, of_function, none_variable):
    """mp_crossover(chromosome_a, chromosome_b)

    Multi-point ordered crossover.

    Parameters
    ----------
    chromosome_a : ndarray
        Encoding of a solution (chromosome).
    chromosome_b : ndarray
        Encoding of a solution (chromosome).
    seed : int | None, optional
        Seed for pseudo-random numbers generation, by default None.

    Returns
    -------
    tuple[ndarray, ndarray]
        Tuple of chromosomes after crossover.
    https://providing.blogspot.com/2015/06/genetic-algorithms-crossover.html?m=1
    https://medium.com/@samiran.bera/crossover-operator-the-heart-of-genetic-algorithm-6c0fdcb405c0
    """
    
    child_a = chromosome_a.copy()
    child_b = chromosome_b.copy()
    mask = np.random.RandomState(seed).randint(2, size=len(chromosome_a)) == 1
    child_a[~mask] = sorted(child_a[~mask], key=lambda x: np.where(chromosome_b == x))
    child_b[mask] = sorted(child_b[mask], key=lambda x: np.where(chromosome_a == x))
    
    of_offspring_a = of_function(child_a, none_variable)
    of_offspring_b = of_function(child_b, none_variable)
    neof = 2
    list_of = [of_offspring_a, of_offspring_b]
    min_value = min(list_of)
    pos_min = list_of.index(min_value)  
    if pos_min == 0:
        x_t1i = child_a.copy()
        of_t1i = of_offspring_a
    else:
        x_t1i = child_b.copy()
        of_t1i = of_offspring_b
    fit_t1i = metapyco.fit_value(of_t1i)

    return x_t1i, of_t1i, fit_t1i, neof


def mp_mutation(chromosome, seed, of_chro, of_function, none_variable):
    """mp_mutation(chromosome)

    Multi-point inversion mutation. A random mask encodes
    which elements will keep the original order or the
    reversed one.

    Parameters
    ----------
    chromosome : ndarray
        Encoding of a solution (chromosome).
    seed : int | None, optional
        Seed for pseudo-random numbers generation, by default None.

    Returns
    -------
    ndarray
        Returns the chromosome after mutation.
    """
    individual = chromosome.copy()
    mask = np.random.RandomState(seed).randint(2, size=len(individual)) == 1
    individual[~mask] = np.flip(individual[~mask])

    of_offspring_b = of_function(individual, none_variable)
    neof = 1
    list_of = [of_chro, of_offspring_b]
    min_value = min(list_of)
    pos_min = list_of.index(min_value)  
    if pos_min == 0:
        x_t1i = chromosome.copy()
        of_t1i = of_chro
    else:
        x_t1i = individual.copy()
        of_t1i = of_offspring_b
    fit_t1i = metapyco.fit_value(of_t1i)

    return x_t1i, of_t1i, fit_t1i, neof


def genetic_algorithm_01(settings):
    """
    Genetic algorithm 01.

    See documentation in https://wmpjrufg.github.io/METAPY/FRA_GA_GA.html
    
    Args:  
        settings (List): [0] setup, [1] initial population, [2] seeds.
        setup keys:
            'number of population' (Integer): number of population.
            'number of iterations' (Integer): number of iterations.
            'number of dimensions' (Integer): Problem dimension.
            'x pop lower limit' (List): Lower limit of the design variables.
            'x pop upper limit' (List): Upper limit of the design variables.
            'none_variable' (None, list, float, dictionary, str or any): None variable. Default is None. 
                                        User can use this variable in objective function.
            'objective function' (Py function (def)): Objective function. 
                                                The Metapy user defined this function.                                                
            'algorithm parameters' (Dictionary): Algorithm parameters. See documentation.
                'selection' (Dictionary): Selection parameters.
                'crossover' (Dictionary): Crossover parameters.
                'mutation'  (Dictionary): Mutation parameters.
        initial population (List or METApy function): Initial population.
        seed (None or integer): Random seed. Use None for random seed.
    
    Returns:
        df_all (Dataframe): All data of the population.
        df_best (Dataframe): Best data of the population.
        delta_time (Float): Time of the algorithm execution in seconds.
        report (String): Report of the algorithm execution.
    """

    # Setup config
    setup = settings[0]
    n_population = setup['number of population']
    n_iterations = setup['number of iterations']
    n_dimensions = setup['number of dimensions']
    x_lower = setup['x pop lower limit']
    x_upper = setup['x pop upper limit']
    none_variable = setup['none variable']
    obj_function = setup['objective function']
    seeds = settings[2]
    if seeds is None:
        pass
    else:
        np.random.seed(seeds)

    # Algorithm_parameters
    algorithm_parameters = setup['algorithm parameters']
    select_type = algorithm_parameters['selection']['type']
    crosso_type = algorithm_parameters['crossover']['type']
    mutati_type = algorithm_parameters['mutation']['type']
    p_c = algorithm_parameters['crossover']['crossover rate (%)']/100
    p_m = algorithm_parameters['mutation']['mutation rate (%)']/100

    # Mutation control
    if mutati_type == 'hill climbing':
        std = algorithm_parameters['mutation']['cov (%)']
        pdf = algorithm_parameters['mutation']['pdf']

    # Crossover control
    if crosso_type == 'linear':
        pass
    elif crosso_type == 'blx-alpha':
        pass
    elif crosso_type == 'single point':
        pass
    elif crosso_type == 'multi point':
        pass
    elif crosso_type == 'uniform':
        pass
    elif crosso_type == 'heuristic':
        pass
    elif crosso_type == 'arithmetic':
        pass
    elif crosso_type == 'binomial':
        pass
    elif crosso_type == 'sbc':
        eta_c = algorithm_parameters['crossover']['eta_c']
    elif crosso_type == 'laplace':
        mu = algorithm_parameters['crossover']['loc']
        sigma = algorithm_parameters['crossover']['scale']

    # Selection control
    if select_type == 'roulette':
        pass


    # Creating variables in the iteration procedure
    of_pop = []
    fit_pop = []
    neof_count = 0

    # Storage values: columns names about dataset results
    columns_all_data = ['X_' + str(i) for i in range(n_dimensions)]
    columns_all_data.append('OF')
    columns_all_data.append('FIT')
    columns_all_data.append('ITERATION')
    columns_repetition_data = ['X_' + str(i) + '_BEST' for i in range(n_dimensions)]
    columns_repetition_data.append('OF BEST')
    columns_repetition_data.append('FIT BET')
    columns_repetition_data.append('ID BEST')
    columns_worst_data  = ['X_' + str(i)  + '_WORST' for i in range(n_dimensions)]
    columns_worst_data.append('OF WORST')
    columns_worst_data.append('FIT WORST')
    columns_worst_data.append('ID WORST')
    columns_other_data = ['OF AVG', 'FIT AVG', 'ITERATION', 'neof']
    report = "Genetic Algorithm 01- report \n\n"
    all_data_pop = []
    resume_result = []

    # Initial population and evaluation solutions
    report += "Initial population\n"
    x_pop = settings[1].copy()
    for i_pop in range(n_population):
        of_pop.append(obj_function(x_pop[i_pop], none_variable))
        fit_pop.append(metapyco.fit_value(of_pop[i_pop]))
        neof_count += 1
        i_pop_solution = metapyco.resume_all_data_in_dataframe(x_pop[i_pop], of_pop[i_pop],
                                                               fit_pop[i_pop], columns_all_data,
                                                               iteration=0)
        all_data_pop.append(i_pop_solution)

    # Best, average and worst values and storage
    repetition_data, best_id = metapyco.resume_best_data_in_dataframe(x_pop, of_pop, fit_pop,
                                                             columns_repetition_data,
                                                             columns_worst_data,
                                                             columns_other_data,
                                                             neof_count, iteration=0)
    resume_result.append(repetition_data)
    for i_pop in range(n_population):
        if i_pop == best_id:
            report += f'x{i_pop} = {x_pop[i_pop]}, of_pop {of_pop[i_pop]}, fit {fit_pop[i_pop]} - best solution\n'
        else:
            report += f'x{i_pop} = {x_pop[i_pop]}, of_pop {of_pop[i_pop]}, fit {fit_pop[i_pop]} \n'

    # Iteration procedure
    report += "\nIterations\n"
    progress_bar = tqdm(total=n_iterations, desc='Progress')
    for iter in range(n_iterations):
        report += f"\nIteration: {iter+1}\n"

        # Time markup
        initial_time = time.time()

        # Copy results
        x_temp = x_pop.copy()
        of_temp = of_pop.copy()
        fit_temp = fit_pop.copy()

        # Population movement
        for pop in range(n_population):
            report += f"Pop id: {pop} - particle movement\n"
            report += f"    current x = {x_temp[pop]}\n"

            # Selection
            if select_type == 'roulette':
                id_parent, report_mov = roulette_wheel_selection(fit_temp, pop)
            report += report_mov

            # Crossover
            if crosso_type == 'linear':
                random_value = np.random.uniform(low=0, high=1)
                if random_value <= p_c:
                    x_i_temp, of_i_temp,\
                        fit_i_temp, neof,\
                        report_mov = linear_crossover(obj_function,
                                                        x_temp[pop],
                                                        x_temp[id_parent],
                                                        n_dimensions,
                                                        x_lower,
                                                        x_upper,
                                                        none_variable)
                else:
                    x_i_temp = x_temp[pop].copy()
                    of_i_temp = of_temp[pop]
                    fit_i_temp = fit_temp[pop]
                    neof = 0
                    report += f"    No crossover r={random_value} > p_c={p_c} \n"
            elif crosso_type == 'blx-alpha':
                random_value = np.random.uniform(low=0, high=1)
                if random_value <= p_c:
                    x_i_temp, of_i_temp,\
                        fit_i_temp, neof,\
                        report_mov = blxalpha_crossover(obj_function,
                                                        x_temp[pop],
                                                        x_temp[id_parent],
                                                        n_dimensions,
                                                        x_lower,
                                                        x_upper,
                                                        none_variable)
                else:
                    x_i_temp = x_temp[pop].copy()
                    of_i_temp = of_temp[pop]
                    fit_i_temp = fit_temp[pop]
                    neof = 0
                    report += f"    No crossover r={random_value} > p_c={p_c} \n"
            elif crosso_type == 'single point':
                random_value = np.random.uniform(low=0, high=1)
                if random_value <= p_c:
                    x_i_temp, of_i_temp,\
                        fit_i_temp, neof,\
                        report_mov = single_point_crossover(obj_function,
                                                        x_temp[pop],
                                                        x_temp[id_parent],
                                                        n_dimensions,
                                                        x_lower,
                                                        x_upper,
                                                        none_variable)
                else:
                    x_i_temp = x_temp[pop].copy()
                    of_i_temp = of_temp[pop]
                    fit_i_temp = fit_temp[pop]
                    neof = 0
                    report += f"    No crossover r={random_value} > p_c={p_c} \n"
            elif crosso_type == 'multi point':
                random_value = np.random.uniform(low=0, high=1)
                if random_value <= p_c:
                    x_i_temp, of_i_temp,\
                        fit_i_temp, neof,\
                        report_mov = multi_point_crossover(obj_function,
                                                        x_temp[pop],
                                                        x_temp[id_parent],
                                                        n_dimensions,
                                                        x_lower,
                                                        x_upper,
                                                        none_variable)
                else:
                    x_i_temp = x_temp[pop].copy()
                    of_i_temp = of_temp[pop]
                    fit_i_temp = fit_temp[pop]
                    neof = 0
                    report += f"    No crossover r={random_value} > p_c={p_c} \n"
            elif crosso_type == 'uniform':
                random_value = np.random.uniform(low=0, high=1)
                if random_value <= p_c:
                    x_i_temp, of_i_temp,\
                        fit_i_temp, neof,\
                        report_mov = uniform_crossover(obj_function,
                                                        x_temp[pop],
                                                        x_temp[id_parent],
                                                        n_dimensions,
                                                        x_lower,
                                                        x_upper,
                                                        none_variable)
                else:
                    x_i_temp = x_temp[pop].copy()
                    of_i_temp = of_temp[pop]
                    fit_i_temp = fit_temp[pop]
                    neof = 0
                    report += f"    No crossover r={random_value} > p_c={p_c} \n"
            elif crosso_type == 'heuristic':
                random_value = np.random.uniform(low=0, high=1)
                if random_value <= p_c:
                    x_i_temp, of_i_temp,\
                        fit_i_temp, neof,\
                        report_mov = heuristic_crossover(obj_function,
                                                        x_temp[pop],
                                                        x_temp[id_parent],
                                                        n_dimensions,
                                                        x_lower,
                                                        x_upper,
                                                        none_variable)
                else:
                    x_i_temp = x_temp[pop].copy()
                    of_i_temp = of_temp[pop]
                    fit_i_temp = fit_temp[pop]
                    neof = 0
                    report += f"    No crossover r={random_value} > p_c={p_c} \n"
            elif crosso_type == 'binomial':
                x_i_temp, of_i_temp,\
                    fit_i_temp, neof,\
                    report_mov = binomial_crossover(obj_function,
                                                    x_temp[pop],
                                                    x_temp[id_parent],
                                                    p_c,
                                                    n_dimensions,
                                                    x_lower,
                                                    x_upper,
                                                    none_variable)
            elif crosso_type == 'arithmetic':
                random_value = np.random.uniform(low=0, high=1)
                if random_value <= p_c:
                    x_i_temp, of_i_temp,\
                        fit_i_temp, neof,\
                        report_mov = arithmetic_crossover(obj_function,
                                                        x_temp[pop],
                                                        x_temp[id_parent],
                                                        n_dimensions,
                                                        x_lower,
                                                        x_upper,
                                                        none_variable)
                else:
                    x_i_temp = x_temp[pop].copy()
                    of_i_temp = of_temp[pop]
                    fit_i_temp = fit_temp[pop]
                    neof = 0
                    report += f"    No crossover r={random_value} > p_c={p_c} \n"
            elif crosso_type == 'sbc':
                random_value = np.random.uniform(low=0, high=1)
                if random_value <= p_c:
                    x_i_temp, of_i_temp,\
                        fit_i_temp, neof,\
                        report_mov = simulated_binary_crossover(obj_function,
                                                        x_temp[pop],
                                                        x_temp[id_parent],
                                                        eta_c,
                                                        n_dimensions,
                                                        x_lower,
                                                        x_upper,
                                                        none_variable)
                else:
                    x_i_temp = x_temp[pop].copy()
                    of_i_temp = of_temp[pop]
                    fit_i_temp = fit_temp[pop]
                    neof = 0
                    report += f"    No crossover r={random_value} > p_c={p_c} \n"
            elif crosso_type == 'laplace':
                random_value = np.random.uniform(low=0, high=1)
                if random_value <= p_c:
                    x_i_temp, of_i_temp,\
                        fit_i_temp, neof,\
                        report_mov = laplace_crossover(obj_function,
                                                        x_temp[pop],
                                                        x_temp[id_parent],
                                                        mu,
                                                        sigma,
                                                        n_dimensions,
                                                        x_lower,
                                                        x_upper,
                                                        none_variable)
                else:
                    x_i_temp = x_temp[pop].copy()
                    of_i_temp = of_temp[pop]
                    fit_i_temp = fit_temp[pop]
                    neof = 0
                    report += f"    No crossover r={random_value} > p_c={p_c} \n"
            report += report_mov
            # Update neof (Number of Objective Function Evaluations)
            neof_count += neof

            # Mutation
            random_value = np.random.uniform(low=0, high=1)
            if random_value <= p_m:
                report += "    Mutation operator\n"
                if mutati_type == 'hill climbing':
                    x_i_temp, of_i_temp,\
                        fit_i_temp, neof,\
                        report_mov = metapyco.mutation_01_hill_movement(obj_function,
                                                                        x_i_temp,
                                                                        x_lower, x_upper,
                                                                        n_dimensions,
                                                                        pdf, std,
                                                                        none_variable)
                report += report_mov
                
                # Update neof (Number of Objective Function Evaluations)
                neof_count += neof
            else:
                report += f"    No mutation r={random_value} > p_m={p_m} \n"

            # New design variables
            if fit_i_temp > fit_pop[pop]:
                report += f"    fit_i_temp={fit_i_temp} > fit_pop[pop]={fit_pop[pop]} - accept this solution\n"
                x_pop[pop] = x_i_temp.copy()
                of_pop[pop] = of_i_temp
                fit_pop[pop] = fit_i_temp
            else:
                report += f"    fit_i_temp={fit_i_temp} < fit_pop[pop]={fit_pop[pop]} - not accept this solution\n"             
            i_pop_solution = metapyco.resume_all_data_in_dataframe(x_i_temp, of_i_temp,
                                                                   fit_i_temp,
                                                                   columns_all_data,
                                                                   iteration=iter+1)
            all_data_pop.append(i_pop_solution)

        # Best, average and worst values and storage
        repetition_data, best_id = metapyco.resume_best_data_in_dataframe(x_pop, of_pop, fit_pop,
                                                                columns_repetition_data,
                                                                columns_worst_data,
                                                                columns_other_data,
                                                                neof_count,
                                                                iteration=iter+1)
        resume_result.append(repetition_data)
        report += "update solutions\n"
        for i_pop in range(n_population):
            if i_pop == best_id:
                report += f'x{i_pop} = {x_pop[i_pop]}, of_pop {of_pop[i_pop]}, fit {fit_pop[i_pop]} - best solution\n'
            else:
                report += f'x{i_pop} = {x_pop[i_pop]}, of_pop {of_pop[i_pop]}, fit {fit_pop[i_pop]} \n'
        progress_bar.update()

    # Time markup
    end_time = time.time()
    delta_time = end_time - initial_time

    # Storage all values in DataFrame
    df_all = pd.concat(all_data_pop, ignore_index=True)

    # Storage best values in DataFrame
    df_best = pd.concat(resume_result, ignore_index=True)
    progress_bar.close()

    return df_all, df_best, delta_time, report
