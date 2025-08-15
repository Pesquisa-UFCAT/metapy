"""firefly algorithm functions"""
import time
import random

import numpy as np
import pandas as pd
from tqdm import tqdm

import metapy_toolbox.common_library as metapyco


def gamma_parameter(x_lower, x_upper, n_dimension, m=2):
    """
    This function calculates the light absorption coefficient.

    Args:
        x_lower (List): Lower limit of the problem
        x_upper (List): Upper limit of the problem
        n_dimensions (Integer): Problem dimension
        m (Integer): Light absorption factor. Default is 2

    Returns:
        gamma (List): Light absorption coefficient  1 / (x_upper - x_lower) ** m
    """

    # Light absorption coefficient
    gamma = []
    for i in range(n_dimension):
        r_ij = x_upper[i] - x_lower[i]
        gamma.append(1 / r_ij ** m)

    return gamma


def discriminant_factor(fit_male, fit_female):
    """
    Calculation of the discriminating factor of the male and female fireflies population

    Args:
        fit_male (Float): Fitness of the i male firefly
        fit_female (Float): Fitness of the k female firefly
    
    Returns:
        d_1 (Integer): Discriminating factor
    """

    # Comparsion fireflies brightness
    if fit_male > fit_female:
        d_1 = 1
    else:
        d_1 = -1

    return d_1


def attractiveness_parameter(beta_0, gamma, x_i, x_j, n_dimensions):
    """
    This function calculates at attractiveness parameter between x_i and x_j fireflies.

    Args:
        beta_0 (Float): Attractiveness at r = 0
        gamma (List): Light absorption coefficient  1 / (x_upper - x_lower) ** m
        x_i (List): Design variables i Firefly
        x_j (List): Design variables j Firefly
        n_dimensions (Integer): Problem dimension
    
    Returns:
        beta (List): Attractiveness
        r_ij (Float): Firefly distance
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


def male_movement(obj_function, beta_0, gamma, x_i_old, fit_i_old, y_j_old, fit_j_old, y_k_old, fit_k_old, n_dimensions, x_lower, x_upper, none_variable=None):
    """
    This function movement an male firefly.

    Args:
        of_function (Py function (def)): Objective function. The Metapy user defined this function.
        beta_0 (Float): Attractiveness at r = 0
        gamma (List): Light absorption coefficient  1 / (x_upper - x_lower) ** m
        x_i_old (List): Design variables i (male) Firefly
        fit_i_old (Float): Fitness of the i firefly
        y_j_old (List): Design variables j (female) Firefly
        fit_j_old (Float): Fitness of the j firefly
        y_k_old (List): Design variables k (female) Firefly
        fit_k_old (Float): Fitness of the k firefly
        n_dimensions (Integer): Problem dimension
        x_lower (List): Lower limit of the problem
        x_upper (List): Upper limit of the problem
        none_variable (None, list, float, dictionary, str or any): None variable. Default is None. User can use this variable in objective function.
    
    Returns:
        x_i_new (List): Update variables of the i agent.
        of_i_new (Float): Update objective function value of the i agent.
        fit_i_new (Float): Update fitness value of the i agent.
        neof (Integer): Number of evaluations of the objective function.
        report (str): Report about the male movement process.
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


def female_movement(obj_function, beta_0, gamma, x_i_old_best, y_j_old, n_dimensions, x_lower, x_upper, none_variable=None):
    """
    This function movement an female firefly.

    Args:
        of_function (Py function (def)): Objective function. The Metapy user defined this function.
        beta_0 (Float): Attractiveness at r = 0
        gamma (List): Light absorption coefficient  1 / (x_upper - x_lower) ** m
         
    Returns:
        y_i_new (List): Update variables of the i agent.
        of_i_new (Float): Update objective function value of the i agent.
        fit_i_new (Float): Update fitness value of the i agent.
        neof (Integer): Number of evaluations of the objective function.
        report_move (str): Report about the male movement process.
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


def gender_firefly_01(settings):
    """
    Gender firefly algorithm.
    
    Args:  
        settings (List): [0] setup (dict), [1] initial population (List), [2] seeds (Integer).
            'number of population' (Integer): number of population.
            'number of iterations' (Integer): number of iterations.
            'number of dimensions' (Integer): Problem dimension.
            'x pop lower limit' (List): Lower limit of the design variables.
            'x pop upper limit' (List): Upper limit of the design variables.
            'none variable' (Object or None): None variable. Default is None. Use in objective function.
            'objective function' (function): Objective function. The Metapy user defined this function.                                                
            'algorithm parameters' (dict): Algorithm parameters.
                'beta 0' (Float): Attractiveness at r = 0.
                gamma (List): Light absorption coefficient  1 / (x_lower - x_upper) ** m.
    
    Returns:
        df_all (dataframe): All data of the population.
        df_best (dataframe): Best data of the population.
        delta_time (Float): Time of the algorithm execution in seconds.
        report (str): Report of the algorithm execution.
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


def firefly_movement(of_function, x_t0i, x_j, beta, alpha, scaling, d, x_lower, x_upper, none_variable):
    """
    This function creates a new solution using the firefly algorithm movement.

    Input:
    of_function  | External def user input this function in arguments       | Py function
    x_t0i        | Design variable I particle before movement               | Py list[D]
    x_j          | J Firefly                                                | Py list[D]
    beta         | Attractiveness                                           | Py list[D]
    alpha        | Randomic factor                                          | Float
    scaling      | Scaling factor                                           | Float
    d            | Problem dimension                                        | Integer
    x_lower      | Lower limit design variables                             | Py list[D]
    x_upper      | Upper limit design variables                             | Py list[D]
    none_variable| Empty variable for the user to use in the obj. function  | ?

    Output:
    x_t1i        | Design variable I particle after movement                | Py list[D]
    of_t1i       | Objective function X_T1I (new particle)                  | Float
    fit_t1i      | Fitness X_T1I (new particle)                             | Float
    neof         | Number of objective function evaluations                 | Integer
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


def sorted_fa(of_pop, x_pop):
    """
    This function sorts the population in descending order of the objective function.

    Input:
        of_pop (list): Objective function values.
        x_pop (list): Population design variables.

    Output:
        of_pop_new (list): Objective function values sorted.
        x_pop_new (list): Population design variables sorted.
    """

    of_pop_new = []
    x_pop_new = []
    sorted_index = np.argsort(of_pop)

    for i in range(len(of_pop)):
        of_pop_new.append(of_pop[sorted_index[i]])
        x_pop_new.append(x_pop[sorted_index[i]])

    return of_pop_new, x_pop_new
