"""Commonly used functions."""
import time
from typing import Callable, Optional

import numpy as np
import pandas as pd
from scipy import stats

from metapy_toolbox import funcs


def initial_population_01(n_population: int, n_dimensions: int, x_lower: np.ndarray, x_upper: np.ndarray, seed: int = None, use_lhs: bool = True, scramble: bool = True):
    """
    Generates an initial population of continuous variables within the specified bounds.  
    If use_lhs=True: uses Latin Hypercube Sampling (scipy.stats.qmc.LatinHypercube).  
    If use_lhs=False: uses numpy uniform RNG.

    :param n_population: number of individuals in the population.
    :param n_dimensions: number of dimensions (variables) in the problem.
    :param x_lower: lower bounds per dimension (size n_dimensions).
    :param x_upper: upper bounds per dimension (size n_dimensions).
    :param seed: random seed for reproducibility. Default None.
    :param use_lhs: True to use Latin Hypercube (default). False to use pure uniform sampling.
    :param scramble: only for LHS — if True, enables scrambling (shuffling) in the LHS.

    :return: generated population, format [n_population][n_dimensions].
    """
    x_lower = np.asarray(x_lower, dtype=float)
    x_upper = np.asarray(x_upper, dtype=float)

    if x_lower.shape[0] != n_dimensions or x_upper.shape[0] != n_dimensions:
        raise ValueError("x_lower and x_upper must have the same length as n_dimensions.")

    # Case: Latin Hypercube Sampling (Scipy)
    if use_lhs:
        # scipy.stats.qmc is available in scipy >= 1.7
        qmc = stats.qmc
        sampler = qmc.LatinHypercube(d=n_dimensions, scramble=bool(scramble), seed=seed)
        # generate points in the unit hypercube [0,1]^d
        sample_unit = sampler.random(n=n_population)  # shape (n_population, n_dimensions)
        # scale to the provided bounds
        sample_scaled = qmc.scale(sample_unit, x_lower, x_upper)
        x_pop = sample_scaled.tolist()

    else:
        # Case: pure uniform sampling with numpy
        rng = np.random.default_rng(seed)
        # generate matrix shape (n_population, n_dimensions) with uniform [0,1)
        u = rng.uniform(size=(n_population, n_dimensions))
        # scale to [x_lower, x_upper]
        sample = x_lower + (x_upper - x_lower) * u
        x_pop = sample.tolist()

    return x_pop


def initial_population_01_opposite(n_population: int, n_dimensions: int, x_lower: np.ndarray, x_upper: np.ndarray, seed: int = None, use_lhs: bool = True, scramble: bool = True):
    """
    Generates an initial population and its opposite population of continuous variables. The opposite population is computed as: x_opposite = x_lower + x_upper - x.

    :param n_population: number of individuals in the population.
    :param n_dimensions: number of dimensions (variables) in the problem.
    :param x_lower: lower bounds per dimension (size n_dimensions).
    :param x_upper: upper bounds per dimension (size n_dimensions).
    :param seed: random seed for reproducibility. Default None.
    :param use_lhs: True to use Latin Hypercube (default). False to use pure uniform sampling.
    :param scramble: only for LHS — if True, enables scrambling (shuffling) in the LHS.

    :return: tuple of two lists: (initial_population, opposite_population)
    """

    x_lower = np.asarray(x_lower, dtype=float)
    x_upper = np.asarray(x_upper, dtype=float)

    if x_lower.shape[0] != n_dimensions or x_upper.shape[0] != n_dimensions:
        raise ValueError("x_lower and x_upper must have the same length as n_dimensions.")

    # Generate initial population
    if use_lhs:
        qmc = stats.qmc
        sampler = qmc.LatinHypercube(d=n_dimensions, scramble=bool(scramble), seed=seed)
        sample_unit = sampler.random(n=n_population)
        sample_scaled = qmc.scale(sample_unit, x_lower, x_upper)
        x_pop = sample_scaled
    else:
        rng = np.random.default_rng(seed)
        u = rng.uniform(size=(n_population, n_dimensions))
        x_pop = x_lower + (x_upper - x_lower) * u

    # Compute opposite population
    x_opposite = x_lower + x_upper - x_pop

    return x_pop.tolist(), x_opposite.tolist()


def initial_population_01_quasi_opposite(n_population: int, n_dimensions: int, x_lower: np.ndarray, x_upper: np.ndarray, 
                                         seed: int = None, use_lhs: bool = True, scramble: bool = True):
    """
    Generates an initial population and its quasi-opposite population of continuous variables.
    
    The quasi-opposite population perturbs around the midpoint between bounds based on the opposite population.

    :param n_population: number of individuals in the population.
    :param n_dimensions: number of dimensions (variables) in the problem.
    :param x_lower: lower bounds per dimension (size n_dimensions).
    :param x_upper: upper bounds per dimension (size n_dimensions).
    :param seed: random seed for reproducibility. Default None.
    :param use_lhs: True to use Latin Hypercube (default). False to use pure uniform sampling.
    :param scramble: only for LHS — if True, enables scrambling (shuffling) in the LHS.

    :return: tuple of two lists: (initial_population, quasi_opposite_population)
    """
    rng = np.random.default_rng(seed)
    x_lower = np.asarray(x_lower, dtype=float)
    x_upper = np.asarray(x_upper, dtype=float)

    if x_lower.shape[0] != n_dimensions or x_upper.shape[0] != n_dimensions:
        raise ValueError("x_lower and x_upper must have the same length as n_dimensions.")

    # Generate initial population
    if use_lhs:
        qmc = stats.qmc
        sampler = qmc.LatinHypercube(d=n_dimensions, scramble=bool(scramble), seed=seed)
        sample_unit = sampler.random(n=n_population)
        x_pop = qmc.scale(sample_unit, x_lower, x_upper)
    else:
        u = rng.uniform(size=(n_population, n_dimensions))
        x_pop = x_lower + (x_upper - x_lower) * u

    # Compute quasi-opposite population
    x_quasi_opposite = np.empty_like(x_pop)
    mid = (x_lower + x_upper) / 2.0

    for i in range(n_population):
        for j in range(n_dimensions):
            op = x_lower[j] + x_upper[j] - x_pop[i, j]
            if x_pop[i, j] < mid[j]:
                x_quasi_opposite[i, j] = mid[j] + (op - mid[j]) * rng.random()
            else:
                x_quasi_opposite[i, j] = op + (mid[j] - op) * rng.random()

    return x_pop.tolist(), x_quasi_opposite.tolist()


def fit_value(of_i_value: float) -> float:
    """
    Calculates the fitness value of the i-th agent based on its objective function value.

    :param of_i_value: Objective function value of the i-th agent in t time step

    :return: Fitness value of the i-th agent in t time step (always positive)
    """

    if of_i_value >= 0:
        fit_i_value = 1 / (1 + of_i_value)
    else:
        fit_i_value = 1 + np.abs(of_i_value)

    return fit_i_value


def best_avg_worst(df: pd.DataFrame, d: int) -> pd.DataFrame:
    """
    Check and save best, average and worst objective function values from dataframe

    :param df: Dataframe with all data
    :param d: problem dimension

    :return: Positions, Objective function values saved
    """

    # Dataframe columns
    columns_all_data = ['ITER']
    columns_all_data.append('OF EVALUATIONS')
    columns_all_data.append('BEST ID')
    columns_all_data.extend(['X_BEST_' + str(i) for i in range(d)])
    columns_all_data.append('OF BEST')
    columns_all_data.append('WORST ID')
    columns_all_data.extend(['X_WORST_' + str(i) for i in range(d)])
    columns_all_data.append('OF WORST')
    columns_all_data.append('MEAN OF')
    columns_all_data.append('STD OF')
    df_resume = pd.DataFrame(columns=columns_all_data)

    # Fill dataframe
    df_resume.loc[0, 'ITER'] = df['ITER'].values[-1]
    df_resume.loc[0, 'OF EVALUATIONS'] = df['OF EVALUATIONS'].values[-1]

    # Find best, worst and statistics
    best_idx = int(df['OF'].idxmin())
    worst_idx = int(df['OF'].idxmax())
    df_resume.loc[0, 'BEST ID'] = best_idx
    df_resume.loc[0, 'OF BEST'] = df.loc[:, 'OF'].min()
    df_resume.loc[0, 'WORST ID'] = worst_idx
    df_resume.loc[0, 'OF WORST'] = df.loc[:, 'OF'].max()
    df_resume.loc[0, 'MEAN OF'] = df.loc[:, 'OF'].mean()
    df_resume.loc[0, 'STD OF'] = df.loc[:, 'OF'].std()

    # Add X_BEST and X_WORST values for all rows
    for j in range(d):
        df_resume.loc[0, 'X_BEST_' + str(j)] = df['X_' + str(j)].values[best_idx]
        df_resume.loc[0, 'X_WORST_' + str(j)] = df['X_' + str(j)].values[worst_idx]

    return df_resume


def query_x_of_fit_from_data(df: pd.DataFrame, i: int, d: int) -> tuple[list, float, float]:
    """
    Query position, objective function value and fitness value of the i-th agent from dataframe

    :param df: All data in time step t
    :param i: Current agent in t time step
    :param d: Number of dimensions

    :return: [0] = Position of the i-th agent in t time step, [1] = Objective function value of the i-th agent in t time step, [2] = Fitness value of the i-th agent in t time step
    """

    aux = df[df['ID'] == i]
    current_x = []
    for k in range(d):
        current_x.append(aux['X_' + str(k)].values[0])
    current_of = aux['OF'].values[0]
    current_fit = aux['FIT'].values[0]

    return current_x, current_of, current_fit


def evaluation(obj: Callable, id: int, x: list, t: int, args: Optional[tuple] = None) -> pd.DataFrame:
    """
    Objective function evaluation and save in dataframe

    :param obj: The objective function: obj(x, args) -> float or obj(x) -> float, where x is a list with shape dim and args is a tuple fixed parameters needed to completely specify the function
    :param id: identifier of the agent
    :param x: Design variables to be evaluated
    :param neof_count: Count of objective function evaluations
    :param t: Current iteration number
    :param args: Extra arguments to pass to the objective function (optional)

    :return: Positions, Objective function values, Fitness values and Time consumption saved
    """

    t0 = time.perf_counter()
    of_value = obj(x, args=args) if args is not None else obj(x)

    new_data = {
        'ID': id,
        'ITER': t,
        **{'X_' + str(j): value for j, value in enumerate(x)},
        'OF': of_value,
        'FIT': fit_value(of_value),
        'OF EVALUATIONS': -1000,
        'TIME CONSUMPTION (s)': time.perf_counter() - t0
    }

    return pd.DataFrame([new_data])


def compare_and_save(df_current: pd.DataFrame, df_temp: pd.DataFrame) -> pd.DataFrame:
    """
    Compare current and temporary solutions and save the best one.

    :param df_current: Positions, Objective function values, Fitness values and Time consumption saved of the current solution
    :param df_temp: Positions, Objective function values, Fitness values and Time consumption saved of the temporary solution

    :return: Positions, Objective function values, Fitness values and Time consumption saved of the best solution
    """

    if df_temp['FIT'].values[0] > df_current['FIT'].values[0]:
        return df_temp
    else:
        df_current.loc[:, 'ITER'] = df_temp['ITER'].values[0]
        df_current.loc[:, 'OF EVALUATIONS'] = df_temp['OF EVALUATIONS'].values[0]
        return df_current
    

def check_interval_01(x: list, x_lower: list, x_upper: list) -> list:
    """
    This function checks if a design variable is out of the limits established ``x_lower`` and ``x_upper`` and updates the variable if necessary.

    :param x: Design variables to be checked
    :param x_lower: Lower limit of the design variables
    :param x_upper: Upper limit of the design variables

    :return: Checked design variables
    """

    aux = np.clip(x, x_lower, x_upper)
    x_checked = aux.tolist()

    return x_checked


def mutation_01_random_walk(parent_0: list, pdf: str, cov: float, x_lower: list, x_upper: list) -> tuple[list, str]:
    """
    This function performs the random walk mutation operator. Three new points are generated from the two parent points (offspring).

    :param parent_0: First parent
    :param pdf: Probability density function. Options: 'gaussian', 'uniform' or 'gumbel'
    :param cov: Coefficient of variation
    :param x_lower: Lower limit of the design variables
    :param x_upper: Upper limit of the design variables

    :return: [0] = First offspring position, [1] = Report about the linear crossover process
    """

    # Start internal variables
    report_move = "    Mutation operator - Random walk mutation\n"
    report_move += f"    current p0 = {parent_0}\n"
    report_move += f"    pdf = {pdf}, cov = {cov}\n"
    offspring_a = []

    # Movement
    for i in range(len(parent_0)):
        if pdf == 'gaussian':
            alpha_a = np.random.normal(loc=parent_0[i], scale=cov*parent_0[i]/100, size=1)[0]
        elif pdf == 'uniform':
            alpha_a = np.random.uniform(low=parent_0[i]-cov*parent_0[i]/100, high=parent_0[i]+cov*parent_0[i]/100, size=1)[0]
        elif pdf == 'gumbel':
            alpha_a = np.random.gumbel(loc=parent_0[i], scale=cov*parent_0[i]/100, size=1)[0]
        report_move += f"    Dimension {i}: alpha_a = {alpha_a}\n"
        offspring_a.append(alpha_a)
    offspring_a = funcs.check_interval_01(offspring_a, x_lower, x_upper)

    return offspring_a, report_move

