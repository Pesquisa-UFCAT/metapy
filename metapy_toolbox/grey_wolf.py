"""Gray Wolf related functions."""
from typing import Callable, Optional, Union, List, Dict, Tuple

import numpy as np
import pandas as pd

from metapy_toolbox import funcs


def gray_wolf_hunting(parent_0: list, x_alpha: list, x_beta: list, x_delta: list, a: float,x_lower: list, x_upper: list) -> tuple[list, list, list, str]:
    """
    This function performs the Grey Wolf Hunting movement.

    :param parent_0: First parent. Current solution
    :param x_alpha: Position of the best wolf at the previous iteration
    :param x_beta: Position of the second best wolf at the previous iteration
    :param x_delta: Position of the third best wolf at the previous iteration
    :param a: Parameter that decreases linearly from 2 to 0 over the course of iterations
    :param x_lower: Lower limit of the design variables
    :param x_upper: Upper limit of the design variables

    :return: [0] = First offspring position, [1] = Second offspring position, [2] = Third offspring position, [3] = Report about the linear crossover process
    """

    # Start internal variables
    report_move = "    Crossover operator - Linear crossover\n"
    report_move += f"    current p0 = {parent_0}\n"
    report_move += f"    x_alpha = {x_alpha}\n"
    report_move += f"    x_beta = {x_beta}\n"
    report_move += f"    x_delta = {x_delta}\n"
    offspring_a = []

    # a e c update
    aa = []
    cc = []
    for j in range(len(parent_0)):
        aa.append(2 * a * np.random.uniform(0, 1) - a)
        cc.append(2 * np.random.uniform(0, 1))

    # Create D vector
    d_alpha = []
    for i in range(len(parent_0)):
        d_alpha.append(abs(cc[i]*x_alpha[i] - parent_0[i]))
    d_beta = []
    for i in range(len(parent_0)):
        d_beta.append(abs(cc[i]*x_beta[i] - parent_0[i]))
    d_delta = []
    for i in range(len(parent_0)):
        d_delta.append(abs(cc[i]*x_delta[i] - parent_0[i]))

    # x_alpha, x_beta, x_delta new positions
    x_alpha_new = []
    for i in range(len(parent_0)):
        x_alpha_new.append(x_alpha[i] - aa[i]*d_alpha[i])
    x_beta_new = []
    for i in range(len(parent_0)):
        x_beta_new.append(x_beta[i] - aa[i]*d_beta[i])
    x_delta_new = []
    for i in range(len(parent_0)):
        x_delta_new.append(x_delta[i] - aa[i]*d_delta[i])

    # New position
    offspring_a = []
    for i in range(len(parent_0)):
        offspring_a.append((x_alpha_new[i] + x_beta_new[i] + x_delta_new[i]) / 3)
    report_move += f"    New position = {offspring_a}\n"

    # Check bounds
    offspring_a = funcs.check_interval_01(offspring_a, x_lower, x_upper)

    return offspring_a, report_move


def n_best_solutions(df_iter: pd.DataFrame, n_best: int, d: int) -> pd.DataFrame:
    """
 
    """


    

    return top_n


def update_aa_cc(a: float, d: int):

    aa = []
    cc = []

    return aa, cc


def d_vector(a: float, parent_0: list, x_best: list) -> list:
    d = []
    return d

def x_new_position(parent_0: list, a: float, d_vector: list) -> list:
    x_new = []
    return x_new


    
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

    # Three best solution
    df_sorted = df.sort_values('FIT', ascending=False)
    top_3_first = df_sorted.head(3)
    print("Top 3 solutions based on fitness:")
    print(top_3)

    # Personal history information (Don't remove this part)
    for j in range(d):
        df.loc[:, 'P_X_BEST_' + str(j)] = df.loc[:, 'X_' + str(j)]
    df.loc[:, 'P_OF_BEST'] = df.loc[:, 'OF']

    # Evaluation diversity (Don't remove this part)
    df['DIVERSITY'] = funcs.diversity_evaluation(df, d)

    # Parameters of Grey Wolf Optimizer (Adapt this part if you add new parameters for your version of the algorithm)
    a = 2
    aa = []
    cc = []
    for j in range(d):
        aa.append(2 * a * np.random.uniform(0, 1) - a)
        cc.append(2 * np.random.uniform(0, 1))
    print(aa, cc)
    df['A'] = aa
    

    # Iterations
    report = "Gray Wolf Algorithm\n" # (Don't remove this part - Give the name of the algorithm)
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

            # Grey Wolf movement: Top n selection
            top_3 = top_3_first.copy()
            x_alpha, _, _ = funcs.query_x_of_fit_from_data(top_3, 0, d)
            x_beta, _, _ = funcs.query_x_of_fit_from_data(top_3, 1, d)
            x_delta, _, _ = funcs.query_x_of_fit_from_data(top_3, 2, d)

            # Grey Wolf movement: Crossover
            current_x, _, _ = funcs.query_x_of_fit_from_data(df_aux, i, d)
            ch_a, report_move = gray_wolf_hunting(current_x, x_alpha, x_beta, x_delta, a, x_lower, x_upper)
            aux_df_a = funcs.evaluation(obj, i, ch_a, t, args=args) if args is not None else funcs.evaluation(obj, i, ch_a, t)
            df_temp = funcs.compare_and_save(df_aux[df_aux['ID'] == i], aux_df_a)
            df_temp.loc[:, 'OF EVALUATIONS'] = 1
            report += report_move

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

    return 'oi' # df, df_resume, df['REPORT'].iloc[-1]