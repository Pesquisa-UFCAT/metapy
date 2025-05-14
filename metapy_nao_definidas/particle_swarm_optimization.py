"""particle swarm optimization functions"""

import numpy as np

def PSO_MOVEMENT(OF_FUNCTION, V_T0I, X_T0I, C_1, C_2, P_BEST, G_BEST, D, X_L, X_U, V_MIN, V_MAX, INERTIA, NULL_DIC):
    """
    PSO velocity update.
    """

    # Start internal variables
    V_T1I = []
    X_T1I = []

    # Update velocity
    for I_COUNT in range(D):
        R_1 = np.random.random()
        R_2 = np.random.random()
        NEW_VEL = INERTIA * V_T0I[I_COUNT] + R_1 * C_1 * (P_BEST[I_COUNT] - X_T0I[I_COUNT]) + R_2 * C_2 * (G_BEST[I_COUNT] - X_T0I[I_COUNT])
        V_T1I.append(NEW_VEL)
    
    # Check boundes velocity
    V_T1I = META_CL.check_interval_01(V_T1I, V_MIN, V_MAX)
    
    # Update position
    for I_COUNT in range(D):
        NEW_VALUE = X_T0I[I_COUNT] + V_T1I[I_COUNT]
        X_T1I.append(NEW_VALUE) 
    
    # Check boundes position
    X_T1I = META_CL.check_interval_01(X_T1I, X_L, X_U) 
    
    # Evaluation of the objective function and fitness
    OF_T1I = OF_FUNCTION(X_T1I, NULL_DIC)
    FIT_T1I = META_CL.fit_value(OF_T1I)
    NEOF = 1
    
    return V_T1I, X_T1I, OF_T1I, FIT_T1I, NEOF


def UPDATE_BEST(X, X_BEST, Y, Y_BEST):
    """
    """
    MASK = Y < Y_BEST

    if MASK == True:
        X_BEST = X.copy()
        Y_BEST = Y

    return X_BEST, Y_BEST
