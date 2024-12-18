# Libraries
import sys
import numpy as np
import unittest

# Change the path in other computer
#TEST_FOLDER = r'C:\Users\wander\Documents\GitHub\METAPYDEV\META_TOOLBOX'
#TEST_FOLDER = '/home/wanderlei/Documentos/GitHub/METAPYDEV/META_TOOLBOX'
TEST_FOLDER = '/home/mateus/Documents/Estágio/META/METAPYDEV/META_TOOLBOX'
sys.path.append(TEST_FOLDER)

# Module import
from metapy_toolbox import *

# Tests
class TestMetaCOLibrary(unittest.TestCase):
    """
    METApy Common library tests.
    """
    
    def test_FIT_POSITIVE_VALUE(self):
        # Output
        RESULT = fit_value(1)

        # Test 
        DESC = f"Description: Fitness value test with positive value"
        EXP_RESULT = (
                        "Expected result: 0.5 with input value OF = 1"
                     )
        MSG = f"{DESC}\n{EXP_RESULT}"
        self.assertEqual(RESULT, 0.5, msg = MSG)

    def test_FIT_NEGATIVE_VALUE(self):
        # Output
        RESULT = fit_value(-3)  

        # Test
        DESC = f"Description: Fitness value test with negative value"
        EXP_RESULT = (
                        "Expected result: 4 with input value OF = -3"
                     )
        MSG = f"{DESC}\n{EXP_RESULT}"
        self.assertEqual(RESULT, 4, msg = MSG)

    def test_FIT_ZERO_VALUE(self):
        # Output
        RESULT = fit_value(0)  

        # Test
        DESC = f"Description: Fitness value test with negative value"
        EXP_RESULT = (
                        "Expected result: 1 with input value OF = 0"
                     )
        MSG = f"{DESC}\n{EXP_RESULT}"
        self.assertEqual(RESULT, 1, msg = MSG)

        
    def test_initial_population_01(self):    
        # Set variables
        X_L = [1, 1, 1]
        X_U = [3, 3, 3]
        N_POP = 3
        D = len(X_L)
        SETUP_RANDOM_SEED = 10
           
        # Output
        RESULT = initial_population_01(n_pop = N_POP, d = D, x_l = X_L, x_u = X_U, seed = SETUP_RANDOM_SEED) 

        # Correct output        
        OUTPUT = [
                  [2.5426412865334918, 1.041503898718803, 2.2672964698525506], 
                  [2.4976077650772237, 1.9970140246051808, 1.4495932910616953], 
                  [1.396125729519248, 2.5210614243979172, 1.338221673125071]
                 ]
        
        # Test
        DESC = f"Description: Initial population value"
        EXP_RESULT = (
                        "Expected result: [ \n"
                        "                  [2.5426412865334918, 1.041503898718803, 2.2672964698525506], \n" 
                        "                  [2.4976077650772237, 1.9970140246051808, 1.4495932910616953], \n" 
                        "                  [1.396125729519248, 2.5210614243979172, 1.338221673125071] \n"
                        "                 ] \n"
                        " with input value [1, 1, 1], [3, 3, 3] and seed = 10"
                     )
        MSG = f"{DESC}\n{EXP_RESULT}"
        self.assertEqual(RESULT, OUTPUT, msg = MSG)


    # def test_mutation_01_movement(self):
    #     # Set variables
    #     X_L = [1, 1, 1]
    #     X_U = [3, 3, 3]
    #     D = len(X_L)
    #     PDF = 'Gaussian'
    #     SIGMA = 15 / 100 # 15%
    #     SETUP_RANDOM_SEED = 10
        
    #     # Objective function
    #     def OF_FUNCTION(X, NULL_DIC):
    #         X_0 = X[0]
    #         X_1 = X[1]
    #         X_2 = X[2]
    #         OF = X_0 ** 2 + X_1 ** 2 + X_2 ** 2
    #         return OF
      
    #     # Output
    #     X_I = [2, 2, 2]
    #     X_II, OF_INEW, FIT_INEW, NEOF = mutation_01_movement(OF_FUNCTION, X_I, X_L, X_U, D, PDF, SIGMA, seed = SETUP_RANDOM_SEED)

    #     # Correct output      
    #     np.random.seed(SETUP_RANDOM_SEED)  
    #     OUTPUT = list(np.random.normal(2, 2 * 0.15, 3))
        
    #     # Test
    #     DESC = f"Description: Population movement"
    #     EXP_RESULT = (
    #                     "Expected result: [ \n"
    #                     "                  [2.39947595, 2.21458369, 1.53637991]"
    #                     "                 ] \n"
    #                     " with input value [2, 2, 2], std = 15 / 100 and seed = 10"
    #                  )
    #     MSG = f"{DESC}\n{EXP_RESULT}"
    #     self.assertEqual(X_II, OUTPUT, msg = MSG)
    #     """
    #     self.assertEqual(len(X_INEW), D)
    #     self.assertTrue(all(limite_inf <= valor <= limite_sup for valor, limite_inf, limite_sup in zip(X_INEW, X_L, X_U)))
    #     self.assertIsInstance(OF_INEW, float)
    #     self.assertIsInstance(FIT_INEW, float)
    #     self.assertEqual(NEOF, 1)    
    #     """
    


    
    def test_initial_pops(self):
        # Set variables
        SETUP = {
                'N_REP': 4,
                'N_POP': 2, 
                'D': 3, 
                'X_L': [1, 1, 1], 
                'X_U': [3, 3, 3], 
                'TYPE CODE': 'REAL CODE',
                'SEED CONTROL': 10
                }
      
        # Output
        POPS = initial_pops(SETUP['N_REP'], SETUP['N_POP'], SETUP['D'], SETUP['X_L'], SETUP['X_U'], SETUP['TYPE CODE'], SETUP['SEED CONTROL'])
        RESULT = len(POPS)

        # Correct output      
        OUTPUT = 4
        
        # Test
        DESC = f"Description: Initial population sampling is not correct dimension"
        EXP_RESULT = (
                        "Expected result: [ \n"
                        "                  [2.39947595, 2.21458369, 1.53637991]"
                        "                 ] \n"
                        " with input value [2, 2, 2], std = 15 / 100 and seed = 10"
                     )
        MSG = f"{DESC}\n{EXP_RESULT}"
        self.assertEqual(RESULT, OUTPUT, msg = EXP_RESULT)
    


    def test_BEST_VALUES(self):
        
        x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        of = [10, 5, 8]
        fit = [0.1, 0.5, 0.3]
        
        OUTPUT = best_values(x, of, fit)
            
        # Test
        self.assertEqual(OUTPUT[0], 1, msg = "Value expected: 1")
        self.assertEqual(OUTPUT[1], 0, msg = "Value expected: 0")
        self.assertEqual(OUTPUT[2], [4, 5, 6], msg = "Value expected: [4, 5, 6]")
        self.assertEqual(OUTPUT[3], [1, 2, 3], msg = "Value expected: [1, 2, 3]")
        self.assertEqual(OUTPUT[4], 5, msg = "Value expected: 5")
        self.assertEqual(OUTPUT[5], 10, msg = "Value expected: 10")
        self.assertEqual(OUTPUT[6], 0.5, msg = "Value expected: 0.5")
        self.assertEqual(OUTPUT[7], 0.1, msg = "Value expected: 0.1")
        self.assertEqual(OUTPUT[8], 7.666666666666667, msg = "Value expected: 7.666666666666667")
        self.assertEqual(OUTPUT[9], 0.3, msg = "Value expected: 0.3")

if __name__ == "__main__":
    unittest.main(argv = [''], verbosity = 2)