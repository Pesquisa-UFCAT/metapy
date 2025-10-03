"""Gray Wolf related functions."""
from typing import Callable, Optional, Union, List, Dict, Tuple

import numpy as np
import pandas as pd

from metapy_toolbox import funcs


def gray_wolf_hunting(parent_0: list, parent_1: list, x_lower: list, x_upper: list) -> tuple[list, list, list, str]:
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


def grey_wolf_optimizer_01(obj: Callable, n_gen: int, params: dict, initial_population: list, x_lower: list, x_upper: list, args: Optional[tuple] = None, robustness: Union[bool, dict] = False) -> tuple[pd.DataFrame, pd.DataFrame, str]:
    """
    Grey Wolf Optimizer 01.

    :param obj: The objective function: obj(x, args) -> float or obj(x) -> float, where x is a list with shape dim and args is a tuple fixed parameters needed to completely specify the function
    :param n_gen: Number of generations or iterations
    :param params: Parameters of Grey Wolf Algorithm
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

    # Initial population evaluation (Don't remove this part)
    for n in range(n_pop):
        aux_df = funcs.evaluation(obj, n, x_t0[n], 0, args=args) if args is not None else funcs.evaluation(obj, n, x_t0[n], 0)
        all_results.append(aux_df)
    df = pd.concat(all_results, ignore_index=True)
    df['REPORT'] = ""
    df['OF EVALUATIONS'] = 1
    print(df)

    # Parameters of Grey Wolf Optimizer (Adapt this part if you add new parameters for your version of the algorithm)
    a = 2
    aa = []
    cc = []
    for j in range(d):
        aa.append(2 * a * np.random.uniform(0, 1) - a)
        cc.append(2 * np.random.uniform(0, 1))
    print(aa, cc)

    # # Personal history information (Don't remove this part)
    # for j in range(d):
    #     df.loc[:, 'P_X_BEST_' + str(j)] = df.loc[:, 'X_' + str(j)]
    # df.loc[:, 'P_OF_BEST'] = df.loc[:, 'OF']

    # # Iterations
    # report = "Genetic Algorithm\n" # (Don't remove this part - Give the name of the algorithm)
    # for t in range(1, n_gen + 1):
    #     # Select t-1 population and last evaluation count (Don't remove this part)
    #     report += f"iteration: {t}\n"
    #     df_aux = df[df['ITER'] == t-1]
    #     df_aux = df_aux.reset_index(drop=True)
    #     aux_t = []
    #     df_copy = df.copy()
    #     bests.append(funcs.best_avg_worst(df_aux, d))

    #     # Population movement (Don't remove this part)
    #     for i in range(n_pop):
    #         report += f" Agent id: {i}\n" # (Don't remove this part)

    #         # GA movement: Selection
    #         if selection_type == 'roulette wheel' or selection_type == 'roulette_wheel' or selection_type == 'roulettewheel' or selection_type == 'roulette-wheel':
    #             fit_pop = df_aux['FIT'].tolist()
    #             i_selected, report_selection = roulette_wheel_selection(fit_pop, i)
    #         else:
    #             # fallback: tournament selection (if implemented elsewhere)
    #             i_selected = None
    #             report_selection = "    Selection operator - not roulette wheel and other not implemented\n"
    #         report += report_selection

    #         # GA movement: Crossover
    #         random_value = np.random.uniform(low=0, high=1)
    #         # linear (existing)
    #         if crossover_type == 'linear':
    #             if random_value <= p_c:
    #                 # Query agents information from dataframe
    #                 current_x, _, _ = funcs.query_x_of_fit_from_data(df_aux, i, d)
    #                 parent_1_x, _, _ = funcs.query_x_of_fit_from_data(df_aux, i_selected, d)
    #                 n_evals = 3 # Three new solutions will be evaluated after crossover
    #                 ch_a, ch_b, ch_c, report_crossover = linear_crossover(current_x, parent_1_x, x_lower, x_upper)
    #                 aux_df_a = funcs.evaluation(obj, i, ch_a, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_a, t)
    #                 df_temp = funcs.compare_and_save(df_aux[df_aux['ID'] == i], aux_df_a)
    #                 aux_df_b = funcs.evaluation(obj, i, ch_b, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_b, t)
    #                 df_temp = funcs.compare_and_save(df_temp, aux_df_b)
    #                 aux_df_c = funcs.evaluation(obj, i, ch_c, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_c, t)
    #                 df_temp = funcs.compare_and_save(df_temp, aux_df_c)
    #                 df_temp.loc[:, 'OF EVALUATIONS'] = n_evals
    #             else:
    #                 n_evals = 0 # No new solution will be evaluated after crossover
    #                 df_temp = df_aux[df_aux['ID'] == i].copy()
    #                 df_temp.loc[:, 'ITER'] = t
    #                 df_temp.loc[:, 'OF EVALUATIONS'] = n_evals
    #                 df_temp.loc[:, 'TIME CONSUMPTION (s)'] = 0
    #                 report_crossover = "    Crossover operator - Linear crossover\n"
    #                 report_crossover += "    Crossover not performed\n"

    #         # blx-alpha (existing)
    #         elif crossover_type ==tests/examples_ga.ipynb
    #                 n_evals = 0 # No new solution will be evaluated after crossover
    #                 df_temp = df_aux[df_aux['ID'] == i].copy()
    #                 df_temp.loc[:, 'ITER'] = t
    #                 df_temp.loc[:, 'OF EVALUATIONS'] = n_evals
    #                 df_temp.loc[:, 'TIME CONSUMPTION (s)'] = 0
    #                 report_crossover = "    Crossover operator - BLX-alpha\n"
    #                 report_crossover += "    Crossover not performed\n"

    #         # heuristic (new)
    #         elif crossover_type == 'heuristic':
    #             if random_value <= p_c:
    #                 current_x, _, _ = funcs.query_x_of_fit_from_data(df_aux, i, d)
    #                 parent_1_x, _, _ = funcs.query_x_of_fit_from_data(df_aux, i_selected, d)
    #                 n_evals = 2
    #                 ch_a, ch_b, report_crossover = heuristic_crossover(current_x, parent_1_x, d, x_upper, x_lower)
    #                 aux_df_a = funcs.evaluation(obj, i, ch_a, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_a, t)
    #                 df_temp = funcs.compare_and_save(df_aux[df_aux['ID'] == i], aux_df_a)
    #                 aux_df_b = funcs.evaluation(obj, i, ch_b, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_b, t)
    #                 df_temp = funcs.compare_and_save(df_temp, aux_df_b)
    #                 df_temp.loc[:, 'OF EVALUATIONS'] = n_evals
    #             else:
    #                 n_evals = 0
    #                 df_temp = df_aux[df_aux['ID'] == i].copy()
    #                 df_temp.loc[:, 'ITER'] = t
    #                 df_temp.loc[:, 'OF EVALUATIONS'] = n_evals
    #                 df_temp.loc[:, 'TIME CONSUMPTION (s)'] = 0
    #                 report_crossover = "    Crossover operator - Heuristic crossover\n"
    #                 report_crossover += "    Crossover not performed\n"

    #         # simulated binary (new)
    #         elif crossover_type == 'simulated_binary' or crossover_type == 'simulated-binary' or crossover_type == 'sbx':
    #             eta_c = params['crossover'].get('eta_c', 20)
    #             if random_value <= p_c:
    #                 current_x, _, _ = funcs.query_x_of_fit_from_data(df_aux, i, d)
    #                 parent_1_x, _, _ = funcs.query_x_of_fit_from_data(df_aux, i_selected, d)
    #                 n_evals = 2
    #                 ch_a, ch_b, report_crossover = simulated_binary_crossover(current_x, parent_1_x, eta_c, d, x_upper, x_lower)
    #                 aux_df_a = funcs.evaluation(obj, i, ch_a, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_a, t)
    #                 df_temp = funcs.compare_and_save(df_aux[df_aux['ID'] == i], aux_df_a)
    #                 aux_df_b = funcs.evaluation(obj, i, ch_b, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_b, t)
    #                 df_temp = funcs.compare_and_save(df_temp, aux_df_b)
    #                 df_temp.loc[:, 'OF EVALUATIONS'] = n_evals
    #             else:
    #                 n_evals = 0
    #                 df_temp = df_aux[df_aux['ID'] == i].copy()
    #                 df_temp.loc[:, 'ITER'] = t
    #                 df_temp.loc[:, 'OF EVALUATIONS'] = n_evals
    #                 df_temp.loc[:, 'TIME CONSUMPTION (s)'] = 0
    #                 report_crossover = "    Crossover operator - Simulated binary crossover\n"
    #                 report_crossover += "    Crossover not performed\n"

    #         # arithmetic (new)
    #         elif crossover_type == 'arithmetic':
    #             if random_value <= p_c:
    #                 current_x, _, _ = funcs.query_x_of_fit_from_data(df_aux, i, d)
    #                 parent_1_x, _, _ = funcs.query_x_of_fit_from_data(df_aux, i_selected, d)
    #                 n_evals = 2
    #                 ch_a, ch_b, report_crossover = arithmetic_crossover(current_x, parent_1_x, d, x_upper, x_lower)
    #                 aux_df_a = funcs.evaluation(obj, i, ch_a, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_a, t)
    #                 df_temp = funcs.compare_and_save(df_aux[df_aux['ID'] == i], aux_df_a)
    #                 aux_df_b = funcs.evaluation(obj, i, ch_b, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_b, t)
    #                 df_temp = funcs.compare_and_save(df_temp, aux_df_b)
    #                 df_temp.loc[:, 'OF EVALUATIONS'] = n_evals
    #             else:
    #                 n_evals = 0
    #                 df_temp = df_aux[df_aux['ID'] == i].copy()
    #                 df_temp.loc[:, 'ITER'] = t
    #                 df_temp.loc[:, 'OF EVALUATIONS'] = n_evals
    #                 df_temp.loc[:, 'TIME CONSUMPTION (s)'] = 0
    #                 report_crossover = "    Crossover operator - Arithmetic crossover\n"
    #                 report_crossover += "    Crossover not performed\n"

    #         # laplace (new)
    #         elif crossover_type == 'laplace':
    #             mu = params['crossover'].get('mu', 0.0)
    #             sigma = params['crossover'].get('sigma', 1.0)
    #             if random_value <= p_c:
    #                 current_x, _, _ = funcs.query_x_of_fit_from_data(df_aux, i, d)
    #                 parent_1_x, _, _ = funcs.query_x_of_fit_from_data(df_aux, i_selected, d)
    #                 n_evals = 2
    #                 ch_a, ch_b, report_crossover = laplace_crossover(current_x, parent_1_x, mu, sigma, d, x_upper, x_lower)
    #                 aux_df_a = funcs.evaluation(obj, i, ch_a, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_a, t)
    #                 df_temp = funcs.compare_and_save(df_aux[df_aux['ID'] == i], aux_df_a)
    #                 aux_df_b = funcs.evaluation(obj, i, ch_b, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_b, t)
    #                 df_temp = funcs.compare_and_save(df_temp, aux_df_b)
    #                 df_temp.loc[:, 'OF EVALUATIONS'] = n_evals
    #             else:
    #                 n_evals = 0
    #                 df_temp = df_aux[df_aux['ID'] == i].copy()
    #                 df_temp.loc[:, 'ITER'] = t
    #                 df_temp.loc[:, 'OF EVALUATIONS'] = n_evals
    #                 df_temp.loc[:, 'TIME CONSUMPTION (s)'] = 0
    #                 report_crossover = "    Crossover operator - Laplace crossover\n"
    #                 report_crossover += "    Crossover not performed\n"

    #         # uniform (new)
    #         elif crossover_type == 'uniform':
    #             if random_value <= p_c:
    #                 current_x, _, _ = funcs.query_x_of_fit_from_data(df_aux, i, d)
    #                 parent_1_x, _, _ = funcs.query_x_of_fit_from_data(df_aux, i_selected, d)
    #                 n_evals = 2
    #                 ch_a, ch_b, report_crossover = uniform_crossover(current_x, parent_1_x, d, x_upper, x_lower)
    #                 aux_df_a = funcs.evaluation(obj, i, ch_a, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_a, t)
    #                 df_temp = funcs.compare_and_save(df_aux[df_aux['ID'] == i], aux_df_a)
    #                 aux_df_b = funcs.evaluation(obj, i, ch_b, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_b, t)
    #                 df_temp = funcs.compare_and_save(df_temp, aux_df_b)
    #                 df_temp.loc[:, 'OF EVALUATIONS'] = n_evals
    #             else:
    #                 n_evals = 0
    #                 df_temp = df_aux[df_aux['ID'] == i].copy()
    #                 df_temp.loc[:, 'ITER'] = t
    #                 df_temp.loc[:, 'OF EVALUATIONS'] = n_evals
    #                 df_temp.loc[:, 'TIME CONSUMPTION (s)'] = 0
    #                 report_crossover = "    Crossover operator - Uniform crossover\n"
    #                 report_crossover += "    Crossover not performed\n"

    #         # binomial (new)
    #         elif crossover_type == 'binomial':
    #             # gene-level probability used inside binomial operator (default 0.5)
    #             gene_prob = params['crossover'].get('p_c_gene', 0.5)
    #             if random_value <= p_c:
    #                 current_x, _, _ = funcs.query_x_of_fit_from_data(df_aux, i, d)
    #                 parent_1_x, _, _ = funcs.query_x_of_fit_from_data(df_aux, i_selected, d)
    #                 n_evals = 2
    #                 ch_a, ch_b, report_crossover = binomial_crossover(current_x, parent_1_x, gene_prob, d, x_upper, x_lower)
    #                 aux_df_a = funcs.evaluation(obj, i, ch_a, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_a, t)
    #                 df_temp = funcs.compare_and_save(df_aux[df_aux['ID'] == i], aux_df_a)
    #                 aux_df_b = funcs.evaluation(obj, i, ch_b, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_b, t)
    #                 df_temp = funcs.compare_and_save(df_temp, aux_df_b)
    #                 df_temp.loc[:, 'OF EVALUATIONS'] = n_evals
    #             else:
    #                 n_evals = 0
    #                 df_temp = df_aux[df_aux['ID'] == i].copy()
    #                 df_temp.loc[:, 'ITER'] = t
    #                 df_temp.loc[:, 'OF EVALUATIONS'] = n_evals
    #                 df_temp.loc[:, 'TIME CONSUMPTION (s)'] = 0
    #                 report_crossover = "    Crossover operator - Binomial crossover\n"
    #                 report_crossover += "    Crossover not performed\n"

    #         # unknown crossover type
    #         else:
    #             # default: no crossover performed
    #             n_evals = 0
    #             df_temp = df_aux[df_aux['ID'] == i].copy()
    #             df_temp.loc[:, 'ITER'] = t
    #             df_temp.loc[:, 'OF EVALUATIONS'] = n_evals
    #             df_temp.loc[:, 'TIME CONSUMPTION (s)'] = 0
    #             report_crossover = f"    Crossover operator - {crossover_type}\n"
    #             report_crossover += "    Crossover type not implemented in GA main loop; no crossover performed\n"

    #         report += report_crossover

    #         # GA movement: Mutation
    #         if mutation_type == 'random walk' or mutation_type == 'random_walk' or mutation_type == 'randomwalk' or mutation_type == 'random-walk':
    #             random_value = np.random.uniform(low=0, high=1)
    #             if random_value <= p_m:
    #                 n_evals_old = df_temp['OF EVALUATIONS'].values[0]
    #                 n_evals = 1 # One new solution will be evaluated after mutation
    #                 current_x, _, _ = funcs.query_x_of_fit_from_data(df_temp, i, d)
    #                 ch_a, report_mutation = funcs.mutation_01_random_walk(current_x, pdf, cov, x_lower, x_upper)
    #                 aux_df_a = funcs.evaluation(obj, i, ch_a, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_a, t)
    #                 df_temp = funcs.compare_and_save(df_temp[df_temp['ID'] == i], aux_df_a)
    #                 df_temp['OF EVALUATIONS'] = n_evals + n_evals_old
    #             else:
    #                 report_mutation = "    Mutation operator - Random walk\n"
    #                 report_mutation += "    Mutation not performed\n"
    #         report += report_mutation

    #         # Robustness evaluation (Don't remove this part)
    #         if isinstance(robustness, dict):
    #             report += "    Robustness evaluation\n"
    #             n_evals_old = df_temp['OF EVALUATIONS'].values[0]
    #             current_x, _, _ = funcs.query_x_of_fit_from_data(df_temp, i, d)
    #             avg_of = df_temp['OF'].values[0]
    #             avg_fit = df_temp['FIT'].values[0]
    #             for _ in range(robustness['n evals']):
    #                 ch_a, report_mutation = funcs.mutation_01_random_walk(current_x, 'uniform', robustness['perturbation (%)'], x_lower, x_upper)
    #                 aux_df_a = funcs.evaluation(obj, i, ch_a, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_a, t)
    #                 report += report_mutation
    #                 avg_of += aux_df_a['OF'].values[0]
    #                 avg_fit += aux_df_a['FIT'].values[0]
    #             df_temp.loc[:, 'FIT'] = avg_fit / (robustness['n evals'] + 1)
    #             df_temp.loc[:, 'OF'] = avg_of / (robustness['n evals'] + 1)
    #             df_temp.loc[:, 'OF EVALUATIONS'] = robustness['n evals'] + n_evals_old

    #         # Save final values of the i-th agent in t time step (Don't remove this part)
    #         aux_t.append(df_temp)

    #     # Update dataframe (Don't remove this part)
    #     df = pd.concat([df_copy] + aux_t, ignore_index=True)

    #     # Update personal history information (Don't remove this part)
    #     df_past = df[df['ITER'] == t-1]
    #     df_past = df_past.reset_index(drop=True)
    #     df_current = df[df['ITER'] == t]
    #     df_current = df_current.reset_index(drop=True)
    #     masks = np.where(df_current['OF'] < df_past['P_OF_BEST'], 1, 0)
    #     cont = 0
    #     for t_aux in range(n_pop * t, n_pop * t + n_pop, 1):
    #         if masks[cont] == 1:
    #             for j in range(d):
    #                 df.loc[t_aux, 'P_X_BEST_' + str(j)] = df_current['X_' + str(j)].values[cont]
    #             df.loc[t_aux, 'P_OF_BEST'] = df_current['OF'].values[cont]
    #         else:
    #             for j in range(d):
    #                 df.loc[t_aux, 'P_X_BEST_' + str(j)] = df_past['P_X_BEST_' + str(j)].values[cont]
    #             df.loc[t_aux, 'P_OF_BEST'] = df_past['P_OF_BEST'].values[cont]
    #         cont += 1

    # # Final best, average and worst (Don't remove this part)
    # dfj = df[df['ITER'] == n_gen]
    # dfj = dfj.reset_index(drop=True)
    # bests.append(funcs.best_avg_worst(dfj, d))
    # df_resume = pd.concat(bests, ignore_index=True)
    # df['REPORT'] = report
    # for t in range(n_gen + 1):
    #     df_resume.loc[t, 'OF EVALUATIONS'] = df[df['ITER'] == t]['OF EVALUATIONS'].sum()
    #     df_resume.loc[t, 'TIME CONSUMPTION (s)'] = df[df['ITER'] == t]['TIME CONSUMPTION (s)'].sum()
    # df_resume['OF EVALUATIONS'] = df_resume['OF EVALUATIONS'].cumsum()
    # df_resume['TIME CONSUMPTION (s)'] = df_resume['TIME CONSUMPTION (s)'].cumsum()

    return 'oi' # df, df_resume, df['REPORT'].iloc[-1]