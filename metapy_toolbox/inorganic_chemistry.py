"""Inorganic Chemistry functions"""
import time

import pandas as pd
import numpy as np
from tqdm import tqdm

import metapy_toolbox.common_library as metapyco


def inorganic_chemistry_algorithm_01(settings):
    """
    Inorganic Chemistry algorithm 01.
    
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
    comp_a = algorithm_parameters['composto A']
    comp_b = algorithm_parameters['composto B']

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
    report = "Inorganic Chemistry Algorithm 01- report \n\n"
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
    y_pop = metapyco.initial_population_01(n_population, n_dimensions, x_lower, x_upper)
    for i_pop in range(n_population):
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
