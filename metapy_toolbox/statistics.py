import numpy as np
from scipy.stats import friedmanchisquare
from typing import Sequence, Dict, Tuple, Optional

#### def COV(population): ... to implement...


## to test ADP/validate, have to confirm and test the formula
def ADP(population: np.ndarray) -> float:
    """ 
    This Function Calculate the Average Distance to the Population.
    
    :param population: Population of shape (N, D)
    :return: Average Distance to the Population (float)
    """
    distances = [] 
    for i in range(population.shape[0]):
        for j in range(i + 1, (population.shape[0])):
            dist = np.linalg.norm(population[i] - population[j])
            distances.append(dist)
    return np.mean(distances) if distances else 0.0

#### in process... and test MDC/validate
# def MDC(population):
#     """Calculate the Mean Distance to the Centroid of a population.
#     Args:
#         population (np.ndarray): Population of shape (N, D) where N is the number of individuals and D is the number of dimensions.
#         dimensions (list, optional): List of dimensions to calculate the distance. If None, all dimensions are used. Defaults to None. 
#         Returns:
#         float: Mean Distance to the Centroid.
#     """
#     if dimensions is None:
#         dimensions = list(range(population.shape[1]))
#     centroid = np.mean(population[:, dimensions], axis=0)
#     distances = np.linalg.norm(population[:, dimensions] - centroid, axis=1)
#     return np.mean(distances)




### Dimension-wise diversity from article: A better balance in metaheuristic algorithms: Does it exist? .... eq(1) eq(2)...
def DIV(population: np.ndarray) -> float:
    """"
    This Function calculate the diversity of a population based on the dimension-wise diversity metric.

    :param population: Population of shape (N, D)
    :return: Exploration level (float)
    """
    n=population.shape[0]   # number of individuals
    d=population.shape[1] # number of dimensions
    mean_pop=[]
    for i in range(d):
        mean_pop.append(population[:,i].mean()) # mean of each dimension
    sum_div=[]
    for i in range(d):
        sum=0
        for j in range(n):
            sum += (population[j, i] - mean_pop[i])**2
        sum_div.append(sum/n)
    div=0
    for i in range(d):
        div+=sum_div[i]
    return div/d


### Pair-wise comparison from article: A Probabilistic metric for comparing metaheuristic optimization algorithms... eq(5), eq(6) and eq(7)
def pair_wise(yp: list, ye: list, mode: str='min') -> Tuple[float, float, float]:
    """ This Function calculate the pair-wise comparison probabilities between two sets of results.

        :param yp: Results from the population of proposed algorithm (1th algorithm)
        :param ye: Results from the population of Existing algorithm (2th algorithm)
        :param mode: 'min' for minimization problems, 'max' for maximization problems.
    
        :return: [0] = P(better) proposed (1th) better than existing (2th) [1] = P(worse) proposed (1th) worse than existing (2th) [2] = P(equal)
    """
    pop_best_p=np.asarray(yp)[:, None] # shape (len(yp), 1)
    pop_best_e=np.asarray(ye)[None, :] # || (1, len(ye))

    if mode=='min':
        lt= (pop_best_p < pop_best_e).astype(int)   #shape (len(yp), len(ye)) of ints 0/1
        gt= (pop_best_p > pop_best_e).astype(int) # ||
    elif mode=='max':
        lt= (pop_best_p > pop_best_e).astype(int)
        gt= (pop_best_p < pop_best_e).astype(int)
    else:
        raise ValueError("mode must be 'min' or 'max'")
    
    P_btter=float(lt.mean()) # the mean of the matrix of 0/1... is gonna be all the 1's/ tt of elements in matrix
    P_worse=float(gt.mean())
    P_equal=1-P_btter-P_worse
    return P_btter, P_worse, P_equal 


#to implement friedman test
# def friedman_test(args:...) -> Tuple[float, float]:
#     """Perform the Friedman test for multiple related samples.


