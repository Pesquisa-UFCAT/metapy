################################################################################
# UNIVERSIDADE FEDERAL DE CATALÃO (UFCAT)
# WANDERLEI MALAQUIAS PEREIRA JUNIOR,                  ENG. CIVIL / PROF (UFCAT)
# JOÃO V. COELHO ESTRELA,                                     ENG. MINAS (UFCAT)
################################################################################

################################################################################
# DESCRIÇÃO ALGORITMO:
# BIBLIO. META DE FUNÇÕES DE BENCHMARK DESENVOLVIDA PELO GRUPO DE PESQUISA E
# ESTUDOS EM ENGENHARIA (GPEE)
################################################################################

################################################################################
# BIBLIOTECAS NATIVAS PYTHON
import numpy as np

# FUNÇÃO SPHERE
def SPHERE(X):
    """
    Sphere benchmark function D-dimension
    """
    DIM = len(X)
    SUM = 0
    for I_COUNT in range(DIM):
        X_I = X[I_COUNT]
        SUM += X_I ** 2
    Y = SUM
    return Y

# FUNÇÃO ROSENBROCK
def ROSENBROCK(X):
    """
    Rosenbrock benchmark function D-dimension
    """
    DIM = len(X)
    SUM = 0
    for I_COUNT in range(DIM - 1):
        X_I = X[I_COUNT]
        X_NEXT = X[I_COUNT + 1]
        NEW = 100 * (X_NEXT - X_I ** 2) ** 2 + (X_I - 1) ** 2
        SUM += NEW
    Y = SUM
    return Y

# FUNÇÃO RASTRIGIN
def RASTRIGIN(X):
    """
    Rastrigin benchmark function D-dimension
    """
    DIM = len(X)
    SUM = 0
    for I_COUNT in range(DIM):
        X_I = X[I_COUNT]
        SUM += (X_I ** 2 - 10 * np.cos(2 * np.pi * X_I))
    Y = 10 * DIM + SUM
    return Y
