# Change the path in other computer
import sys
import pandas as pd
import numpy as np
import scipy
TEST_FOLDER = r'C:\Users\wander\Documents\GitHub\METAPYDEV'
sys.path.append(TEST_FOLDER)

from META_TOOLBOX_OBSOLETOS.META import *
from META_TOOLBOX_OBSOLETOS.META_CO_LIBRARY import *
from obj_function import *

# https://sci-hub.se/https://doi.org/10.1016/j.asoc.2016.09.045

SETUP = {
            'ALGORITHM': 'HILL CLIMBING 01',
            'N_REP': 1,
            'N_POP': 5,
            'N_ITER': 50,
            'X_L': [-5, -5],
            'X_U': [5, 5],
            'D': 2,
            'PARAMETERS': {'SIGMA (%)': 15},
            'NULL_DIC': None,
            'TYPE CODE': 'REAL CODE',
            'OF': MY_FUNCTION,
        }


POP = META_CO.initial_pops(SETUP['N_REP'], SETUP['N_POP'], SETUP['D'], SETUP['X_L'], SETUP['X_U'], SETUP['TYPE CODE'])

INFO = [[SETUP, I] for I in POP]

RESULTS_ITER, BEST_ITER, AVERAGE_ITER, WORST_ITER  = HILL_CLIMBING_001(INFO[0])