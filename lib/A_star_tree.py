from heapq import heappop, heappush
from node import Node, SourceNode
from math import factorial

class A_star_tree:
    """
    Implementation of A* algorithm for a special type of graph : trees. Thus, each node has one and
    only one predecessor. There is no need to check if a shorter path has been found
    for a node already visited because it is impossible to find one.

    Attributes to give as parameters:
        - cost_matrix : is a numpy arrray. C[i,j] where i are agents and j are jobs, is the
        affectation cost to link them.
        - heuristic : is a fonction which returns a score for a given node

    Attributes:
        - open : a list that will act as heap thanks to heapq module, to keep the most interesting
        node to visit at the top. The first node to be contained is obviously the SourceNode
        - agents : a list containing all available agents
        - visited : int value to keep track of the number of nodes visited thus far
    """
    def __init__(self, cost_matrix, heuristic):
        self.cost_matrix = cost_matrix
        self.heuristic = heuristic
        self.open = [SourceNode()]
        self.agents = set(range(cost_matrix.shape[0]))
        self.visited = 0

    def set_heuristic(self, node):
        """
        Sets node's heuristic value based on the class's heuristic function and the node itself.

        Parameters:
            - node : the node to assign a score to
        """
        node.heuristic = self.heuristic(self, node)

    def push_successors_in_open(self, father_node):
        """
        Adds all the father_node's successors in open, maintaining coherent heap structure.

        Parameters:
            - father_node : the node from which the successors will be added to open
        """
        available_agents = self.agents - father_node.attributed_agents
        # print(available_agents)
        job_nbr = father_node.job +1
        for agent in available_agents:
            cost = self.cost_matrix[job_nbr][agent]
            child_node = Node(
                job = job_nbr,
                agent = agent,
                predecessor = father_node,
                cost = int(cost),
            )
            self.set_heuristic(child_node)
            heappush(self.open, child_node)
            # print('--> '.join((str(el.f) for el in self.open)))

    def get_bests_affectations(self):
        """
        Returns the best affectations possible of the cost_matrix. To do so, we'll
        find the least expensive path from the initial node to one of the terminal nodes.
        """
        while self.open:
            self.visited += 1
            best_node = heappop(self.open)
            if best_node.job == self.cost_matrix.shape[0]-1:
                return best_node.path
            self.push_successors_in_open(best_node)
            # print(str(best_node.heuristic))
        return None

    def GRP_size(self):
        """Returns the total number of nodes in the GRP"""
        value = 0
        for i in range(self.cost_matrix.shape[0]):
            value+= factorial(i+1)
        return value
