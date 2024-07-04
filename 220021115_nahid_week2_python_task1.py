import sys
from heapq import heapify, heappop, heappush

class WGraph:
    def __init__(self,node):
        self.n=node
        self.adj = {}
        for i in self.n:
             self.adj[i] = {}

    def addEdge(self, a, b, w):    
        if a not in self.adj:
             self.adj[a] = {}
        if b not in self.adj:
             self.adj[b] = {}   	
        
        self.adj[a][b] = w
        self.adj[b][a] = w
    
    def shortest_distances(self, source: str):
       
       distances = {n: float("inf") for n in self.n}
       distances[source] = 0 
       pq = [(0, source)]
       heapify(pq)
       visited = set()
       while pq:  
           current_distance, current_node = heappop(pq)  
           if current_node in visited:
               continue  
           visited.add(current_node)
           for neighbor, weight in self.adj[current_node].items():
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    heappush(pq, (tentative_distance, neighbor))
       
       e=0
       for n, distance in distances.items():
            if e<distance:
                 e=distance

       predecessors = {no: None for no in self.n}

       for node, distance in distances.items():
            for neighbor, weight in self.adj[node].items():
                if distances[neighbor] == distance + weight:
                    predecessors[neighbor] = node

       return distances, e, predecessors
    
    def printadj(self):
        for i in self.n:
             print(i,":",self.adj[i])
    
    def shortest_path(self, source: str, target: str):
        _, _, predecessors = self.shortest_distances(source)
        
        path = []
        current_node = target

        while current_node:
            path.append(current_node)
            current_node = predecessors[current_node]

        path.reverse()
        return path


D = input(" vertice and edge: ").split()
v=int(D[0])
e=int(D[1])
b='0'
S=list(range(0,v))
for i in range(v):
     S[i]=chr(ord(b)+1)
     b=chr(ord(b)+1)
g=WGraph(S)

f=0
while f<e:
    E=input("node1, node2 and weight: ").split()
    
    F=E[0]
    D=E[1]
    V=int(E[2])
    g.addEdge(F,D,V)
    f+=1
g.printadj()
g.shortest_path('1','5')
       
        

