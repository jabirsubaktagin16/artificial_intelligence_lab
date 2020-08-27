inf = 99999
from queue import PriorityQueue

graph = [[(2, 22), (3, 32), (8, 35)], 
        [(3, 28),(4, 36), (5, 27), (8, 45)], 
        [(0, 22), (3, 31), (6, 47)], 
        [(0, 32), (2, 31), (1, 28), (6, 30)], 
        [(1, 36), (6, 26)], 
        [(1, 27)], 
        [(2, 47), (3, 30), (4, 26)], 
        [], 
        [(0, 35), (1, 45)]]
 
heuristics_ = [55, 42, 34, 25, 20, 17, 0, inf, 80]

Q = PriorityQueue()

def empty():
    return Q.empty()
def push(value):
    Q.put(value)
def pop():
    if (empty()):
        return None
    return Q.get()

def execute_gbfs():
    source=8 #i
    goal=6 #g
    parent = [-1] * len(graph)
    visited = [False] * len(graph)

    push((heuristics_[source], source))
    visited[source]=True
    while(empty()==False):
        x=pop()
        if(x[1]==goal):
            break
        for adj in graph[x[1]]:
            v = adj[0]
            if(visited[v]==False):
                push((heuristics_[v],v))
                visited[v]=True
                parent[v]=x[1]
    
    temp = goal
    cost = 0
    print("Possible Path: ", end=' ')
    while (parent[temp]!=-1):
        x = parent[temp]
        v = temp
        print(chr(ord('a')+temp), end=' ')
        for adj in graph[x]:
            if(adj[0]==v):
                cost+=adj[1]
                break
        temp = parent[temp]
    print(chr(ord('a')+temp))
    print("Total Cost = ", cost)

execute_gbfs()
