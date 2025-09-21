"""Genetic Algorithm related functions."""
import numpy as np
import pandas as pd
from typing import Callable, Optional
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


def genetic_algorithm_01(obj: Callable, n_gen: int, params: dict, initial_population: list, x_lower: list, x_upper: list, args: Optional[tuple] = None):
    """
    Genetic algorithm.

    :param obj: The objective function: obj(x, args) -> float or obj(x) -> float, where x is a list with shape dim and args is a tuple fixed parameters needed to completely specify the function
    :param n_gen: Number of generations or iterations
    :param params: Parameters of Genetic Algorithm
    :param initial_population: Initial population
    :param x_lower: Lower limit of the design variables
    :param x_upper: Upper limit of the design variables
    :param args: Extra arguments to pass to the objective function (optional)

    :return: dictionary with results
    """

    # Initialize variables and dataframes (Don't remove this part)
    x_t0 = initial_population.copy()
    d = len(x_t0[0])
    n_pop = len(x_t0)
    all_results = []
    bests = []
    rob = params['robustness'] 

    # Parameters of Genetic Algorithm (Adapt this part if you add new parameters for your version of the algorithm)
    selection_type = params['selection']
    crossover_type = params['crossover']['type']
    p_c = params['crossover']['crossover rate (%)'] / 100
    mutation_type = params['mutation']['type']
    p_m = params['mutation']['mutation rate (%)'] / 100

    # Initial population evaluation (Don't remove this part)
    for n in range(n_pop):
        aux_df = funcs.evaluation(obj, n, x_t0[n], n, 0, args=args) if args is not None else funcs.evaluation(obj, n, x_t0[n], n, 0)
        all_results.append(aux_df)
    df = pd.concat(all_results, ignore_index=True)
    df['REPORT'] = ""

    # Personal history information (Don't remove this part)
    for j in range(d):
        df.loc[:, 'P_X_BEST_' + str(j)] = df.loc[:, 'X_' + str(j)]
    df.loc[:, 'P_OF_BEST'] = df.loc[:, 'OF']

    # Iterations
    report = "Genetic Algorithm\n"
    for t in range(1, n_gen + 1):
        # Select t-1 population and last evaluation count (Don't remove this part)
        report += f"iteration: {t}\n"
        df_aux = df[df['ITER'] == t-1]
        df_aux = df_aux.reset_index(drop=True)
        aux_t = []
        df_copy = df.copy()
        n_evals = df['OF EVALUATIONS'].values[-1]
        bests.append(funcs.best_avg_worst(df_aux, d))

        # Population movement (Don't remove this part)
        for i in range(n_pop):
            report += f" Agent id: {i}\n"

            # GA movement: Selection
            if selection_type == 'roulette wheel':
                fit_pop = df_aux['FIT'].tolist()
                i_selected, report_selection = roulette_wheel_selection(fit_pop, i)
            else:
                pass
            report += report_selection

            # GA movement: Crossover
            # Query agents information from dataframe
            current_x, _, _ = funcs.query_x_of_fit_from_data(df_aux, i, d)
            parent_1_x, _, _ = funcs.query_x_of_fit_from_data(df_aux, i_selected, d)
            if crossover_type == 'linear':
                random_value = np.random.uniform(low=0, high=1)
                if random_value <= p_c:
                    n_evals += 3 # Three new solutions will be evaluated after crossover
                    ch_a, ch_b, ch_c, report_crossover = linear_crossover(current_x, parent_1_x, x_lower, x_upper)
                    aux_df_a = funcs.evaluation(obj, i, ch_a, n_evals, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_a, n_evals, t)
                    df_temp = funcs.compare_and_save(df_aux[df_aux['ID'] == i], aux_df_a)
                    aux_df_b = funcs.evaluation(obj, i, ch_b, n_evals, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_b, n_evals, t)
                    df_temp = funcs.compare_and_save(df_temp, aux_df_b)
                    aux_df_c = funcs.evaluation(obj, i, ch_c, n_evals, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_c, n_evals, t)
                    df_temp = funcs.compare_and_save(df_temp, aux_df_c)
                else:
                    n_evals += 0 # No new solution will be evaluated after crossover
                    df_temp = df_aux[df_aux['ID'] == i].copy()
                    df_temp.loc[:, 'ITER'] = t
                    df_temp.loc[:, 'OF EVALUATIONS'] = n_evals
                    report_crossover = "    Crossover operator - Linear crossover\n"
                    report_crossover += "    Crossover not performed\n"
            report += report_crossover

            # GA movement: Mutation
            if mutation_type == 'uniform':
                random_value = np.random.uniform(low=0, high=1)
                if random_value <= p_m:
                    n_evals += 1 # One new solution will be evaluated after mutation
            #         ch_a, ch_b, ch_c, report_crossover = linear_crossover(current_x, parent_1_x, x_lower, x_upper)
            #         aux_df_a = funcs.evaluation(obj, i, ch_a, n_evals, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_a, n_evals, t)
            #         df_temp = funcs.compare_and_save(df_aux[df_aux['ID'] == i], aux_df_a)
            #         aux_df_b = funcs.evaluation(obj, i, ch_b, n_evals, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_b, n_evals, t)
            #         df_temp = funcs.compare_and_save(df_temp, aux_df_b)
            #         aux_df_c = funcs.evaluation(obj, i, ch_c, n_evals, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_c, n_evals, t)
            #         df_temp = funcs.compare_and_save(df_temp, aux_df_c)
            #     else:
            #         n_evals += 0
            #         df_temp = df_aux[df_aux['ID'] == i].copy()
            #         df_temp.loc[:, 'ITER'] = t
            #         df_temp.loc[:, 'OF EVALUATIONS'] = n_evals

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

    return df, df_resume, df['REPORT'].iloc[-1]

