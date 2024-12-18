"""differential evolution functions"""
import time

import numpy as np
import pandas as pd
from tqdm import tqdm

import metapy_toolbox.common_library as metapyco


def de_movement_01(obj_function, p_c, x_i_old, x_i_mutation, n_dimensions, x_lower, x_upper, none_variable=None):
    """
    This function performs the differential evolution movement (binomial crossover).

    Args:
        of_function (Py function (def)): Objective function. The Metapy user defined this function.
        p_c (Float): Crossover rate.
        x_i_old (List): Current design variables of the i agent.
        x_i_mutation (List): Current design variables of the mutation agent.
        n_dimensions (Integer): Problem dimension.
        x_lower (List): Lower limit of the design variables.
        x_upper (List): Upper limit of the design variables.
        none_variable (None, list, float, dictionary, str or any): None variable. Default is None. User can use this variable in objective function.

    Returns:
        x_i_new (List): Update variables of the i agent.
        of_i_new (Float): Update objective function value of the i agent.
        fit_i_new (Float): Update fitness value of the i agent.
        neof (Integer): Number of evaluations of the objective function.
        report (String): Report about the male movement process.
    """

    # Start internal variables
    report_move = "    Crossover movement - Binomial DE\n"
    report_move += f"    current x_current = {x_i_old}\n"
    report_move += f"    current x mutation = {x_i_mutation}\n"
    x_i_new = []

    # Movement
    for i in range(n_dimensions):
        lambda_paras = np.random.uniform(low=0, high=1)
        if lambda_paras <= p_c:
            neighbor = x_i_mutation[i]
            type_move = f'random_number {lambda_paras} <= p_c {p_c} (copy mutation)'
        else:
            neighbor = x_i_old[i]
            type_move = f'random_number {lambda_paras} > p_c {p_c} (dont copy mutation)'
        x_i_new.append(neighbor)
        report_move += f"    Dimension {i}: {type_move}, neighbor = {neighbor}\n"

    # Check bounds
    x_i_new = metapyco.check_interval_01(x_i_new, x_lower, x_upper)

    # Evaluation of the objective function and fitness
    of_i_new = obj_function(x_i_new, none_variable)
    fit_i_new = metapyco.fit_value(of_i_new)
    report_move += f"    update x = {x_i_new}, of = {of_i_new}, fit = {fit_i_new}\n"
    neof = 1

    return x_i_new, of_i_new, fit_i_new, neof, report_move


def differential_evolution_01(settings):
    """
    Differential Evolution algorithm 01.
    
    Args:  
        settings (List): [0] setup, [1] initial population, [2] seeds.
            'number of population' (int): number of population.
            'number of iterations' (int): number of iterations.
            'number of dimensions' (int): Problem dimension.
            'x pop lower limit' (List): Lower limit of the design variables.
            'x pop upper limit' (List): Upper limit of the design variables.
            'none_variable' (None, list, float, dictionary, str or any): None variable. Default is None. User can use this variable in objective function.
            'objective function' (Py function (def)): Objective function. The Metapy user defined this function.                                                
            'algorithm parameters' (Dictionary): Algorithm parameters. See documentation.
                'mutation'  (Dictionary): Mutation parameters.
                'crossover' (Dictionary): Crossover parameters.
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
    p_m = algorithm_parameters['mutation']['mutation rate (%)']/100
    mut_type = algorithm_parameters['mutation']['type']
    f_scale = algorithm_parameters['mutation']['scale factor (F)']
    p_c = algorithm_parameters['crossover']['crossover rate (%)']/100
    crosso_type = algorithm_parameters['crossover']['type']

    # Mutation control
    if mut_type == 'de/rand/1':
        pass

    # Crossover control
    if crosso_type == 'binomial':
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
            report += f'x{i_pop} = {x_pop[i_pop]}, of_pop {of_pop[i_pop]} - best solution\n'
        else:
            report += f'x{i_pop} = {x_pop[i_pop]}, of_pop {of_pop[i_pop]} \n'

    # Iteration procedure
    progress_bar = tqdm(total=n_iterations, desc='Progress')
    report += "\nIterations\n"
    for iter in range(n_iterations):
        report += f"\nIteration: {iter+1}\n"

        # Time markup
        initial_time = time.time()

        # Copy results
        x_temp = x_pop.copy()

        # Population movement
        for pop in range(n_population):
            report += f"Pop id: {pop} - particle movement\n"
            report += f"    current x = {x_temp[pop]}\n"

            # Selection and Mutation
            random_value = np.random.uniform(low=0, high=1)
            if random_value <= p_m:
                if mut_type == 'de/rand/1':
                    # Selection
                    selected, report_mov = metapyco.agent_selection(n_population, 3, pop)
                    report += report_mov
                    report += "    Mutation operator - de/rand/1\n"
                    x_i_temp, of_i_temp,\
                        fit_i_temp, neof,\
                        report_mov = metapyco.mutation_03_de_movement(obj_function,
                                                                        x_temp[selected[0]],
                                                                        x_temp[selected[1]],
                                                                        x_temp[selected[2]],
                                                                        x_lower,
                                                                        x_upper,
                                                                        n_dimensions,
                                                                        f_scale,
                                                                        none_variable)
                elif mut_type == 'de/rand/2':
                    # Selection
                    selected, report_mov = metapyco.agent_selection(n_population, 4, pop)
                    report += report_mov
                    report += "    Mutation operator - de/rand/2\n"
                    x_i_temp, of_i_temp,\
                        fit_i_temp, neof,\
                        report_mov = metapyco.mutation_04_de_movement(obj_function,
                                                                        x_temp[selected[0]],
                                                                        x_temp[selected[1]],
                                                                        x_temp[selected[2]],
                                                                        x_temp[selected[3]],
                                                                        x_lower,
                                                                        x_upper,
                                                                        n_dimensions,
                                                                        f_scale,
                                                                        none_variable)
                report += report_mov

            # Crossover
            x_i_temp, of_i_temp,\
                fit_i_temp, neof,\
                report_mov = de_movement_01(obj_function,
                                            p_c,
                                            x_pop[pop],
                                            x_i_temp,
                                            n_dimensions,
                                            x_lower,
                                            x_upper,
                                            none_variable)
            report += report_mov

            # Update neof (Number of Objective Function Evaluations)
            neof_count += neof

            # New design variables
            if fit_i_temp > fit_pop[pop]:
                report += "    fit_i_temp > fit_pop[pop] - accept this solution\n"
                x_pop[pop] = x_i_temp.copy()
                of_pop[pop] = of_i_temp
                fit_pop[pop] = fit_i_temp
            else:
                report += "    fit_i_temp < fit_pop[pop] - not accept this solution\n"              
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
                report += f'x{i_pop} = {x_pop[i_pop]}, of_pop {of_pop[i_pop]} - best solution\n'
            else:
                report += f'x{i_pop} = {x_pop[i_pop]}, of_pop {of_pop[i_pop]} \n'
        progress_bar.update()        

    # Time markup
    end_time = time.time()
    delta_time = end_time - initial_time

    # Storage all values in DataFrame
    df_all = pd.concat(all_data_pop, ignore_index=True)

    # Storage best values in DataFrame
    df_best = pd.concat(resume_result, ignore_index=True)

    return df_all, df_best, delta_time, report
