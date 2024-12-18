import numpy as np

def SPHERE(X):
    """
    Sphere benchmark function d-dimension

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/BENCHMARKS.html
    """
    
    DIM = len(X)
    SUM = 0
    for I_COUNT in range(DIM):
        X_I = X[I_COUNT]
        SUM += X_I ** 2
    OF = SUM
    return OF

def ROSENBROCK(X):
    """
    Rosenbrock benchmark function d-dimension.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/BENCHMARKS.html
    """
    
    DIM = len(X)
    SUM = 0
    for I_COUNT in range(DIM - 1):
        X_I = X[I_COUNT]
        X_NEXT = X[I_COUNT + 1]
        NEW = 100 * (X_NEXT - X_I ** 2) ** 2 + (X_I - 1) ** 2
        SUM += NEW
    OF = SUM
    return OF

def RASTRIGIN(X):
    """
    Rastrigin benchmark function d-dimension.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/BENCHMARKS.html
    """
    
    DIM = len(X)
    SUM = 0
    for I_COUNT in range(DIM):
        X_I = X[I_COUNT]
        SUM += (X_I ** 2 - 10 * np.cos(2 * np.pi * X_I))
    OF = 10 * DIM + SUM
    return OF

def ACKLEY(X):
    """
    Ackley benchmark function d-dimension.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/BENCHMARKS.html
    """
    
    DIM = len(X)
    SUM1 = 0
    SUM2 = 0
    A = 20
    B = 0.2
    C = 2 * np.pi
    for I_COUNT in range(DIM):
        X_I = X[I_COUNT]
        SUM1 += X_I ** 2
        SUM2 += np.cos(C * X_I)
    TERM_1 = -A * np.exp(-B * np.sqrt(SUM1 / DIM))
    TERM_2 = -np.exp(SUM2 / DIM)
    OF = TERM_1 + TERM_2 + A + np.exp(1)
    return OF

def GRIEWANK(X):
    """
    Griewank benchmark function d-dimension.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/BENCHMARKS.html
    """
    
    DIM = len(X)
    SUM = 0
    for I_COUNT in range(DIM):
        X_I = X[I_COUNT]
        SUM += (X_I ** 2) / 4000
    PROD = np.cos(X_I / np.sqrt(X_I))
    OF = SUM - PROD + 1
    return OF

def ZAKHAROV(X):
    """
    Zakharov benchmark function d-dimension.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/BENCHMARKS.html
    """
    
    DIM = len(X)
    SUM_1 = 0
    SUM_2 = 0
    for I_COUNT in range(DIM):
        X_I = X[I_COUNT]
        SUM_1 += X_I ** 2
        SUM_2 += (0.5 * I_COUNT * X_I)
    OF = SUM_1 + SUM_2**2 + SUM_2**4
    return OF

def EASOM(X):
    """
    Easom benchmark function 2-dimension

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/BENCHMARKS.html
    """
    
    X_1 = X[0]
    X_2 = X[1]
    FACT_1 = - np.cos(X_1) * np.cos(X_2)
    FACT_2 = np.exp(- (X_1 - np.pi) ** 2 - (X_2 - np.pi) ** 2)
    OF = FACT_1 * FACT_2
    return OF

def MICHALEWICS(X):
    """
    Sphere benchmark function 2-dimension, 5-dimension and 10-dimension.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/BENCHMARKS.html
    """
    
    DIM = len(X)
    SUM = 0
    M = 10
    for I_COUNT in range(DIM):
        X_I = X[I_COUNT]
        SUM += np.sin(X_I) * (np.sin((I_COUNT * X_I ** 2) / np.pi)**(2 * M))
    OF = - SUM
    return OF

def RESIDUAL(S, O):
    """
    Residual value.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/008-BENCHMARKS.html
    """
    return S - O

def LOSS_FUNCTION_1(Y_EXP, Y_NUM):
    """
    Loss function d-dimension. Mean Square Error.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/008-BENCHMARKS.html
    """
    
    ERROR = 0
    for I in range(len(Y_EXP)):
        RES = RESIDUAL(Y_NUM[I], Y_EXP[I])
        ERROR += (RES) ** 2
    OF = ERROR / len(Y_EXP)
    
    return OF

def LOSS_FUNCTION_2(Y_EXP, Y_NUM):
    """
    Loss function d-dimension. Mean Absolute Error.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/BENCHMARKS.html

    https://search.r-project.org/CRAN/refmans/hydroGOF/html/mae.html
    """
    
    ERROR = 0
    for I in range(len(Y_EXP)):
        RES = RESIDUAL(Y_NUM[I], Y_EXP[I])
        ERROR += np.abs(RES)
    OF = ERROR / len(Y_EXP)
    
    return OF

def LOSS_FUNCTION_3(Y_EXP, Y_NUM):
    """
    Loss function d-dimension. Square Error.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/BENCHMARKS.html
    """
    
    ERROR = 0
    for I in range(len(Y_EXP)):
        RES = RESIDUAL(Y_NUM[I], Y_EXP[I])
        ERROR += (RES) ** 2
    OF = ERROR
    
    return OF

def LOSS_FUNCTION_4(Y_EXP, Y_NUM, DELTA):
    """
    Loss function d-dimension. Smooth Mean Absolute Error or Hubber Loss.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/BENCHMARKS.html
    """

    ERROR = 0
    for I in range(len(Y_EXP)):
        RES = RESIDUAL(Y_NUM[I], Y_EXP[I])
        CRITERIA = np.abs(RES)
        if CRITERIA <= DELTA:
            ERROR += 0.5 * (RES) ** 2
        else:
            ERROR += DELTA * (np.abs(RES) - 0.5 * DELTA)
    OF = ERROR
    
    return OF

def LOSS_FUNCTION_5(Y_EXP, Y_NUM):
    """
    Loss function d-dimension. Root Mean Square Error.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/BENCHMARKS.html
    """
    
    ERROR = 0
    for I in range(len(Y_EXP)):
        RES = RESIDUAL(Y_NUM[I], Y_EXP[I])
        ERROR += (RES) ** 2
    OF = ERROR / len(Y_EXP)
    OF = OF ** (0.5)
    
    return OF

def LOSS_FUNCTION_6(Y_EXP, Y_NUM):
    """
    Loss function d-dimension. Mean Absolute Relative Error or Mean Magnitude Relative error.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/BENCHMARKS.html

    https://arxiv.org/ftp/arxiv/papers/1809/1809.03006.pdf
    """
    
    ERROR = 0
    for I in range(len(Y_EXP)):
        RES = RESIDUAL(Y_NUM[I], Y_EXP[I])
        ERROR += np.abs(RES) / np.abs(Y_EXP[I])
    OF = ERROR / len(Y_EXP)
    
    return OF

def LOSS_FUNCTION_7(Y_EXP, Y_NUM):
    """
    Loss function d-dimension. Normalized Root Mean Square Error.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/BENCHMARKS.html

    https://arxiv.org/ftp/arxiv/papers/1809/1809.03006.pdf
    https://www.analyticsvidhya.com/blog/2021/10/evaluation-metric-for-regression-models/#:~:text=Relative%20Root%20Mean%20Square%20Error,to%20compare%20different%20measurement%20techniques.
    """
    
    RMSE = LOSS_FUNCTION_5(Y_EXP, Y_NUM)
    NVAL = np.std(Y_EXP)
    OF = RMSE / NVAL
    
    return OF

# Ler https://sci-hub.hkvisa.net/10.1016/j.rser.2015.11.058