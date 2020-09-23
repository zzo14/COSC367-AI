from search import *
from math import *


class LocationGraph(ExplicitGraph):
    def __init__(self, nodes, locations, edges, starting_nodes, goal_nodes):
        self.nodes=nodes
        self.locations=locations
        self.edges=edges
        self.starting_nodes=starting_nodes
        self.goal_nodes=goal_nodes
        
    def cost_arc(self, points):
        point1, point2 = points
        point1_x = self.locations[point1][0]
        point1_y = self.locations[point1][1]
        point2_x = self.locations[point2][0]
        point2_y = self.locations[point2][1]  
        return sqrt((point2_x - point1_x)**2 + (point2_y - point1_y)**2)
        
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
    


graph = LocationGraph(nodes=set('ABC'),
                      locations={'A': (0, 0),
                                 'B': (3, 0),
                                 'C': (3, 4)},
                      edges={('A', 'B'), ('B','C'),
                             ('C', 'A')},
                      starting_nodes=['A'],
                      goal_nodes={'C'})


for arc in graph.outgoing_arcs('A'):
    print(arc)

for arc in graph.outgoing_arcs('B'):
    print(arc)

for arc in graph.outgoing_arcs('C'):
    print(arc)