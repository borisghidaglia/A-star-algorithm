from A_star_tree import A_star_tree
from heuristic import null_heuristic, sum_min_in_lines
import numpy as np
import time

def get_random_matrix(dim, min_val=1, max_val=1001):
    return np.array([[np.random.randint(min_val, max_val) for i in range(dim)] for j in range(dim)])

cost_matrix = get_random_matrix(12)

for fun in (null_heuristic, sum_min_in_lines):
    tree = A_star_tree(cost_matrix, fun)
    start_time = time.time()
    print(' --> '.join((str(el) for el in tree.get_bests_affectations())))
    print(time.time() - start_time)
    print(tree.visited)
    print(cost_matrix)
