"""Efficient Global Optimization (EGO) related functions."""
from typing import Callable, Optional
from functools import partial

import numpy as np
import pandas as pd
import sklearn as sk
import scipy as sc
import mealpy as mp

from metapy_toolbox import funcs


def ego_01_architecture(obj: Callable, n_gen: int, initial_population: list, x_lower: list, x_upper: list, params_opt: dict, params_kernel: Optional[dict] = None, args: Optional[tuple] = None) -> tuple[list, float, pd.DataFrame]:
    """Hybrid Architecture for Efficient Global Optimization (EGO) algorithm.

    :param obj: The objective function: obj(x, args) -> float or obj(x) -> float, where x is a list with shape dim and args is a tuple fixed parameters needed to completely specify the function
    :param n_gen: Number of generations or iterations
    :param initial_population: Initial population
    :param x_lower: Lower limit of the design variables
    :param x_upper: Upper limit of the design variables
    :param params_opt: Parameters of the optimization algorithm. Suppport optimizers from scipy or mealpy. Scipy optimizers: 'scipy_lbfgs', 'scipy_tnc',  'scipy_slsqp', 'scipy_trust'. Mealpy optimizers: Any optimizer from mealpy library
    :param params_kernel: Parameters of the kernel function. Support kernels from sklearn.gaussian_process.kernels (optional)
    :param args: Extra arguments to pass to the objective function (optional)
    :param robustness: If True, the objective function is evaluated in a robust way (default is False)

    :return: [0] = Best solution, [1] = Best objective function value, [2] = Dataframe with all evaluations

    Example 1: Using SciPy (SLSQP) as optimizer algorithm and RBF kernel from sklearn
        >>> from sklearn.gaussian_process.kernels import RBF
        >>> from function import f
        >>> 
        >>> # Function in python file (function.py)
        >>> def f(x):
        >>>     of = (x[0] - 3.5) * np.sin((x[0] - 3.5) / (np.pi))
        >>>     return of
        >>>
        >>> x_ini = [[0.0], [4.5], [7.0], [10.0], [15.0], [20.0], [25.0]]
        >>> paras_opt = {'optimizer algorithm': 'scipy_slsqp'}
        >>> paras_kernel = {'kernel': RBF()}
        >>> 
        >>> x_new, best_of, df = ego_01_architecture(obj=f, n_gen=30, initial_population=x_ini, x_lower=[-10.0], x_upper=[25.0], params_opt=paras_opt, params_kernel=paras_kernel)
        >>> print(f"Best solution: {x_new} -> OF: {best_of}")

    Example 2: Using SciPy (TNC) as optimizer algorithm and RBF kernel from sklearn
        >>> from sklearn.gaussian_process.kernels import RBF
        >>> from function import f
        >>> 
        >>> # Function in python file (function.py)
        >>> def f(x):
        >>>     of = (x[0] - 3.5) * np.sin((x[0] - 3.5) / (np.pi))
        >>>     return of
        >>>
        >>> x_ini = [[0.0], [4.5], [7.0], [10.0], [15.0], [20.0], [25.0]]
        >>> paras_opt = {'optimizer algorithm': 'scipy_tnc'}
        >>> paras_kernel = {'kernel': RBF()}
        >>> 
        >>> x_new, best_of, df = ego_01_architecture(obj=f, n_gen=30, initial_population=x_ini, x_lower=[-10.0], x_upper=[25.0], params_opt=paras_opt, params_kernel=paras_kernel)
        >>> print(f"Best solution: {x_new} -> OF: {best_of}")
    
    Example 3: Using Mealpy – Genetic Algorithm (GA)
        >>> from sklearn.gaussian_process.kernels import RBF
        >>> from mealpy import GA
        >>> from function import f
        >>> 
        >>> # Function in python file (function.py)
        >>> def f(x):
        >>>     of = (x[0] - 3.5) * np.sin((x[0] - 3.5) / (np.pi))
        >>>     return of
        >>>
        >>> x_ini = [[0.0], [4.5], [7.0], [10.0], [15.0], [20.0], [25.0]]
        >>> paras_opt = {'optimizer algorithm': GA.BaseGA(epoch=40, pop_size=50)}
        >>> # You can improve the GA parameters. Use this documentation for that: https://mealpy.readthedocs.io/en/latest/pages/models/mealpy.evolutionary_based.html#module-mealpy.evolutionary_based.GA
        >>> paras_kernel = {'kernel': RBF()}
        >>> 
        >>> x_new, best_of, df = ego_01_architecture(obj=f, n_gen=30, initial_population=x_ini, x_lower=[-10.0], x_upper=[25.0], params_opt=paras_opt, params_kernel=paras_kernel)
        >>> print(f"Best solution: {x_new} -> OF: {best_of}")
    
    Example 4: Using Mealpy – Particle Swarm Optimization (PSO)
        >>> from sklearn.gaussian_process.kernels import RBF
        >>> from mealpy import PSO
        >>> from function import f
        >>> 
        >>> # Function in python file (function.py)
        >>> def f(x):
        >>>     of = (x[0] - 3.5) * np.sin((x[0] - 3.5) / (np.pi))
        >>>     return of
        >>>
        >>> x_ini = [[0.0], [4.5], [7.0], [10.0], [15.0], [20.0], [25.0]]
        >>> paras_opt = {'optimizer algorithm': PSO.AIW_PSO(epoch=1000, pop_size=50, c1=2.05, c2=2.05, alpha=0.4)}
        >>> # You can improve the PSO parameters. Use this documentation for that: https://mealpy.readthedocs.io/en/latest/pages/models/mealpy.swarm_based.html#module-mealpy.swarm_based.PSO
        >>> paras_kernel = {'kernel': RBF()}
        >>> 
        >>> x_new, best_of, df = ego_01_architecture(obj=f, n_gen=30, initial_population=x_ini, x_lower=[-10.0], x_upper=[25.0], params_opt=paras_opt, params_kernel=paras_kernel)
        >>> print(f"Best solution: {x_new} -> OF: {best_of}")
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
    
    # Iterations
    for t in range(1, n_gen + 1):
        # Training the surrogate model
        for i in range(n_pop):
            y_train = df['OF'].to_list()
            x_train = []
            for j in range(d):
                x_train.append(df[f'X_{j}'].to_list())
            x_train = np.array(x_train).T
            y_train = np.array(y_train)
        scaler_x = sk.preprocessing.StandardScaler()
        x_train_scaled = scaler_x.fit_transform(x_train)

        if params_kernel is None:
            model = sk.gaussian_process.GaussianProcessRegressor(kernel=sk.gaussian_process.kernels.RBF(), n_restarts_optimizer=5, normalize_y = True, alpha=1e-8).fit(x_train_scaled, y_train)
        else:
            model = sk.gaussian_process.GaussianProcessRegressor(kernel=params_kernel['kernel'], n_restarts_optimizer=5, normalize_y = True, alpha=1e-8).fit(x_train_scaled, y_train)
        
        # Traditional optimization
        argss = (model, df['OF'].min(), scaler_x)
        def obj_ego(x, coef):
            model, fmin, sc_x = coef
            x_new_array = np.array(x).reshape(1, -1)
            x_new_scaled = sc_x.transform(x_new_array)
            mu, sig = model.predict(x_new_scaled, return_std=True)
            if sig[0] < 1e-10:
                sigma = 1e-10
            else:
                sigma = sig[0]
            z = (fmin - mu[0]) / sigma
            of = (fmin - mu[0]) * sc.stats.norm.cdf(z) + sigma * sc.stats.norm.pdf(z)
            return -of
        wrapped_obj = partial(obj_ego, coef=argss)
        opt = params_opt["optimizer algorithm"]
        if isinstance(opt, str) and opt.lower().startswith("scipy"):
            if opt.lower() == "scipy_lbfgs":
                method = "L-BFGS-B"
            elif opt.lower() == "scipy_tnc":
                method = "TNC"
            elif opt.lower() == "scipy_slsqp":
                method = "SLSQP"
            elif opt.lower() == "scipy_trust":
                method = "trust-constr"
            bounds = list(zip(x_lower, x_upper))
            x0 = np.random.uniform(x_lower, x_upper)
            res = sc.optimize.minimize(wrapped_obj, x0, method=method, bounds=bounds, options={"maxiter": 300, "ftol": 1e-9})     
            x_best = res.x
            x_new = x_best.tolist()
        else:
            problem_dict = {
                                "obj_func": wrapped_obj,
                                "bounds": mp.FloatVar(lb=x_lower, ub=x_upper),
                                "minmax": "min",
                                "log_to": None,
                            }
            optimizer = params_opt["optimizer algorithm"]
            g_best = optimizer.solve(problem_dict)
            x_new = g_best.solution
        
        # Add new training point
        aux_df = funcs.evaluation(obj, n, x_new, 0, args=args) if args is not None else funcs.evaluation(obj, n, x_new, 0)
        df = pd.concat([df, aux_df], ignore_index=True)
    
    # Best solution extraction
    x_cols = [col for col in df.columns if col.startswith("X_")]
    idx_min = df["OF"].idxmin()
    best_x = df.loc[idx_min, x_cols].tolist()

    return best_x, df['OF'].min(), df
