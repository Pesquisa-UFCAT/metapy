import numpy as np
import pandas as pd
from typing import Callable, Optional, Union

from metapy_toolbox import funcs

def roulette_wheel_selection_abc(fit_pop: list, current_id: int, rng: np.random.Generator, return_report: bool = False) -> Union[int, tuple[int, str]]:
    """
    This function selects a position from the population using the roulette wheel selection method.

    :param fit_pop: Population fitness values
    :param i_pop:   current agent in t time step

    :return: [0] = selected agent id, [1] = Report about the roulette wheel selection process.
    """

    report_move = "    Selection operator\n"
    n_pop = len(fit_pop)
    pos = [i for i in range(n_pop) if i != current_id]  # exclude current agent
    fit_arr = np.array([fit_pop[i] for i in pos], dtype=float)

    min_fit = fit_arr.min()
    if min_fit < 0:
        fit_arr -= min_fit
    prob_sum = fit_arr.sum()
    if prob_sum == 0:
        selection_probs = np.ones_like(fit_arr) / len(fit_arr)
    else:
        selection_probs = fit_arr / prob_sum

    report_move += f"    probs(fit) = {selection_probs.tolist()}\n"
    selected_idx = rng.choice(len(pos), 1, replace=False, p=selection_probs)[0]
    i_selected = pos[selected_idx]
    report_move += f"    selected agent id = {i_selected}\n"

    if return_report:
        return i_selected, report_move
    else:
        return i_selected


def abc_algorithm_01(obj: Callable, n_gen: int, params: dict, initial_population: list, x_lower: list, x_upper: list, args: Optional[tuple] = None) -> tuple[pd.DataFrame, pd.DataFrame, str]:
    """ 
    Artificial Bee Colony (ABC) algorithm implementation.

    :param obj: The objective function: obj(x, args) -> float or obj(x) -> float
    :param n_gen: Number of generations or iterations
    :param params: parameters for ABC
    :param initial_population: Initial population (list of lists)
    :param x_lower: Lower limit of the design variables (scalar or list)
    :param x_upper: Upper limit of the design variables (scalar or list)
    :param args: Extra arguments to pass to the objective function (optional)
    
    :return: [0] DataFrame with all evaluations, [1] DataFrame with best/avg/worst per iteration, [2] Report string
    """
    # Init variables
    x_t0 = initial_population.copy()
    d = len(x_t0[0])
    n_pop = len(x_t0)
    all_results = []
    bests = []
    trials = np.zeros(n_pop, dtype=int)
    rng = np.random.default_rng(params.get('seed', None))
    limit = int(params.get('limit', 50))
    employed_updates = int(params.get('employed_updates', 1))
    onlooker_updates = params.get('onlooker_updates', n_pop)

    report = "Artificial Bee Colony (ABC)\n"

    # bounds arrays
    x_lower_arr = np.array(x_lower, dtype=float)
    x_upper_arr = np.array(x_upper, dtype=float)
    if x_lower_arr.shape == (): x_lower_arr = np.full(d, float(x_lower_arr))
    if x_upper_arr.shape == (): x_upper_arr = np.full(d, float(x_upper_arr))

    # Evaluation of initial population
    for n in range(n_pop):
        aux_df = funcs.evaluation(obj, n, x_t0[n], 0, args=args) if args else funcs.evaluation(obj, n, x_t0[n], 0)
        all_results.append(aux_df)

    df = pd.concat(all_results, ignore_index=True)
    df['REPORT'] = ""
    df['OF EVALUATIONS'] = 1
    # Personal best columns
    for j in range(d):
        df[f'P_X_BEST_{j}'] = df[f'X_{j}']
    df['P_OF_BEST'] = df['OF']

    # Helper: neighbor generator
    def _generate_neighbor_from_array(X_array, i):
        k = i
        while k == i:
            k = rng.integers(0, n_pop)
        j = rng.integers(0, d)
        phi = rng.uniform(-1.0, 1.0)
        v = X_array[i].copy()
        v[j] = X_array[i][j] + phi * (X_array[i][j] - X_array[k][j])
        return np.minimum(np.maximum(v, x_lower_arr), x_upper_arr)

    # Main loop
    for t in range(1, n_gen + 1):
        report += f"Iteration: {t}\n"

        # Get latest population per ID
        df_latest = df[df['ITER'] == t-1].drop_duplicates(subset=['ID'])
        bests.append(funcs.best_avg_worst(df_latest, d))

        # Build current X array
        X_curr = np.zeros((n_pop, d), dtype=float)
        for _, row in df_latest.iterrows():
            agent_id = int(row['ID'])
            for j in range(d):
                X_curr[agent_id, j] = row[f'X_{j}']

        # Employed bees
        for i in range(n_pop):
            best_candidate_df = df_latest[df_latest['ID'] == i].copy()
            total_evals = 0
            for _ in range(employed_updates):
                v = _generate_neighbor_from_array(X_curr, i)
                fv = funcs.evaluation(obj, i, v, t, args=args) if args else funcs.evaluation(obj, i, v, t)
                best_candidate_df = funcs.compare_and_save(best_candidate_df, fv)
                total_evals += 1
            best_candidate_df['OF EVALUATIONS'] = total_evals
            prev_of = df_latest[df_latest['ID'] == i]['OF'].values[0]
            new_of = best_candidate_df['OF'].values[0]
            trials[i] = 0 if new_of < prev_of else trials[i] + 1
            df = pd.concat([df, best_candidate_df], ignore_index=True)

        # Onlooker bees
        fit_pop = df_latest['FIT'].tolist()
        n_onlookers = int(onlooker_updates if isinstance(onlooker_updates, int) else n_pop)
        for _ in range(n_onlookers):
            i = roulette_wheel_selection_abc(fit_pop, current_id=-1, rng=rng)
            v = _generate_neighbor_from_array(X_curr, i)
            fv = funcs.evaluation(obj, i, v, t, args=args) if args else funcs.evaluation(obj, i, v, t)
            # compare and append
            df_candidate = df[(df['ITER'] == t-1) & (df['ID'] == i)].copy()
            df_candidate = funcs.compare_and_save(df_candidate, fv)
            df_candidate['OF EVALUATIONS'] = 1
            df = pd.concat([df, df_candidate], ignore_index=True)

        # Update personal best
        df_current = df[df['ITER'] == t].copy()
        for _, row in df_current.iterrows():
            id_val = int(row['ID'])
            mask = row['OF'] < df_latest[df_latest['ID'] == id_val]['P_OF_BEST'].values[0]
            for j in range(d):
                df.loc[(df['ITER'] == t) & (df['ID'] == id_val), f'P_X_BEST_{j}'] = \
                    row[f'X_{j}'] if mask else df_latest[df_latest['ID'] == id_val][f'P_X_BEST_{j}'].values[0]
            df.loc[(df['ITER'] == t) & (df['ID'] == id_val), 'P_OF_BEST'] = \
                row['OF'] if mask else df_latest[df_latest['ID'] == id_val]['P_OF_BEST'].values[0]

    # Final summary
    df_final = df[df['ITER'] == n_gen].reset_index(drop=True)
    bests.append(funcs.best_avg_worst(df_final, d))
    df_resume = pd.concat(bests, ignore_index=True)
    df['REPORT'] = report
    for t in range(n_gen + 1):
        df_resume.loc[t, 'OF EVALUATIONS'] = df[df['ITER'] == t]['OF EVALUATIONS'].sum()
        df_resume.loc[t, 'TIME CONSUMPTION (s)'] = df[df['ITER'] == t]['TIME CONSUMPTION (s)'].sum()
    df_resume['OF EVALUATIONS'] = df_resume['OF EVALUATIONS'].cumsum()
    df_resume['TIME CONSUMPTION (s)'] = df_resume['TIME CONSUMPTION (s)'].cumsum()

    return df, df_resume, df['REPORT'].iloc[-1]
