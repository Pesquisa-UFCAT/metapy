import numpy as np
import sys
import META_CO_LIBRARY as META_CO

def ROULETE_WHEEL_SELECTION(FIT, N_POP, I):
    """
    This function selects a position from the population using the roulette wheel selection method.
    """
    FIT  = list(FIT.flatten())
    POS = [int(C) for C in list(np.arange(0, N_POP, 1, dtype = int))]
    del POS[I]
    del FIT[I]
    MAXIMUM = np.sum(FIT)
    SELECTION_PROBS = [VALUE / MAXIMUM for VALUE in FIT]
    SELECTED = np.random.choice(POS, 1, replace = False, p = SELECTION_PROBS)
    return list(SELECTED)[0]

def TOURNAMENT_SELECTION(FIT, N_POP, I, RUNS):
    """
    This function selects a position from the population using the tournament selection method.
    """
    FIT_NEW  = list(FIT.flatten())
    POS = [int(C) for C in list(np.arange(0, N_POP, 1, dtype = int))]
    del POS[I]
    del FIT_NEW[I]
    POINTS = [0 for C in range(N_POP)]
    for J in range(RUNS):
        SELECTED_POS = np.random.choice(POS, 2, replace = False)
        SELECTED_FIT = [FIT[SELECTED_POS[0]], FIT[SELECTED_POS[1]]]
        if SELECTED_FIT[0][0] <= SELECTED_FIT[1][0]:
            WIN = SELECTED_POS[1]
        elif SELECTED_FIT[0][0] > SELECTED_FIT[1][0]:
            WIN = SELECTED_POS[0]
        POINTS[WIN] += 1
    M = max(POINTS)
    POSS = [K for K in range(len(POINTS)) if POINTS[K] == M]
    SELECTED = np.random.choice(POSS, 1, replace = False)
    return SELECTED[0]

def LINEAR_CROSSOVER(FATHER_1, FATHER_2, OF_FUNCTION, NULL_DIC, X_L, X_U):
    """
    A hybrid harmony search with arithmetic crossover operation for economic dispatch
    https://medium.com/geekculture/crossover-operators-in-ga-cffa77cdd0c8
    """

    OFFSPRING_A = []
    OFFSPRING_B = []
    OFFSPRING_C = []

    for I in range(len(FATHER_1)):
        OFFSPRING_A.append(0.5 * FATHER_1[I] + 0.5 * FATHER_2[I])
        OFFSPRING_B.append(1.5 * FATHER_1[I] - 0.5 * FATHER_2[I])
        OFFSPRING_C.append(0.5 * FATHER_1[I] + 1.5 * FATHER_2[I])
        
    OFFSPRING_A = META_CO.check_interval_01(OFFSPRING_A, X_L, X_U) 
    OFFSPRING_B = META_CO.check_interval_01(OFFSPRING_B, X_L, X_U) 
    OFFSPRING_C = META_CO.check_interval_01(OFFSPRING_C, X_L, X_U) 
    
    OF_OFFSPRING_A = OF_FUNCTION(OFFSPRING_A, NULL_DIC)
    OF_OFFSPRING_B = OF_FUNCTION(OFFSPRING_B, NULL_DIC)
    OF_OFFSPRING_C = OF_FUNCTION(OFFSPRING_C, NULL_DIC)
    NEOF = 3
    
    LIST_OF = [OF_OFFSPRING_A, OF_OFFSPRING_B, OF_OFFSPRING_C]
    MIN_VALUE = min(LIST_OF)
    POS_MIN = LIST_OF.index(MIN_VALUE)  

    if POS_MIN == 0:
        X_T1I = OFFSPRING_A.copy()
        OF_T1I = OF_OFFSPRING_A
    elif POS_MIN == 1:
        X_T1I = OFFSPRING_B.copy()
        OF_T1I = OF_OFFSPRING_B
    else:
        X_T1I = OFFSPRING_C.copy()
        OF_T1I = OF_OFFSPRING_C

    FIT_T1I = META_CO.fit_value(OF_T1I)
    
    return X_T1I, OF_T1I, FIT_T1I, NEOF

def BINOMIAL_CROSSOVER(FATHER_1, FATHER_2, BINOMIAL_RATE, OF_FUNCTION, NULL_DIC, X_L, X_U):
    """
    https://sci-hub.se/https://doi.org/10.1007/978-3-642-29353-5_17
    """
    # Start internal variables
    X_T1I = []

    # Movement
    for I_COUNT in range(len(FATHER_1)):
        if np.random.uniform(0, 1) <= BINOMIAL_RATE:
            X_T1I.append(FATHER_2[I_COUNT])
        else:
            X_T1I.append(FATHER_1[I_COUNT])
    
    # Check boundes
    X_T1I = META_CO.check_interval_01(X_T1I, X_L, X_U) 
    
    # Evaluation of the objective function and fitness
    OF_T1I = OF_FUNCTION(X_T1I, NULL_DIC)
    FIT_T1I = META_CO.fit_value(OF_T1I)
    NEOF = 1
    
    return X_T1I, OF_T1I, FIT_T1I, NEOF

def BLXALPHA_CROSSOVER(FATHER_1, FATHER_2, OF_FUNCTION, NULL_DIC, X_L, X_U):
    """
    https://engineering.purdue.edu/~sudhoff/ee630/Lecture04.pdf
    https://sci-hub.se/https://doi.org/10.1016/j.ijepes.2014.04.031
    https://www.diva-portal.org/smash/get/diva2:1051466/FULLTEXT01.pdf
    """
     
    # Start internal variables
    X_T1I = []
    OFFSPRING_A = []
    OFFSPRING_B = []
    ALPHA = np.random.uniform(0, 1)

    # Movement
    for I in range(len(FATHER_1)):
        MAX = max(FATHER_1[I], FATHER_2[I])
        MIN = min(FATHER_1[I], FATHER_2[I])
        OFFSPRING_A.append(MIN - ALPHA * (MAX - MIN))
        OFFSPRING_B.append(MAX + ALPHA * (MAX - MIN))
    OFFSPRING_A = META_CO.check_interval_01(OFFSPRING_A, X_L, X_U) 
    OFFSPRING_B = META_CO.check_interval_01(OFFSPRING_B, X_L, X_U)    
    OF_OFFSPRING_A = OF_FUNCTION(OFFSPRING_A, NULL_DIC)
    OF_OFFSPRING_B = OF_FUNCTION(OFFSPRING_B, NULL_DIC)
    NEOF = 2
    LIST_OF = [OF_OFFSPRING_A, OF_OFFSPRING_B]
    MIN_VALUE = min(LIST_OF)
    POS_MIN = LIST_OF.index(MIN_VALUE)  
    if POS_MIN == 0:
        X_T1I = OFFSPRING_A.copy()
        OF_T1I = OF_OFFSPRING_A
    else:
        X_T1I = OFFSPRING_B.copy()
        OF_T1I = OF_OFFSPRING_B
    FIT_T1I = META_CO.fit_value(OF_T1I)
    
    return X_T1I, OF_T1I, FIT_T1I, NEOF

def mp_crossover(chromosome_a, chromosome_b, seed, OF_FUNCTION, NULL_DIC):
    """mp_crossover(chromosome_a, chromosome_b)

    Multi-point ordered crossover.

    Parameters
    ----------
    chromosome_a : NDArray
        Encoding of a solution (chromosome).
    chromosome_b : NDArray
        Encoding of a solution (chromosome).
    seed : int | None, optional
        Seed for pseudo-random numbers generation, by default None.

    Returns
    -------
    tuple[NDArray, NDArray]
        Tuple of chromosomes after crossover.
    https://providing.blogspot.com/2015/06/genetic-algorithms-crossover.html?m=1
    https://medium.com/@samiran.bera/crossover-operator-the-heart-of-genetic-algorithm-6c0fdcb405c0
    """
    child_a = chromosome_a.copy()
    child_b = chromosome_b.copy()
    mask = np.random.RandomState(seed).randint(2, size=len(chromosome_a)) == 1
    child_a[~mask] = sorted(child_a[~mask], key=lambda x: np.where(chromosome_b == x))
    child_b[mask] = sorted(child_b[mask], key=lambda x: np.where(chromosome_a == x))
    
    OF_OFFSPRING_A = OF_FUNCTION(child_a, NULL_DIC)
    OF_OFFSPRING_B = OF_FUNCTION(child_b, NULL_DIC)
    NEOF = 2
    LIST_OF = [OF_OFFSPRING_A, OF_OFFSPRING_B]
    MIN_VALUE = min(LIST_OF)
    POS_MIN = LIST_OF.index(MIN_VALUE)  
    if POS_MIN == 0:
        X_T1I = child_a.copy()
        OF_T1I = OF_OFFSPRING_A
    else:
        X_T1I = child_b.copy()
        OF_T1I = OF_OFFSPRING_B
    FIT_T1I = META_CO.fit_value(OF_T1I)
    
    return X_T1I, OF_T1I, FIT_T1I, NEOF

def mp_mutation(chromosome, seed, OF_CHRO, OF_FUNCTION, NULL_DIC):
    """mp_mutation(chromosome)

    Multi-point inversion mutation. A random mask encodes
    which elements will keep the original order or the
    reversed one.

    Parameters
    ----------
    chromosome : NDArray
        Encoding of a solution (chromosome).
    seed : int | None, optional
        Seed for pseudo-random numbers generation, by default None.

    Returns
    -------
    NDArray
        Returns the chromosome after mutation.
    """
    individual = chromosome.copy()
    mask = np.random.RandomState(seed).randint(2, size=len(individual)) == 1
    individual[~mask] = np.flip(individual[~mask])

    OF_OFFSPRING_B = OF_FUNCTION(individual, NULL_DIC)
    NEOF = 1
    LIST_OF = [OF_CHRO, OF_OFFSPRING_B]
    MIN_VALUE = min(LIST_OF)
    POS_MIN = LIST_OF.index(MIN_VALUE)  
    if POS_MIN == 0:
        X_T1I = chromosome.copy()
        OF_T1I = OF_CHRO
    else:
        X_T1I = individual.copy()
        OF_T1I = OF_OFFSPRING_B
    FIT_T1I = META_CO.fit_value(OF_T1I)
    
    return X_T1I, OF_T1I, FIT_T1I, NEOF