"""differential evolution functions"""
import time
import numpy as np
import pandas as pd
import metapy_toolbox.common_library as metapyco

from tqdm import tqdm
from typing import Any, Callable, List, Optional, Tuple



def de_movement_01(obj_function: Callable, p_c: float, x_i_old: List[float], x_i_mutation: List[float], n_dimensions: int, x_lower: List[float], x_upper: List[float], none_variable: Optional[object] = None) -> Tuple[List[float], float, float, int, str]:
    """
    This function performs the differential evolution movement (binomial crossover).

    :param obj_function: User-defined objective function.
    :param p_c: Crossover probability.
    :param x_i_old: Current design variables of the i-th agent.
    :param x_i_mutation: Mutated design variables.
    :param n_dimensions: Number of design variables (problem dimension).
    :param x_lower: Lower bounds of the design variables.
    :param x_upper: Upper bounds of the design variables.
    :param none_variable: Optional variable to be passed to the objective function.

    :return: Tuple containing:

        - x_i_new: New design variables after crossover.
        - of_i_new: Objective function value of the new solution.
        - fit_i_new: Fitness value of the new solution.
        - neof: Number of objective function evaluations (always 1).
        - report: Text report of the crossover operation.
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


def differential_evolution_01(settings: List[Any]) -> Tuple[pd.DataFrame, pd.DataFrame, float, str]:
    """
    Differential Evolution algorithm 01.

    :param settings: A list with three elements:

        1. **setup (dict)** – Dictionary with DE configuration:
            - 'number of population': int, number of individuals in the population
            - 'number of iterations': int, number of generations
            - 'number of dimensions': int, number of decision variables
            - 'x pop lower limit': list[float], lower bounds
            - 'x pop upper limit': list[float], upper bounds
            - 'none variable': optional input passed to the objective function
            - 'objective function': callable, the objective function
            - 'algorithm parameters': dict with:
                - 'mutation': dict with:
                    - 'mutation rate (%)'
                    - 'type': e.g., 'de/rand/1'
                    - 'scale factor (F)'
                - 'crossover': dict with:
                    - 'crossover rate (%)'
                    - 'type': e.g., 'binomial'

        2. **initial population (list or callable)** – A list of individuals or a function to generate them.

        3. **seeds (int or None)** – Random seed or None for stochastic runs.

    :return: Tuple with the following elements:

        - df_all (DataFrame): All individuals over all iterations
        - df_best (DataFrame): Best/worst/average solution stats per iteration
        - delta_time (float): Time in seconds
        - report (str): Text report with execution trace
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
