def obj(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    sum_penalty = sum(g) * 1E6
    f = of + sum_penalty
    return f