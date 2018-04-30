from A_star_tree import A_star_tree
from heuristic import all_heuristics
from test_matrices import matrices
import numpy as np
import time

def get_random_matrix(dim, min_val=1, max_val=11):
    """Returns numpy array of dimension dim, of randoms values between min_val and max_val"""
    return np.array([[np.random.randint(min_val, max_val) for i in range(dim)] for j in range(dim)])

def print_array(a):
    """Prints numpy array passed as parameter"""
    print('[')
    for i in range(a.shape[0]):
        print('\t[%s],' %','.join(str(el) for el in a[i]))
    print(']')

def main():
    for cost_matrix in matrices:
        print()
        print(cost_matrix)

        for fun in all_heuristics:
            tree = A_star_tree(cost_matrix, fun)
            start_time = time.time()
            path = tree.get_bests_affectations()
            end_time = time.time()
            print()
            print('Heuristic : %s' %fun.__name__)
            print('Path : %s' %' --> '.join((str(el) for el in path)))
            print('Cost : %s' %path[-1].g)
            print('Number of visited nodes : %s' %tree.visited)
            print('GRP size : %s' %tree.GRP_size())
            print('Ratio : %s' %(tree.visited/tree.GRP_size()))
            print('Time : %s' %str(end_time - start_time))
            print()

if __name__=='__main__':
    main()
