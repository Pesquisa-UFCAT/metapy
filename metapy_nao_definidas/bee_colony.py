"""bee colony algorithm functions"""
# https://sci-hub.wf/10.1016/j.knosys.2019.105002 melhor deles
# https://sci-hub.wf/10.1016/j.istruc.2021.01.016
# https://sci-hub.wf/10.1016/j.cam.2020.113199
# https://sci-hub.wf/10.1016/j.asoc.2020.106391

import numpy as np
from typing import Callable, List, Optional, Tuple


def employee_bee_movement(of_function: Callable[[List[float], Optional[object]], float], x_i_old: List[float], x_k_old: List[float], n_dimensions: int, x_upper: List[float], x_lower: List[float], none_variable: Optional[object] = None) -> Tuple[List[float], float, float, int, str]:
    """
    Performs the movement of an employee bee in the Artificial Bee Colony (ABC) algorithm.

    :param of_function: Objective function to be evaluated.
    :param x_i_old: Current solution vector (i-th bee).
    :param x_k_old: Neighbor solution vector (k-th bee).
    :param n_dimensions: Number of dimensions in the solution space.
    :param x_upper: Upper bounds for each variable.
    :param x_lower: Lower bounds for each variable.
    :param none_variable: Optional argument to be passed to the objective function.

    :return: Tuple containing:
    
        - x_i_new: New solution vector after movement.
        - of_i_new: Objective function value for the new solution.
        - fit_i_new: Fitness value for the new solution.
        - neof: Number of objective function evaluations (usually 1).
        - report_move: Movement report log as a string.
    """

    # Start internal variables
    report_move = "    ABC movement\n"
    report_move += f"    current xi = {x_i_old}\n"
    report_move += f"    current xk = {x_k_old}\n"    
    x_i_new = x_i_old.copy()

    # Movement
    id_j = id_selection(n_dimensions) ### aqui tem que implementar ainda na commonlibrary e chamar aqui corretamente
    phi = np.random.uniform(low=-1, high=1)
    x_i_new[id_j] = x_i_old[id_j] + phi*(x_i_old[id_j] - x_k_old[id_j])
    report_move += f"    j dimension selected = {id_j}, phi = {phi} neighbor = {x_i_new[id_j]}\n"

    # check interval
    # avaliar a função objetivo


    return x_i_new, of_i_new, fit_i_new, neof, report_move 
