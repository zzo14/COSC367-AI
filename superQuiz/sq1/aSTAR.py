from search import *
import math
from heapq import *

#Q1
class RoutingGraph:
    def __init__(self, map_str):
        self.map_str = map_str
        self.graph = [list(item) for item in self.map_str.strip().split('\n')]
        self.agent = []
        self.goal_node = []
        
        for row in range(len(self.graph)):
            for column in range(len(self.graph[row])):
                node = self.graph[row][column]
                if node == 'S':
                    self.agent.append((row, column, math.inf))
                elif node.isdigit():
                    self.agent.append((row, column, int(node)))
                elif node == 'G':
                    self.goal_node.append((row, column))
                    
    def is_goal(self, node):
        return (node[0], node[1]) in self.goal_node

    def starting_nodes(self):
        return self.agent

    def outgoing_arcs(self, tail_node):
        directions = [('N' , -1, 0),
                     ('E' ,  0, 1),
                     ('S' ,  1, 0),
                     ('W' ,  0, -1)]
        environment = ['+', '-', '|', 'X']
        for direction in directions:
            row, column, fuel = tail_node[0] + direction[1], tail_node[1] + direction[2], tail_node[2]
            if self.graph[row][column] not in environment and fuel > 0:
                head_node = (row, column, fuel-1)
                yield Arc(tail_node, head_node, direction[0], 5)
        if self.graph[tail_node[0]][tail_node[1]] == 'F' and fuel < 9:
            head_node = (tail_node[0], tail_node[1], 9)
            yield Arc(tail_node, head_node, 'Fuel up', 15)            
            
    def estimated_cost_to_goal(self, node):
        return min([(abs(goal[0] - node[0]) + abs(goal[1] - node[1])) * 5 for goal in self.goal_node])

#Q2
class AStarFrontier(Frontier):
    def __init__(self, graph):
        self.graph = graph
        self.container = set()
        self.queue = []
        self.counter = 1
    
    def add(self, path):
        arc = path[-1]
        if arc.head not in self.container:
            costs = sum([item.cost for item in path])
            heappush(self.queue, (self.graph.estimated_cost_to_goal(arc.head) + costs, self.counter, path))
        self.counter += 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.queue:
            path = heappop(self.queue)[2]
            arc = path[-1]
            if arc.head not in self.container:
                self.container.add(arc.head)
                return path
        else:
            raise StopIteration   # don't change this one  
        
        
#Q3
def print_map(map_graph, frontier, solution):
    for row in range(len(map_graph.graph)):
        for column in range(len(map_graph.graph[row])):
            node = (row, column, math.inf)
            if map_graph.graph[row][column] in ['S', 'G']:
                is_goal = True
            else:
                is_goal = False
            
            if solution is not None and node in [arc.tail for arc in solution] and not is_goal:
                print('*', end='')
            elif node in frontier.container and not is_goal:
                print('.', end='')
            else:
                print(map_graph.graph[row][column], end='')
        print()
