"""Genetic Algorithm related functions."""
from typing import Callable, Optional, Union, List, Dict, Tuple

import numpy as np
import pandas as pd

from metapy_toolbox import funcs

def roulette_wheel_selection(fit_pop: list, i_pop: int) -> tuple[int, str]:
    """
    This function selects a position from the population using the roulette wheel selection method.

    :param fit_pop: Population fitness values
    :param i_pop:   current agent in t time step

    :return: [0] = selected agent id, [1] = Report about the roulette wheel selection process.
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


def linear_crossover(parent_0: list, parent_1: list, x_lower: list, x_upper: list) -> tuple[list, list, list, str]:
    """
    This function performs the linear crossover operator. Three new points are generated from the two parent points (offspring).

    :param parent_0: First parent
    :param parent_1: Second parent
    :param x_lower: Lower limit of the design variables
    :param x_upper: Upper limit of the design variables

    :return: [0] = First offspring position, [1] = Second offspring position, [2] = Third offspring position, [3] = Report about the linear crossover process
    """

    # Start internal variables
    report_move = "    Crossover operator - Linear crossover\n"
    report_move += f"    current p0 = {parent_0}\n"
    report_move += f"    current p1 = {parent_1}\n"
    offspring_a = []
    offspring_b = []
    offspring_c = []

    # Movement
    for i in range(len(parent_0)):
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
    offspring_a = funcs.check_interval_01(offspring_a, x_lower, x_upper)
    offspring_b = funcs.check_interval_01(offspring_b, x_lower, x_upper)
    offspring_c = funcs.check_interval_01(offspring_c, x_lower, x_upper)

    return offspring_a, offspring_b, offspring_c, report_move


def blxalpha_crossover(parent_0: list, parent_1: list, x_lower: list, x_upper: list) -> tuple[list, list, str]:
    """
    This function performs the BLX-alpha crossover operator. Two new points are generated from the two parent points (offspring).

    :param parent_0: First parent
    :param parent_1: Second parent
    :param x_lower: Lower limit of the design variables
    :param x_upper: Upper limit of the design variables

    :return: [0] = First offspring position, [1] = Second offspring position, [2] = Report about the linear crossover process
    """

    # Start internal variables
    report_move = "    Crossover operator - BLX-alpha\n"
    report_move += f"    current p0 = {parent_0}\n"
    report_move += f"    current p1 = {parent_1}\n"
    offspring_a = []
    offspring_b = []

    # Movement
    for i in range(len(parent_0)):
        alpha = np.random.uniform(low=0, high=1)
        max_val = max(parent_0[i], parent_1[i])
        min_val = min(parent_0[i], parent_1[i])
        r_ij = np.abs(parent_0[i] - parent_1[i])
        report_move += f"    Dimension {i}: min_val = {min_val}, max_val = {max_val}, r_ij = {r_ij}\n"
        report_move += f"    neighbor_a = {min_val - alpha*r_ij}, neighbor_b = {max_val + alpha*r_ij}\n"
        offspring_a.append(min_val - alpha*r_ij)
        offspring_b.append(max_val + alpha*r_ij)

    # Check bounds
    offspring_a = funcs.check_interval_01(offspring_a, x_lower, x_upper)
    offspring_b = funcs.check_interval_01(offspring_b, x_lower, x_upper)

    return offspring_a, offspring_b, report_move


def tournament_selection(fit: np.ndarray, i: int, n_pop: int, runs: int) -> int:
    """
    This function selects a position from the population using the tournament selection method.

    :param fit: Population fitness values
    :param i:   current agent in t time step
    :param n_pop: Population size
    :param runs: Number of tournaments

    :return: selected agent id
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


def heuristic_crossover(parent_0: list, parent_1: list, n_dimensions: int, x_upper: list, x_lower: list) -> tuple[list, list, str]:
    """
    This function performs the heuristic crossover operator. Two new points are generated from the two parent points (offspring).

    :param of_function: Objective function. The Metapy user defined this function.
    :param parent_0: Current design variables of the first parent.
    :param parent_1: Current design variables of the second parent.
    :param n_dimensions: Problem dimension.
    :param x_lower: Lower limit of the design variables.
    :param x_upper: Upper limit of the design variables.
    :param none_variable: None variable. Default is None. User can use this variable in objective function.

    :return: [0] = First offspring position, [1] = Second offspring position, [2] = Report about the linear crossover process
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
    offspring_a = funcs.check_interval_01(offspring_a, x_lower, x_upper)
    offspring_b = funcs.check_interval_01(offspring_b, x_lower, x_upper)

    return offspring_a, offspring_b, report_move


def simulated_binary_crossover(of_function: Callable, parent_0: list, parent_1: list, eta_c: float, n_dimensions: int, x_upper: list, x_lower: list, none_variable=None) -> tuple[list, float, float, int, str]:
    """
    This function performs the simulated binary crossover operator. Two new points are generated from the two parent points (offspring).

    :param of_function: Objective function. The Metapy user defined this function.
    :param parent_0: Current design variables of the first parent.
    :param parent_1: Current design variables of the second parent.
    :param eta_c: Distribution index.
    :param n_dimensions: Problem dimension.
    :param x_lower: Lower limit of the design variables.
    :param x_upper: Upper limit of the design variables.
    :param none_variable: None variable. Default is None. User can use this variable in objective function.

    :return: A tuple containing:
        - x_i_new (List): Update variables of the i agent.
        - of_i_new (Float): Update objective function value of the i agent.
        - fit_i_new (Float): Update fitness value of the i agent.
        - neof (Integer): Number of evaluations of the objective function.
        - report (String): Report about the crossover process.   
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
    offspring_a = funcs.check_interval_01(offspring_a, x_lower, x_upper)
    offspring_b = funcs.check_interval_01(offspring_b, x_lower, x_upper)

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
    fit_i_new = funcs.fit_value(of_i_new)
    report_move += f"    update pos = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"

    return x_i_new, of_i_new, fit_i_new, neof, report_move


def arithmetic_crossover(of_function: Callable, parent_0: list, parent_1: list, n_dimensions: int, x_upper: list, x_lower: list, none_variable=None) -> tuple[list, float, float, int, str]:
    """
    This function performs the arithmetic crossover operator. Two new points are generated from the two parent points (offspring).

    :param of_function: Objective function. The Metapy user defined this function.
    :param parent_0: Current design variables of the first parent.
    :param parent_1: Current design variables of the second parent.
    :param n_dimensions: Problem dimension.
    :param x_lower: Lower limit of the design variables.
    :param x_upper: Upper limit of the design variables.
    :param none_variable: None variable. Default is None. User can use this variable in objective function.

    :return: A tuple containing:
        - x_i_new (List): Update variables of the i agent.
        - of_i_new (Float): Update objective function value of the i agent.
        - fit_i_new (Float): Update fitness value of the i agent.
        - neof (Integer): Number of evaluations of the objective function.
        - report (String): Report about the crossover process.
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
    offspring_a = funcs.check_interval_01(offspring_a, x_lower, x_upper)
    offspring_b = funcs.check_interval_01(offspring_b, x_lower, x_upper)

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
    fit_i_new = funcs.fit_value(of_i_new)
    report_move += f"    update pos = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"

    return x_i_new, of_i_new, fit_i_new, neof, report_move


def laplace_crossover(of_function: Callable, parent_0: list, parent_1: list, mu: float, sigma: float, n_dimensions: int, x_upper: list, x_lower: list, none_variable=None) -> tuple[list, float, float, int, str]:
    """
    This function performs the laplace crossover operator. Two new points are generated from the two parent points (offspring).

    :param of_function: Objective function. The Metapy user defined this function.
    :param parent_0: Current design variables of the first parent.
    :param parent_1: Current design variables of the second parent.
    :param mu: location parameter.
    :param sigma: scale parameter.
    :param n_dimensions: Problem dimension.
    :param x_lower: Lower limit of the design variables.
    :param x_upper: Upper limit of the design variables.
    :param none_variable: None variable. Default is None. User can use this variable in objective function.

    :return: A tuple containing:
        - x_i_new (List): Update variables of the i agent.
        - of_i_new (Float): Update objective function value of the i agent.
        - fit_i_new (Float): Update fitness value of the i agent.
        - neof (Integer): Number of evaluations of the objective function.
        - report (String): Report about the crossover process.
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
    offspring_a = funcs.check_interval_01(offspring_a, x_lower, x_upper)
    offspring_b = funcs.check_interval_01(offspring_b, x_lower, x_upper)

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
    fit_i_new = funcs.fit_value(of_i_new)
    report_move += f"    update pos = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"

    return x_i_new, of_i_new, fit_i_new, neof, report_move

def uniform_crossover(of_function: Callable, parent_0: List[float], parent_1: List[float], n_dimensions: int, x_upper: List[float], x_lower: List[float], none_variable=None) -> tuple[List[float], float, float, int, str]:
    """
    This function performs the uniform crossover operator. Two new points are generated from the two parent points (offspring).

    :param of_function: Objective function. The Metapy user defined this function.
    :param parent_0: Current design variables of the first parent.
    :param parent_1: Current design variables of the second parent.
    :param n_dimensions: Problem dimension.
    :param x_lower: Lower limit of the design variables.
    :param x_upper: Upper limit of the design variables.
    :param none_variable: None variable. Default is None. User can use this variable in objective function.

    :return: A tuple containing:
        - x_i_new (List): Update variables of the i agent.
        - of_i_new (Float): Update objective function value of the i agent.
        - fit_i_new (Float): Update fitness value of the i agent.
        - neof (Integer): Number of evaluations of the objective function.
        - report (String): Report about the crossover process.
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
    offspring_a = funcs.check_interval_01(offspring_a, x_lower, x_upper)
    offspring_b = funcs.check_interval_01(offspring_b, x_lower, x_upper)

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
    fit_i_new = funcs.fit_value(of_i_new)
    report_move += f"    update pos = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"

    return x_i_new, of_i_new, fit_i_new, neof, report_move


def binomial_crossover(of_function: Callable, parent_0: List[float], parent_1: List[float], p_c: float, n_dimensions: int, x_upper: List[float], x_lower: List[float], none_variable=None) -> tuple[List[float], float, float, int, str]:
    """
    This function performs the uniform crossover operator. Two new points are generated from the two parent points (offspring).

    :param of_function: Objective function. The Metapy user defined this function.
    :param parent_0: Current design variables of the first parent.
    :param parent_1: Current design variables of the second parent.
    :param p_c: Crossover probability rate (% * 0.01).
    :param n_dimensions: Problem dimension.
    :param x_lower: Lower limit of the design variables.
    :param x_upper: Upper limit of the design variables.
    :param none_variable: None variable. Default is None. User can use this variable in objective function.

    :return: A tuple containing:
        - x_i_new (List): Update variables of the i agent.
        - of_i_new (Float): Update objective function value of the i agent.
        - fit_i_new (Float): Update fitness value of the i agent.
        - neof (Integer): Number of evaluations of the objective function.
        - report (String): Report about the crossover process.
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
    offspring_a = funcs.check_interval_01(offspring_a, x_lower, x_upper)
    offspring_b = funcs.check_interval_01(offspring_b, x_lower, x_upper)

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
    fit_i_new = funcs.fit_value(of_i_new)
    report_move += f"    update pos = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"

    return x_i_new, of_i_new, fit_i_new, neof, report_move

# ------- ATÉ AQUI ------- #

def single_point_crossover(of_function: Callable, parent_0: List[float], parent_1: List[float], n_dimensions: int, x_upper: List[float], x_lower: List[float], none_variable: Optional[Union[None, List[float], float, Dict[str, float], str]] = None) -> Tuple[List[float], float, float, int, str]:
    """
    This function performs the single point crossover operator. Two new points are generated from the two parent points (offspring).

    :param of_function: Objective function. The Metapy user defined this function.
    :param parent_0: Current design variables of the first parent.
    :param parent_1: Current design variables of the second parent.
    :param n_dimensions: Problem dimension.
    :param x_lower: Lower limit of the design variables.
    :param x_upper: Upper limit of the design variables.
    :param none_variable: None variable. Default is None. User can use this variable in objective function.

    :return: A tuple containing:
        - x_i_new (List): Update variables of the i agent.
        - of_i_new (Float): Update objective function value of the i agent.
        - fit_i_new (Float): Update fitness value of the i agent.
        - neof (Integer): Number of evaluations of the objective function.
        - report (String): Report about the crossover process.
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
    offspring_a = funcs.check_interval_01(offspring_a, x_lower, x_upper)
    offspring_b = funcs.check_interval_01(offspring_b, x_lower, x_upper)

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
    fit_i_new = funcs.fit_value(of_i_new)
    report_move += f"    update n_dimensions = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"

    return x_i_new, of_i_new, fit_i_new, neof, report_move


def multi_point_crossover(of_function: Callable, parent_0: List[float], parent_1: List[float], n_dimensions: int, x_upper: List[float], x_lower: List[float], none_variable: Optional[Union[None, List[float], float, Dict[str, float], str]] = None) -> Tuple[List[float], float, float, int, str]:
    """
    This function performs the multi point crossover operator. Two new points are generated from the two parent points (offspring).

    :param of_function: Objective function. The Metapy user defined this function.
    :param parent_0: Current design variables of the first parent.
    :param parent_1: Current design variables of the second parent.
    :param n_dimensions: Problem dimension.
    :param x_lower: Lower limit of the design variables.
    :param x_upper: Upper limit of the design variables.
    :param none_variable: None variable. Default is None. User can use this variable in objective function.
    
    :return: A tuple containing:
        - x_i_new (List): Update variables of the i agent.
        - of_i_new (Float): Update objective function value of the i agent.
        - fit_i_new (Float): Update fitness value of the i agent.
        - neof (Integer): Number of evaluations of the objective function.
        - report (String): Report about the crossover process.
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
    offspring_a = funcs.check_interval_01(offspring_a, x_lower, x_upper)
    offspring_b = funcs.check_interval_01(offspring_b, x_lower, x_upper)

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
    fit_i_new = funcs.fit_value(of_i_new)
    report_move += f"    update pos = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"

    return x_i_new, of_i_new, fit_i_new, neof, report_move


def mp_crossover(chromosome_a: np.ndarray, chromosome_b: np.ndarray, seed: int | None, of_function: callable, none_variable: any) -> tuple[np.ndarray, np.ndarray]:
    """

    Multi-point ordered crossover.

    :param chromosome_a: Current design variables of the first parent.
    :param chromosome_b: Current design variables of the second parent.
    :param seed: Seed for pseudo-random numbers generation, by default None.
    :param of_function: Objective function. The Metapy user defined this function.
    :param none_variable: None variable. Default is None. User can use this variable in objective function.

    :return: Tuple of chromosomes after crossover.
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
    fit_t1i = funcs.fit_value(of_t1i)

    return x_t1i, of_t1i, fit_t1i, neof


def mp_mutation(chromosome: np.ndarray, seed: int | None, of_chro: float, of_function: callable, none_variable: any) -> tuple[np.ndarray, float, float, int]:
    """

    Multi-point inversion mutation. A random mask encodes which elements will keep the original order or the reversed one.

    :param chromosome: Current design variables of the individual.
    :param seed: Seed for pseudo-random numbers generation, by default None.
    :param of_chro: Objective function value of the chromosome before mutation.
    :param of_function: Objective function. The Metapy user defined this function.
    :param none_variable: None variable. Default is None. User can use this variable in objective function.

    :return: Tuple of chromosome after mutation, objective function value after mutation, fitness value after mutation, number of evaluations of the objective function.
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
    fit_t1i = funcs.fit_value(of_t1i)

    return x_t1i, of_t1i, fit_t1i, neof


def genetic_algorithm_01(obj: Callable, n_gen: int, params: dict, initial_population: list, x_lower: list, x_upper: list, args: Optional[tuple] = None, robustness: Union[bool, dict] = False) -> tuple[pd.DataFrame, pd.DataFrame, str]:
    """
    Genetic algorithm 01. Supports: roulette wheel selection, linear crossover and random walk mutation.

    :param obj: The objective function: obj(x, args) -> float or obj(x) -> float, where x is a list with shape dim and args is a tuple fixed parameters needed to completely specify the function
    :param n_gen: Number of generations or iterations
    :param params: Parameters of Genetic Algorithm
    :param initial_population: Initial population
    :param x_lower: Lower limit of the design variables
    :param x_upper: Upper limit of the design variables
    :param robustness: If True, the objective function is evaluated in a robust way (default is False)
    :param args: Extra arguments to pass to the objective function (optional)

    :return: [0] = All evaluations dataframe, [1] = Best, average and worst values dataframe, [2] = Report about the optimization process
    """

    # Initialize variables and dataframes (Don't remove this part)
    x_t0 = initial_population.copy()
    d = len(x_t0[0])
    n_pop = len(x_t0)
    all_results = []
    bests = [] 

    # Parameters of Genetic Algorithm (Adapt this part if you add new parameters for your version of the algorithm)
    selection_type = params['selection'].lower()
    crossover_type = params['crossover']['type'].lower()
    p_c = params['crossover']['crossover rate (%)'] / 100
    mutation_type = params['mutation']['type'].lower()
    p_m = params['mutation']['mutation rate (%)'] / 100
    if mutation_type == 'random walk' or mutation_type == 'random_walk' or mutation_type == 'randomwalk' or mutation_type == 'random-walk':
        pdf = params['mutation']['params']['pdf'].lower()
        cov = params['mutation']['params']['cov (%)']

    # Initial population evaluation (Don't remove this part)
    for n in range(n_pop):
        aux_df = funcs.evaluation(obj, n, x_t0[n], 0, args=args) if args is not None else funcs.evaluation(obj, n, x_t0[n], 0)
        all_results.append(aux_df)
    df = pd.concat(all_results, ignore_index=True)
    df['REPORT'] = ""
    df['OF EVALUATIONS'] = 1

    # Personal history information (Don't remove this part)
    for j in range(d):
        df.loc[:, 'P_X_BEST_' + str(j)] = df.loc[:, 'X_' + str(j)]
    df.loc[:, 'P_OF_BEST'] = df.loc[:, 'OF']

    # Iterations
    report = "Genetic Algorithm\n" # (Don't remove this part - Give the name of the algorithm)
    for t in range(1, n_gen + 1):
        # Select t-1 population and last evaluation count (Don't remove this part)
        report += f"iteration: {t}\n"
        df_aux = df[df['ITER'] == t-1]
        df_aux = df_aux.reset_index(drop=True)
        aux_t = []
        df_copy = df.copy()
        bests.append(funcs.best_avg_worst(df_aux, d))

        # Population movement (Don't remove this part)
        for i in range(n_pop):
            report += f" Agent id: {i}\n" # (Don't remove this part)

            # GA movement: Selection
            if selection_type == 'roulette wheel' or selection_type == 'roulette_wheel' or selection_type == 'roulettewheel' or selection_type == 'roulette-wheel':
                fit_pop = df_aux['FIT'].tolist()
                i_selected, report_selection = roulette_wheel_selection(fit_pop, i)
            else:
                pass
            report += report_selection

            # GA movement: Crossover
            if crossover_type == 'linear':
                random_value = np.random.uniform(low=0, high=1)
                if random_value <= p_c:
                    # Query agents information from dataframe
                    current_x, _, _ = funcs.query_x_of_fit_from_data(df_aux, i, d)
                    parent_1_x, _, _ = funcs.query_x_of_fit_from_data(df_aux, i_selected, d)
                    n_evals = 3 # Three new solutions will be evaluated after crossover
                    ch_a, ch_b, ch_c, report_crossover = linear_crossover(current_x, parent_1_x, x_lower, x_upper)
                    aux_df_a = funcs.evaluation(obj, i, ch_a, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_a, t)
                    df_temp = funcs.compare_and_save(df_aux[df_aux['ID'] == i], aux_df_a)
                    aux_df_b = funcs.evaluation(obj, i, ch_b, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_b, t)
                    df_temp = funcs.compare_and_save(df_temp, aux_df_b)
                    aux_df_c = funcs.evaluation(obj, i, ch_c, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_c, t)
                    df_temp = funcs.compare_and_save(df_temp, aux_df_c)
                    df_temp.loc[:, 'OF EVALUATIONS'] = n_evals
                else:
                    n_evals = 0 # No new solution will be evaluated after crossover
                    df_temp = df_aux[df_aux['ID'] == i].copy()
                    df_temp.loc[:, 'ITER'] = t
                    df_temp.loc[:, 'OF EVALUATIONS'] = n_evals
                    df_temp.loc[:, 'TIME CONSUMPTION (s)'] = 0
                    report_crossover = "    Crossover operator - Linear crossover\n"
                    report_crossover += "    Crossover not performed\n"
            elif crossover_type == 'blx-alpha' or crossover_type == 'blxalpha' or crossover_type == 'blx_alpha' or crossover_type == 'blx-alpha':
                random_value = np.random.uniform(low=0, high=1)
                if random_value <= p_c:
                    # Query agents information from dataframe
                    current_x, _, _ = funcs.query_x_of_fit_from_data(df_aux, i, d)
                    parent_1_x, _, _ = funcs.query_x_of_fit_from_data(df_aux, i_selected, d)
                    n_evals = 2 # Two new solutions will be evaluated after crossover
                    ch_a, ch_b, report_crossover = blxalpha_crossover(current_x, parent_1_x, x_lower, x_upper)
                    aux_df_a = funcs.evaluation(obj, i, ch_a, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_a, t)
                    df_temp = funcs.compare_and_save(df_aux[df_aux['ID'] == i], aux_df_a)
                    aux_df_b = funcs.evaluation(obj, i, ch_b, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_b, t)
                    df_temp = funcs.compare_and_save(df_temp, aux_df_b)
                    df_temp.loc[:, 'OF EVALUATIONS'] = n_evals
                else:
                    n_evals = 0 # No new solution will be evaluated after crossover
                    df_temp = df_aux[df_aux['ID'] == i].copy()
                    df_temp.loc[:, 'ITER'] = t
                    df_temp.loc[:, 'OF EVALUATIONS'] = n_evals
                    df_temp.loc[:, 'TIME CONSUMPTION (s)'] = 0
                    report_crossover = "    Crossover operator - Linear crossover\n"
                    report_crossover += "    Crossover not performed\n"
            report += report_crossover

            # GA movement: Mutation
            if mutation_type == 'random walk' or mutation_type == 'random_walk' or mutation_type == 'randomwalk' or mutation_type == 'random-walk':
                random_value = np.random.uniform(low=0, high=1)
                if random_value <= p_m:
                    n_evals_old = df_temp['OF EVALUATIONS'].values[0]
                    n_evals = 1 # One new solution will be evaluated after mutation
                    current_x, _, _ = funcs.query_x_of_fit_from_data(df_temp, i, d)
                    ch_a, report_mutation = funcs.mutation_01_random_walk(current_x, pdf, cov, x_lower, x_upper)
                    aux_df_a = funcs.evaluation(obj, i, ch_a, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_a, t)
                    df_temp = funcs.compare_and_save(df_temp[df_temp['ID'] == i], aux_df_a)
                    df_temp['OF EVALUATIONS'] = n_evals + n_evals_old
                else:
                    report_mutation = "    Mutation operator - Random walk\n"
                    report_mutation += "    Mutation not performed\n"
            report += report_mutation

            # Robustness evaluation (Don't remove this part)
            if isinstance(robustness, dict):
                report += "    Robustness evaluation\n"
                n_evals_old = df_temp['OF EVALUATIONS'].values[0]
                current_x, _, _ = funcs.query_x_of_fit_from_data(df_temp, i, d)
                avg_of = df_temp['OF'].values[0]
                avg_fit = df_temp['FIT'].values[0]
                for _ in range(robustness['n evals']):
                    ch_a, report_mutation = funcs.mutation_01_random_walk(current_x, 'uniform', robustness['perturbation (%)'], x_lower, x_upper)
                    aux_df_a = funcs.evaluation(obj, i, ch_a, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_a, t)
                    report += report_mutation
                    avg_of += aux_df_a['OF'].values[0]
                    avg_fit += aux_df_a['FIT'].values[0]
                df_temp.loc[:, 'FIT'] = avg_fit / (robustness['n evals'] + 1)
                df_temp.loc[:, 'OF'] = avg_of / (robustness['n evals'] + 1)
                df_temp.loc[:, 'OF EVALUATIONS'] = robustness['n evals'] + n_evals_old

            # Save final values of the i-th agent in t time step (Don't remove this part)
            aux_t.append(df_temp)

        # Update dataframe (Don't remove this part)
        df = pd.concat([df_copy] + aux_t, ignore_index=True)

        # Update personal history information (Don't remove this part)
        df_past = df[df['ITER'] == t-1]
        df_past = df_past.reset_index(drop=True)
        df_current = df[df['ITER'] == t]
        df_current = df_current.reset_index(drop=True)
        masks = np.where(df_current['OF'] < df_past['P_OF_BEST'], 1, 0)
        cont = 0
        for t_aux in range(n_pop * t, n_pop * t + n_pop, 1):
            if masks[cont] == 1:
                for j in range(d):
                    df.loc[t_aux, 'P_X_BEST_' + str(j)] = df_current['X_' + str(j)].values[cont]
                df.loc[t_aux, 'P_OF_BEST'] = df_current['OF'].values[cont]
            else:
                for j in range(d):
                    df.loc[t_aux, 'P_X_BEST_' + str(j)] = df_past['P_X_BEST_' + str(j)].values[cont]
                df.loc[t_aux, 'P_OF_BEST'] = df_past['P_OF_BEST'].values[cont]
            cont += 1

    # Final best, average and worst (Don't remove this part)
    dfj = df[df['ITER'] == n_gen]
    dfj = dfj.reset_index(drop=True)
    bests.append(funcs.best_avg_worst(dfj, d))
    df_resume = pd.concat(bests, ignore_index=True)
    df['REPORT'] = report
    for t in range(n_gen + 1):
        df_resume.loc[t, 'OF EVALUATIONS'] = df[df['ITER'] == t]['OF EVALUATIONS'].sum()
        df_resume.loc[t, 'TIME CONSUMPTION (s)'] = df[df['ITER'] == t]['TIME CONSUMPTION (s)'].sum()
    df_resume['OF EVALUATIONS'] = df_resume['OF EVALUATIONS'].cumsum()
    df_resume['TIME CONSUMPTION (s)'] = df_resume['TIME CONSUMPTION (s)'].cumsum()

    return df, df_resume, df['REPORT'].iloc[-1]

