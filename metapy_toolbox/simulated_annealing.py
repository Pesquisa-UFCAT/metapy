"""simulated annealing functions"""
import time

import numpy as np
import pandas as pd

from tqdm import tqdm
from typing import Callable, Any, List, Tuple, Union

import metapy_toolbox.common_library as metapyco


def start_temperature(n_population: int, obj_function: Callable[[List[float], Any], float], x_pop: List[List[float]], of_pop: List[float], x_lower: List[float], x_upper: List[float], n_dimensions: int, pdf: str, cov: float, none_variable: Any) -> Tuple[float, str]:
    """ 
    This function calculates the initial temperature with an acceptance rate greater than 80% of the initial solutions. Fixed at 500 attempts.

    :param n_population: Number of individuals in the population.
    :param obj_function: Objective function to evaluate the solutions.
    :param x_pop: Current population design variables.
    :param of_pop: Objective function values for the current population.
    :param x_lower: Lower bounds for each decision variable.
    :param x_upper: Upper bounds for each decision variable.
    :param n_dimensions: Number of dimensions (design variables).
    :param pdf: Probability density function used for mutation ('gaussian' or 'uniform').
    :param cov: Coefficient of variation in percentage.
    :param none_variable: Optional parameter passed to the objective function.

    :return: 

        - t_0mean: Calculated initial temperature.
        - report: Textual report with details of the initial temperature calculation.
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


def hill_climbing_01(settings: List[Union[dict, List[List[float]], Union[int, None]]]) -> Tuple[pd.DataFrame, pd.DataFrame, float, str]:
    """
    Hill Climbing algorithm 01.

    :param settings: A list with three elements:

        1. **setup (dict)** – Dictionary with configuration keys:
            - 'number of population': int, number of individuals in the population
            - 'number of iterations': int, number of algorithm iterations
            - 'number of dimensions': int, problem dimensionality
            - 'x pop lower limit': list[float], lower bounds for the design variables
            - 'x pop upper limit': list[float], upper bounds for the design variables
            - 'none variable': any, optional variable passed to the objective function
            - 'objective function': callable, objective function to be minimized
            - 'algorithm parameters': dict, algorithm-specific configuration

        2. **initial population (list)** – A list of candidate solutions.

        3. **seed (int or None)** – Optional random seed for reproducibility.

    :return: Tuple with the following elements:

        - df_all (DataFrame): All population data over all iterations
        - df_best (DataFrame): Best solution data per iteration
        - delta_time (float): Execution time in seconds
        - report (str): Text report describing the population evolution
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


def simulated_annealing_01(settings: List[Union[dict, List[List[float]], Union[int, None]]]) -> Tuple[pd.DataFrame, pd.DataFrame, float, str]:
    """
    Simulated Annealing algorithm 01.

    :param settings: A list with three elements:

        1. **setup (dict)** – Dictionary with configuration keys:
            - 'number of population': int, size of the population
            - 'number of iterations': int, number of algorithm iterations
            - 'number of dimensions': int, dimensionality of the problem
            - 'x pop lower limit': list[float], lower bounds for each variable
            - 'x pop upper limit': list[float], upper bounds for each variable
            - 'none variable': any, optional auxiliary parameter for the objective function
            - 'objective function': callable, objective function to minimize
            - 'algorithm parameters': dict, includes mutation and temperature control parameters

        2. **initial population (list)** – List of individuals representing the initial population.

        3. **seed (int or None)** – Optional random seed for reproducibility.

    :return: Tuple with the following elements:

        - df_all (DataFrame): All population data throughout the iterations
        - df_best (DataFrame): Best individuals from each iteration
        - delta_time (float): Total execution time in seconds
        - report (str): Detailed execution report with operation logs
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
