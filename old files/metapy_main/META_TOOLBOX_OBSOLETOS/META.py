import numpy as np
import pandas as pd
import time
import multiprocessing
from multiprocessing import Pool

import META_TOOLBOX_OBSOLETOS.META_CO_LIBRARY as META_CO
import metapy_toolbox.simulated_annealing as META_SA
import META_TOOLBOX_OBSOLETOS.META_FA_LIBRARY as META_FA
#import META_TOOLBOX.META_DE_LIBRARY as META_DE
import META_TOOLBOX_OBSOLETOS.META_GA_LIBRARY as META_GA
import META_TOOLBOX_OBSOLETOS.META_PSO_LIBRARY as META_PSO
import META_TOOLBOX_OBSOLETOS.META_ZERO_LIBRARY as META_ZERO
import META_TOOLBOX_OBSOLETOS.META_GRADIENT_LIBRARY as META_GRAD
from datetime import datetime

def HILL_CLIMBING_001(OF_FUNCTION, SETUP):
    """ 
    Standard Hill climbing algorithm. Continuous version. The algorithm also presents the results formatted in a spreadsheet.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/HC.html
    """


def META(SETUP):
    
    # Start variables
    INI = time.time()
    RESULTS_REP = []
    BEST_REP = []

    try:
        if not isinstance(SETUP, dict):
            raise TypeError('The SETUP parameter must be a dictionary.')
        if len(SETUP) != 7:
            raise ValueError('The SETUP parameter must have 7 keys (N_REP, N_POP, D, X_L, X_U, TYPE CODE, SEED CONTROL).')

        for key in SETUP.keys():
            if key not in ['N_REP', 'N_POP', 'D', 'X_L', 'X_U', 'TYPE CODE', 'SEED CONTROL']:
                raise ValueError('The SETUP parameter must have the following keys: N_REP, N_POP, D, X_L, X_C, TYPE CODE, SEED CONTROL.')
            
        if not isinstance(SETUP['N_REP'], int):
            raise TypeError('The N_REP parameter must be an integer.')
        if not isinstance(SETUP['N_POP'], int):
            raise TypeError('The N_POP parameter must be an integer.')
        if not isinstance(SETUP['D'], int):
            raise TypeError('The D parameter must be an integer.')
        if not isinstance(SETUP['X_L'], list):
            raise TypeError('The X_L parameter must be a list.')
        if not isinstance(SETUP['X_U'], list):
            raise TypeError('The X_U parameter must be a list.')
        if not isinstance(SETUP['TYPE CODE'], list):
            raise TypeError('The TYPE CODE parameter must be a list.')
        if not isinstance(SETUP['SEED CONTROL'], (int, type(None))):
            raise TypeError('The SEED CONTROL parameter must be an integer or None.')

    except TypeError as te:
        print(f'Error {te}')

    except ValueError as ve:
        print(f'Error {ve}')



    POP = META_CO.initial_pops(SETUP['N_REP'], SETUP['N_POP'], SETUP['D'], SETUP['X_L'], SETUP['X_U'], SETUP['TYPE CODE'], SETUP['SEED CONTROL'])
    
    # Algorithm selection and general results
    if SETUP['ALGORITHM'] == 'HILL CLIMBING 01':
        # Define the name of the model
        MODEL_NAME = 'META_HC001_'
        # Multiprocess
        with Pool() as p:
            INFO = [[SETUP, I] for I in POP]
            RESULT = p.map_async(func = HILL_CLIMBING_001, iterable = INFO)
            for RESULTS in RESULT.get():
                RESULTS_REP.append(RESULTS[0])
                BEST_REP.append(RESULTS[1])
    elif SETUP['ALGORITHM'] == 'GRADIENT 01':
        # Define the name of the model
        MODEL_NAME = 'META_GRAD001_'
        # Multiprocess
        POOLS = multiprocessing.cpu_count() - 1 
        with Pool(processes = POOLS) as p:
            INFO = [[SETUP, I] for I in POP]
            RESULT = p.map_async(func = GRADIENT_001, iterable = INFO)
            FINAL_RESULT = RESULT.get()   
    elif SETUP['ALGORITHM'] == 'GENETIC ALGORITHM 01':
        # Define the name of the model
        MODEL_NAME = 'META_GA001_'
        # Multiprocess
        POOLS = multiprocessing.cpu_count() - 1 
        with Pool(processes = POOLS) as p:
            INFO = [[SETUP, I] for I in POP]
            RESULT = p.map_async(func = GENETIC_ALGORITHM_001, iterable = INFO)
            FINAL_RESULT = RESULT.get()  
    elif SETUP['ALGORITHM'] == 'GENETIC ALGORTIHM 01 COMB':
        # Define the name of the model
        MODEL_NAME = 'META_GA001COMB_'
        # Multiprocess
        POOLS = multiprocessing.cpu_count() - 1 
        with Pool(processes = POOLS) as p:
            INFO = [[SETUP, I] for I in POP]
            RESULT = p.map_async(func = GENETIC_ALGORITHM_001_COMB, iterable = INFO)
            FINAL_RESULT = RESULT.get()  
    elif SETUP['ALGORITHM'] == 'FIREFLY ALGORITHM 01':
        # Define the name of the model
        MODEL_NAME = 'META_FA001_'
        # Multiprocess
        POOLS = multiprocessing.cpu_count() - 1 
        with Pool(processes = POOLS) as p:
            INFO = [[SETUP, I] for I in POP]
            RESULT = p.map_async(func = FIREFLY_001, iterable = INFO)
            FINAL_RESULT = RESULT.get()  

    # # Resume process (Time and Excel outputs)
    # STATUS_PROCEDURE = META_CO.SUMMARY_ANALYSIS(BEST_REP, SETUP['N_REP'], SETUP['N_ITER'])

    # # Command window report
    # BESTBEST = STATUS_PROCEDURE[0]
    # BEST = BEST_REP[BESTBEST]
    # DIMENSIONS = list(BEST['X_POSITION'][-1,:])
    # BEST_RESULT = BEST['OF'][-1]
    # END = time.time()

    # # Print
    # print(' Optimization results:', '\n')
    # print(' - Design Variables: ', DIMENSIONS, '\n')
    # print(' - Of value:         {:.6e}'.format(BEST_RESULT), '\n')
    # print(' - Process time (s): {:.6f}'.format(END - INI), '\n')

    return RESULTS_REP, BEST_REP

def HILL_CLIMBING_001(INFO):
    """
    Hill Climbing algorithm.

    See documentation in https://wmpjrufg.github.io/METAPY/ALGORITHMS.html
    """

    # Setup config
    SETUP = INFO[0]
    N_ITER = SETUP['N_ITER']
    N_POP = SETUP['N_POP']
    D = SETUP['D']
    X_L = SETUP['X_L']
    X_U = SETUP['X_U']
    NULL_DIC = SETUP['NULL_DIC']
    OF_FUNCTION = SETUP['OF']
    SEED = SETUP['SEED CONTROL']
    
    # Parameters
    PARAMETERS = SETUP['PARAMETERS']
    SIGMA = PARAMETERS['SIGMA (%)'] / 100
    PDF = PARAMETERS['PDF'] 

    # Creating variables in the iteration procedure
    OF = []
    FIT = []
    NEOF_COUNT = 0 

    # Storage values: start variables
    DATASET_COLUMNS1 = ['X_' + str(I) for I in range(D)]
    DATASET_COLUMNS1.append('OF')
    DATASET_COLUMNS1.append('FIT')
    DATASET_COLUMNS1.append('ITERATION')
    DATASET_COLUMNS2 = ['X_' + str(I) for I in range(D)]
    DATASET_COLUMNS2.append('OF BEST')
    DATASET_COLUMNS2.append('FIT BET')
    DATASET_COLUMNS2.append('ID BEST')
    DATASET_COLUMNS3 = ['X_' + str(I) for I in range(D)]
    DATASET_COLUMNS3.append('OF WORST')
    DATASET_COLUMNS3.append('FIT WORST')
    DATASET_COLUMNS3.append('ID WORST')
    DATASET_COLUMNS4 = ['OF AVG', 'FIT AVG', 'ITERATION', 'NEOF']
    ALL_DATA = []
    RESUME = []

    # Initial population
    X = INFO[1]
    for POP in range(N_POP):
        OF.append(OF_FUNCTION(X[POP], NULL_DIC))
        FIT.append(META_CO.fit_value(OF[POP]))
        NEOF_COUNT += 1
        SOLUTIONS = META_CO.RESUME_ALL_DATA_IN_DATAFRAME(X[POP], OF[POP], FIT[POP], DATASET_COLUMNS1, 0)
        ALL_DATA.append(SOLUTIONS)
    
    # Best, average and worst values and storage
    BEST_DATA = META_CO.RESUME_PROCESS_IN_DATAFRAME(X, OF, FIT, DATASET_COLUMNS2, DATASET_COLUMNS3, DATASET_COLUMNS4, 0, NEOF_COUNT)
    RESUME.append(BEST_DATA)

    # Iteration procedure
    for ITER in range(N_ITER):
        
        # Time markup
        INI = time.time()
        
        # Population movement
        for POP in range(N_POP):
            
            # Hill Climbing particle movement
            X_I_TEMP, OF_I_TEMP, FIT_I_TEMP, NEOF = META_CO.mutation_01_movement(OF_FUNCTION, X[POP], X_L, X_U, D, PDF, SIGMA, SEED, NULL_DIC)
            SOLUTIONS = META_CO.RESUME_ALL_DATA_IN_DATAFRAME(X_I_TEMP, OF_I_TEMP, FIT_I_TEMP, DATASET_COLUMNS1, ITER + 1)
            ALL_DATA.append(SOLUTIONS)

            # New design variables
            if FIT_I_TEMP > FIT[POP]:
                X[POP] = X_I_TEMP.copy()
                OF[POP] = OF_I_TEMP
                FIT[POP] = FIT_I_TEMP
            else:
                pass
            
            # Update NEOF (Number of Objective Function Evaluations)
            NEOF_COUNT += NEOF

        # Best, average and worst values and storage
        DATA = META_CO.RESUME_PROCESS_IN_DATAFRAME(X, OF, FIT, DATASET_COLUMNS2, DATASET_COLUMNS3, DATASET_COLUMNS4, ITER + 1, NEOF_COUNT)
        RESUME.append(DATA)
        
        # Time markup
        END = time.time()
        DELTA = END - INI
    
    # Storage all values in DataFrame
    DF_ALL = pd.concat(ALL_DATA, ignore_index = True)

    # Storage best values in DataFrame
    DF_BEST = pd.concat(RESUME, ignore_index = True)

    return DF_ALL, DF_BEST, DELTA

def NEW_FA(INFO):
    """
    Hill Climbing algorithm.

    See documentation in https://wmpjrufg.github.io/METAPY/ALGORITHMS.html
    """

    # Setup config
    SETUP = INFO[0]
    N_ITER = SETUP['N_ITER']
    N_POP = SETUP['N_POP']
    D = SETUP['D']
    X_L = SETUP['X_L']
    X_U = SETUP['X_U']
    NULL_DIC = SETUP['NULL_DIC']
    OF_FUNCTION = SETUP['OF']
    SEED = SETUP['SEED CONTROL']
    
    # Parameters
    PARAMETERS = SETUP['PARAMETERS']
    SIGMA = PARAMETERS['SIGMA (%)'] / 100
    PDF = PARAMETERS['PDF'] 

    # Creating variables in the iteration procedure
    OF = []
    FIT = []
    NEOF_COUNT = 0 

    # Storage values: start variables
    DATASET_COLUMNS1 = ['X_' + str(I) for I in range(D)]
    DATASET_COLUMNS1.append('OF')
    DATASET_COLUMNS1.append('FIT')
    DATASET_COLUMNS1.append('ITERATION')
    DATASET_COLUMNS2 = ['X_' + str(I) for I in range(D)]
    DATASET_COLUMNS2.append('OF BEST')
    DATASET_COLUMNS2.append('FIT BET')
    DATASET_COLUMNS2.append('ID BEST')
    DATASET_COLUMNS3 = ['X_' + str(I) for I in range(D)]
    DATASET_COLUMNS3.append('OF WORST')
    DATASET_COLUMNS3.append('FIT WORST')
    DATASET_COLUMNS3.append('ID WORST')
    DATASET_COLUMNS4 = ['OF AVG', 'FIT AVG', 'ITERATION', 'NEOF']
    ALL_DATA = []
    RESUME = []

    # Initial population

    X = INFO[1]
    for POP in range(N_POP):
        OF.append(OF_FUNCTION(X[POP], NULL_DIC))
        FIT.append(META_CO.fit_value(OF[POP]))
        NEOF_COUNT += 1
        SOLUTIONS = META_CO.RESUME_ALL_DATA_IN_DATAFRAME(X[POP], OF[POP], FIT[POP], DATASET_COLUMNS1, 0)
        ALL_DATA.append(SOLUTIONS)
    
    # Best, average and worst values and storage
    BEST_DATA = META_CO.RESUME_PROCESS_IN_DATAFRAME(X, OF, FIT, DATASET_COLUMNS2, DATASET_COLUMNS3, DATASET_COLUMNS4, 0, NEOF_COUNT)
    RESUME.append(BEST_DATA)

    # Iteration procedure
    for ITER in range(N_ITER):
        
        # Time markup
        INI = time.time()
        
        # Population movement
        for POP in range(N_POP):
            
            X_MALENEWI, OF_MALENEWI, FIT_MALENEWI = META_FA.MALE_FIREFLY_MOVEMENT(OF_FUNCTION, X_MALECURRENTI[POP], FIT_MALECURRENT[POP], Y_K_FEMALE[POP], FIT_K_FEMALECURRENT[POP], Y_J_FEMALE[POP], FIT_J_FEMALECURRENT[POP],0.80, GAMMA, D, X_L, X_U, NULL_DIC)
            Y_FEMALENEWI, OF_FEMALENEWI, FIT_FEMALENEWI = META_FA.FEMALE_FIREFLY_MOVEMENT(OF_FUNCTION, Y_FEMALE[POP], X_MALENEWI, FIT_MALENEWI,0.80, GAMMA, D, X_L, X_U, NULL_DIC) 
            
            # Hill Climbing particle movement
            X_I_TEMP, OF_I_TEMP, FIT_I_TEMP, NEOF = META_CO.mutation_01_movement(OF_FUNCTION, X[POP], X_L, X_U, D, PDF, SIGMA, SEED, NULL_DIC)
            SOLUTIONS = META_CO.RESUME_ALL_DATA_IN_DATAFRAME(X_I_TEMP, OF_I_TEMP, FIT_I_TEMP, DATASET_COLUMNS1, ITER + 1)
            ALL_DATA.append(SOLUTIONS)

            # New design variables
            if FIT_I_TEMP > FIT[POP]:
                X[POP] = X_I_TEMP.copy()
                OF[POP] = OF_I_TEMP
                FIT[POP] = FIT_I_TEMP
            else:
                pass
            
            # Update NEOF (Number of Objective Function Evaluations)
            NEOF_COUNT += NEOF

        # Best, average and worst values and storage
        DATA = META_CO.RESUME_PROCESS_IN_DATAFRAME(X, OF, FIT, DATASET_COLUMNS2, DATASET_COLUMNS3, DATASET_COLUMNS4, ITER + 1, NEOF_COUNT)
        RESUME.append(DATA)
        
        # Time markup
        END = time.time()
        DELTA = END - INI
    
    # Storage all values in DataFrame
    DF_ALL = pd.concat(ALL_DATA, ignore_index = True)

    # Storage best values in DataFrame
    DF_BEST = pd.concat(RESUME, ignore_index = True)

    return DF_ALL, DF_BEST, DELTA

def SIMULATED_ANNEALING_001(INFO):
        
    # Setup config
    SETUP = INFO[0]
    N_ITER = SETUP['N_ITER']
    N_POP = SETUP['N_POP']
    D = SETUP['D']
    X_L = SETUP['X_L']
    X_U = SETUP['X_U']
    NULL_DIC = SETUP['NULL_DIC']
    OF_FUNCTION = SETUP['OF']
    
    # Parameters
    PARAMETERS = SETUP['PARAMETERS']
    SIGMA = PARAMETERS['SIGMA (%)'] / 100
    SCHEDULE = PARAMETERS['COOLING SCHEME']
    ALPHA = PARAMETERS['TEMP. UPDATE (ALPHA)']
    TEMP_INI = PARAMETERS['INITIAL TEMP. (T_0)']

    # Creating variables in the repetitions procedure
    if NULL_DIC == None:
        NULL_DIC = []
    else:
        pass    
    OF = np.zeros((N_POP, 1))
    FIT = np.zeros((N_POP, 1))
    RESULTS_ITER = [{'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': J} for J in range(N_POP)]
    BEST_ITER = {'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': np.empty(N_ITER + 1), 'PARAMETERS': []}
    AVERAGE_ITER = {'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1)}
    WORST_ITER = {'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': np.empty(N_ITER + 1)}
    NEOF_COUNT = 0 
        
    # Initial population
    X = INFO[1]
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
    BEST_ITER['NEOF'][0] = NEOF_COUNT
    AVERAGE_ITER['NEOF'][0] = NEOF_COUNT
    WORST_ITER['NEOF'][0] = NEOF_COUNT
    BEST_ITER['PARAMETERS'].append({'TIME (s)': 0.0, 'TEMP': TEMPERATURE})
        
    # Iteration procedure
    for ITER in range(N_ITER):
        
        # Time markup
        INI = time.time()
        
        # Population movement
        for POP in range(N_POP):
            
            # Hill Climbing particle movement
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

        # Time markup
        END = time.time()
        DELTA = END - INI
        
        # Storage all values in RESULTS_ITER
        for I, X_ALL, OF_ALL, FIT_ALL  in zip(RESULTS_ITER, X, OF, FIT):
            I['X_POSITION'][ITER + 1, :] = X_ALL
            I['OF'][ITER + 1] = OF_ALL
            I['FIT'][ITER + 1] = FIT_ALL
            I['NEOF'][ITER + 1] = NEOF_COUNT
        
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
        BEST_ITER['NEOF'][ITER + 1] = NEOF_COUNT
        AVERAGE_ITER['NEOF'][ITER + 1] = NEOF_COUNT
        WORST_ITER['NEOF'][ITER + 1] = NEOF_COUNT
        BEST_ITER['PARAMETERS'].append({'TIME (s)': DELTA, 'TEMP': TEMPERATURE})

    return RESULTS_ITER, BEST_ITER, AVERAGE_ITER, WORST_ITER 

def GRADIENT_001(INFO):
        
    # Setup config
    SETUP = INFO[0]
    N_ITER = SETUP['N_ITER']
    N_POP = SETUP['N_POP']
    D = SETUP['D']
    X_L = SETUP['X_L']
    X_U = SETUP['X_U']
    NULL_DIC = SETUP['NULL_DIC']
    OF_FUNCTION = SETUP['OF']
    OF_FUNCTION_DERIVATIVE = SETUP['FIRST ORDER DERIVATIVE']
    
    # Parameters
    PARAMETERS = SETUP['PARAMETERS']
    DIRECTION_SEARCH = PARAMETERS['DIRECTION_SEARCH']

    # Creating variables in the repetitions procedure
    if NULL_DIC == None:
        NULL_DIC = []
    else:
        pass    
    OF = np.zeros((N_POP, 1))
    FIT = np.zeros((N_POP, 1))
    HISTORY = [0, 0]
    HISTORY_FO = [0, 0]
    DIRC_HIST = [0] * D
    RESULTS_ITER = [{'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': J} for J in range(N_POP)]
    BEST_ITER = {'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': np.empty(N_ITER + 1), 'PARAMETERS': []}
    AVERAGE_ITER = {'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1)}
    WORST_ITER = {'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': np.empty(N_ITER + 1)}
    NEOF_COUNT = 0 
        
    # Initial population
    X = INFO[1]
    for I in range(N_POP):
        OF[I, 0] = OF_FUNCTION(X[I, :], NULL_DIC)
        FIT[I, 0] = META_CO.fit_value(OF[I, 0])
        NEOF_COUNT += 1
               
    # Storage all values in RESULTS_ITER
    for I, X_ALL, OF_ALL, FIT_ALL, in zip(RESULTS_ITER, X, OF, FIT):
        I['X_POSITION'][0, :] = X_ALL
        I['OF'][0] = OF_ALL
        I['FIT'][0] = FIT_ALL
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
    BEST_ITER['NEOF'][0] = NEOF_COUNT
    AVERAGE_ITER['NEOF'][0] = NEOF_COUNT
    WORST_ITER['NEOF'][0] = NEOF_COUNT
    BEST_ITER['PARAMETERS'].append({'ITER': 0, 'TIME (s)': 0.0, 'X_(K)': X.copy(), 'X_(K-1)': HISTORY[0], 'BETA': None, 'S(K-1)': DIRC_HIST, 'ERROR': 1000})
        
    # Iteration procedure
    for ITER in range(N_ITER):
        
        # Time markup
        INI = time.time()
        
        # Population movement
        for POP in range(N_POP):
            HISTORY.append(X.copy())
            HISTORY_FO.append(OF[POP, 0])
            del HISTORY[0]
            DIC = {'ITER': ITER + 1, 'TIME (s)': None, 'X_(K)': X.copy(), 'X_(K-1)': HISTORY[0], 'BETA': None, 'S(K-1)': DIRC_HIST}

            # Gradient particle movement
            X_ITEMP, OF_ITEMP, FIT_ITEMP, NEOF, ALPHA, BETA, DIREC = META_GRAD.GRADIENT_MOVEMENT_FIRST_ORDER(X[POP,:], HISTORY, DIC['S(K-1)'], OF_FUNCTION, OF_FUNCTION_DERIVATIVE, DIRECTION_SEARCH, X_L, X_U, NULL_DIC, ITER)
            DIC['BETA'] = BETA
            DIC['ALPHA'] = ALPHA
            DIC['ERROR'] = np.abs(OF_ITEMP - HISTORY_FO[-1]) / max(np.abs(OF_ITEMP), 1E-10)
            DIRC_HIST = DIREC.copy()
                        
            # New design variables
            X[POP, :] = X_ITEMP
            OF[POP, 0] = OF_ITEMP
            FIT[POP, 0] = FIT_ITEMP
            
            # Update NEOF (Number of Objective Function Evaluations)
            NEOF_COUNT += NEOF

        # Time markup
        END = time.time()
        DELTA = END - INI
        DIC['TIME (s)'] = DELTA

        # Storage all values in RESULTS_ITER
        for I, X_ALL, OF_ALL, FIT_ALL  in zip(RESULTS_ITER, X, OF, FIT):
            I['X_POSITION'][ITER + 1, :] = X_ALL
            I['OF'][ITER + 1] = OF_ALL
            I['FIT'][ITER + 1] = FIT_ALL
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
        BEST_ITER['NEOF'][ITER + 1] = NEOF_COUNT
        AVERAGE_ITER['NEOF'][ITER + 1] = NEOF_COUNT
        WORST_ITER['NEOF'][ITER + 1] = NEOF_COUNT
        BEST_ITER['PARAMETERS'].append(DIC)

    return RESULTS_ITER, BEST_ITER, AVERAGE_ITER, WORST_ITER     

def GENETIC_ALGORITHM_001(INFO):
        
    # Setup config
    SETUP = INFO[0]
    N_ITER = SETUP['N_ITER']
    N_POP = SETUP['N_POP']
    D = SETUP['D']
    X_L = SETUP['X_L']
    X_U = SETUP['X_U']
    NULL_DIC = SETUP['NULL_DIC']
    OF_FUNCTION = SETUP['OF']
    
    # Parameters
    PARAMETERS = SETUP['PARAMETERS']
    # Selection
    SELECTION_AUX = PARAMETERS['SELECTION']
    if SELECTION_AUX.split('-')[0] == 'ROULETE WHEEL':
        SELECTION = 'ROULETE WHEEL'
    elif SELECTION_AUX.split('-')[0] == 'TOURNAMENT':
        SELECTION_AUX = SELECTION_AUX.split('-')
        SELECTION = SELECTION_AUX[0]
        RUNS = int(SELECTION_AUX[1])
    # Crossover
    CROSSOVER_AUX = PARAMETERS['CROSSOVER']
    if CROSSOVER_AUX .split('-')[0] == 'LINEAR CROSSOVER (C)':
        CROSSOVER = 'LINEAR CROSSOVER (C)'
    elif CROSSOVER_AUX .split('-')[0] == 'BINOMIAL CROSSOVER (C)':
        CROSSOVER_AUX = CROSSOVER_AUX.split('-')
        CROSSOVER = CROSSOVER_AUX[0]
        P_C = float(CROSSOVER_AUX[1])
    elif CROSSOVER_AUX .split('-')[0] == 'BLX ALPHA CROSSOVER (C)':
        CROSSOVER = 'BLX ALPHA CROSSOVER (C)'
    # Mutation
    P_M = PARAMETERS['MUTATION RATE (%)'] / 100

    # Creating variables in the repetitions procedure
    if NULL_DIC == None:
        NULL_DIC = []
    else:
        pass    
    OF = np.zeros((N_POP, 1))
    FIT = np.zeros((N_POP, 1))
    RESULTS_ITER = [{'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': J} for J in range(N_POP)]
    BEST_ITER = {'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': np.empty(N_ITER + 1), 'PARAMETERS': []}
    AVERAGE_ITER = {'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1)}
    WORST_ITER = {'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': np.empty(N_ITER + 1)}
    NEOF_COUNT = 0 
        
    # Initial population
    X = INFO[1]
    for I in range(N_POP):
        OF[I, 0] = OF_FUNCTION(X[I, :], NULL_DIC)
        FIT[I, 0] = META_CO.fit_value(OF[I, 0])
        NEOF_COUNT += 1
               
    # Storage all values in RESULTS_ITER
    for I, X_ALL, OF_ALL, FIT_ALL, in zip(RESULTS_ITER, X, OF, FIT):
        I['X_POSITION'][0, :] = X_ALL
        I['OF'][0] = OF_ALL
        I['FIT'][0] = FIT_ALL
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
    BEST_ITER['NEOF'][0] = NEOF_COUNT
    AVERAGE_ITER['NEOF'][0] = NEOF_COUNT
    WORST_ITER['NEOF'][0] = NEOF_COUNT
    BEST_ITER['PARAMETERS'].append({'TIME (s)': 0.0})
        
    # Iteration procedure
    for ITER in range(N_ITER):
        
        # Time markup
        INI = time.time()
        
        # Population movement
        for POP in range(N_POP):
            
            # Selection procedure
            if SELECTION == 'TOURNAMENT':
                SELECTED_POS = META_GA.TOURNAMENT_SELECTION(FIT, N_POP, int(POP), RUNS)
            elif SELECTION == 'ROULETE WHEEL':
                SELECTED_POS = META_GA.ROULETE_WHEEL_SELECTION(FIT, N_POP, int(POP))
                
            # Movement procedure
            if CROSSOVER == 'LINEAR CROSSOVER (C)':
                X_ITEMP, OF_ITEMP, FIT_ITEMP, NEOF1 = META_GA.LINEAR_CROSSOVER(X[POP, :], X[SELECTED_POS, :], OF_FUNCTION, NULL_DIC, X_L, X_U)
            elif CROSSOVER == 'BINOMIAL CROSSOVER (C)':
                X_ITEMP, OF_ITEMP, FIT_ITEMP, NEOF1 = META_GA.BINOMIAL_CROSSOVER(X[POP, :], X[SELECTED_POS, :], P_C, OF_FUNCTION, NULL_DIC, X_L, X_U)
            elif CROSSOVER == 'BLX ALPHA CROSSOVER (C)':     
                X_ITEMP, OF_ITEMP, FIT_ITEMP, NEOF1 = META_GA.BLXALPHA_CROSSOVER(X[POP, :], X[SELECTED_POS, :], OF_FUNCTION, NULL_DIC, X_L, X_U)                                                       

            # Mutation procedure
            if np.random.uniform(0, 1) <= P_M:
                X_ITEMP, OF_ITEMP, FIT_ITEMP, NEOF2 = META_HC.HC_MOVEMENT(OF_FUNCTION, NULL_DIC, X_ITEMP, X_L, X_U, D, SIGMA = 5 / 100) 
            else:
                NEOF2 = 0
            
            # New design variables
            if FIT_ITEMP > FIT[POP, 0]:
                X[POP, :] = X_ITEMP
                OF[POP, 0] = OF_ITEMP
                FIT[POP, 0] = FIT_ITEMP
            else:
                pass
            
            # Update NEOF (Number of Objective Function Evaluations)
            NEOF_COUNT += NEOF1 + NEOF2

        # Time markup
        END = time.time()
        DELTA = END - INI
        
        # Storage all values in RESULTS_ITER
        for I, X_ALL, OF_ALL, FIT_ALL  in zip(RESULTS_ITER, X, OF, FIT):
            I['X_POSITION'][ITER + 1, :] = X_ALL
            I['OF'][ITER + 1] = OF_ALL
            I['FIT'][ITER + 1] = FIT_ALL
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
        BEST_ITER['NEOF'][ITER + 1] = NEOF_COUNT
        AVERAGE_ITER['NEOF'][ITER + 1] = NEOF_COUNT
        WORST_ITER['NEOF'][ITER + 1] = NEOF_COUNT
        BEST_ITER['PARAMETERS'].append({'TIME (s)': DELTA})

    return RESULTS_ITER, BEST_ITER, AVERAGE_ITER, WORST_ITER 

def GENETIC_ALGORITHM_001_COMB(INFO):
        
    # Setup config
    SETUP = INFO[0]
    N_ITER = SETUP['N_ITER']
    N_POP = SETUP['N_POP']
    D = SETUP['D']
    # X_L = SETUP['X_L']
    # X_U = SETUP['X_U']
    NULL_DIC = SETUP['NULL_DIC']
    OF_FUNCTION = SETUP['OF']
    
    # Parameters
    PARAMETERS = SETUP['PARAMETERS']
    # Selection
    SELECTION_AUX = PARAMETERS['SELECTION']
    if SELECTION_AUX.split('-')[0] == 'ROULETE WHEEL':
        SELECTION = 'ROULETE WHEEL'
    elif SELECTION_AUX.split('-')[0] == 'TOURNAMENT':
        SELECTION_AUX = SELECTION_AUX.split('-')
        SELECTION = SELECTION_AUX[0]
        RUNS = int(SELECTION_AUX[1])
    # Crossover
    CROSSOVER_AUX = PARAMETERS['CROSSOVER']
    if CROSSOVER_AUX .split('-')[0] == 'MULTI POINT CROSSOVER':
        CROSSOVER = 'MULTI POINT CROSSOVER'
    # Mutation
    P_M = PARAMETERS['MUTATION RATE (%)'] / 100

    # Creating variables in the repetitions procedure
    if NULL_DIC == None:
        NULL_DIC = []
    else:
        pass    
    OF = np.zeros((N_POP, 1))
    FIT = np.zeros((N_POP, 1))
    RESULTS_ITER = [{'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': J} for J in range(N_POP)]
    BEST_ITER = {'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': np.empty(N_ITER + 1), 'PARAMETERS': []}
    AVERAGE_ITER = {'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1)}
    WORST_ITER = {'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': np.empty(N_ITER + 1)}
    NEOF_COUNT = 0 
        
    # Initial population
    X = INFO[1]
    for I in range(N_POP):
        OF[I, 0] = OF_FUNCTION(X[I, :], NULL_DIC)
        FIT[I, 0] = META_CO.fit_value(OF[I, 0])
        NEOF_COUNT += 1
               
    # Storage all values in RESULTS_ITER
    for I, X_ALL, OF_ALL, FIT_ALL, in zip(RESULTS_ITER, X, OF, FIT):
        I['X_POSITION'][0, :] = X_ALL
        I['OF'][0] = OF_ALL
        I['FIT'][0] = FIT_ALL
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
    BEST_ITER['NEOF'][0] = NEOF_COUNT
    AVERAGE_ITER['NEOF'][0] = NEOF_COUNT
    WORST_ITER['NEOF'][0] = NEOF_COUNT
    BEST_ITER['PARAMETERS'].append({'TIME (s)': 0.0})
        
    # Iteration procedure
    for ITER in range(N_ITER):
        
        # Time markup
        INI = time.time()
        
        # Population movement
        for POP in range(N_POP):
            
            # Selection procedure
            if SELECTION == 'TOURNAMENT':
                SELECTED_POS = META_GA.TOURNAMENT_SELECTION(FIT, N_POP, int(POP), RUNS)
            elif SELECTION == 'ROULETE WHEEL':
                SELECTED_POS = META_GA.ROULETE_WHEEL_SELECTION(FIT, N_POP, int(POP))
                
            # Movement procedure
            if CROSSOVER == 'MULTI POINT CROSSOVER':
                X_ITEMP, OF_ITEMP, FIT_ITEMP, NEOF1 = META_GA.mp_crossover(X[POP, :], X[SELECTED_POS, :], 10, OF_FUNCTION, NULL_DIC)                                 

            # Mutation procedure
            if np.random.uniform(0, 1) <= P_M:
                X_ITEMP, OF_ITEMP, FIT_ITEMP, NEOF2 = META_GA.mp_mutation(X_ITEMP, 10, OF_ITEMP, OF_FUNCTION, NULL_DIC)
            else:
                NEOF2 = 0
            
            # New design variables
            if FIT_ITEMP > FIT[POP, 0]:
                X[POP, :] = X_ITEMP
                OF[POP, 0] = OF_ITEMP
                FIT[POP, 0] = FIT_ITEMP
            else:
                pass
            
            # Update NEOF (Number of Objective Function Evaluations)
            NEOF_COUNT += NEOF1 + NEOF2

        # Time markup
        END = time.time()
        DELTA = END - INI
        
        # Storage all values in RESULTS_ITER
        for I, X_ALL, OF_ALL, FIT_ALL  in zip(RESULTS_ITER, X, OF, FIT):
            I['X_POSITION'][ITER + 1, :] = X_ALL
            I['OF'][ITER + 1] = OF_ALL
            I['FIT'][ITER + 1] = FIT_ALL
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
        BEST_ITER['NEOF'][ITER + 1] = NEOF_COUNT
        AVERAGE_ITER['NEOF'][ITER + 1] = NEOF_COUNT
        WORST_ITER['NEOF'][ITER + 1] = NEOF_COUNT
        BEST_ITER['PARAMETERS'].append({'TIME (s)': DELTA})

    return RESULTS_ITER, BEST_ITER, AVERAGE_ITER, WORST_ITER


def FIREFLY_001(INFO):
        
    # Setup config
    SETUP = INFO[0]
    N_ITER = SETUP['N_ITER']
    N_POP = SETUP['N_POP']
    D = SETUP['D']
    X_L = SETUP['X_L']
    X_U = SETUP['X_U']
    NULL_DIC = SETUP['NULL_DIC']
    OF_FUNCTION = SETUP['OF']
    
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
    if NULL_DIC == None:
        NULL_DIC = []
    else:
        pass    
    OF = np.zeros((N_POP, 1))
    FIT = np.zeros((N_POP, 1))
    RESULTS_ITER = [{'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': J} for J in range(N_POP)]
    BEST_ITER = {'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': np.empty(N_ITER + 1), 'PARAMETERS': []}
    AVERAGE_ITER = {'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1)}
    WORST_ITER = {'X_POSITION': np.empty((N_ITER + 1, D)), 'OF': np.empty(N_ITER + 1), 'FIT': np.empty(N_ITER + 1), 'NEOF': np.empty(N_ITER + 1), 'ID_PARTICLE': np.empty(N_ITER + 1)}
    NEOF_COUNT = 0 
        
    # Initial population
    X = INFO[1]
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
    BEST_ITER['NEOF'][0] = NEOF_COUNT
    AVERAGE_ITER['NEOF'][0] = NEOF_COUNT
    WORST_ITER['NEOF'][0] = NEOF_COUNT
    BEST_ITER['PARAMETERS'].append({'TIME (s)': 0.0, 'ALPHA': ALPHA})
        
    # Iteration procedure
    for ITER in range(N_ITER):
        
        # Time markup
        INI = time.time()
        
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

        # Time markup
        END = time.time()
        DELTA = END - INI
        
        # Storage all values in RESULTS_ITER
        for I, X_ALL, OF_ALL, FIT_ALL  in zip(RESULTS_ITER, X, OF, FIT):
            I['X_POSITION'][ITER + 1, :] = X_ALL
            I['OF'][ITER + 1] = OF_ALL
            I['FIT'][ITER + 1] = FIT_ALL
            I['NEOF'][ITER + 1] = NEOF_COUNT
        
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
        BEST_ITER['NEOF'][ITER + 1] = NEOF_COUNT
        AVERAGE_ITER['NEOF'][ITER + 1] = NEOF_COUNT
        WORST_ITER['NEOF'][ITER + 1] = NEOF_COUNT
        BEST_ITER['PARAMETERS'].append({'TIME (s)': DELTA, 'ALPHA': ALPHA}) 

    return RESULTS_ITER, BEST_ITER, AVERAGE_ITER, WORST_ITER 