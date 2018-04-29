from heapq import heappop, heappush
from node import Node, SourceNode

class A_star_tree:
    """
    Implement A* algorithm for a special type of graph : trees. Thus, each node has one and
    only one predecessor. There is no need to check if a shorter path has been found
    for a node already discovered because it is impossible.

    Attributes to give as parameters:
        - cost_matrix : is a numpy arrray. C[i,j] where i are agents and j are jobs, is the
        affectation cost to link them.
        - heuristic : is a fonction which return a score for a given node

    Attributes:
        - open : a list that we'll use as heap thanks to heappush, to keep the most interessant
        node to visit on the top. The fisrt node to be contained is obviously the SourceNode
        - agents : the list of available agents
        - visited : a value to keep track of the number of node A* will have to visit in order to
        find the shortest path
    """
    def __init__(self, cost_matrix, heuristic):
        self.cost_matrix = cost_matrix
        self.heuristic = heuristic
        self.open = [SourceNode()]
        self.agents = set(range(cost_matrix.shape[0]))
        self.visited = 0

    def set_heuristic(self, node):
        """
        Will score a node based on the class's heuristic and set it.

        Parameters:
            - node : the node to assign a score to
        """
        node.heuristic = self.heuristic(self, node)

    def push_successors_in_open(self, father_node):
        """
        Add all the father_node's successors in open (in a heap way).

        Parameters:
            - father_node : the node we want the successors added
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
        Return the less expensive affectations possible in this cost_matrix. To do so, we'll
        find the shortest path of the tree representing all the affectations possibles.
        """
        while self.open:
            self.visited += 1
            best_node = heappop(self.open)
            if best_node.job == self.cost_matrix.shape[0]-1:
                return best_node.path
            self.push_successors_in_open(best_node)
            # print(str(best_node.heuristic))
        return None
