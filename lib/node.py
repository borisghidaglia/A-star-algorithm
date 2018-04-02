import functools

from utils import cached_property

# All other comparison functions are derived from __eq__ and __lt__
# thanks to @functools.total_ordering class decorator
@functools.total_ordering
class Node:
    """Node objects allow for simpler data structuring and
        easier comparison between one another.


    N.B. The 'decorator' (e.g. @cached_property) is native to python.

        @cached_property allows the function to behave just like an attribute,
        it is accesible from <node obj>.func

        The function is computed once and the result stored for later calls.


        @functools.total_ordering creates all six comparison methods from two only
    """
    def __init__(self, job, agent, heuristic, predecessor, cost= float('inf')):
        """
        N.B. heuristic param must be a function
        """
        self.job= job #int
        self.agent= agent #int
        self.heuristic= property(heuristic)
        self.predecessor= predecessor #Node type
        self.cost= cost #int, cost of path from predecessor to self

    def __str__(self):
        return 'C[%s,%s]' %(self.agent,self.job)


    @cached_property
    def path(self):
        """Concatenation of all nodes from source to self

        return type: list
        """
        return self.predecessor.path+[self]


    @cached_property
    def g(self):
        """A* g fucntion, represents the cost from source to self.

        return type: int
        """
        return self.predecessor.g + self.cost

    @cached_property
    def f(self):
        """A* f function, which is the simple sum of g and h

        return type: int
        """
        return self.g + self.heuristic.__get__(self, type(self))

    @cached_property
    def attributed_agents(self):
        """Concatenation of predecessor's attributed agents and own agent

        return type: set
        """
        return self.predecessor.attributed_agents | {self.agent}

    def __eq__(self, other): #equal
        return self.f==other.f

    def __lt__(self, other): #less than
        return self.f < other.f


class SourceNode(Node):
    """
    This class enables the creation of a simple Source node
        with no attributes to take care of.

    The cached_property functions inherited from Node class
        are overridden by respective attributes in __init__
    """
    def __init__(self):
        self.job=-1
        self.agent=-1
        self.predecessor= None
        self.attributed_agents = set()
        self.path= []
        self.g= 0
        self.f= float('inf')
