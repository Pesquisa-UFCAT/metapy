import numpy as np
from benchmark import sphere as sp
from grey_wolf_huting_movement import grey_wolf_huting_movement_ as gwhm

d=2
x_lower = [0, 0]
x_upper = [5, 5]
u=1000

def initial_population(n,d,x_lower,x_upper):
    return [list(np.random.uniform(x_lower[i], x_upper[i]) for i in range(d)) for j in range(n)]

x_alpha=initial_population(1,d,x_lower,x_upper)[0]
x_beta=initial_population(1,d,x_lower,x_upper)[0]
x_delta=initial_population(1,d,x_lower,x_upper)[0]
x_current=initial_population(1,d,x_lower,x_upper)[0]

for t in range(u):
    gwhm(sp,x_alpha,x_beta,x_delta,x_current,t,u,d)
    print("posição atual: ",x_current)
    print("função resultado: ",sp(x_alpha))
