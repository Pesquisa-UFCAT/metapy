import numpy as np
import pandas as pd

def initial_population_01(n_pop, d, x_l, x_u, seed=None):
    """  
    Generates a random population with defined limits. 
    Continuum variables generator.

    See documentation in https://wmpjrufg.github.io/METAPY/COMMON.html
    """
    
    # Set random seed
    if seed is None:
        pass
    else: 
        np.random.seed(seed)

    # Random variable generator
    x_new = []
    for i in range(n_pop):
        aux = []
        for j in range(d):
            random_number = np.random.random()
            value_i_dimension = x_l[j] + (x_u[j] - x_l[j]) * random_number
            aux.append(value_i_dimension)
        x_new.append(aux)
    
    return x_new

def initial_population_02(n_pop, d, seed=None):
    """  
    The function generates a random population.
    Combinatorial variables generator.

    See documentation in https://wmpjrufg.github.io/METAPY/COMMON.html
    """

    # Set random seed
    if seed is None:
        pass
    else:
        np.random.seed(seed)

    # Random variable generator
    nodes = [i for i in range(d)]
    x_new = [list(np.random.permutation(nodes)) for _ in range(n_pop)]
    
    return x_new

def initial_pops(n_rep, n_pop, d, x_l, x_u, type_pop, seeds):
    """
    This function initializes the population randomly for n_rep procedures.
    Real code or combinatorial code.

    See documentation at https://wmpjrufg.github.io/METAPY/COMMON.html
    """

    # Set random seed
    if seeds is None:
        # Random variable generator
        pops = []
        if type_pop == 'REAL CODE':
            for i in range(n_rep):
                pops.append(initial_population_01(n_pop, d, x_l, x_u))
        elif type_pop == 'COMBINATORIAL CODE':
            for i in range(n_rep):
                pops.append(initial_population_02(n_pop, d))
    else:
        # Random variable generator
        pops = []
        if type_pop == 'REAL CODE':
            for i in range(n_rep):
                pops.append(initial_population_01(n_pop, d, x_l, x_u, seed=seeds))
        elif type_pop == 'COMBINATORIAL CODE':
            for i in range(n_rep):
                pops.append(initial_population_02(n_pop, d, seed=seeds))

    return pops

def fit_value(of_i_value):
    """ 
    This function calculates the fitness of the i agent.

    See documentation in https://wmpjrufg.github.io/METAPY/COMMON.html
    """

    # Positive or zero OF value
    if of_i_value >= 0:
        fit_i_value = 1 / (1 + of_i_value)
    # Negative OF value
    elif of_i_value < 0:
        fit_i_value = 1 + abs(of_i_value)
    
    return fit_i_value

def check_interval_01(x_i_old, x_l, x_u):
    """
    This function checks if a design variable is out of the limits established x_l and x_u.

    See documentation in https://wmpjrufg.github.io/METAPY/COMMON.html
    """
    
    x_i_new = list(np.clip(x_i_old, x_l, x_u))
    
    return x_i_new

def mutation_01_movement(of_function, x_i_old, x_l, x_u, d, pdf, sigma, seed=None, null_dic=None):
    """ 
    This function creates a new solution using Gaussian or Uniform distribution.
    
    See documentation in https://wmpjrufg.github.io/METAPY/COMMON.html
    """
    # Set random seed
    if seed is None:
        pass
    else: 
        np.random.seed(seed)

    # Start internal variables
    x_inew = []
    of_inew = 0
    fit_inew = 0
    
    # Particle movement - Gaussian distribution or Uniform distribution
    for i in range(d):
        mean_value = x_i_old[i]
        sigma_value = abs(mean_value * sigma)
        if pdf.upper() == 'GAUSSIAN' or pdf.upper() == 'NORMAL':
            neighbor = np.random.normal(mean_value, sigma_value, 1)
        elif pdf.upper() == 'UNIFORM':
            neighbor = np.random.uniform(mean_value - sigma_value, mean_value + sigma_value, 1)
        x_inew.append(neighbor[0])
    
    # Check bounds
    x_inew = check_interval_01(x_inew, x_l, x_u) 
    
    # Evaluation of the objective function and fitness
    of_inew = of_function(x_inew, null_dic)
    fit_inew = fit_value(of_inew)
    neof = 1
    
    return x_inew, of_inew, fit_inew, neof



def best_values(x, of, fit):
    """ 
    This function determines the best and worst particle. 
    It also determines the average value (OF and FIT) of the population.

    See documentation in https://wmpjrufg.github.io/METAPY/COMMON.html
    """
    
    # Best and worst ID in population
    best_position = of.index(min(of))
    worst_position = of.index(max(of))

    # Global best values
    x_best = x[best_position]
    of_best = of[best_position]
    fit_best = fit[best_position]
    
    # Global worst values
    x_worst = x[worst_position]
    of_worst = of[worst_position]
    fit_worst = fit[worst_position]
    
    # Average values
    of_average = sum(of) / len(of)
    fit_average = sum(fit) / len(fit)

    return (
        best_position, worst_position, x_best, x_worst, of_best, of_worst,
        fit_best, fit_worst, of_average, fit_average
    )


def RESUME_PROCESS_IN_DATAFRAME(X, OF, FIT, COLUMN_BEST, COLUMN_WORST, OTHER_COLUMNS, ITERATION, NEOF_COUNT):
    """
    This function creates a dataframe with the best, worst and average values of the population.
    """
    
    # Best, average and worst values
    BEST_POSITION, WORST_POSITION, X_BEST, X_WORST, OF_BEST, OF_WORST, FIT_BEST, FIT_WORST, OF_AVERAGE, FIT_AVERAGE = best_values(X, OF, FIT)
    
    # Dataframe creation
    AUX = X_BEST.copy()
    AUX.append(OF_BEST)
    AUX.append(FIT_BEST)
    AUX.append(BEST_POSITION)
    SOLUTION_LIST_BEST = [AUX]
    SOL1 = pd.DataFrame(SOLUTION_LIST_BEST, columns = COLUMN_BEST)
    AUX = X_WORST.copy()
    AUX.append(OF_WORST)
    AUX.append(FIT_WORST)
    AUX.append(WORST_POSITION)
    SOLUTION_LIST_WORS = [AUX]
    SOL2 = pd.DataFrame(SOLUTION_LIST_WORS, columns = COLUMN_WORST)
    SOLUTION_LIST_AVG = [[OF_AVERAGE, FIT_AVERAGE, ITERATION, NEOF_COUNT]]
    SOL3 = pd.DataFrame(SOLUTION_LIST_AVG, columns = OTHER_COLUMNS)
    DATA = pd.concat([SOL1, SOL2, SOL3], axis = 1)

    return DATA

def RESUME_ALL_DATA_IN_DATAFRAME(X_I, OF_I, FIT_I, COLUMNS, ITERATION):
    """
    This function creates a dataframme with all values of the population.
    """

    # Dataframe creation
    AUX = X_I.copy()
    AUX.append(OF_I)
    AUX.append(FIT_I)
    AUX.append(ITERATION)
    SOLUTION_LIST = [AUX]
    DATA = pd.DataFrame(SOLUTION_LIST, columns = COLUMNS)

    return DATA

def CONVERT_CONTINUOUS_DISCRETE(X, DATA_DISCRETE):
    """
    This function converts a continuous variable to a discrete variable.   
    """
    # Convert
    X_NEW = []
    for I in range(len(X)):
        AUX = round(X[I])
        X_NEW.append(DATA_DISCRETE[I]['X'][AUX])
    return X_NEW

"""
def PROGRESS_BAR(REP, TOTAL, PREFIX = 'Progress:', SUFFIX = 'Complete', DECIMALS = 1, LENGTH = 50, FILL = '█', PRINT_END = "\r"):

    This function create terminal progress bar.
    
    Input:
    REP        | Current iteration (required)                     | Integer
    TOTAL      | Total iterations (required)                      | Integer
    PREFIX     | Prefix string                                    | String
    SUFFIX     | Suffix string                                    | String
    DECIMALS   | Positive number of decimals in percent complete  | Integer
    LENGTH     | Character length of bar                          | Integer
    FILL       | Bar fill character                               | String
    PRINT_END  | End character (e.g. "\r", "\r\n")                | String
    
    Output:
    N/A
    
    # Progress bar
    PERCENT = ("{0:." + str(DECIMALS) + "f}").format(100 * (REP / float(TOTAL)))
    FILLED_LENGTH = int(LENGTH * REP // TOTAL)
    BAR = FILL * FILLED_LENGTH + '-' * (LENGTH - FILLED_LENGTH)
    print(f'\r{PREFIX} |{BAR}| {PERCENT}% {SUFFIX}', end = PRINT_END)
    
    # Print new line on complete
    if REP == TOTAL: 
        print()
    
    return

def SUMMARY_ANALYSIS(BEST_REP, N_REP, N_ITER):

    This function presents a written summary of the best simulation. 

    Input:
    BEST_REP         | Best population results by repetition                            | Py dictionary
                     |   Dictionary tags                                                |
                     |     'X_POSITION'    = Design variables by iteration              | Py Numpy array[N_ITER + 1 x D]
                     |     'OF'            = Obj function value by iteration            | Py Numpy array[N_ITER + 1 x 1]
                     |     'FIT'           = Fitness value by iteration                 | Py Numpy array[N_ITER + 1 x 1]
                     |     '??_PARAMETERS' = Algorithm parametrs                        | Py Numpy array[N_ITER + 1 x 1]
                     |     'NEOF'          = Number of objective function evaluations   | Py Numpy array[N_ITER + 1 x 1]
                     |     'ID_PARTICLE'   = ID best particle by iteration              | Integer 
    N_REP            | Number of repetitions                                            | Integer
    N_ITER           | Number of iterations                                             | Integer

    Output:
    STATUS_PROCEDURE | Process repetition ID - from lowest OF value to highest OF value | Py list[N_REP]
    
    # Start reserved space for repetitions
    OF_MINVALUES = []
    
    # Checking which is the best process 
    for I_COUNT in range(N_REP):
        ID = I_COUNT
        OF_MIN = BEST_REP[ID]['OF'][N_ITER]
        OF_MINVALUES.append(OF_MIN)
    STATUS_PROCEDURE = np.argsort(OF_MINVALUES)    
    
    return STATUS_PROCEDURE

def EXCEL_WRITER_ITERATION(NAME, D, DATASET):

    This function create output Excel files by iteration.
    
    Input:
    NAME       | Filename                                         | String
    D          | Problem dimension                                | Integer
    DATASET    | Best results I repetition                        | Py Numpy array
    
    Output:
    Save xls file in current directory
    
    # Individual results
    X = DATASET['X_POSITION']
    COLUMNS = []
    for I_COUNT in range(D):
        COLUMNS_X = 'X_' + str(I_COUNT)
        COLUMNS.append(COLUMNS_X)
    DATA1 = pd.DataFrame(X, columns = COLUMNS)
    OF = DATASET['OF']
    DATA2 = pd.DataFrame(OF, columns = ['OF'])
    FIT = DATASET['FIT']
    DATA3 = pd.DataFrame(FIT, columns = ['FIT'])
    NEOF = DATASET['NEOF']
    DATA4 = pd.DataFrame(NEOF, columns = ['NEOF'])
    FRAME = [DATA1, DATA2, DATA3, DATA4]
    DATA = pd.concat(FRAME, axis = 1)
    NAME += '.xlsx' 
    print(NAME)
    WRITER = pd.ExcelWriter(NAME, engine = 'xlsxwriter')
    DATA.to_excel(WRITER, sheet_name = 'Sheet1')
    WRITER.close()

def EXCEL_PROCESS_RESUME(NAME, D, DATASET, N_ITER, N_REP):

    This function create output Excel files complete process.

    Input:
    NAME       | Filename                                         | String
    D          | Problem dimension                                | Integer
    DATASET    | Best results I repetition                        | Py Numpy array
    N_REP      | Number of repetitions                            | Integer
    N_ITER     | Number of iterations                             | Integer

    Output:
    Save xls file in current directory

    
    # Resume process in arrays
    X = np.zeros((N_REP, D))
    OF = np.zeros((N_REP, 1))
    FIT = np.zeros((N_REP, 1))
    NEOF = np.zeros((N_REP, 1))
    for REP in range(N_REP):
        X_I = DATASET[REP]['X_POSITION'][N_ITER]
        X[REP, :] = X_I
        OF[REP, :] = DATASET[REP]['OF'][N_ITER]
        FIT[REP, :] = DATASET[REP]['FIT'][N_ITER]
        NEOF[REP, :] = DATASET[REP]['NEOF'][N_ITER]
    
    # Save output in Excel file
    COLUMNS = []
    for I in range(D):
        COLUMNS_X = 'X_' + str(I)
        COLUMNS.append(COLUMNS_X)
    DATA1 = pd.DataFrame(X, columns = COLUMNS)
    DATA2 = pd.DataFrame(OF, columns = ['OF'])
    DATA3 = pd.DataFrame(FIT, columns = ['FIT'])
    DATA4 = pd.DataFrame(NEOF, columns = ['NEOF'])
    FRAME = [DATA1, DATA2, DATA3, DATA4]
    DATA = pd.concat(FRAME, axis = 1)
    NAME += '.xlsx' 
    print(NAME)
    WRITER = pd.ExcelWriter(NAME, engine = 'xlsxwriter')
    DATA.to_excel(WRITER, sheet_name = 'Sheet1')
    WRITER.close()
"""

if __name__ == "__main__":
    
    # initial_population_01
    # Data
    nPop = 5
    xL = [1, 1, 2]
    xU = [4, 4, 4]
    d = len(xU) # or d = len(xL) or d = 3

    # Call function
    population = initial_population_01(nPop, d, xL, xU)

    # Output details
    print('particle 0: ', population[0])
    print('particle 1: ', population[1])
    print('particle 2: ', population[2])
    print('particle 3: ', population[3])
    print('particle 4: ', population[4])
    print('\n\n')

    # initial_population_02
    # Data
    nPop = 5
    d = 3
    
    # Call function
    population = initial_population_02(nPop, d)

    # Output details
    print('particle 0: ', population[0])
    print('particle 1: ', population[1])
    print('particle 2: ', population[2])
    print('particle 3: ', population[3])
    print('particle 4: ', population[4])
    print('\n\n')

    # initial_pops
    # Data
    setup = {
            'N_REP': 4,
            'N_POP': 2,
            'D': 3,
            'X_L': [1, 1, 1],
            'X_U': [3, 3, 3],
            'TYPE CODE': 'REAL CODE',
            'SEED CONTROL': [10, 11, 10, 11]
            }

    # Call function
    pops = initial_pops(setup['N_REP'], setup['N_POP'], setup['D'], setup['X_L'], setup['X_U'], setup['TYPE CODE'], setup['SEED CONTROL'])

    # Output details
    print('population repetition ID = 0: ', pops[0])
    print('population repetition ID = 1: ', pops[1])
    print('population repetition ID = 2: ', pops[2])
    print('population repetition ID = 3: ', pops[3])
    print('\n Agent example:')
    print('init. population rep. ID = 0 - agent id = 0: ', pops[0][0])
    print('init. population rep. ID = 0 - agent id = 1: ', pops[0][1])
    print('\n\n')

    # fit_value
    # Data
    nPop = 3
    ofI = 1

    # Call function
    fitI = fit_value(ofI)
    
    # Output details
    print(f'fit value i agent when OF = {ofI} is ', fitI)
    print('\n\n')

    # check_interval_01
    # Data
    xL = [1, 2, 3]
    xU = [5, 5, 5]
    xI = [6, -1, 2.5]

    # Call function
    xINew = check_interval_01(xI, xL, xU)
    
    # Output details
    print(xINew)
    print('\n\n')

    # mutation_01_movement
    # Data
    xL = [1, 1, 1]
    xU = [3, 3, 3]
    d = len(xL)
    sigma = 15 / 100 # 15%
    xI = [2, 2, 2]
    pdf = 'UNIFORM'

    # Objective function
    def OF_FUNCTION(X, NULL_DIC):
        x0 = X[0]
        x1 = X[1]
        x2 = X[2]
        of = x0 ** 2 + x1 ** 2 + x2 ** 2
        return of

    # Call function
    xII, ofINew, fitINew, neof = mutation_01_movement(OF_FUNCTION, xI, xL, xU, d, pdf, sigma)

    # Output details
    print('x New: ', xII)
    print('of New: ',ofINew)
    print('fit New: ', fitINew)
    print('number of evalutions objective function: ',neof)


    # Definição das listas de exemplo
    xValues = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Exemplo de valores para X
    ofValues = [10, 5, 8]  # Exemplo de valores para OF
    fitValues = [0.1, 0.5, 0.3]  # Exemplo de valores para FIT

    # Chamando a função best_values com os dados de exemplo
    bestPos, worstPos, xBest, xWorst, ofBest, ofWorst, fitBest, fitWorst, ofAverage, fitAverage = best_values(xValues, ofValues, fitValues)

    # Exibindo os resultados
    print("Best position in the population:", bestPos)
    print("Worst position in the population:", worstPos)
    print("Best value of X:", xBest)
    print("Worst value of X:", xWorst)
    print("Best value of OF:", ofBest)
    print("Worst value of OF:", ofWorst)
    print("Best value of FIT:", fitBest)
    print("Worst value of FIT:", fitWorst)
    print("Average OF value:", ofAverage)
    print("Average FIT value:", fitAverage)
