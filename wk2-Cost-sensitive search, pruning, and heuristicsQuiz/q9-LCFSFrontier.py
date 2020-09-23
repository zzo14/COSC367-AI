from search import *
import math
   
class Arc(namedtuple('Arc', 'tail, head, action, cost')):
    """Represents an arc in a graph.

    Keyword arguments:
    tail -- the source node (state)
    head -- the target node (state)
    action -- a string describing the action that must be taken in
             order to get from the source state to the destination state.
    cost -- a number that specifies the cost of the action
    """

class LocationGraph:
    def __init__(self, nodes, locations, edges, starting_nodes, goal_nodes):
        self.nodes = nodes
        self.locations = locations
        self.edges = edges
        self.start = starting_nodes
        self.goal = goal_nodes
        
    def cost_arc(self, points):
        point1, point2 = points
        point1_x = self.locations[point1][0]
        point1_y = self.locations[point1][1]
        point2_x = self.locations[point2][0]
        point2_y = self.locations[point2][1]  
        return math.sqrt((point2_x - point1_x)**2 + (point2_y - point1_y)**2)
    
    def starting_nodes(self):
        """Returns a sequence of starting nodes."""
        return self.start

    def is_goal(self, node):
        """Returns true if the given node is a goal node."""
        return node in self.goal    
        
    def outgoing_arcs(self, node):
        arcs = []
        for edge in self.edges:
            if len(edge) == 2:  # if no cost is specified
                tail, head = edge
                cost = self.cost_arc(edge)        # assume unit cost
            else:
                tail, head, cost = edge
            if tail == node:
                new = Arc(tail, head, str(tail) + '->' + str(head), cost)
                if new not in arcs:
                    arcs.append(new)
            if head == node:
                new = Arc(head, tail, str(head) + '->' + str(tail), cost)
                if new not in arcs:
                    arcs.append(new)                
        return sorted(arcs)


class LCFSFrontier(Frontier):
    def __init__(self):
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        return self

    
    def __next__(self):
        if len(self.container) > 0:
            if len(self.container) == 1:
                return self.container.pop(0)
            else:
                self.container.sort(key=lambda x: sum(i.cost for i in x))
                return self.container.pop(0)
        else:
            raise StopIteration   # don't change this one  