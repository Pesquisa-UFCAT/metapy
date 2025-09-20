"""Benchmark functions for optimization."""
import numpy as np


def sphere(x: list) -> float:
    """
    The Sphere function has d local minima except for the global one. It is continuous, convex and unimodal.

    :param x: Design variables.

    :return: Objective function value.
    """

    d = len(x)
    of = 0
    for i in range(d):
        x_i = x[i]
        of += x_i ** 2

    return of


def rosenbrock(x: list) -> float:
    """
    The Rosenbrock function is unimodal, and the global minimum lies in a narrow, parabolic valley.

    :param x: Design variables.

    :return: Objective function value.
    """

    d = len(x)
    sum = 0
    for i in range(d - 1):
        x_i = x[i]
        x_next = x[i + 1]
        new = 100 * (x_next - x_i ** 2) ** 2 + (x_i - 1) ** 2
        sum += new
    of = sum

    return of


def rastrigin(x: list) -> float:
    """
    The Rastrigin function has several local minima. It is highly multimodal, but locations of the minima are regularly distributed.

    :param x: Design variables.

    :return: Objective function value.
    """

    d = len(x)
    sum = 0
    for i in range(d):
        x_i = x[i]
        sum += (x_i ** 2 - 10 * np.cos(2 * np.pi * x_i))
    of = 10 * d + sum

    return of
