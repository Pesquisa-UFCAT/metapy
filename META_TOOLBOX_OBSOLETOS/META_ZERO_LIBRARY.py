import numpy as np
from scipy.optimize import minimize_scalar
import META_TOOLBOX_OBSOLETOS.META_CO_LIBRARY as META_CO

# Fibonacci method
def FIBONACCI_SEQUENCE(N):
    GOLDEN_RATIO = ((1 + 5 ** (0.5)) / 2)
    INVERSE_GOLDEN_RATIO = ((1 - 5 ** (0.5)) / 2)
    FIBONACCI_NUMBER_N = (1 / 5 ** (0.5)) * (GOLDEN_RATIO ** N - INVERSE_GOLDEN_RATIO ** N) 
    return FIBONACCI_NUMBER_N

def FIBONACCI_MOVEMENT(X_L, X_U, I, N_ITER):
    INDEX_FNUM = N_ITER - I - 1
    INDEX_FDEN = N_ITER - I
    F_NUM = FIBONACCI_SEQUENCE(INDEX_FNUM)
    F_DEN = FIBONACCI_SEQUENCE(INDEX_FDEN)
    L_I = (F_NUM / F_DEN) * (X_U - X_L)
    U_I = X_U - L_I
    V_I = X_L + L_I
    return U_I, V_I, L_I, INDEX_FNUM, F_NUM, INDEX_FDEN, F_DEN

# Golden section method
def GOLDEN_MOVEMENT(X_L, X_U):
    PHI = (1 + np.sqrt(5)) / 2
    L_I = (X_U - X_L) / PHI
    U_I = X_U - L_I 
    V_I = X_L + L_I
    return U_I, V_I, L_I

def F_ALPHA(alpha, args):
    X = args[0]
    D = args[1]
    NULL_DIC = args[2]
    OF_FUNCTION = args[3]
    X_ALPHA = []
    for I in range(len(X)):
        X_ALPHA.append(X[I] + alpha * D[I])
    return OF_FUNCTION(X_ALPHA, NULL_DIC)

def GRADIENT_MOVEMENT_FIRST_ORDER(X_T0I, HISTORY, S_KMINUS1, OF_FUNCTION, OF_FUNCTION_DERIVATIVE, METHOD_TYPE, X_L, X_U, NULL_DIC, ITER):
    S = []
    X_T1I = []

    if METHOD_TYPE == "SD": # Steepest descent
        OF_DIFF = OF_FUNCTION_DERIVATIVE(X_T0I, NULL_DIC)
        for I in range(len(X_T0I)):
            S.append(-OF_DIFF[I])
        BETA = None
       
    elif METHOD_TYPE == "CGM-FR": # Conjugate Gradient Method Fletcher-Reeves
        NUM = 0 
        DEN = 0
        G_K = OF_FUNCTION_DERIVATIVE(X_T0I, NULL_DIC)
        
        if ITER == 0:
            for J in range(len(X_T0I)):
                S.append(-G_K[J])
            BETA = None 
        else:
            G_KMINUS = OF_FUNCTION_DERIVATIVE(HISTORY[0][0, :], NULL_DIC)
            for J in range(len(X_T0I)):
                DEN += G_KMINUS[J] ** 2 
                NUM += G_K[J] ** 2     
            BETA = NUM / DEN 
            for J in range(len(X_T0I)):
                S.append(-G_K[J] + BETA *(S_KMINUS1[J]))

    elif METHOD_TYPE == "CGM-PRP": # Conjugate Gradient Method Polak-Ribiére-Polyak
        NUM = 0 
        DEN = 0
        G_K = OF_FUNCTION_DERIVATIVE(X_T0I, NULL_DIC)
        
        if ITER == 0:
            for J in range(len(X_T0I)):
                S.append(-G_K[J])
            BETA = None 
        else:
            G_KMINUS = OF_FUNCTION_DERIVATIVE(HISTORY[0][0, :], NULL_DIC)
            for J in range(len(X_T0I)):
                DEN += G_KMINUS[J] ** 2 
                NUM += G_K[J] * (G_K[J] - G_KMINUS[J])    
            BETA = NUM / DEN 
            for J in range(len(X_T0I)):
                S.append(-G_K[J] + BETA *(S_KMINUS1[J])) 
                                
    elif METHOD_TYPE == "CGM-HS": # Conjugate Gradient Descent Method Hestenes–Stiefel
        NUM = 0 
        DEN = 0
        G_K = OF_FUNCTION_DERIVATIVE(X_T0I, NULL_DIC)
        
        if ITER == 0:
            for J in range(len(X_T0I)):
                S.append(-G_K[J])
            BETA = None 
        else:
            G_KMINUS = OF_FUNCTION_DERIVATIVE(HISTORY[0][0, :], NULL_DIC)
            for J in range(len(X_T0I)):
                DEN += S_KMINUS1[J] * (G_K[J] - G_KMINUS[J])
                NUM += G_K[J] * (G_K[J] - G_KMINUS[J])    
            BETA = NUM / DEN 
            for J in range(len(X_T0I)):
                S.append(-G_K[J] + BETA *(S_KMINUS1[J])) 
    
    elif METHOD_TYPE == "CGM-DY": # Conjugate Gradient Descent Method Dai-Yuan
        NUM = 0 
        DEN = 0
        G_K = OF_FUNCTION_DERIVATIVE(X_T0I, NULL_DIC)
        
        if ITER == 0:
            for J in range(len(X_T0I)):
                S.append(-G_K[J])
            BETA = None 
        else:
            G_KMINUS = OF_FUNCTION_DERIVATIVE(HISTORY[0][0, :], NULL_DIC)
            for J in range(len(X_T0I)):
                DEN += S_KMINUS1[J] * (G_K[J] - G_KMINUS[J])
                NUM += G_K[J] ** 2 
            BETA = NUM / DEN 
            for J in range(len(X_T0I)):
                S.append(-G_K[J] + BETA *(S_KMINUS1[J])) 

    elif METHOD_TYPE == "CGM-LS": # Conjugate Gradient Descent Method Liu-Storey
        NUM = 0 
        DEN = 0
        G_K = OF_FUNCTION_DERIVATIVE(X_T0I, NULL_DIC)
        
        if ITER == 0:
            for J in range(len(X_T0I)):
                S.append(-G_K[J])
            BETA = None 
        else:
            G_KMINUS = OF_FUNCTION_DERIVATIVE(HISTORY[0][0, :], NULL_DIC)
            for J in range(len(X_T0I)):
                DEN += -S_KMINUS1[J] * G_KMINUS[J]
                NUM += G_K[J] * (G_K[J] - G_KMINUS[J])   
            BETA = NUM / DEN 
            for J in range(len(X_T0I)):
                S.append(-G_K[J] + BETA *(S_KMINUS1[J])) 

    elif METHOD_TYPE == "CGM-DL": # Conjugate Gradient Descent Method Dai-Liao
        NUM = 0 
        DEN = 0
        G_K = OF_FUNCTION_DERIVATIVE(X_T0I, NULL_DIC)
        
        if ITER == 0:
            for J in range(len(X_T0I)):
                S.append(-G_K[J])
            BETA = None 
        else:
            G_KMINUS = OF_FUNCTION_DERIVATIVE(HISTORY[0][0, :], NULL_DIC)
            Y_K = []
            S_K = []
            for J in range(len(X_T0I)):
                Y_K.append(G_K[J] - G_KMINUS[J])
                S_K.append(X_T0I[J] - HISTORY[0][0, :][J])
            T_RATE = (2 * (np.sqrt(sum([I ** 2 for I in Y_K]))) ** 2) / (sum([I * J for I, J in zip(Y_K, S_K)]))
            for J in range(len(X_T0I)):
                DEN += S_KMINUS1[J] * Y_K[J]
                NUM += (Y_K[J] - T_RATE * S_K[J]) * G_K[J] 
            BETA = NUM / DEN 
            for J in range(len(X_T0I)):
                S.append(-G_K[J] + BETA *(S_KMINUS1[J])) 

    elif METHOD_TYPE == "DFP" or METHOD_TYPE == "BFGS": # Davidon-Fletcher-Powell and Broyden-Fletcher-Goldfarb-Shanno" 
        
        G_K = OF_FUNCTION_DERIVATIVE(X_T0I, NULL_DIC)
        G_K = np.array(G_K).reshape(len(X_T0I), 1)
        S = []
        
        if METHOD_TYPE == "DFP":
            THETA = 0
        elif METHOD_TYPE == "BFGS":
            THETA = 1

        BETA = None
       
        if ITER == 0:
            H = np.eye(len(X_T0I))
            AUX_H = H.copy()
        else:
            H = S_KMINUS1.copy()
            G_KMINUS = OF_FUNCTION_DERIVATIVE(HISTORY[0][0, :], NULL_DIC)
            G_KMINUS = np.array(G_KMINUS).reshape(len(X_T0I), 1)
            X_T0I = np.array(X_T0I).reshape(len(X_T0I), 1)
            X_TMINUS11 = np.array(HISTORY[0][0, :]).reshape(len(X_T0I), 1)
            P_K = X_T0I - X_TMINUS11
            Y_K = G_K - G_KMINUS        
            SIGMA = np.dot(P_K.T, Y_K)[0,0]
            X_T0I = np.transpose(X_T0I).tolist()[0]
            TAL = np.dot(np.dot(Y_K.T, H), Y_K)[0,0] 
            FACTOR_1 = (SIGMA + THETA * TAL) / (SIGMA ** 2)
            FACTOR_2 = (THETA - 1) / TAL
            FACTOR_3 = THETA / SIGMA 
            D_Q1 = FACTOR_1 * np.dot(P_K, P_K.T)    
            D_Q2 = FACTOR_2 * np.dot(np.dot(H, Y_K), np.transpose(np.dot(H, Y_K)))
            D_Q3 = FACTOR_3 * (np.dot(np.dot(H, Y_K), P_K.T) + np.dot(P_K, np.transpose(np.dot(H, Y_K))))
            D_Q = D_Q1 + D_Q2 - D_Q3
            H += D_Q
            AUX_H = H.copy()

        AUX = np.dot(-H, G_K)
        S = np.transpose(AUX).tolist()[0]

    # Movement
    STEP = minimize_scalar(F_ALPHA, bounds = (.0001, 1.00), args = ([X_T0I, S, NULL_DIC, OF_FUNCTION]), method = 'bounded')
    ALPHA = STEP.x
    for I in range(len(X_T0I)):
        X_T1I.append(X_T0I[I] + S[I] * ALPHA)

    # Storage update matrix in S
    if METHOD_TYPE == "DFP" or METHOD_TYPE == "BFGS":
        S = AUX_H.copy()
    
    # Check bounds
    # X_INEW = META_CO.check_interval_01(X_INEW, X_L, X_U) 
    
    # Evaluation of the objective function and fitness
    OF_INEW = OF_FUNCTION(X_T1I, NULL_DIC)
    FIT_INEW = META_CO.fit_value(OF_INEW)
    NEOF = 1

    return X_T1I, OF_INEW, FIT_INEW, NEOF, ALPHA, BETA, S

"""
http://www2.peq.coppe.ufrj.br/Pessoal/Professores/Arge/EQE489/Material_extra/Otimiza.pdf

# Bissection method
def BISECTION_MOVEMENT(X_L, X_U):
    PHI = 2
    L_I = (X_U - X_L) / PHI
    U_I = X_U - L_I
    V_I = X_L + L_I
    return U_I, V_I, L_I
"""

