from A_star_tree import A_star_tree
from heuristic import all_heuristics
import numpy as np
import time

def get_random_matrix(dim, min_val=1, max_val=11):
    return np.array([[np.random.randint(min_val, max_val) for i in range(dim)] for j in range(dim)])

cost_matrix = get_random_matrix(5)
print(cost_matrix)

for fun in all_heuristics:
    tree = A_star_tree(cost_matrix, fun)
    start_time = time.time()
    path = tree.get_bests_affectations()
    end_time = time.time()
    print('\nCost : %s' %path[-1].g)
    print(' --> '.join((str(el) for el in path)))
    print(end_time - start_time)
    print(tree.visited)
