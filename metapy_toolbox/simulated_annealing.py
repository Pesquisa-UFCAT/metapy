"""simulated annealing functions"""
import time

import numpy as np
import pandas as pd
from tqdm import tqdm

import metapy_toolbox.common_library as metapyco


def start_temperature(n_population, obj_function, x_pop, of_pop, x_lower, x_upper, n_dimensions, pdf, cov, none_variable):
    """ 
    This function calculates the initial temperature with an acceptance rate greater than 80% of the initial solutions. Fixed at 500 attempts.

    Args:
        n_population (Integer): Number of population
        obj_function (Py function (def)): Objective function. The Metapy user defined this function
        x_pop (List): Population design variables
        of_pop (List): Population objective function values
        x_lower (List): Lower limit of the design variables
        x_upper (List): Upper limit of the design variables
        n_dimensions (Integer): Problem dimension
        pdf (String): Probability density function. Options: 'gaussian' or 'uniform'
        cov (Float): Coefficient of variation in percentage
        none_variable (None, list, float, dictionary, str or any): None variable. User can use this variable in objective function
    
    Returns:
        t_0mean (Float): Initial temperature.
        report (String): Report of the initial temperature calculation.
    """

    report = "\nAutomotic initial temperature\n"
    t_0 = []
    for i in range(500):
        # Trial opulation movement
        for pop in range(n_population):
            _, of_i_temp, _, _, _ = metapyco.mutation_01_hill_movement(obj_function, x_pop[pop],
                                                                    x_lower, x_upper,
                                                                    n_dimensions,
                                                                    pdf, cov,
                                                                    none_variable)

            # Probability of acceptance of the movement
            delta_energy = of_i_temp - of_pop[pop]
            if delta_energy < 0:
                pass       
            elif delta_energy >= 0:
                t_0.append(-delta_energy / np.log(0.8))
    t_0mean = sum(t_0)/len(t_0)
    report += f"    sum_t0 = {sum(t_0)}, number of accepted moves (delta_e > 0) = {len(t_0)}, t_mean = {t_0mean}\n"

    return t_0mean, report


def hill_climbing_01(settings):
    """
    Hill Climbing algorithm 01.
    
    Args:  
        settings (List): [0] setup (Dictionary), [1] initial population (List or METApy function), [2] seeds (None or integer)
        'number of population' (Integer): number of population (key in setup Dictionary)
        'number of iterations' (Integer): number of iterations (key in setup Dictionary)
        'number of dimensions' (Integer): Problem dimension (key in setup Dictionary)
        'x pop lower limit' (List): Lower limit of the design variables (key in setup Dictionary)
        'x pop upper limit' (List): Upper limit of the design variables (key in setup Dictionary)
        'none_variable' (None, list, float, dictionary, str or any): None variable. Default is None. User can use this variable in objective function (key in setup Dictionary)
        'objective function' (Py function [def]): Objective function. The Metapy user defined this function (key in setup Dictionary)                                          
        'algorithm parameters' (Dictionary): Algorithm parameters. See documentation (key in setup Dictionary)
        'mutation' (Dictionary): Mutation parameters (key in algorithm parameters Dictionary)
        initial population (List or METApy function): Users can inform the initial population or use initial population functions
        seed (None or integer): Random seed. Use None for random seed
    
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
    report = "Hill Climbing 01 - report \n\n"
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
    report += "\nIterations\n"
    progress_bar = tqdm(total=n_iterations, desc='Progress')
    for iter in range(n_iterations):
        report += f"\nIteration: {iter+1}\n"
        # Time markup
        initial_time = time.time()

        # Population movement
        for pop in range(n_population):
            report += f"Pop id: {pop} - particle movement - mutation procedure\n"
            # Hill Climbing particle movement
            x_i_temp, of_i_temp, \
                fit_i_temp, neof, \
                report_mov = metapyco.mutation_01_hill_movement(obj_function,
                                                        x_pop[pop],
                                                        x_lower, x_upper,
                                                        n_dimensions,
                                                        pdf, std,
                                                        none_variable)
            report += report_mov
            i_pop_solution = metapyco.resume_all_data_in_dataframe(x_i_temp, of_i_temp,
                                                                   fit_i_temp,
                                                                   columns_all_data,
                                                                   iteration=iter+1)
            all_data_pop.append(i_pop_solution)

            # New design variables
            if fit_i_temp > fit_pop[pop]:
                report += f"    fit_i_temp={fit_i_temp} > fit_pop[pop]={fit_pop[pop]} - accept this solution\n"
                x_pop[pop] = x_i_temp.copy()
                of_pop[pop] = of_i_temp
                fit_pop[pop] = fit_i_temp
            else:
                report += f"    fit_i_temp={fit_i_temp} < fit_pop[pop]={fit_pop[pop]} - not accept this solution\n"

            # Update neof (Number of Objective Function Evaluations)
            neof_count += neof

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
                report += f'x{i_pop} = {x_pop[i_pop]}, of_pop {of_pop[i_pop]}  \n'
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


def simulated_annealing_01(settings):
    """
    Simulated Annealing algorithm 01.
    
    Args:  
        settings (List): [0] setup (Dictionary), [1] initial population (List or METApy function), [2] seeds (None or integer)
        'number of population' (Integer): number of population (key in setup Dictionary)
        'number of iterations' (Integer): number of iterations (key in setup Dictionary)
        'number of dimensions' (Integer): Problem dimension (key in setup Dictionary)
        'x pop lower limit' (List): Lower limit of the design variables (key in setup Dictionary)
        'x pop upper limit' (List): Upper limit of the design variables (key in setup Dictionary)
        'none_variable' (None, list, float, dictionary, str or any): None variable. Default is None. User can use this variable in objective function (key in setup Dictionary)
        'objective function' (Py function [def]): Objective function. The Metapy user defined this function (key in setup Dictionary)                                          
        'algorithm parameters' (Dictionary): Algorithm parameters. See documentation (key in setup Dictionary)
        'temp. control' (Dictionary): Temperature parameters (key in algorithm parameters Dictionary)
        'mutation' (Dictionary): Mutation parameters (key in algorithm parameters Dictionary)
        initial population (List or METApy function): Users can inform the initial population or use initial population functions
        seed (None or integer): Random seed. Use None for random seed
    
    Returns:
        df_all (Dataframe): All data of the population.
        df_best (Dataframe): Best data of the population.
        delta_time (Float): Time of the algorithm execution in seconds.
        report (String): Report of the algorithm execution.
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
    std = algorithm_parameters['mutation']['cov (%)']
    pdf = algorithm_parameters['mutation']['pdf']
    temperature = algorithm_parameters['temp. control']['temperature t_0']
    schedule = algorithm_parameters['temp. control']['temperature update']
    alpha = algorithm_parameters['temp. control']['alpha']

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
    report = "Simulated Annealing 01 - report \n\n"
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

    # Initial temperature
    if temperature == 'auto':
        temperature, report_move = start_temperature(n_population,
                                            obj_function, x_pop,
                                            of_pop, x_lower, x_upper,
                                            n_dimensions, pdf, std,
                                            none_variable)
        report += report_move
    else:
        pass

    # Iteration procedure
    report += "\nIterations\n"
    progress_bar = tqdm(total=n_iterations, desc='Progress')
    for iter in range(n_iterations):
        report += f"\nIteration: {iter+1}\n"
        report += f"Temperature: {temperature}\n"
        # Time markup
        initial_time = time.time()

        # Population movement
        for pop in range(n_population):
            report += f"Pop id: {pop} - particle movement - mutation procedure\n"
            # Hill Climbing particle movement
            x_i_temp, of_i_temp, \
                fit_i_temp, neof, \
                report_mov = metapyco.mutation_01_hill_movement(obj_function,
                                                        x_pop[pop],
                                                        x_lower, x_upper,
                                                        n_dimensions,
                                                        pdf, std,
                                                        none_variable)
            report += report_mov
            i_pop_solution = metapyco.resume_all_data_in_dataframe(x_i_temp, of_i_temp,
                                                                   fit_i_temp,
                                                                   columns_all_data,
                                                                   iteration=iter+1)
            all_data_pop.append(i_pop_solution)

            # Probability of acceptance of the movement
            delta_energy = of_i_temp - of_pop[pop]
            if delta_energy < 0:
                prob_state = 1
            elif delta_energy >= 0:
                prob_state = np.exp(-delta_energy/temperature)
            report += f"    energy = {delta_energy}, prob. state = {prob_state}\n"

            # New design variables
            random_number = np.random.random()
            if random_number <= prob_state:
                report += f"    random number={random_number} <= prob. state={prob_state} - accept this solution\n"
                x_pop[pop] = x_i_temp.copy()
                of_pop[pop] = of_i_temp
                fit_pop[pop] = fit_i_temp
            else:
                report += f"    random number={random_number} > prob. state={prob_state} - not accept this solution\n"

            # Update neof (Number of Objective Function Evaluations)
            neof_count += neof

        # Update temperature
        # Geometric cooling scheme
        if schedule.upper() == 'GEOMETRIC':
            temperature = temperature*alpha
        # Lundy cooling scheme
        elif schedule.upper() == 'LUNDY':
            temperature = temperature / (1+alpha*temperature)
        # Linear cooling scheme
        elif schedule.upper() == 'LINEAR' or schedule.upper() == 'ARITHMETIC':
            temperature = temperature - alpha*temperature
        # Logarithmic cooling scheme
        elif schedule.upper() == 'EXPONENTIAL':
            temperature = temperature * np.exp(-alpha*(1+iter))

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
    progress_bar.close()

    return df_all, df_best, delta_time, report
