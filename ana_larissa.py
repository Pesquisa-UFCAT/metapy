import numpy as np
from metapy_toolbox import *

def my_obj_function(x, none_variable):

    # objective design variables
    c1 = x[0]
    c2 = x[1]

    # dataset
    t = none_variable['x']
    y_true = none_variable['y_true']
    if none_variable['noise']:
       y_true_noise = []
       for i in y_true:
            mean = 0  # Média do ruído
            std_dev = none_variable['noise level (%)'] / 100
            noise = np.random.normal(mean, std_dev * i, 1)
            y_with_noise = i + noise[0]
            y_true_noise.append(y_with_noise)
    else:
        y_true_noise = y_true.copy()

    # numerical model and loss function
    omega = 0.471911008
    t_0 = t[0]
    a_0 = y_true_noise[0]
    y_pred = []
    for i in t:
        c_0 = ((8*a_0*c2*omega) + (3*np.pi*c1)) / (3*a_0*np.pi*c1*np.exp(0.5*c1*t_0))
        y_pred_aux = (3*np.pi*c1) / ((3*np.pi*c_0*c1*np.exp(0.5*c1*i)) - (8*omega*c2))
        y_pred.append(y_pred_aux)
    
    loss = loss_function_mse(y_true_noise, y_pred)

    return loss

def my_obj_function2(x, none_variable):

    # objective design variables
    c1 = x[0]
    c2 = x[1]

    # dataset
    t = none_variable['x']
    y_true = none_variable['y_true']
    if none_variable['noise']:
        y_true_noise = []
        for i in y_true:
                mean = 0  # Média do ruído
                std_dev = none_variable['noise level (%)'] / 100
                noise = np.random.normal(mean, std_dev * i, 1)
                y_with_noise = i + noise[0]
                y_true_noise.append(y_with_noise)
    else:
        y_true_noise = y_true.copy()

    # numerical model and loss function
    omega = 0.471911008
    t_0 = t[0]
    a_0 = y_true_noise[0]
    y_pred = []
    for i in t:
        c_0 = ((8*a_0*c2*omega) + (3*np.pi*c1)) / (3*a_0*np.pi*c1*np.exp(0.5*c1*t_0))
        y_pred_aux = (3*np.pi*c1) / ((3*np.pi*c_0*c1*np.exp(0.5*c1*i)) - (8*omega*c2))
        y_pred.append(y_pred_aux)

    return y_true_noise, y_pred, t
