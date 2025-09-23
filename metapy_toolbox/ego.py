"""Efficient Global Optimization (EGO) related functions."""
from typing import Callable, Optional, Union

import numpy as np
import pandas as pd
import sklearn as sk
import scipy as sc

from metapy_toolbox import funcs, genetic_algorithm

def filter_improvements(df: pd.DataFrame, objective_column: str = 'OF', iteration_column: str = 'ITER', minimize: bool = True) -> pd.DataFrame:
    """
    Filters a dataframe in EGO algorithm and sort the values to keep only the improvements.

    :param df: Data with all evaluations

    :return: Data with only the improvements
    """
    
    result_df = pd.DataFrame()  # New DataFrame to store results
    best_objective = None
    
    for index, row in df.iterrows():
        current_objective = row[objective_column]
        
        # First row is always saved
        if best_objective is None:
            best_objective = current_objective
            result_df = pd.concat([result_df, pd.DataFrame([row])], ignore_index=True)
        else:
            # Check if current objective improves
            if minimize:
                improves = current_objective < best_objective
            else:
                improves = current_objective > best_objective
            
            if improves:
                best_objective = current_objective
                result_df = pd.concat([result_df, pd.DataFrame([row])], ignore_index=True)
            else:
                # If no improvement, repeat the last good row with current iteration
                last_good_row = result_df.iloc[-1].copy()
                last_good_row[iteration_column] = row[iteration_column]
                result_df = pd.concat([result_df, pd.DataFrame([last_good_row])], ignore_index=True)
    
    return result_df


def ego_01(obj: Callable, n_gen: int, params: dict, initial_population: list, x_lower: list, x_upper: list, args: Optional[tuple] = None, robustness: Union[bool, dict] = False):
    """
    Efficient Global Optimization (EGO) algorithm.

    :param obj: The objective function: obj(x, args) -> float or obj(x) -> float, where x is a list with shape dim and args is a tuple fixed parameters needed to completely specify the function
    :param n_gen: Number of generations or iterations
    :param params: Parameters of Genetic Algorithm
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

    # Initial population evaluation (Don't remove this part)
    for n in range(n_pop):
        aux_df = funcs.evaluation(obj, n, x_t0[n], 0, args=args) if args is not None else funcs.evaluation(obj, n, x_t0[n], 0)
        all_results.append(aux_df)
    df = pd.concat(all_results, ignore_index=True)
    df['REPORT'] = ""
    df['OF EVALUATIONS'] = 1

    # Iterations
    report = "Efficient Global Optimization (EGO)\n" # (Don't remove this part - Give the name of the algorithm)
    for t in range(1, n_gen + 1):
        f_min = df['OF'].min()
        for i in range(n_pop):
            y_train = df['OF'].to_list()
            x_train = []
            for j in range(d):
                x_train.append(df[f'X_{j}'].to_list())
            x_train = np.array(x_train).T
            y_train = np.array(y_train)
        model = sk.gaussian_process.GaussianProcessRegressor(n_restarts_optimizer=20).fit(x_train, y_train)
        argss = (model, f_min)
        # 
        def obj_ego(x, args):
            model, fmin = args
            mu, sig = model.predict(np.array([x]), return_std=True)
            if sig[0] < 1e-10:
                sigma = 1e-10
            else:
                sigma = sig[0]
            z = (fmin - mu[0]) / sigma
            of = (fmin - mu[0]) * sc.stats.norm.cdf(z) + sigma * sc.stats.norm.pdf(z)
            return -of
        
        x_ini = [
            [0.0],
            [5.0],
            [15.],
            [25.]
        ]
        paras = {
                    'selection': 'roulette wheel',
                    'crossover': {'type': 'blx-alpha', 'crossover rate (%)': 90},
                    'mutation': {'type': 'random walk', 'mutation rate (%)': 20, 'params': {'pdf': 'gaussian', 'cov (%)': 10}}
                }
        n_gen = 20
        _, best, _ = genetic_algorithm.genetic_algorithm_01(obj_ego, n_gen, paras, x_ini, [0], [25], args=argss)
        x = []
        for i in range(d):
            x.append(best[f'X_BEST_{i}'].values[-1])
        x = [float(i) for i in x]
        aux_df = funcs.evaluation(obj, n, x, 0, args=args) if args is not None else funcs.evaluation(obj, n, x, 0)
        all_results = [aux_df]
        df = pd.concat([df] + all_results, ignore_index=True)

    return filter_improvements(df)