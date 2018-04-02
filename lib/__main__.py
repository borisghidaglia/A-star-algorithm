from A_star_tree import A_star_tree
from heuristic import null_heuristic
import numpy as np

def get_random_matrix(dim, min_val=1, max_val=11):
    return np.array([[np.random.randint(min_val, max_val) for i in range(dim)] for j in range(dim)])

cost_matrix = get_random_matrix(3)
print(cost_matrix)
tree = A_star_tree(cost_matrix, null_heuristic)
print(' --> '.join((str(el) for el in tree.get_bests_affectations())))
