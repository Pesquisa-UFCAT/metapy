import numpy as np
import time
from multiprocessing import Pool

import META_TOOLBOX_OBSOLETOS.META_CO_LIBRARY as META_CO
import META_TOOLBOX_OBSOLETOS.META_HC_LIBRARY as META_HC
import metapy_toolbox.simulated_annealing as META_SA
import META_TOOLBOX_OBSOLETOS.META_FA_LIBRARY as META_FA
import META_TOOLBOX_OBSOLETOS.META_DE_LIBRARY as META_DE
import META_TOOLBOX_OBSOLETOS.META_GA_LIBRARY as META_GA
import META_TOOLBOX_OBSOLETOS.META_PSO_LIBRARY as META_PSO
import META_TOOLBOX_OBSOLETOS.META_ZERO_LIBRARY as META_ZERO
from datetime import datetime

def HELLO():
    """
    Test function.
    """
    print("hello world")
    return

def HILL_CLIMBING_001(OF_FUNCTION, SETUP):
    """ 
    Standard Hill climbing algorithm. Continuous version. The algorithm also presents the results formatted in a spreadsheet.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/HC.html
    """
    
    # Setup config
    N_REP = SETUP['N_REP']
    N_ITER = SETUP['N_ITER']
    N_POP = SETUP['N_POP']
    D = SETUP['D']
    X_L = SETUP['X_L']
    X_U = SETUP['X_U']
    NULL_DIC = SETUP['NULL_DIC']
    MODEL_NAME = 'META_HC001_'

    # Parameters
    PARAMETERS = SETUP['PARAMETERS']
    SIGMA = PARAMETERS['PERCENTAGE STD (SIGMA)'] / 100
    
    # Creating variables in the repetitions procedure
    RESULTS_REP = []
    BEST_REP = []
    WORST_REP = []
    AVERAGE_REP = []
    NAME = []
    if NULL_DIC == None:
        NULL_DIC = []
    else:
        pass 
    
    # Repetition looping
    INIT = time.time()
    for REP in range(N_REP):
        
        # Creating variables in the iterations procedure
        OF = np.zeros((N_POP, 1)); 
        FIT = np.zeros((N_POP, 1))
        RESULTS_ITER = [{'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'PARAMETERS': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': J} for J in range(N_POP)]
        BEST_ITER = {'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'PARAMETERS': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': np.empty(N_ITER + 1)}
        AVERAGE_ITER = {'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1)}
        WORST_ITER = {'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': np.empty(N_ITER + 1)}
        NEOF_COUNT = 0 
        
        # Initial population
        X = META_CO.initial_population_01(N_POP, D, X_L, X_U)
        for I in range(N_POP):
            OF[I, 0] = OF_FUNCTION(X[I, :], NULL_DIC)
            FIT[I, 0] = META_CO.fit_value(OF[I, 0])
            NEOF_COUNT += 1
               
        # Storage all values in RESULTS_ITER
        for I, X_ALL, OF_ALL, FIT_ALL, in zip(RESULTS_ITER, X, OF, FIT):
            I['X_POSITION'][0, :] = X_ALL
            I['OF'][0] = OF_ALL
            I['FIT'][0] = FIT_ALL
            I['PARAMETERS'][0] = None
            I['NEOF'][0] = NEOF_COUNT
        
        # Best, average and worst storage
        BEST_POSITION, WORST_POSITION, X_BEST, X_WORST, OF_BEST, OF_WORST, FIT_BEST, FIT_WORST, OF_AVERAGE, FIT_AVERAGE = META_CO.best_values(X, OF, FIT, N_POP)
        BEST_ITER['ID_PARTICLE'][0] = BEST_POSITION
        WORST_ITER['ID_PARTICLE'][0] = WORST_POSITION
        BEST_ITER['X_POSITION'][0, :] = X_BEST
        WORST_ITER['X_POSITION'][0, :] = X_WORST
        BEST_ITER['OF'][0] = OF_BEST
        AVERAGE_ITER['OF'][0] = OF_AVERAGE
        WORST_ITER['OF'][0] = OF_WORST
        BEST_ITER['FIT'][0] = FIT_BEST
        AVERAGE_ITER['FIT'][0] = FIT_AVERAGE
        WORST_ITER['FIT'][0] = FIT_WORST
        BEST_ITER['PARAMETERS'][0] = None
        BEST_ITER['NEOF'][0] = NEOF_COUNT
        AVERAGE_ITER['NEOF'][0] = NEOF_COUNT
        WORST_ITER['NEOF'][0] = NEOF_COUNT
        
        # Iteration procedure
        for ITER in range(N_ITER):

            # Population movement
            for POP in range(N_POP):
                
                # Hill Climbing particle movement
                X_ITEMP, OF_ITEMP, FIT_ITEMP, NEOF = META_HC.HC_MOVEMENT(OF_FUNCTION, NULL_DIC, X[POP, :], X_L, X_U, D, SIGMA) 
                
                # New design variables
                if FIT_ITEMP > FIT[POP, 0]:
                    X[POP, :] = X_ITEMP
                    OF[POP, 0] = OF_ITEMP
                    FIT[POP, 0] = FIT_ITEMP
                else:
                    pass
                
                # Update NEOF (Number of Objective Function Evaluations)
                NEOF_COUNT += NEOF
            
            # Storage all values in RESULTS_ITER
            for I, X_ALL, OF_ALL, FIT_ALL  in zip(RESULTS_ITER, X, OF, FIT):
                I['X_POSITION'][ITER + 1, :] = X_ALL
                I['OF'][ITER + 1] = OF_ALL
                I['FIT'][ITER + 1] = FIT_ALL
                I['PARAMETERS'][ITER + 1] = None
                I['NEOF'][ITER + 1] = NEOF_COUNT
            
            # Best, average and worst storage
            BEST_POSITION, WORST_POSITION, X_BEST, X_WORST, OF_BEST, OF_WORST, FIT_BEST, FIT_WORST, OF_AVERAGE, FIT_AVERAGE = META_CO.best_values(X, OF, FIT, N_POP)
            BEST_ITER['ID_PARTICLE'][ITER + 1] = BEST_POSITION
            WORST_ITER['ID_PARTICLE'][ITER + 1] = WORST_POSITION
            BEST_ITER['X_POSITION'][ITER + 1, :] = X_BEST
            WORST_ITER['X_POSITION'][ITER + 1, :] = X_WORST
            BEST_ITER['OF'][ITER + 1] = OF_BEST
            AVERAGE_ITER['OF'][ITER + 1] = OF_AVERAGE
            WORST_ITER['OF'][ITER + 1] = OF_WORST
            BEST_ITER['FIT'][ITER + 1] = FIT_BEST
            AVERAGE_ITER['FIT'][ITER + 1] = FIT_AVERAGE
            WORST_ITER['FIT'][ITER + 1] = FIT_WORST
            BEST_ITER['PARAMETERS'][ITER + 1] = None
            BEST_ITER['NEOF'][ITER + 1] = NEOF_COUNT
            AVERAGE_ITER['NEOF'][ITER + 1] = NEOF_COUNT
            WORST_ITER['NEOF'][ITER + 1] = NEOF_COUNT
        
        # Append iteration results
        RESULTS_REP.append(RESULTS_ITER)
        BEST_REP.append(BEST_ITER)
        AVERAGE_REP.append(AVERAGE_ITER)
        WORST_REP.append(WORST_ITER)
        
        # Progress bar update
        time.sleep(0.01)
        META_CO.PROGRESS_BAR(REP + 1, N_REP)
    END = time.time()
    
    # Resume process (Time and Excel outputs)
    print('Process Time: %.2f' % (END - INIT), 'Seconds', '\n', 'Seconds per repetition: %.2f' % ((END - INIT) / N_REP))
    STATUS_PROCEDURE = META_CO.SUMMARY_ANALYSIS(BEST_REP, N_REP, N_ITER)
    for REP in range(N_REP):
        NAME.append(MODEL_NAME + 'REP_' + str(REP) + '_BEST_' + str(REP) + '_' + str(datetime.now().strftime('%Y%m%d %H%M%S')))
        META_CO.EXCEL_WRITER_ITERATION(NAME[REP], D, BEST_REP[REP])
    NAME_RESUME = MODEL_NAME + 'RESUME' + '_' + str(datetime.now().strftime('%Y%m%d %H%M%S'))
    META_CO.EXCEL_PROCESS_RESUME(NAME_RESUME, D, BEST_REP, N_ITER, N_REP)    
    
    return RESULTS_REP, BEST_REP, AVERAGE_REP, WORST_REP, STATUS_PROCEDURE

def SIMULATED_ANNEALING_001(OF_FUNCTION, SETUP):
    """ 
    Standard Simulated annealing algorithm. Continuous version. The algorithm also presents the results formatted in a spreadsheet.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/SA001.html
    """
    
    # Setup config
    N_REP = SETUP['N_REP']
    N_ITER = SETUP['N_ITER']
    N_POP = SETUP['N_POP']
    D = SETUP['D']
    X_L = SETUP['X_L']
    X_U = SETUP['X_U']
    NULL_DIC = SETUP['NULL_DIC']
    MODEL_NAME = 'META_SA001_'

    # Parameters
    PARAMETERS = SETUP['PARAMETERS']
    SIGMA = PARAMETERS['PERCENTAGE STD (SIGMA)'] / 100
    SCHEDULE = PARAMETERS['COOLING SCHEME']
    ALPHA = PARAMETERS['TEMP. UPDATE (ALPHA)']
    TEMP_INI = PARAMETERS['INITIAL TEMP. (T_0)']
        
    # Creating variables in the repetitions procedure
    RESULTS_REP = []
    BEST_REP = []
    WORST_REP = []
    AVERAGE_REP = []
    NAME = []
    if NULL_DIC == None:
        NULL_DIC = []
    else:
        pass 
    
    # Repetition looping
    INIT = time.time()
    for REP in range(N_REP):
        
        # Creating variables in the iterations procedure
        OF = np.zeros((N_POP, 1)); 
        FIT = np.zeros((N_POP, 1))
        RESULTS_ITER = [{'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'PARAMETERS': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': J} for J in range(N_POP)]
        BEST_ITER = {'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'PARAMETERS': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': np.empty(N_ITER + 1)}
        AVERAGE_ITER = {'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1)}
        WORST_ITER = {'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': np.empty(N_ITER + 1)}
        NEOF_COUNT = 0 
        
        # Initial population
        X = META_CO.initial_population_01(N_POP, D, X_L, X_U)
        for I in range(N_POP):
            OF[I, 0] = OF_FUNCTION(X[I, :], NULL_DIC)
            FIT[I, 0] = META_CO.fit_value(OF[I, 0])
            NEOF_COUNT += 1
      
        # Initial temperature
        if TEMP_INI is None:
            TEMPERATURE = META_SA.START_TEMPERATURE(OF_FUNCTION, NULL_DIC, N_POP, D, X_L, X_U, X, OF, SIGMA)                      
        else:
            TEMPERATURE = TEMP_INI
                       
        # Storage all values in RESULTS_ITER
        for I, X_ALL, OF_ALL, FIT_ALL, in zip(RESULTS_ITER, X, OF, FIT):
            I['X_POSITION'][0, :] = X_ALL
            I['OF'][0] = OF_ALL
            I['FIT'][0] = FIT_ALL
            I['PARAMETERS'][0] = TEMPERATURE
            I['NEOF'][0] = NEOF_COUNT
        
        # Best, average and worst storage
        BEST_POSITION, WORST_POSITION, X_BEST, X_WORST, OF_BEST, OF_WORST, FIT_BEST, FIT_WORST, OF_AVERAGE, FIT_AVERAGE = META_CO.best_values(X, OF, FIT, N_POP)
        BEST_ITER['ID_PARTICLE'][0] = BEST_POSITION
        WORST_ITER['ID_PARTICLE'][0] = WORST_POSITION
        BEST_ITER['X_POSITION'][0, :] = X_BEST
        WORST_ITER['X_POSITION'][0, :] = X_WORST
        BEST_ITER['OF'][0] = OF_BEST
        AVERAGE_ITER['OF'][0] = OF_AVERAGE
        WORST_ITER['OF'][0] = OF_WORST
        BEST_ITER['FIT'][0] = FIT_BEST
        AVERAGE_ITER['FIT'][0] = FIT_AVERAGE
        WORST_ITER['FIT'][0] = FIT_WORST
        BEST_ITER['PARAMETERS'][0] = TEMPERATURE
        BEST_ITER['NEOF'][0] = NEOF_COUNT
        AVERAGE_ITER['NEOF'][0] = NEOF_COUNT
        WORST_ITER['NEOF'][0] = NEOF_COUNT
        
        # Iteration procedure
        for ITER in range(N_ITER):

            # Population movement
            for POP in range(N_POP):
                
                # Simulated Annealing particle movement (Same Hill Climbing movement)
                X_ITEMP, OF_ITEMP, FIT_ITEMP, NEOF = META_HC.HC_MOVEMENT(OF_FUNCTION, NULL_DIC, X[POP, :], X_L, X_U, D, SIGMA) 
                
                # Energy
                DELTAE = OF_ITEMP - OF[POP, 0]
                
                # Probability of acceptance of the movement
                if DELTAE < 0:
                    PROBABILITY_STATE = 1
                elif DELTAE >= 0:
                    PROBABILITY_STATE = np.exp(- DELTAE / TEMPERATURE)
                
                # New design variables
                RANDON_NUMBER = np.random.random()
                if RANDON_NUMBER < PROBABILITY_STATE:
                    X[POP, :] = X_ITEMP
                    OF[POP, 0] = OF_ITEMP
                    FIT[POP, 0] = FIT_ITEMP
                else:
                    pass
                
                # Update NEOF (Number of Objective Function Evaluations)
                NEOF_COUNT += NEOF
            
            # Storage all values in RESULTS_ITER
            for I, X_ALL, OF_ALL, FIT_ALL  in zip(RESULTS_ITER, X, OF, FIT):
                I['X_POSITION'][ITER + 1, :] = X_ALL
                I['OF'][ITER + 1] = OF_ALL
                I['FIT'][ITER + 1] = FIT_ALL
                I['PARAMETERS'][ITER + 1] = TEMPERATURE
                I['NEOF'][ITER + 1] = NEOF_COUNT
            
            # Best, average and worst storage
            BEST_POSITION, WORST_POSITION, X_BEST, X_WORST, OF_BEST, OF_WORST, FIT_BEST, FIT_WORST, OF_AVERAGE, FIT_AVERAGE = META_CO.best_values(X, OF, FIT, N_POP)
            BEST_ITER['ID_PARTICLE'][ITER + 1] = BEST_POSITION
            WORST_ITER['ID_PARTICLE'][ITER + 1] = WORST_POSITION
            BEST_ITER['X_POSITION'][ITER + 1, :] = X_BEST
            WORST_ITER['X_POSITION'][ITER + 1, :] = X_WORST
            BEST_ITER['OF'][ITER + 1] = OF_BEST
            AVERAGE_ITER['OF'][ITER + 1] = OF_AVERAGE
            WORST_ITER['OF'][ITER + 1] = OF_WORST
            BEST_ITER['FIT'][ITER + 1] = FIT_BEST
            AVERAGE_ITER['FIT'][ITER + 1] = FIT_AVERAGE
            WORST_ITER['FIT'][ITER + 1] = FIT_WORST
            BEST_ITER['PARAMETERS'][ITER + 1] = TEMPERATURE
            BEST_ITER['NEOF'][ITER + 1] = NEOF_COUNT
            AVERAGE_ITER['NEOF'][ITER + 1] = NEOF_COUNT
            WORST_ITER['NEOF'][ITER + 1] = NEOF_COUNT

            # Update temperature
            # https://pdfs.semanticscholar.org/da04/e9aa59e9bac1926c2ee776fc8881566739c4.pdf
            # Geometric cooling scheme
            if SCHEDULE == 'GEOMETRIC':
                TEMPERATURE = TEMPERATURE * ALPHA
            # Lundy cooling scheme
            elif SCHEDULE == 'LUNDY':
                TEMPERATURE = TEMPERATURE / (1 + ALPHA * TEMPERATURE) 
            # Linear cooling scheme
            elif SCHEDULE == 'LINEAR':
                TEMPERATURE = TEMPERATURE - ALPHA
            # Logarithmic cooling scheme
            elif SCHEDULE == 'LOGARITHMIC':
                TEMPERATURE = TEMPERATURE / np.log2(ITER + ALPHA)
        
        # Append iteration results
        RESULTS_REP.append(RESULTS_ITER)
        BEST_REP.append(BEST_ITER)
        AVERAGE_REP.append(AVERAGE_ITER)
        WORST_REP.append(WORST_ITER)
        
        # Progress bar update
        time.sleep(0.01)
        META_CO.PROGRESS_BAR(REP + 1, N_REP)
    END = time.time()
    
    # Resume process (Time and Excel outputs)
    print('Process Time: %.2f' % (END - INIT), 'Seconds', '\n', 'Seconds per repetition: %.2f' % ((END - INIT) / N_REP))
    STATUS_PROCEDURE = META_CO.SUMMARY_ANALYSIS(BEST_REP, N_REP, N_ITER)
    for REP in range(N_REP):
        NAME.append(MODEL_NAME + 'REP_' + str(REP) + '_BEST_' + str(REP) + '_' + str(datetime.now().strftime('%Y%m%d %H%M%S')))
        META_CO.EXCEL_WRITER_ITERATION(NAME[REP], D, BEST_REP[REP])
    NAME_RESUME = MODEL_NAME + 'RESUME' + '_' + str(datetime.now().strftime('%Y%m%d %H%M%S'))
    META_CO.EXCEL_PROCESS_RESUME(NAME_RESUME, D, BEST_REP, N_ITER, N_REP)    
    
    return RESULTS_REP, BEST_REP, AVERAGE_REP, WORST_REP, STATUS_PROCEDURE

def FIREFLY_ALGORITHM_001(OF_FUNCTION, SETUP):
    """ 
    Standard Firefly algorithm.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/FA.html
    """
    
    # Setup config
    N_REP = SETUP['N_REP']
    N_ITER = SETUP['N_ITER']
    N_POP = SETUP['N_POP']
    D = SETUP['D']
    X_L = SETUP['X_L']
    X_U = SETUP['X_U']
    NULL_DIC = SETUP['NULL_DIC']
    MODEL_NAME = 'META_FA001_'
    
    # Parameters
    PARAMETERS = SETUP['PARAMETERS']
    BETA_0 = PARAMETERS['ATTRACTIVENESS (BETA_0)']
    ALPHA_MIN = PARAMETERS['MIN. RANDOM FACTOR (ALPHA_MIN)']
    ALPHA_MAX = PARAMETERS['MAX. RANDOM FACTOR (ALPHA_MAX)']
    THETA = PARAMETERS['THETA']
    GAMMA = PARAMETERS['LIGHT ABSORPTION (GAMMA)']
    ALPHA_UPDATE = PARAMETERS['TYPE ALPHA UPDATE']
    SCALING = PARAMETERS['SCALING (S_D)']
    
    # Creating variables in the repetitions procedure
    RESULTS_REP = []
    BEST_REP = []
    WORST_REP = []
    AVERAGE_REP = []
    NAME = []
    if NULL_DIC == None:
        NULL_DIC = []
    else:
        pass 
    
    # Repetition looping
    INIT = time.time()
    for REP in range(N_REP):
        
        # Creating variables in the iterations procedure
        OF = np.zeros((N_POP, 1)); 
        FIT = np.zeros((N_POP, 1))
        RESULTS_ITER = [{'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'PARAMETERS': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': J} for J in range(N_POP)]
        BEST_ITER = {'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'PARAMETERS': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': np.empty(N_ITER + 1)}
        AVERAGE_ITER = {'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1)}
        WORST_ITER = {'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': np.empty(N_ITER + 1)}
        NEOF_COUNT = 0 
        
        # Initial population
        X = META_CO.initial_population_01(N_POP, D, X_L, X_U)
        for I in range(N_POP):
            OF[I, 0] = OF_FUNCTION(X[I, :], NULL_DIC)
            FIT[I, 0] = META_CO.fit_value(OF[I, 0])
            NEOF_COUNT += 1
        
        # Initial random parameter
        ALPHA = ALPHA_MAX
   
        # Storage all values in RESULTS_ITER
        for I, X_ALL, OF_ALL, FIT_ALL, in zip(RESULTS_ITER, X, OF, FIT):
            I['X_POSITION'][0, :] = X_ALL
            I['OF'][0] = OF_ALL
            I['FIT'][0] = FIT_ALL
            I['PARAMETERS'][0] = ALPHA
            I['NEOF'][0] = NEOF_COUNT
        
        # Best, average and worst storage
        BEST_POSITION, WORST_POSITION, X_BEST, X_WORST, OF_BEST, OF_WORST, FIT_BEST, FIT_WORST, OF_AVERAGE, FIT_AVERAGE = META_CO.best_values(X, OF, FIT, N_POP)
        BEST_ITER['ID_PARTICLE'][0] = BEST_POSITION
        WORST_ITER['ID_PARTICLE'][0] = WORST_POSITION
        BEST_ITER['X_POSITION'][0, :] = X_BEST
        WORST_ITER['X_POSITION'][0, :] = X_WORST
        BEST_ITER['OF'][0] = OF_BEST
        AVERAGE_ITER['OF'][0] = OF_AVERAGE
        WORST_ITER['OF'][0] = OF_WORST
        BEST_ITER['FIT'][0] = FIT_BEST
        AVERAGE_ITER['FIT'][0] = FIT_AVERAGE
        WORST_ITER['FIT'][0] = FIT_WORST
        BEST_ITER['PARAMETERS'][0] = ALPHA
        BEST_ITER['NEOF'][0] = NEOF_COUNT
        AVERAGE_ITER['NEOF'][0] = NEOF_COUNT
        WORST_ITER['NEOF'][0] = NEOF_COUNT
        
        # Iteration procedure
        for ITER in range(N_ITER):
            # Ordering firefly according to fitness
            X_TEMP = X.copy()
            OF_TEMP = OF.copy()
            FIT_TEMP = FIT.copy()
            SORT_POSITIONS = np.argsort(OF_TEMP.T)
            
            for I in range(N_POP):
                AUX = SORT_POSITIONS[0, I]
                X[I, :] = X_TEMP[AUX, :]
                OF[I, 0] = OF_TEMP[AUX, 0] 
                FIT[I, 0] = FIT_TEMP[AUX, 0]
            
            # Population movement
            X_J = X.copy()
            FITJ = FIT.copy()
            for POP_I in range(N_POP):
                FIT_I = FIT[POP_I, 0]
                for POP_J in range(N_POP):
                    FIT_J = FITJ[POP_J, 0]
                    if FIT_I < FIT_J:
                        BETA = META_FA.ATTRACTIVENESS_FIREFLY_PARAMETER(BETA_0, GAMMA, X[POP_I, :], X_J[POP_J, :], D)                            
                        X_ITEMP, OF_ITEMP, FIT_ITEMP, NEOF = META_FA.FIREFLY_MOVEMENT(OF_FUNCTION, X[POP_I, :], X_J[POP_J, :], BETA, ALPHA, SCALING, D, X_L, X_U, NULL_DIC)
                    else:
                        X_ITEMP = X[POP_I, :]
                        OF_ITEMP = OF[POP_I, 0]
                        FIT_ITEMP = FIT[POP_I, 0]
                        NEOF = 0
                    
                    # New design variables
                    X[POP_I, :] = X_ITEMP
                    OF[POP_I, 0] = OF_ITEMP
                    FIT[POP_I, 0] = FIT_ITEMP
                    NEOF_COUNT += NEOF
            
            # Storage all values in RESULTS_ITER
            for I, X_ALL, OF_ALL, FIT_ALL  in zip(RESULTS_ITER, X, OF, FIT):
                I['X_POSITION'][ITER + 1, :] = X_ALL
                I['OF'][ITER + 1] = OF_ALL
                I['FIT'][ITER + 1] = FIT_ALL
                I['PARAMETERS'][ITER + 1] = ALPHA
                I['NEOF'][ITER + 1] = NEOF_COUNT
            
            # Best, average and worst storage
            BEST_POSITION, WORST_POSITION, X_BEST, X_WORST, OF_BEST, OF_WORST, FIT_BEST, FIT_WORST, OF_AVERAGE, FIT_AVERAGE = META_CO.best_values(X, OF, FIT, N_POP)
            BEST_ITER['ID_PARTICLE'][ITER + 1] = BEST_POSITION
            WORST_ITER['ID_PARTICLE'][ITER + 1] = WORST_POSITION
            BEST_ITER['X_POSITION'][ITER + 1, :] = X_BEST
            WORST_ITER['X_POSITION'][ITER + 1, :] = X_WORST
            BEST_ITER['OF'][ITER + 1] = OF_BEST
            AVERAGE_ITER['OF'][ITER + 1] = OF_AVERAGE
            WORST_ITER['OF'][ITER + 1] = OF_WORST
            BEST_ITER['FIT'][ITER + 1] = FIT_BEST
            AVERAGE_ITER['FIT'][ITER + 1] = FIT_AVERAGE
            WORST_ITER['FIT'][ITER + 1] = FIT_WORST
            BEST_ITER['PARAMETERS'][ITER + 1] = ALPHA
            BEST_ITER['NEOF'][ITER + 1] = NEOF_COUNT
            AVERAGE_ITER['NEOF'][ITER + 1] = NEOF_COUNT
            WORST_ITER['NEOF'][ITER + 1] = NEOF_COUNT

            # Update random parameter
            if ALPHA_UPDATE == 'YANG 0':
                ALPHA = ALPHA_MIN + (ALPHA_MAX - ALPHA_MIN) * THETA ** ITER
            elif ALPHA_UPDATE == 'YANG 1':
                ALPHA = ALPHA_MAX * THETA ** ITER      
            elif ALPHA_UPDATE == 'YANG 2':
                ALPHA = ALPHA_MAX + (ALPHA_MIN - ALPHA_MAX) * np.exp(- ITER)      
            elif ALPHA_UPDATE == 'YANG 3':
                AUX = 1 + np.exp((ITER - N_ITER) / 200)
                ALPHA = 0.40 / AUX
            elif ALPHA_UPDATE == 'YANG 4':
                ALPHA *= 0.99         
            elif ALPHA_UPDATE == 'YANG 5':
                ALPHA *= (1 - ITER / N_ITER)  
            elif ALPHA_UPDATE == 'YANG 6':
                ALPHA *= (ITER / 9000) ** (1 / ITER)                   
        # Append iteration results
        RESULTS_REP.append(RESULTS_ITER)
        BEST_REP.append(BEST_ITER)
        AVERAGE_REP.append(AVERAGE_ITER)
        WORST_REP.append(WORST_ITER)
        
        # Progress bar update
        time.sleep(0.01)
        META_CO.PROGRESS_BAR(REP + 1, N_REP)
    END = time.time()
    
    # Resume process (Time and Excel outputs)
    print('Process Time: %.2f' % (END - INIT), 'Seconds', '\n', 'Seconds per repetition: %.2f' % ((END - INIT) / N_REP))
    STATUS_PROCEDURE = META_CO.SUMMARY_ANALYSIS(BEST_REP, N_REP, N_ITER)
    for REP in range(N_REP):
        NAME.append(MODEL_NAME + 'REP_' + str(REP) + '_BEST_' + str(REP) + '_' + str(datetime.now().strftime('%Y%m%d %H%M%S')))
        META_CO.EXCEL_WRITER_ITERATION(NAME[REP], D, BEST_REP[REP])
    NAME_RESUME = MODEL_NAME + 'RESUME' + '_' + str(datetime.now().strftime('%Y%m%d %H%M%S'))
    META_CO.EXCEL_PROCESS_RESUME(NAME_RESUME, D, BEST_REP, N_ITER, N_REP)    
    
    return RESULTS_REP, BEST_REP, AVERAGE_REP, WORST_REP, STATUS_PROCEDURE

def PSO_ALGORITHM_001(OF_FUNCTION, SETUP):
    """ 
    Standard Particle Swarm Optimization algorithm. Continuous version. The algorithm also presents the results formatted in a spreadsheet.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/PSO.html
    """
    
    # Setup config
    N_REP = SETUP['N_REP']
    N_ITER = SETUP['N_ITER']
    N_POP = SETUP['N_POP']
    D = SETUP['D']
    X_L = SETUP['X_L']
    X_U = SETUP['X_U']
    NULL_DIC = SETUP['NULL_DIC']
    MODEL_NAME = 'META_PSO001_'

    # Parameters
    PARAMETERS = SETUP['PARAMETERS']
    V_MIN = PARAMETERS['MIN VELOCITY (V_MIN)']
    V_MAX = PARAMETERS['MAX VELOCITY (V_MAX)']
    C_1 = PARAMETERS['COGNITIVE COEFFICIENT (C_1)']
    C_2 = PARAMETERS['SOCIAL COEFFICIENT (C_2)']
    W_MIN = PARAMETERS['MIN INTERIA (W_MIN)']
    W_MAX = PARAMETERS['MAX INERTIA (W_MAX)']
    INERTIA_UPDATE = PARAMETERS['INERTIA UPDATE']
    
    # Creating variables in the repetitions procedure
    RESULTS_REP = []
    BEST_REP = []
    WORST_REP = []
    AVERAGE_REP = []
    NAME = []
    if NULL_DIC == None:
        NULL_DIC = []
    else:
        pass 
    
    # Repetition looping
    INIT = time.time()
    for REP in range(N_REP):
        
        # Creating variables in the iterations procedure
        OF = np.zeros((N_POP, 1)); 
        FIT = np.zeros((N_POP, 1))
        RESULTS_ITER = [{'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'PARAMETERS': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': J} for J in range(N_POP)]
        BEST_ITER = {'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'PARAMETERS': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': np.empty(N_ITER + 1)}
        AVERAGE_ITER = {'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1)}
        WORST_ITER = {'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': np.empty(N_ITER + 1)}
        NEOF_COUNT = 0 
        
        # Initial population
        X = META_CO.initial_population_01(N_POP, D, X_L, X_U)
        for I in range(N_POP):
            OF[I, 0] = OF_FUNCTION(X[I, :], NULL_DIC)
            FIT[I, 0] = META_CO.fit_value(OF[I, 0])
            NEOF_COUNT += 1

        # Initial velociity
        VEL = META_CO.initial_population_01(N_POP, D, V_MIN, V_MAX)
        
        # Initial random parameter
        INERTIA = W_MAX
             
        # Storage all values in RESULTS_ITER
        for I, X_ALL, OF_ALL, FIT_ALL, in zip(RESULTS_ITER, X, OF, FIT):
            I['X_POSITION'][0, :] = X_ALL
            I['OF'][0] = OF_ALL
            I['FIT'][0] = FIT_ALL
            I['PARAMETERS'][0] = INERTIA
            I['NEOF'][0] = NEOF_COUNT
        
        # Best, average and worst storage
        BEST_POSITION, WORST_POSITION, X_BEST, X_WORST, OF_BEST, OF_WORST, FIT_BEST, FIT_WORST, OF_AVERAGE, FIT_AVERAGE = META_CO.best_values(X, OF, FIT, N_POP)
        BEST_ITER['ID_PARTICLE'][0] = BEST_POSITION
        WORST_ITER['ID_PARTICLE'][0] = WORST_POSITION
        BEST_ITER['X_POSITION'][0, :] = X_BEST
        WORST_ITER['X_POSITION'][0, :] = X_WORST
        BEST_ITER['OF'][0] = OF_BEST
        AVERAGE_ITER['OF'][0] = OF_AVERAGE
        WORST_ITER['OF'][0] = OF_WORST
        BEST_ITER['FIT'][0] = FIT_BEST
        AVERAGE_ITER['FIT'][0] = FIT_AVERAGE
        WORST_ITER['FIT'][0] = FIT_WORST
        BEST_ITER['PARAMETERS'][0] = INERTIA
        BEST_ITER['NEOF'][0] = NEOF_COUNT
        AVERAGE_ITER['NEOF'][0] = NEOF_COUNT
        WORST_ITER['NEOF'][0] = NEOF_COUNT

        # Initial PBEST and GBEST
        P_BEST = X.copy()
        OF_PBEST = OF.copy()
        G_BEST = X_BEST.copy()
        
        # Iteration procedure
        for ITER in range(N_ITER):

            # Population movement
            for POP in range(N_POP):
                
                # Particle Swarm Optimization particle movement
                V_ITEMP, X_ITEMP, OF_ITEMP, FIT_ITEMP, NEOF = META_PSO.PSO_MOVEMENT(OF_FUNCTION, VEL[POP, :], X[POP, :], C_1, C_2, P_BEST[POP, :], G_BEST, D, X_L, X_U, V_MIN, V_MAX, INERTIA, NULL_DIC) 

                # Update PBEST and GBEST
                P_BEST[POP, :], OF_PBEST[POP, 0] = META_PSO.UPDATE_BEST(X_ITEMP, P_BEST[POP, :], OF_ITEMP, OF_PBEST[POP, 0])
                               
                # New design variables
                VEL[POP, :] = V_ITEMP
                X[POP, :] = X_ITEMP
                OF[POP, 0] = OF_ITEMP
                FIT[POP, 0] = FIT_ITEMP
               
                # Update NEOF (Number of Objective Function Evaluations)
                NEOF_COUNT += NEOF
            
            # Storage all values in RESULTS_ITER
            for I, X_ALL, OF_ALL, FIT_ALL  in zip(RESULTS_ITER, X, OF, FIT):
                I['X_POSITION'][ITER + 1, :] = X_ALL
                I['OF'][ITER + 1] = OF_ALL
                I['FIT'][ITER + 1] = FIT_ALL
                I['PARAMETERS'][ITER + 1] = None
                I['NEOF'][ITER + 1] = NEOF_COUNT
            
            # GBEST
            X_BEST = P_BEST[OF_PBEST.argmin(), :]
            OF_BEST = OF_PBEST[OF_PBEST.argmin(), :]
            BEST_POSITION = OF_PBEST.argmin()

            # Best, average and worst storage
            _, WORST_POSITION, _, X_WORST, _, OF_WORST, FIT_BEST, FIT_WORST, OF_AVERAGE, FIT_AVERAGE = META_CO.best_values(X, OF, FIT, N_POP)
            BEST_ITER['ID_PARTICLE'][ITER + 1] = BEST_POSITION
            WORST_ITER['ID_PARTICLE'][ITER + 1] = WORST_POSITION
            BEST_ITER['X_POSITION'][ITER + 1, :] = X_BEST
            WORST_ITER['X_POSITION'][ITER + 1, :] = X_WORST
            BEST_ITER['OF'][ITER + 1] = OF_BEST
            AVERAGE_ITER['OF'][ITER + 1] = OF_AVERAGE
            WORST_ITER['OF'][ITER + 1] = OF_WORST
            BEST_ITER['FIT'][ITER + 1] = FIT_BEST
            AVERAGE_ITER['FIT'][ITER + 1] = FIT_AVERAGE
            WORST_ITER['FIT'][ITER + 1] = FIT_WORST
            BEST_ITER['PARAMETERS'][ITER + 1] = None
            BEST_ITER['NEOF'][ITER + 1] = NEOF_COUNT
            AVERAGE_ITER['NEOF'][ITER + 1] = NEOF_COUNT
            WORST_ITER['NEOF'][ITER + 1] = NEOF_COUNT
        
            # Update inertia parameter
            if INERTIA_UPDATE == 'PSO 0':
                INERTIA = W_MAX
            elif INERTIA_UPDATE == 'PSO 1':
                INERTIA = W_MAX - (W_MAX - W_MIN) * (ITER / N_ITER)   
            elif INERTIA_UPDATE == 'PSO 2':
                ALPHA = 1 / np.pi() ** 2
                INERTIA = W_MAX - (W_MAX - W_MIN) * (ITER / N_ITER)  ** ALPHA        
            elif INERTIA_UPDATE == 'PSO 3':
                ALPHA = 1 / np.pi() ** 2
                INERTIA = (2 / N_ITER)  ** 0.30  
            elif INERTIA_UPDATE == 'PSO 4':
                INERTIA = W_MIN + (W_MAX - W_MIN) * np.exp((-10 * ITER) / N_ITER)   
            elif INERTIA_UPDATE == 'PSO 5':
                INERTIA = W_MAX + (W_MIN - W_MAX) * np.log10(1 + (10 * ITER) / N_ITER)  
            elif INERTIA_UPDATE == 'PSO 6':
                INERTIA = 0.50 + np.random.random() / 2 

        # Append iteration results
        RESULTS_REP.append(RESULTS_ITER)
        BEST_REP.append(BEST_ITER)
        AVERAGE_REP.append(AVERAGE_ITER)
        WORST_REP.append(WORST_ITER)
        
        # Progress bar update
        time.sleep(0.01)
        META_CO.PROGRESS_BAR(REP + 1, N_REP)
    END = time.time()
    
    # Resume process (Time and Excel outputs)
    print('Process Time: %.2f' % (END - INIT), 'Seconds', '\n', 'Seconds per repetition: %.2f' % ((END - INIT) / N_REP))
    STATUS_PROCEDURE = META_CO.SUMMARY_ANALYSIS(BEST_REP, N_REP, N_ITER)
    for REP in range(N_REP):
        NAME.append(MODEL_NAME + 'REP_' + str(REP) + '_BEST_' + str(REP) + '_' + str(datetime.now().strftime('%Y%m%d %H%M%S')))
        META_CO.EXCEL_WRITER_ITERATION(NAME[REP], D, BEST_REP[REP])
    NAME_RESUME = MODEL_NAME + 'RESUME' + '_' + str(datetime.now().strftime('%Y%m%d %H%M%S'))
    META_CO.EXCEL_PROCESS_RESUME(NAME_RESUME, D, BEST_REP, N_ITER, N_REP)    
    
    return RESULTS_REP, BEST_REP, AVERAGE_REP, WORST_REP, STATUS_PROCEDURE

def DE_ALGORITHM_001(OF_FUNCTION, SETUP):
    """ 
    Standard Differential Evolution Optimization algorithm. Continuous version. The algorithm also presents the results formatted in a spreadsheet.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/DE.html
    """
    
    # Setup config
    N_REP = SETUP['N_REP']
    N_ITER = SETUP['N_ITER']
    N_POP = SETUP['N_POP']
    D = SETUP['D']
    X_L = SETUP['X_L']
    X_U = SETUP['X_U']
    NULL_DIC = SETUP['NULL_DIC']
    MODEL_NAME = 'META_DE001_'

    # Parameters
    PARAMETERS = SETUP['PARAMETERS']
    F = PARAMETERS['MUTATION FACTOR (F)']
    CR =  PARAMETERS['CROSSOVER RATE (CR)']
    
    # Creating variables in the repetitions procedure
    RESULTS_REP = []
    BEST_REP = []
    WORST_REP = []
    AVERAGE_REP = []
    NAME = []
    if NULL_DIC == None:
        NULL_DIC = []
    else:
        pass 
    
    # Repetition looping
    INIT = time.time()
    for REP in range(N_REP):
        
        # Creating variables in the iterations procedure
        OF = np.zeros((N_POP, 1)); 
        FIT = np.zeros((N_POP, 1))
        RESULTS_ITER = [{'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'PARAMETERS': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': J} for J in range(N_POP)]
        BEST_ITER = {'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'PARAMETERS': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': np.empty(N_ITER + 1)}
        AVERAGE_ITER = {'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1)}
        WORST_ITER = {'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': np.empty(N_ITER + 1)}
        NEOF_COUNT = 0 
        
        # Initial population
        X = META_CO.initial_population_01(N_POP, D, X_L, X_U)
        for I in range(N_POP):
            OF[I, 0] = OF_FUNCTION(X[I, :], NULL_DIC)
            FIT[I, 0] = META_CO.fit_value(OF[I, 0])
            NEOF_COUNT += 1
            
        # Storage all values in RESULTS_ITER
        for I, X_ALL, OF_ALL, FIT_ALL, in zip(RESULTS_ITER, X, OF, FIT):
            I['X_POSITION'][0, :] = X_ALL
            I['OF'][0] = OF_ALL
            I['FIT'][0] = FIT_ALL
            I['PARAMETERS'][0] = None
            I['NEOF'][0] = NEOF_COUNT
        
        # Best, average and worst storage
        BEST_POSITION, WORST_POSITION, X_BEST, X_WORST, OF_BEST, OF_WORST, FIT_BEST, FIT_WORST, OF_AVERAGE, FIT_AVERAGE = META_CO.best_values(X, OF, FIT, N_POP)
        BEST_ITER['ID_PARTICLE'][0] = BEST_POSITION
        WORST_ITER['ID_PARTICLE'][0] = WORST_POSITION
        BEST_ITER['X_POSITION'][0, :] = X_BEST
        WORST_ITER['X_POSITION'][0, :] = X_WORST
        BEST_ITER['OF'][0] = OF_BEST
        AVERAGE_ITER['OF'][0] = OF_AVERAGE
        WORST_ITER['OF'][0] = OF_WORST
        BEST_ITER['FIT'][0] = FIT_BEST
        AVERAGE_ITER['FIT'][0] = FIT_AVERAGE
        WORST_ITER['FIT'][0] = FIT_WORST
        BEST_ITER['PARAMETERS'][0] = None
        BEST_ITER['NEOF'][0] = NEOF_COUNT
        AVERAGE_ITER['NEOF'][0] = NEOF_COUNT
        WORST_ITER['NEOF'][0] = NEOF_COUNT

        # Initial PBEST and GBEST
        P_BEST = X.copy()
        OF_PBEST = OF.copy()
        G_BEST = X_BEST.copy()
        
        # Iteration procedure
        for ITER in range(N_ITER):

            # Population movement
            for POP in range(N_POP):
                
                # ID selection
                IDS_RANDOM = META_DE.SELECTION_ID(N_POP)
                X_GAMA = X[IDS_RANDOM[0], :]
                X_BETA = X[IDS_RANDOM[1], :]
                X_ALFA = X[IDS_RANDOM[2], :]

                # Mutation phase
                V_TI, _, _, _ = META_GA.MUTATION_OPERATOR_DE_RAND_1(OF_FUNCTION, NULL_DIC, F, X_GAMA, X_BETA, X_ALFA, D, X_L, X_U)

                # Crossover phase
                X_ITEMP, OF_ITEMP, FIT_ITEMP, NEOF = META_GA.BINOMIAL_CROSSOVER_OPERATOR(OF_FUNCTION, NULL_DIC, V_TI, X[POP, :], CR, D, X_L, X_U)


                             
                # New design variables
                if FIT_ITEMP > FIT[POP, 0]:
                    X[POP, :] = X_ITEMP
                    OF[POP, 0] = OF_ITEMP
                    FIT[POP, 0] = FIT_ITEMP
                else:
                    pass
               
                # Update NEOF (Number of Objective Function Evaluations)
                NEOF_COUNT += NEOF
            
            # Storage all values in RESULTS_ITER
            for I, X_ALL, OF_ALL, FIT_ALL  in zip(RESULTS_ITER, X, OF, FIT):
                I['X_POSITION'][ITER + 1, :] = X_ALL
                I['OF'][ITER + 1] = OF_ALL
                I['FIT'][ITER + 1] = FIT_ALL
                I['PARAMETERS'][ITER + 1] = None
                I['NEOF'][ITER + 1] = NEOF_COUNT
            
            # Best, average and worst storage
            BEST_POSITION, WORST_POSITION, X_BEST, X_WORST, OF_BEST, OF_WORST, FIT_BEST, FIT_WORST, OF_AVERAGE, FIT_AVERAGE = META_CO.best_values(X, OF, FIT, N_POP)
            BEST_ITER['ID_PARTICLE'][ITER + 1] = BEST_POSITION
            WORST_ITER['ID_PARTICLE'][ITER + 1] = WORST_POSITION
            BEST_ITER['X_POSITION'][ITER + 1, :] = X_BEST
            WORST_ITER['X_POSITION'][ITER + 1, :] = X_WORST
            BEST_ITER['OF'][ITER + 1] = OF_BEST
            AVERAGE_ITER['OF'][ITER + 1] = OF_AVERAGE
            WORST_ITER['OF'][ITER + 1] = OF_WORST
            BEST_ITER['FIT'][ITER + 1] = FIT_BEST
            AVERAGE_ITER['FIT'][ITER + 1] = FIT_AVERAGE
            WORST_ITER['FIT'][ITER + 1] = FIT_WORST
            BEST_ITER['PARAMETERS'][ITER + 1] = None
            BEST_ITER['NEOF'][ITER + 1] = NEOF_COUNT
            AVERAGE_ITER['NEOF'][ITER + 1] = NEOF_COUNT
            WORST_ITER['NEOF'][ITER + 1] = NEOF_COUNT
              
        # Append iteration results
        RESULTS_REP.append(RESULTS_ITER)
        BEST_REP.append(BEST_ITER)
        AVERAGE_REP.append(AVERAGE_ITER)
        WORST_REP.append(WORST_ITER)
        
        # Progress bar update
        time.sleep(0.01)
        META_CO.PROGRESS_BAR(REP + 1, N_REP)
    END = time.time()
    
    # Resume process (Time and Excel outputs)
    print('Process Time: %.2f' % (END - INIT), 'Seconds', '\n', 'Seconds per repetition: %.2f' % ((END - INIT) / N_REP))
    STATUS_PROCEDURE = META_CO.SUMMARY_ANALYSIS(BEST_REP, N_REP, N_ITER)
    for REP in range(N_REP):
        NAME.append(MODEL_NAME + 'REP_' + str(REP) + '_BEST_' + str(REP) + '_' + str(datetime.now().strftime('%Y%m%d %H%M%S')))
        META_CO.EXCEL_WRITER_ITERATION(NAME[REP], D, BEST_REP[REP])
    NAME_RESUME = MODEL_NAME + 'RESUME' + '_' + str(datetime.now().strftime('%Y%m%d %H%M%S'))
    META_CO.EXCEL_PROCESS_RESUME(NAME_RESUME, D, BEST_REP, N_ITER, N_REP)    
    
    return RESULTS_REP, BEST_REP, AVERAGE_REP, WORST_REP, STATUS_PROCEDURE

def FIBONACCI_ALGORITHM(OF_FUNCTION, SETUP):
    """ 
    Standard Fibonacci Optimization algorithm. Continuous version. The algorithm also presents the results formatted in a spreadsheet.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/FIBONACCI.html
    """
    
    # Setup config
    N_REP = 1
    N_POP = 1
    D = 1
    N_ITER = SETUP['N_ITER']
    X_L = SETUP['X_L']
    X_U = SETUP['X_U']
    NULL_DIC = SETUP['NULL_DIC']
    MODEL_NAME = 'META_FIBONACCI_'

    # Parameters
    PARAMETERS = None
    
    # Creating variables in the repetitions procedure
    RESULTS_REP = []
    NAME = []
    if NULL_DIC == None:
        NULL_DIC = []
    else:
        pass 
    
    # Repetition looping
    INIT = time.time()
    for REP in range(N_REP):

        # Creating variables in the iterations procedure
        X = np.zeros((N_POP, 1)) 
        OF = np.zeros((N_POP, 1))
        FIT = np.zeros((N_POP, 1))
        RESULTS_ITER = [{'X_POSITION': np.empty((N_ITER, D)), 'OF': np.empty(N_ITER), 'FIT': np.empty(N_ITER), 'PARAMETERS': [], 'NEOF': np.empty(N_ITER), 'ID_PARTICLE': J} for J in range(N_POP)]
        NEOF_COUNT = 0 
                    
        # Iteration procedure
        for ITER in range(N_ITER):

            # Population movement
            for POP in range(N_POP):
                U_I, V_I, REDUCTION_RATIO, INDEX_FNUM, F_NUM, INDEX_FDEN, F_DEN = META_ZERO.FIBONACCI_MOVEMENT(X_L, X_U, ITER, N_ITER)
                THETA_UI = OF_FUNCTION(U_I, NULL_DIC)
                THETA_VI = OF_FUNCTION(V_I, NULL_DIC)
                if THETA_UI <= THETA_VI:
                    TEST = 'F(U) <= F(V) [A, V_I]'
                    X_U = V_I
                elif THETA_UI > THETA_VI:
                    TEST = 'F(U) > F(V) [U_I, B]'
                    X_L = U_I
                X[POP,0] = (X_U + X_L) / 2
                OF[POP, 0] = OF_FUNCTION(X[POP,0], NULL_DIC)
                NEOF_COUNT += 1 
                FIT[POP, 0] = META_CO.fit_value(OF[POP,0])
            

            # Storage all values in RESULTS_ITER
            for I, X_ALL, OF_ALL, FIT_ALL  in zip(RESULTS_ITER, X, OF, FIT):
                I['X_POSITION'][ITER, :] = X_ALL
                I['OF'][ITER] = OF_ALL
                I['FIT'][ITER] = FIT_ALL
                I['PARAMETERS'].append({'INDEX F_NUM': INDEX_FNUM, 'F_NUM': F_NUM, 'INDEX F_DEN': INDEX_FDEN, 'F_DEN': F_DEN, 'L_I': REDUCTION_RATIO, 'U': U_I, 'V': V_I, 'θ(U)': THETA_UI, 'θ(V)': THETA_VI, 'TEST': TEST})
                I['NEOF'][ITER] = NEOF_COUNT      
        # Append iteration results
        RESULTS_REP.append(RESULTS_ITER)
        
        # Progress bar update
        time.sleep(0.01)
        META_CO.PROGRESS_BAR(REP + 1, N_REP)
    END = time.time()
    BEST = RESULTS_REP[0]
    
    # Resume process (Time and Excel outputs)
    print('Process Time: %.2f' % (END - INIT), 'Seconds', '\n', 'Seconds per repetition: %.2f' % ((END - INIT) / N_REP))
    for REP in range(N_REP):
        NAME.append(MODEL_NAME + 'REP_' + str(REP) + '_BEST_' + str(REP) + '_' + str(datetime.now().strftime('%Y%m%d %H%M%S')))
        META_CO.EXCEL_WRITER_ITERATION(NAME[REP], D, BEST[REP])
    NAME_RESUME = MODEL_NAME + 'RESUME' + '_' + str(datetime.now().strftime('%Y%m%d %H%M%S'))
    META_CO.EXCEL_PROCESS_RESUME(NAME_RESUME, D, BEST, ITER, N_REP)    
    
    return BEST

def GOLDEN_SECTION_ALGORITHM(OF_FUNCTION, SETUP):
    """ 
    Standard Golden Section Optimization algorithm. Continuous version. The algorithm also presents the results formatted in a spreadsheet.

    See documentation in https://wmpjrufg.github.io/METAPY/GOLDEN.html
    """
    
    # Setup config
    N_REP = 1
    N_POP = 1
    D = 1
    N_ITER = SETUP['N_ITER']
    X_L = SETUP['X_L']
    X_U = SETUP['X_U']
    NULL_DIC = SETUP['NULL_DIC']
    MODEL_NAME = 'META_GOLDEN_'

    # Parameters
    PARAMETERS = None
    
    # Creating variables in the repetitions procedure
    RESULTS_REP = []
    NAME = []
    if NULL_DIC == None:
        NULL_DIC = []
    else:
        pass 
    
    # Repetition looping
    INIT = time.time()
    for REP in range(N_REP):

        # Creating variables in the iterations procedure
        X = np.zeros((N_POP, 1)) 
        OF = np.zeros((N_POP, 1))
        FIT = np.zeros((N_POP, 1))
        RESULTS_ITER = [{'X_POSITION': np.empty((N_ITER, D)), 'OF': np.empty(N_ITER), 'FIT': np.empty(N_ITER), 'PARAMETERS': [], 'NEOF': np.empty(N_ITER), 'ID_PARTICLE': J} for J in range(N_POP)]
        NEOF_COUNT = 0 
                    
        # Iteration procedure
        for ITER in range(N_ITER):

            # Population movement
            for POP in range(N_POP):
                U_I, V_I, REDUCTION_RATIO = META_ZERO.GOLDEN_MOVEMENT(X_L, X_U)
                THETA_UI = OF_FUNCTION(U_I, NULL_DIC)
                THETA_VI = OF_FUNCTION(V_I, NULL_DIC)
                if THETA_UI <= THETA_VI:
                    TEST = 'F(U) <= F(V) [A, V_I]'
                    X_U = V_I
                elif THETA_UI > THETA_VI:
                    TEST = 'F(U) > F(V) [U_I, B]'
                    X_L = U_I
                X[POP,0] = (X_U + X_L) / 2
                OF[POP, 0] = OF_FUNCTION(X[POP,0], NULL_DIC)
                NEOF_COUNT += 1 
                FIT[POP, 0] = META_CO.fit_value(OF[POP,0])
            

            # Storage all values in RESULTS_ITER
            for I, X_ALL, OF_ALL, FIT_ALL  in zip(RESULTS_ITER, X, OF, FIT):
                I['X_POSITION'][ITER, :] = X_ALL
                I['OF'][ITER] = OF_ALL
                I['FIT'][ITER] = FIT_ALL
                I['PARAMETERS'].append({'L_I': REDUCTION_RATIO, 'U': U_I, 'V': V_I, 'θ(U)': THETA_UI, 'θ(V)': THETA_VI, 'TEST': TEST})
                I['NEOF'][ITER] = NEOF_COUNT      
        # Append iteration results
        RESULTS_REP.append(RESULTS_ITER)
        
        # Progress bar update
        time.sleep(0.01)
        META_CO.PROGRESS_BAR(REP + 1, N_REP)
    END = time.time()
    BEST = RESULTS_REP[0]
    
    # Resume process (Time and Excel outputs)
    print('Process Time: %.2f' % (END - INIT), 'Seconds', '\n', 'Seconds per repetition: %.2f' % ((END - INIT) / N_REP))
    for REP in range(N_REP):
        NAME.append(MODEL_NAME + 'REP_' + str(REP) + '_BEST_' + str(REP) + '_' + str(datetime.now().strftime('%Y%m%d %H%M%S')))
        META_CO.EXCEL_WRITER_ITERATION(NAME[REP], D, BEST[REP])
    NAME_RESUME = MODEL_NAME + 'RESUME' + '_' + str(datetime.now().strftime('%Y%m%d %H%M%S'))
    META_CO.EXCEL_PROCESS_RESUME(NAME_RESUME, D, BEST, ITER, N_REP)    
    
    return BEST

"""
def BISECTION_ALGORITHM(OF_FUNCTION, SETUP):
    Standard Bissection Optimization algorithm. Continuous version. The algorithm also presents the results formatted in a spreadsheet.

    See documentation in https://wmpjrufg.github.io/METAPY/BISECTION.html
    
    # Setup config
    N_REP = 1
    N_POP = 1
    D = 1
    N_ITER = SETUP['N_ITER']
    X_L = SETUP['X_L']
    X_U = SETUP['X_U']
    NULL_DIC = SETUP['NULL_DIC']
    MODEL_NAME = 'META_BISSECTION_'

    # Parameters
    PARAMETERS = None
    
    # Creating variables in the repetitions procedure
    RESULTS_REP = []
    NAME = []
    if NULL_DIC == None:
        NULL_DIC = []
    else:
        pass 
    
    # Repetition looping
    INIT = time.time()
    for REP in range(N_REP):

        # Creating variables in the iterations procedure
        X = np.zeros((N_POP, 1)) 
        OF = np.zeros((N_POP, 1))
        FIT = np.zeros((N_POP, 1))
        RESULTS_ITER = [{'X_POSITION': np.empty((N_ITER, D)), 'OF': np.empty(N_ITER), 'FIT': np.empty(N_ITER), 'PARAMETERS': [], 'NEOF': np.empty(N_ITER), 'ID_PARTICLE': J} for J in range(N_POP)]
        NEOF_COUNT = 0 
                   
        # Iteration procedure
        for ITER in range(N_ITER):

            # Population movement
            for POP in range(N_POP):
                U_I, V_I, REDUCTION_RATIO = META_ZERO.BISECTION_MOVEMENT(X_L, X_U)
                THETA_UI = OF_FUNCTION(U_I, NULL_DIC)
                THETA_VI = OF_FUNCTION(V_I, NULL_DIC)
                if THETA_UI <= THETA_VI:
                    TEST = 'F(U) <= F(V) [A, V_I]'
                    X_U = V_I
                elif THETA_UI > THETA_VI:
                    TEST = 'F(U) > F(V) [U_I, B]'
                    X_L = U_I
                X[POP,0] = (X_U + X_L) / 2
                OF[POP, 0] = OF_FUNCTION(X[POP,0], NULL_DIC)
                NEOF_COUNT += 1 
                FIT[POP, 0] = META_CO.fit_value(OF[POP,0])
            

            # Storage all values in RESULTS_ITER
            for I, X_ALL, OF_ALL, FIT_ALL  in zip(RESULTS_ITER, X, OF, FIT):
                I['X_POSITION'][ITER, :] = X_ALL
                I['OF'][ITER] = OF_ALL
                I['FIT'][ITER] = FIT_ALL
                I['PARAMETERS'].append({'L_I': REDUCTION_RATIO, 'U': U_I, 'V': V_I, 'θ(U)': THETA_UI, 'θ(V)': THETA_VI, 'TEST': TEST})
                I['NEOF'][ITER] = NEOF_COUNT      
        # Append iteration results
        RESULTS_REP.append(RESULTS_ITER)
        
        # Progress bar update
        time.sleep(0.01)
        META_CO.PROGRESS_BAR(REP + 1, N_REP)
    END = time.time()
    BEST = RESULTS_REP[0]
    
    # Resume process (Time and Excel outputs)
    print('Process Time: %.2f' % (END - INIT), 'Seconds', '\n', 'Seconds per repetition: %.2f' % ((END - INIT) / N_REP))
    for REP in range(N_REP):
        NAME.append(MODEL_NAME + 'REP_' + str(REP) + '_BEST_' + str(REP) + '_' + str(datetime.now().strftime('%Y%m%d %H%M%S')))
        META_CO.EXCEL_WRITER_ITERATION(NAME[REP], D, BEST[REP])
    NAME_RESUME = MODEL_NAME + 'RESUME' + '_' + str(datetime.now().strftime('%Y%m%d %H%M%S'))
    META_CO.EXCEL_PROCESS_RESUME(NAME_RESUME, D, BEST, ITER, N_REP)    
    
    return BEST
"""
