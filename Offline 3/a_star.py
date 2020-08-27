import heapq
from collections import defaultdict

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def insert(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def remove(self):
        return heapq.heappop(self._queue)[-1]

    def isEmpty(self):
        return len(self._queue) == 0

    def getSize(self):
        return self._index

class Node:
    def __init__(self, key, forward_cost):
        self.key = key
        self.forward_cost = forward_cost

    def getKey(self):
        return self.key

    def getForwardCost(self):
        return self.forward_cost

class Graph:

    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.path = []

        self.successors = defaultdict(list)

    def addEdge(self, source, destination, weight):
        edge = (source, destination, weight)
        if not self.existsEdge(edge):
            self.nodes[source], self.nodes[destination] = source, destination 
            self.edges.append(edge)
            self.successors[source.getKey()].append((destination, weight)) 
        else:
            print('Error: edge (%s -> %s with weight %s) already exists!!' \
                % (edge[0].getKey(), edge[1].getKey(), edge[2]))

    def existsEdge(self, edge):
        for e in self.edges:
            if e[0].getKey() == edge[0].getKey() and \
                e[1].getKey() == edge[1].getKey() and e[2] == edge[2]:
                return True
        return False

    def getPath(self):
        return self.path

    def executeAStar(self, initial_node, goal_node):
        if not self.edges:
            print('Error: graph not contains edges!!')
        else:
            if initial_node in self.nodes and goal_node in self.nodes:
                if initial_node == goal_node:
                    return 0

                queue = PriorityQueue() 

                distance_vector, antecessors = {}, {}
                for node in self.nodes:
                    distance_vector[node.getKey()] = None
                    antecessors[node.getKey()] = None
                distance_vector[initial_node.getKey()] = 0

                g_cost, h_cost = 0, initial_node.getForwardCost()
                f_cost = g_cost + h_cost
                queue.insert((initial_node, g_cost, h_cost), f_cost)
                total_cost = None

                while True:
                    current_node, g_cost, h_cost = queue.remove()
                    successors = self.successors[current_node.getKey()]
                    for successor in successors:
                        destination, weight = successor 
                        new_g_cost = g_cost + weight
                        h_cost = destination.getForwardCost()
                        f_cost = new_g_cost + h_cost
                        queue.insert((destination, new_g_cost, h_cost), f_cost)

                        if distance_vector[destination.getKey()]:
                            if distance_vector[destination.getKey()] > new_g_cost:
                                distance_vector[destination.getKey()] = new_g_cost
                                antecessors[destination.getKey()] = current_node.getKey()
                        else:
                            distance_vector[destination.getKey()] = new_g_cost
                            antecessors[destination.getKey()] = current_node.getKey()

                        if destination.getKey() == goal_node.getKey():
                            if not total_cost:
                                total_cost = f_cost
                            elif f_cost < total_cost:
                                total_cost = f_cost

                    if queue.isEmpty():
                        curr_node = goal_node.getKey()
                        while curr_node:
                            self.path.append(curr_node)
                            curr_node = antecessors[curr_node]
                        self.path = self.path[::-1]
                        return total_cost
            else:
                print('Error: the node(s) not exists in the graph!!')

nodeI = Node('i', 80)
nodeA = Node('a', 55)
nodeB = Node('b', 42)
nodeC = Node('c', 34)
nodeD = Node('d', 25)
nodeE = Node('e', 20)
nodeF = Node('f', 17)
nodeG = Node('g', 0)

graph = Graph()

graph.addEdge(nodeI,nodeA,35)
graph.addEdge(nodeI,nodeB,45) 
graph.addEdge(nodeA,nodeC,22)
graph.addEdge(nodeA,nodeD,32)
graph.addEdge(nodeB,nodeD,28)
graph.addEdge(nodeB,nodeE,36)
graph.addEdge(nodeB,nodeF,27)
graph.addEdge(nodeC,nodeD,31)
graph.addEdge(nodeC,nodeG,47)
graph.addEdge(nodeD,nodeG,30)
graph.addEdge(nodeE,nodeG,26)

total_cost = graph.executeAStar(nodeI, nodeG)
path = graph.getPath()
if total_cost:
    print('Total Cost: %s. \nPossible Path: %s' % (total_cost, ' '.join(path)))
else:
    print('Did not reach the goal!')