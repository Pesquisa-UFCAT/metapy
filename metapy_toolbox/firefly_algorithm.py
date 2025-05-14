"""firefly algorithm functions"""
import time
import random

import numpy as np
import pandas as pd
from tqdm import tqdm

import metapy_toolbox.common_library as metapyco

from typing import Any, Callable, List, Optional, Tuple, Union

def gamma_parameter(x_lower: List[float], x_upper: List[float], n_dimension: int, m: int = 2) -> List[float]:
    """
    This function calculates the light absorption coefficient.

    :param x_lower: Lower limit for each variable.
    :param x_upper: Upper limit for each variable.
    :param n_dimension: Number of design variables.
    :param m: Light absorption exponent (default is 2).

    :return: List of gamma values for each dimension.
    """

    # Light absorption coefficient
    gamma = []
    for i in range(n_dimension):
        r_ij = x_upper[i] - x_lower[i]
        gamma.append(1 / r_ij ** m)

    return gamma


def discriminant_factor(fit_male: float, fit_female: float) -> int:
    """
    Calculation of the discriminating factor of the male and female fireflies population

    :param fit_male: Fitness of the male firefly.
    :param fit_female: Fitness of the female firefly.

    :return: Discriminating factor
    """

    # Comparsion fireflies brightness
    if fit_male > fit_female:
        d_1 = 1
    else:
        d_1 = -1

    return d_1


def attractiveness_parameter(beta_0: float, gamma: List[float], x_i: List[float], x_j: List[float], n_dimensions: int) -> Tuple[List[float], float]:

    """
    This function calculates at attractiveness parameter between `x_i` and `x_j` fireflies.

    :param beta_0: Base attractiveness (at distance = 0).
    :param gamma: Light absorption coefficient for each dimension.
    :param x_i: Position of the i-th firefly.
    :param x_j: Position of the j-th firefly.
    :param n_dimensions: Number of design variables.

    :return: Tuple with:
        - beta: List of attractiveness values for each dimension.
        - r_ij: Euclidean distance between fireflies.
    """

    # Firefly distance
    r_i = 0
    for i in range(n_dimensions):
        r_i += (x_i[i] - x_j[i]) ** 2
    r_ij = np.sqrt(r_i)

    # Attractiveness between fireflies
    beta = []
    for i in range(n_dimensions):
        beta.append(beta_0 * np.exp(-gamma[i]*r_ij))

    return beta, r_ij


def male_movement(obj_function: Callable, beta_0: float, gamma: List[float], x_i_old: List[float], fit_i_old: float, y_j_old: List[float], fit_j_old: float, y_k_old: List[float], fit_k_old: float, n_dimensions: int, x_lower: List[float], x_upper: List[float], none_variable: Optional[object] = None) -> Tuple[List[float], float, float, int, str]:
    """
    This function movement an male firefly.

    :param obj_function: User-defined objective function.
    :param beta_0: Base attractiveness (at distance = 0).
    :param gamma: Light absorption coefficient list.
    :param x_i_old: Current position of the male firefly.
    :param fit_i_old: Fitness of the male firefly.
    :param y_j_old: Position of the first female firefly.
    :param fit_j_old: Fitness of the first female firefly.
    :param y_k_old: Position of the second female firefly.
    :param fit_k_old: Fitness of the second female firefly.
    :param n_dimensions: Number of design variables.
    :param x_lower: Lower bounds for design variables.
    :param x_upper: Upper bounds for design variables.
    :param none_variable: Optional variable passed to the objective function.

    :return: Tuple with:

        - x_i_new: New position of the male firefly.
        - of_i_new: Objective function value.
        - fit_i_new: Fitness value.
        - neof: Number of evaluations of the objective function (always 1).
        - report: Text report describing the movement.
    """

    # Discriminant factor
    d_j = discriminant_factor(fit_i_old, fit_j_old)
    d_k = discriminant_factor(fit_i_old, fit_k_old)
    report_move = f"    d_j = {d_j}, d_k = {d_k}\n"

    # Attractiveness parameter
    beta_j, r_j = attractiveness_parameter(beta_0, gamma, x_i_old, y_j_old, n_dimensions)
    beta_k, r_k = attractiveness_parameter(beta_0, gamma, x_i_old, y_k_old, n_dimensions)
    report_move += f"    r_j = {r_j} beta_j = {beta_j}, r_k = {r_k} beta_k = {beta_k}\n"

    # Lambda and mu random parameters
    lambda_paras = np.random.random()
    mu_paras = np.random.random()
    report_move += f"    lambda = {lambda_paras}, mu = {mu_paras}\n"

    # Movement
    x_i_new = []
    for i in range(n_dimensions):
        # Second term
        second_term = d_j * beta_j[i] * lambda_paras * (y_j_old[i] - x_i_old[i])
        # Third term
        third_term = d_k * beta_k[i] * mu_paras * (y_k_old[i] - x_i_old[i])
        # Update firefly position
        aux = x_i_old[i] + second_term + third_term
        x_i_new.append(aux)
        report_move += f"    Dimension {i}: 2nd = {second_term}, 3rd = {third_term}, neighbor = {aux}\n"

    # Check bounds
    x_i_new = metapyco.check_interval_01(x_i_new, x_lower, x_upper)

    # Evaluation of the objective function and fitness
    of_i_new = obj_function(x_i_new, none_variable)
    fit_i_new = metapyco.fit_value(of_i_new)
    report_move += f"    update x = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"
    neof = 1

    return x_i_new, of_i_new, fit_i_new, neof, report_move


def female_movement(obj_function: Callable, beta_0: float, gamma: List[float], x_i_old_best: List[float], y_j_old: List[float], n_dimensions: int, x_lower: List[float], x_upper: List[float], none_variable: Optional[object] = None) -> Tuple[List[float], float, float, int, str]:
    """
    This function movement an female firefly.

    :param obj_function: User-defined objective function.
    :param beta_0: Attractiveness at distance r = 0.
    :param gamma: Light absorption coefficients for each dimension.
    :param x_i_old_best: Position of the best male firefly.
    :param y_j_old: Current position of the female firefly.
    :param n_dimensions: Number of design variables.
    :param x_lower: Lower bounds for the design variables.
    :param x_upper: Upper bounds for the design variables.
    :param none_variable: Optional variable passed to the objective function.

    :return: Tuple with:

        - y_i_new: New position of the female firefly.
        - of_i_new: Objective function value at new position.
        - fit_i_new: Fitness value at new position.
        - neof: Number of objective function evaluations (always 1).
        - report_move: Report describing the movement process.
    """

    # Attractiveness parameter
    beta_j, r_j = attractiveness_parameter(beta_0, gamma, x_i_old_best, y_j_old, n_dimensions)
    report_move = f"    r_j = {r_j} beta_j = {beta_j}\n"

    # phi random parameter
    phi_paras = np.random.random()
    report_move += f"    phi = {phi_paras}\n"

    # Movement
    y_i_new = []
    for i in range(n_dimensions):
        # Second term
        second_term = beta_j[i] * phi_paras * (x_i_old_best[i] - y_j_old[i])
        # Update firefly position
        aux = y_j_old[i] + second_term
        report_move += f"    Dimension {i}: 2nd = {second_term}, neighbor = {aux}\n"
    y_i_new.append(aux)

    # Check bounds
    y_i_new = metapyco.check_interval_01(y_i_new, x_lower, x_upper)

    # Evaluation of the objective function and fitness
    of_i_new = obj_function(y_i_new, none_variable)
    fit_i_new = metapyco.fit_value(of_i_new)
    report_move += f"    update x = {y_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"
    neof = 1

    return y_i_new, of_i_new, fit_i_new, neof, report_move


def gender_firefly_01(settings: List[Union[dict, list, int]]) -> Tuple[pd.DataFrame, pd.DataFrame, float, str]:
    """
    Executes the Gender Firefly Optimization Algorithm.

    This metaheuristic separates the population into male and female fireflies,
    where males are attracted to females based on their brightness, and females
    move toward the best male in the population. Mutation operators such as
    chaotic maps or hill climbing are optionally applied to improve exploration.

    :param settings: A list containing the following elements:

        1. **setup (dict)** – Dictionary with algorithm configuration:
            - 'number of population': int, number of male fireflies.
            - 'number of iterations': int, number of iterations.
            - 'number of dimensions': int, dimensionality of the problem.
            - 'x pop lower limit': list[float], lower bounds for each variable.
            - 'x pop upper limit': list[float], upper bounds for each variable.
            - 'none variable': optional input passed to the objective function.
            - 'objective function': callable, user-defined function to optimize.
            - 'algorithm parameters': dict with:
                - 'attractiveness':
                    - 'beta_0': float, attractiveness at distance r = 0.
                    - 'gamma': float or 'auto', light absorption coefficient.
                - 'female population':
                    - 'number of females': int, count of female fireflies.
                - 'mutation': dict with:
                    - 'type': str, mutation strategy ('chaotic map 01' or 'hill climbing').
                    - 'number of tries', 'alpha' (for chaotic map).
                    - 'cov (%)', 'pdf' (for hill climbing).

        2. **initial population (list)** – List of individuals (male fireflies).

        3. **seeds (int or None)** – Random seed for reproducibility.

    :return: A tuple containing:
        - **df_all (DataFrame)** – All evaluated solutions across all iterations.
        - **df_best (DataFrame)** – Best, worst, and average results per iteration.
        - **delta_time (float)** – Execution time in seconds.
        - **report (str)** – Full log of algorithm steps and solution trace.
    """
    # setup config
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

    # algorithm_parameters
    algorithm_parameters = setup['algorithm parameters']
    beta_0 = algorithm_parameters['attractiveness']['beta_0']
    gamma = algorithm_parameters['attractiveness']['gamma']
    n_pop_female = algorithm_parameters['female population']['number of females']

    # Light absorption coefficient
    if gamma == 'auto':
        gamma = gamma_parameter(x_lower, x_upper, n_dimensions)
    else:
        pass

    # Mutation control
    type_mut = algorithm_parameters['mutation']['type']
    if type_mut == 'chaotic map 01':
        n_tries = algorithm_parameters['mutation']['number of tries']
        alpha = algorithm_parameters['mutation']['alpha']
    elif type_mut == 'hill climbing':
        std = algorithm_parameters['mutation']['cov (%)']
        pdf = algorithm_parameters['mutation']['pdf']

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
    report = "Firefly Gender Algorithm - report\n\n"
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

    # Female population and evaluation solutions
    y_pop = metapyco.initial_population_01(n_pop_female, n_dimensions, x_lower, x_upper)
    for i_pop in range(n_pop_female):
        x_pop.append(y_pop[i_pop].copy())
        y_obj = obj_function(y_pop[i_pop], none_variable)
        of_pop.append(y_obj)
        fit_pop.append(metapyco.fit_value(y_obj))
        neof_count += 1
        i_pop_solution = metapyco.resume_all_data_in_dataframe(y_pop[i_pop],
                                                               of_pop[i_pop+n_population],
                                                               fit_pop[i_pop+n_population],
                                                               columns_all_data,
                                                               iteration=0)
        all_data_pop.append(i_pop_solution)

    # Best, average and worst values and storage
    repetition_data, best_id = metapyco.resume_best_data_in_dataframe(x_pop, of_pop, fit_pop,
                                                             columns_repetition_data,
                                                             columns_worst_data,
                                                             columns_other_data,
                                                             neof_count, iteration=0)
    resume_result.append(repetition_data)
    for i_pop in range(n_population+n_pop_female):
        if i_pop <= (n_population - 1):
            id_pop_male_or_female = 'MA'
        else:
            id_pop_male_or_female = f'FE (y_{i_pop-n_population})'
        if i_pop == best_id:
            report += f'{id_pop_male_or_female} x{i_pop} = {x_pop[i_pop]}, of_pop {of_pop[i_pop]} - best solution\n'
        else:
            report += f'{id_pop_male_or_female} x{i_pop} = {x_pop[i_pop]}, of_pop {of_pop[i_pop]} \n'

    # Iteration procedure
    report += "\nIterations\n"
    for iter in range(n_iterations):
        report += f"\nIteration: {iter+1}\n"

        # Time markup
        initial_time = time.time()

        # Population separation
        x_male_pop = x_pop[:n_population]
        y_female_pop = x_pop[n_population:]
        fit_male_pop = fit_pop[:n_population]
        fit_female_pop = fit_pop[n_population:]
        of_male_pop = of_pop[:n_population]
        of_female_pop = of_pop[n_population:]

        # Best male
        _, _, x_male_best, _, _,\
            _, _, _, _, _ = metapyco.best_values(x_male_pop, of_male_pop, fit_male_pop)

        # Male population movement
        for pop in range(n_population):
            report += f"Pop id: {pop} - particle movement - male procedure\n"
            report += f"    current x = {x_male_pop[pop]}, of = {of_male_pop[pop]}, fit = {fit_male_pop[pop]}\n"
            pos = random.sample(range(0, n_pop_female), 2)
            id_y_j, id_y_k = pos[0], pos[1]
            report += f"    selected female id y_j = {id_y_j} y_j{y_female_pop[id_y_j]}, id y_k = {id_y_k} y_k{y_female_pop[id_y_k]}\n"
            x_i_temp, of_i_temp,\
                fit_i_temp, neof,\
                report_mov = male_movement(obj_function,
                                            beta_0,
                                            gamma,
                                            x_male_pop[pop],
                                            fit_male_pop[pop],
                                            y_female_pop[id_y_j],
                                            fit_female_pop[id_y_j],
                                            y_female_pop[id_y_k],
                                            fit_female_pop[id_y_k],
                                            n_dimensions,
                                            x_lower,
                                            x_upper,
                                            none_variable=none_variable)
            report += report_mov
            i_pop_solution = metapyco.resume_all_data_in_dataframe(x_i_temp, of_i_temp,
                                                                   fit_i_temp,
                                                                   columns_all_data,
                                                                   iteration=iter+1)
            all_data_pop.append(i_pop_solution)

            # New design variables
            if fit_i_temp > fit_pop[pop]:
                report += "    fit_i_temp > fit_pop[pop] - accept this solution\n"
                x_pop[pop] = x_i_temp.copy()
                of_pop[pop] = of_i_temp
                fit_pop[pop] = fit_i_temp
            else:
                report += "    fit_i_temp < fit_pop[pop] - not accept this solution\n"

            # Update neof (Number of Objective Function Evaluations)
            neof_count += neof

        # Female movement
        for pop in range(n_pop_female):
            report += f"Pop id: {pop} - particle movement - female procedure \n"
            report += f"    current y = {y_female_pop[pop]}, of = {of_female_pop[pop]}, fit = {fit_female_pop[pop]}\n"
            report += f"    best male = {x_male_best}\n"
            y_i_temp, of_i_temp,\
                fit_i_temp, neof,\
                report_mov = female_movement(obj_function,
                                                beta_0,
                                                gamma,
                                                x_male_best,
                                                y_female_pop[pop],
                                                n_dimensions,
                                                x_lower,
                                                x_upper,
                                                none_variable)
            report += report_mov
            i_pop_solution = metapyco.resume_all_data_in_dataframe(y_i_temp, of_i_temp,
                                                                   fit_i_temp,
                                                                   columns_all_data,
                                                                   iteration=iter+1)
            all_data_pop.append(i_pop_solution)

            # New design variables
            if fit_i_temp > fit_pop[pop+n_population]:
                report += "    fit_i_temp > fit_pop[pop] - accept this solution\n"
                x_pop[pop+n_population] = y_i_temp.copy()
                of_pop[pop+n_population] = of_i_temp
                fit_pop[pop+n_population] = fit_i_temp
            else:
                report += "    fit_i_temp < fit_pop[pop] - not accept this solution\n"

            # Update neof (Number of Objective Function Evaluations)
            neof_count += neof

        # Best solution
        id_best, _, x_best, _, of_best,\
            _, fit_best, _, _, _ = metapyco.best_values(x_pop, of_pop, fit_pop)

        # Mutation movement
        report += f"Pop id: {id_best} - particle movement - mutation procedure\n"
        if type_mut == 'chaotic map 01':
            report += "    Chaotic Map 01\n"
            x_i_temp, of_i_temp,\
                fit_i_temp, neof,\
                report_mov = metapyco.mutation_02_chaos_movement(obj_function, x_best, of_best, fit_best,
                                                                        x_lower, x_upper, n_dimensions, alpha,
                                                                        n_tries, iter, n_iterations,
                                                                        none_variable=none_variable)
        elif type_mut == 'hill climbing':
            report += "    Hill Climbing\n"
            x_i_temp, of_i_temp,\
                fit_i_temp, neof,\
                report_mov = metapyco.mutation_01_hill_movement(obj_function,
                                                            x_best,
                                                            x_lower, x_upper,
                                                            n_dimensions,
                                                            pdf, std,
                                                            none_variable)
        report += report_mov

        # Update neof (Number of Objective Function Evaluations)
        neof_count += neof

        # New design variables
        if fit_i_temp > fit_best:
            report += "    fit_i_temp > fit_pop[pop] - accept this solution\n"
            x_pop[id_best] = x_i_temp.copy()
            of_pop[id_best] = of_i_temp
            fit_pop[id_best] = fit_i_temp
        else:
            report += "    fit_i_temp < fit_pop[pop] - not accept this solution\n"
        
        # Best, average and worst values and storage
        repetition_data, best_id = metapyco.resume_best_data_in_dataframe(x_pop, of_pop, fit_pop,
                                                                columns_repetition_data,
                                                                columns_worst_data,
                                                                columns_other_data,
                                                                neof_count,
                                                                iteration=iter+1)
        resume_result.append(repetition_data)
        report += "update solutions\n"
        for i_pop in range(n_population+n_pop_female):
            if i_pop <= (n_population - 1):
                id_pop_male_or_female = 'MA'
            else:
                id_pop_male_or_female = f'FE (y_{i_pop-n_population})'
            if i_pop == best_id:
                report += f'{id_pop_male_or_female} x{i_pop} = {x_pop[i_pop]}, of_pop {of_pop[i_pop]} - best solution\n'
            else:
                report += f'{id_pop_male_or_female} x{i_pop} = {x_pop[i_pop]}, of_pop {of_pop[i_pop]} \n'

    # Time markup
    end_time = time.time()
    delta_time = end_time - initial_time

    # Storage all values in DataFrame
    df_all = pd.concat(all_data_pop, ignore_index=True)

    # Storage best values in DataFrame
    df_best = pd.concat(resume_result, ignore_index=True)

    return df_all, df_best, delta_time, report


def firefly_movement(of_function: Callable[[List[float], Any], float], x_t0i: List[float], x_j: List[float], beta: List[float], alpha: float, scaling: bool, d: int, x_lower: List[float], x_upper: List[float], none_variable: Any) -> Tuple[List[float], float, float, int]:
    """
    This function creates a new solution using the firefly algorithm movement.

    :param of_function: Objective function defined by the user.
    :param x_t0i: Design variables of firefly i before movement.
    :param x_j: Design variables of firefly j (attractive target).
    :param beta: Attractiveness values for each dimension.
    :param alpha: Randomization parameter.
    :param scaling: Whether to apply scaling by variable bounds.
    :param d: Number of dimensions.
    :param x_lower: Lower bounds for the variables.
    :param x_upper: Upper bounds for the variables.
    :param none_variable: Optional user-defined variable passed to the objective function.

    :return: Tuple containing:

        - x_t1i: Updated design variables of firefly i after movement.
        - of_t1i: Objective function value for x_t1i.
        - fit_t1i: Fitness value of x_t1i.
        - neof: Number of objective function evaluations (always 1).
    """

    # Start internal variables
    x_t1i = []
    of_t1i = 0
    fit_t1i = 0
    for i_count in range(d):
        epsilon_i = np.random.random() - 0.50
        if scaling:
            s_d = x_upper[i_count] - x_lower[i_count]
        else:
            s_d = 1
        new_value = x_t0i[i_count] + beta[i_count] * (x_j[i_count] - x_t0i[i_count]) + alpha * s_d * epsilon_i
        x_t1i.append(new_value)

    # Check boundes
    x_t1i = metapyco.check_interval_01(x_t1i, x_lower, x_upper)
    # Evaluation of the objective function and fitness
    of_t1i = of_function(x_t1i, none_variable)
    fit_t1i = metapyco.fit_value(of_t1i)
    neof = 1
    return x_t1i, of_t1i, fit_t1i, neof


def sorted_fa(of_pop: List[float], x_pop: List[List[float]]) -> Tuple[List[float], List[List[float]]]:
    """
    This function sorts the population in descending order of the objective function.

    :param of_pop: List of objective function values for each individual.
    :param x_pop: List of corresponding design variable vectors.

    :return: Tuple containing:
    
        - of_pop_new: Sorted list of objective function values.
        - x_pop_new: Sorted list of design variable vectors.
    """

    of_pop_new = []
    x_pop_new = []
    sorted_index = np.argsort(of_pop)

    for i in range(len(of_pop)):
        of_pop_new.append(of_pop[sorted_index[i]])
        x_pop_new.append(x_pop[sorted_index[i]])

    return of_pop_new, x_pop_new
