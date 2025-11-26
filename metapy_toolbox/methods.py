# """Module has functions that are used in all metaheuristic algorithms"""
# import numpy as np
# import pandas as pd
# from typing import Optional

# def initial_population_01(n_population: int, n_dimensions: int, x_lower: list, x_upper: list, seed: Optional[int] = None) -> list:
#     """Generates a random population with defined limits. Continuum variables generator.

#     :param n_population: Number of population
#     :param n_dimensions: Problem dimension
#     :param x_lower: Lower limit of the design variables
#     :param x_upper: Upper limit of the design variables
#     :param seed: Random seed. Default is None. Use None for random seed

#     :return: Population design variables
#     """

#     # Set random seed
#     if seed is None:
#         pass
#     else:
#         np.random.seed(seed)

#     # Random variable generator
#     x_pop = []
#     for _ in range(n_population):
#         aux = []
#         for j in range(n_dimensions):
#             random_number = np.random.random()
#             value_i_dimension = x_lower[j] + (x_upper[j] - x_lower[j]) * random_number
#             aux.append(value_i_dimension)
#         x_pop.append(aux)

#     return x_pop


# if __name__ == "__main__":
#     # First test
#     n_pop = 10
#     n_dim = 2
#     x_low = [-5.0] * n_dim
#     x_upp = [5.0] * n_dim
#     pop = initial_population_01(n_pop, n_dim, x_low, x_upp, seed=42)
#     print(pop)

#     # Second test
#     n_pop = 10
#     n_dim = 2
#     x_low = [-5.0] * n_dim
#     x_upp = [5.0] * n_dim
#     pop = initial_population_01(n_pop, n_dim, x_low, x_upp)
#     print(pop)