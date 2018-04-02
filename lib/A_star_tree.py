from heapq import heappop, heappush
from node import Node, SourceNode

class A_star_tree:
    """
    Implement A* algorithm for a special type of graph : trees. Thus, each node has one and
    only one predecessor. There is no need to check if a shorter path has been found
    for a node already discovered.

    Parameters:
        - cost_matrix : is a numpy arrray. C[i,j] where i are agents and j are jobs, is the
        affectation cost to link them.
        - heuristic : is a fonction which return a score
    """
    def __init__(self, cost_matrix, heuristic):
        self.cost_matrix = cost_matrix
        self.heuristic = heuristic
        self.open = [SourceNode()]
        self.agents_ids = set(range(cost_matrix.shape[0]))

    def push_successors_in_open(self, father_node):
        available_agents_ids = self.agents_ids - father_node.attributed_agents
        print(available_agents_ids)
        job_nbr = father_node.job +1
        for agent_id in available_agents_ids:
            cost = self.cost_matrix[job_nbr][agent_id]
            child_node = Node(
                job = job_nbr,
                agent = agent_id,
                heuristic = self.heuristic,
                predecessor = father_node,
                cost = int(cost),
            )
            heappush(self.open, child_node)
            print('--> '.join((str(el.f) for el in self.open)))

    def get_bests_affectations(self):
        """
        Return the less expensive affectations possible in this cost_matrix. To do so, we'll
        find the shortest path of the tree representing all the affectations possibles.
        """
        while self.open:
            best_node = heappop(self.open)
            if best_node.job == self.cost_matrix.shape[0]-1:
                return best_node.path
            self.push_successors_in_open(best_node)
        return None
