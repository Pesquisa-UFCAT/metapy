################################################################################
# UNIVERSIDADE FEDERAL DE CATALÃO (UFCAT)
# WANDERLEI MALAQUIAS PEREIRA JUNIOR,                  ENG. CIVIL / PROF (UFCAT)
# JOÃO V. COELHO ESTRELA,                                     ENG. MINAS (UFCAT)
################################################################################

################################################################################
# DESCRIÇÃO ALGORITMO:
# BIBLIO. DE FUNÇÕES COMUNS DA PLATAFORMA "META OPTIMIZATION TOOLBOX" DESENVOL-
# VIDA PELO GRUPO DE PESQUISAS E ESTUDOS EM ENGENHARIA (GPEE)
################################################################################

################################################################################
# BIBLIOTECAS NATIVAS PYTHON
import numpy as np

################################################################################
# BIBLIOTECAS DESENVOLVEDORES GPEE

# CRIAÇÃO DA POP. INICIAL
def INITIAL_POPULATION(N_POP, D, X, X_L, X_U):
    """ 
    This function initializes the population randomically between the limits X_L 
    and X_U 

    Input:
    N_POP: Number of population (integer);
    D: Problem dimension (integer);
    X: Empty design variables (Python Numpy array[N_POP x D], float);
    X_L: Lower limit design variables (Python list[D], float);
    X_U: Upper limit design variables (Python list[D], float);
        
    Output:
    X: Initial design variables (Python Numpy array[N_POP x D], float);
    """
    for I_COUNT in range(N_POP):
        for J_COUNT in range(D):
            RANDON_NUMBER = np.random.random()
            X[I_COUNT, J_COUNT] = X_L[J_COUNT] + (X_U[J_COUNT] - X_L[J_COUNT]) * RANDON_NUMBER
    return X

# AVALIAÇÃO DA APTIDÃO DE UMA ÚNICA PARTÍCULA
def FIT_VALUE(OF_VALUEI):
    """ 
    This function calculates the fitness of a value of the objective function

    Input:
    OF_VALUEI: Objective function I particle value (float);

    Output:
    FIT_VALUEI: Fitness I particle value (float);
    """
    if OF_VALUEI >= 0:
        FIT_VALUEI = 1 / (1 + OF_VALUEI)
    elif OF_VALUEI < 0:
        FIT_VALUEI = 1 + abs(OF_VALUEI)
    return FIT_VALUEI

# CHECAGEM DOS LIMITES DAS VARIÁVEIS DE PROJETO DE UMA ÚNICA PARTÍCULA
def CHECK_INTERVAL(X_T0I, X_L, X_U):
    """
    This function checks if a variable is out of the limits established X_L and X_U

    Input:
    X_T0I: Design variable I particle before check (list[D], float);
    X_L: Lower limit design variables (Python list[D], float);
    X_U: Upper limit design variables (Python list[D], float);

    Output:
    X_T1I: Design variable I particle after check (list[D], float);
    """
    X_T1I = np.clip(X_T0I, X_L, X_U)
    return X_T1I

# VERIFICAÇÃO DA MELHOR PARTÍCULA, PIOR E VALOR MÉDIO
def BEST_VALUES(X, OF, FIT, N_POP):
    """ 
    This function determines the best and worst particle. 
    It also determines the average value (OF and FIT) of the population

    Input:
    X: Design variables (Python Numpy array[N_POP x D], float);
    OF: all objective function values (Python Numpy array[N_POP x 1], float);
    FIT: all fitness values (Python Numpy array[N_POP x 1], float);  
    N_POP: Number of population (integer);

    Output:
    BEST_POSITION: ID best position (integer)
    WORST_POSITION: ID worst position (integer)
    X_BEST: Design variables best particle (Python list[D], float)
    X_WORST: Design variables worst particle (Python list[D], float)
    OF_BEST: Objective function best particle value (float);
    OF_WORST: Objective function worst particle value (float);
    FIT_BEST: Fitness best particle value (float);
    FIT_WORST: Fitness worst particle value (float);
    OF_AVERAGE: Average Objective function value (float);
    FIT_AVERAGE: Average Fitness value (float);
    """
    # BEST AND WORST POSITION IN POPULATION
    SORT_POSITIONS = np.argsort(OF.T)
    BEST_POSITION = SORT_POSITIONS[0, 0]
    WORST_POSITION = SORT_POSITIONS[0, N_POP - 1]
    # GLOBAL BEST VALUES
    X_BEST = X[BEST_POSITION, :]
    OF_BEST = OF[BEST_POSITION, 0]
    FIT_BEST = FIT[BEST_POSITION, 0]
    # WORST BEST VALUES
    X_WORST = X[WORST_POSITION, :]
    OF_WORST = OF[WORST_POSITION, 0]
    FIT_WORST = FIT[WORST_POSITION, 0]
    # AVERAGE VALUES
    OF_AVERAGE = np.mean(OF)
    FIT_AVERAGE = np.mean(FIT)
    return BEST_POSITION, WORST_POSITION, X_BEST, X_WORST, OF_BEST, OF_WORST, FIT_BEST, FIT_WORST, OF_AVERAGE, FIT_AVERAGE

# VERIFICAÇÃO DA MELHOR RESPOSTA NO BEST_REPEAT
def SUMMARY_ANALYSIS(BEST_REP, N_REP, N_ITER):
    """ 
    This function presents a written summary of the best simulation 

    Input:
    BEST_REP: Best population results (Python dictionary);
    N_REP: Number of repetitions (integer);

    Output:

    """
    # Start reserved space for repetitions
    OF_MINVALUES = []
    # Checking which is the best process 
    for I_COUNT in range(N_REP):
        ID = I_COUNT
        OF_MIN = BEST_REP[ID]['OF'][N_ITER]
        OF_MINVALUES.append(OF_MIN)
    STATUS_PROCEDURE = np.argsort(OF_MINVALUES)    
    return STATUS_PROCEDURE