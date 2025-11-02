"""Whale Movement function."""

import math
import random
from benchmark import sphere as sp
from benchmark import rosenbrock as ros
from benchmark import rastrigin as ras
from benchmark import ackley as ack
from benchmark import griewank as gri
from benchmark import zakharov as zak
from benchmark import easom as eas
from benchmark import michalewicz as mic
from benchmark import dixon_price as dix
from benchmark import goldstein_price as gol
from benchmark import powell as powe
from benchmark import *

def whale_movement_(x_best: list, x_current: list, t: int, T: int, d: int, 
                    x_lower: list, x_upper: list) -> list:
    """
    Whale Optimization Algorithm (WOA) movement step.

    :param x_best: Best known solution (leader whale)
    :param x_current: Current whale position
    :param t: Current iteration
    :param T: Total number of iterations
    :param d: Dimension of the search space
    :param x_lower: Lower bounds for each dimension
    :param x_upper: Upper bounds for each dimension
    :return: Updated position of the current whale
    """

    a = 2 - 2 * (t / T)
    p = random.random()  # probabilidade para decidir tipo de movimento

    x_new = x_current.copy()

    if p < 0.5:
        # --- Movimento de cerco (encircling) ou exploração ---
        A = 2 * a * random.random() - a
        C = 2 * random.random()
        for i in range(d):
            D = abs(C * x_best[i] - x_current[i])
            if abs(A) < 1:
                # Movimento de cerco (encircling)
                x_new[i] = x_best[i] - A * D
            else:
                # Exploração: move em direção a uma posição aleatória
                rand_pos = random.uniform(x_lower[i], x_upper[i])
                D = abs(C * rand_pos - x_current[i])
                x_new[i] = rand_pos - A * D
    else:
        # --- Movimento em espiral ---
        b = 1
        l = random.uniform(-1, 1)
        for i in range(d):
            D = abs(x_best[i] - x_current[i])
            x_new[i] = D * math.exp(b * l) * math.cos(2 * math.pi * l) + x_best[i]

    # Limita a posição dentro dos limites de busca
    for i in range(d):
        x_new[i] = max(min(x_new[i], x_upper[i]), x_lower[i])

    return x_new
