"""bee colony algorithm functions"""
# https://sci-hub.wf/10.1016/j.knosys.2019.105002 melhor deles
# https://sci-hub.wf/10.1016/j.istruc.2021.01.016
# https://sci-hub.wf/10.1016/j.cam.2020.113199
# https://sci-hub.wf/10.1016/j.asoc.2020.106391

import numpy as np

def employee_bee_movement(of_function, x_i_old, x_k_old,
                            n_dimensions, x_upper, x_lower, none_variable=None):
    """
    employee bee movement
    xi (List):  
    xk (List):

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
