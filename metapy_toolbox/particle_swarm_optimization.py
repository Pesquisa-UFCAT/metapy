import numpy as np
import pandas as pd
from typing import Callable, Optional, Union, Tuple # Corrigido aqui

# Supondo que 'funcs' é um módulo importado
# import funcs

def update_velocity_pso(w: float, c1: float, c2: float,
                    current_velocity: list, current_position: list,
                    p_best_position: list, g_best_position: list) -> Tuple[list, str]: # Corrigido aqui
    report_move = "    Atualização de Velocidade\n"
    report_move += f"    v_atual = {current_velocity}\n"
    report_move += f"    x_atual = {current_position}\n"
    new_velocity = []
    d = len(current_position)

    r1 = np.random.uniform(low=0, high=1, size=d)
    r2 = np.random.uniform(low=0, high=1, size=d)

    for j in range(d):
        inertia = w * current_velocity[j]
        cognitive = c1 * r1[j] * (p_best_position[j] - current_position[j])
        social = c2 * r2[j] * (g_best_position[j] - current_position[j])
        v_j = inertia + cognitive + social
        new_velocity.append(v_j)
        report_move += f"    Dimensão {j}: v_novo = {inertia:.3f} (inercia) + {cognitive:.3f} (cognitivo) + {social:.3f} (social) = {v_j:.3f}\n"

    report_move += f"    Velocidade final nova = {new_velocity}\n"
    return new_velocity, report_move


def update_position_pso(current_position: list, new_velocity: list,
                    x_lower: list, x_upper: list) -> Tuple[list, str]: # Corrigido aqui
    report_move = "    Atualização de Posição\n"
    report_move += f"    x_atual = {current_position}\n"
    report_move += f"    v_aplicada = {new_velocity}\n"

    x_new = (np.array(current_position) + np.array(new_velocity)).tolist()
    report_move += f"    x antes da verificação de limites = {x_new}\n"

    x_new_checked = funcs.check_interval_01(x_new, x_lower, x_upper)

    report_move += f"    Posição final nova = {x_new_checked}\n"
    return x_new_checked, report_move


def particle_swarm_optimization_01(obj: Callable, n_gen: int, params: dict, initial_population: list, x_lower: list, x_upper: list, args: Optional[Tuple] = None, robustness: Union[bool, dict] = False) -> Tuple[pd.DataFrame, pd.DataFrame, str]: # Corrigido aqui (duas vezes)
    x_t0 = initial_population.copy()
    d = len(x_t0[0])
    n_pop = len(x_t0)
    all_results = []
    bests = []
    report = "Particle Swarm Optimization\n"

    w_start = params['inertia weight']['w_start']
    w_end = params['inertia weight']['w_end']
    c1 = params['cognitive']['c1']
    c2 = params['social']['c2']
    velocity_init_type = params['velocity']['type'].lower()

    v_t = []
    if velocity_init_type == 'random':
        v_max = params['velocity']['vmax']
        v_min = params['velocity']['vmin']
        for _ in range(n_pop):
            v_t.append(np.random.uniform(low=v_min, high=v_max, size=d).tolist())
    else:
        for _ in range(n_pop):
            v_t.append([0.0] * d)
            
    for n in range(n_pop):
        aux_df = funcs.evaluation(obj, n, x_t0[n], 0, args=args) if args is not None else funcs.evaluation(obj, n, x_t0[n], 0)
        all_results.append(aux_df)
    df = pd.concat(all_results, ignore_index=True)
    df['REPORT'] = ""
    df['OF EVALUATIONS'] = 1

    df['W'] = np.nan
    df.loc[df['ITER'] == 0, 'W'] = w_start
    
    for j in range(d):
        df.loc[:, 'P_X_BEST_' + str(j)] = df.loc[:, 'X_' + str(j)]
    df.loc[:, 'P_OF_BEST'] = df.loc[:, 'OF']
    
    g_best_row = df.loc[df['P_OF_BEST'].idxmin()]
    g_best_x = [g_best_row[f'P_X_BEST_{j}'] for j in range(d)]
    g_best_of = g_best_row['P_OF_BEST']
    report += f"Initial Global Best OF: {g_best_of}\n"

    report = "Particle Swarm Optimization\n"
    for t in range(1, n_gen + 1):
        w = w_start - (w_start - w_end) * (t / n_gen)
        report += f"iteration: {t}, w = {w:.4f}\n"
        df_aux = df[df['ITER'] == t-1]
        df_aux = df_aux.reset_index(drop=True)
        aux_t = []
        df_copy = df.copy()
        bests.append(funcs.best_avg_worst(df_aux, d))
        
        g_best_row_candidate = df_aux.loc[df_aux['P_OF_BEST'].idxmin()]
        if g_best_row_candidate['P_OF_BEST'] < g_best_of:
            g_best_of = g_best_row_candidate['P_OF_BEST']
            g_best_x = [g_best_row_candidate[f'P_X_BEST_{j}'] for j in range(d)]
            report += f"  New Global Best found in generation {t-1}: {g_best_of}\n"

        for i in range(n_pop):
            report += f" Agent id: {i}\n"

            x_current, _, _ = funcs.query_x_of_fit_from_data(df_aux, i, d)
            p_best_x = [df_aux.loc[i, f'P_X_BEST_{j}'] for j in range(d)]
            current_velocity = v_t[i]

            new_velocity, report_v = update_velocity_pso(w, c1, c2, current_velocity, x_current, p_best_x, g_best_x)
            report += report_v

            x_new, report_p = update_position_pso(x_current, new_velocity, x_lower, x_upper)
            report += report_p

            v_t[i] = new_velocity
            
            n_evals_total = len(df)
            aux_df_eval = funcs.evaluation(obj, i, x_new, n_evals_total, t, args=args) if args is not None else funcs.evaluation(obj, i, x_new, n_evals_total, t)
            aux_t.append(aux_df_eval)

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
            
            aux_t.append(df_temp)

        df = pd.concat([df_copy] + aux_t, ignore_index=True)

        df.loc[df['ITER'] == t, 'W'] = w

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

    return df, df_resume, report