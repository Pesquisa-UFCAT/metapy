import numpy as np

from mealpy import FloatVar, GWO, WOA

def objective_function(solution):
    return np.sum(solution**2)

problem_dict = {
    "bounds": FloatVar(lb=(-10.,) * 30, ub=(10.,) * 30, name="delta"),
    "minmax": "min",
    "obj_func": objective_function,
}

pop_size = 50

gwo = GWO.ExGWO(epoch=50, pop_size=pop_size)
gwo_best = gwo.solve(problem_dict)

final_pop = gwo.pop
starting = [sol.solution.copy() for sol in final_pop]
#print(starting)
#best_in_start = min(starting, key=lambda x: objective_function(x))
#print("Fitness best GWO:", gwo_best.target.fitness)
#print("Fitness best na objetiva:", objective_function(best_in_start))

woa_warm = WOA.OriginalWOA(epoch=50, pop_size=pop_size)
woa_warm_best = woa_warm.solve(problem_dict, starting_solutions=starting)

print("WOA final:", woa_warm_best.target.fitness)
