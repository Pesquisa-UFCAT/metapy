"""Efficient Global Optimization (EGO) related functions."""
from typing import Callable, Optional, Union

import numpy as np
import pandas as pd
import sklearn as sk

from metapy_toolbox import funcs

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
    bests = [] 

    # Initial population evaluation (Don't remove this part)
    for n in range(n_pop):
        aux_df = funcs.evaluation(obj, n, x_t0[n], 0, args=args) if args is not None else funcs.evaluation(obj, n, x_t0[n], 0)
        all_results.append(aux_df)
    df = pd.concat(all_results, ignore_index=True)
    df['REPORT'] = ""
    df['OF EVALUATIONS'] = 1
    print(df)

    # Iterations
    report = "Efficient Global Optimization (EGO)\n" # (Don't remove this part - Give the name of the algorithm)
    for t in range(1, n_gen + 1):
        fmin = df['OF'].min()
        for i in range(n_pop):
            y_train = df['OF'].to_list()
            x_train = []
            for j in range(d):
                x_train.append(df[f'X_{j}'].to_list())
            x_train = np.array(x_train).T
            y_train = np.array(y_train)
        model = sk.gaussian_process.GaussianProcessRegressor().fit(x_train, y_train)

        
        if args is not None:
            args = (model,) + args
            def obj_ego(x, args):
                model = args[0]
                x = np.array(x).reshape(1, -1)
                y_pred, sigma = model.predict(x, return_std=True)
                return y_pred[0] - 1.96 * sigma[0]
        else:
            args = (model,)
            def obj_ego(x, args):
                model = args[0]
                x = np.array(x).reshape(1, -1)
                y_pred, sigma = model.predict(x, return_std=True)
                return y_pred[0] - 1.96 * sigma[0]

    return None # df, df_resume, df['REPORT'].iloc[-1]