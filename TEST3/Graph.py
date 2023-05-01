class Graph:
    def __init__(self):
        self.graph={}
    
    def add(self,data):
        self.graph.update({data:[]})
        
    def insert(self,vertex,edge,isBidirectional,weight=1):
        if vertex not in self.graph:
            self.add(vertex)
        if edge not in self.graph:
            self.add(edge)
        self.graph.get(vertex).append((edge,weight))
        if isBidirectional:
            self.graph.get(edge).append((vertex,weight))
            
    def display(self):
        for x in self.graph:
            print(x,":",end=" ")
            for y in self.graph[x]:
                print(y,end=' ')
            print()
    def bfs(self,vertex):
        visited = [vertex]
        queue=[vertex]
        while queue:
            dequeue = queue.pop(0)
            print(dequeue)
            for adjacent in self.graph[dequeue]:
                if adjacent[0] not in visited:
                    visited.append(adjacent[0])
                    queue.append(adjacent[0])
    def dfs(self,vertex):
        visited = [vertex]
        stack=[vertex]
        while stack:
            pop = stack.pop()
            print(pop)
            for adjacent in self.graph[pop]:
                if adjacent[0] not in visited:
                    visited.append(adjacent[0])
                    stack.append(adjacent[0])
                    
    def shortestPath(self,start,end):
        if start not in self.graph or end not in self.graph:
            return None
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node==end:
                return path
            for adjacent in self.graph.get(node,[]):
                new_path = list(path)
                new_path.append(adjacent[0]) 
                queue.append(new_path)
    
    def dijkstra(self,start,end):
        if start not in self.graph or end not in self.graph:
            return None
        distance = {vertex:float("inf") for vertex in self.graph }
        distance[start]=0
        route = {vertex:None for vertex in self.graph}
        unvisited =set(self.graph)
        dist = 0
        while unvisited:
            current = min(unvisited,key=lambda vertex:distance[vertex])
            if current == end:
                path = []
                while current is not None:
                    path.insert(0,current)
                    current = route[current]
                return path,dist
            unvisited.remove(current)
            for adjacent,weight in self.graph[current]:
                if adjacent in unvisited:
                    new_distance = distance[current]+weight
                    if new_distance < distance[adjacent]:
                        dist = new_distance
                        distance[adjacent]=new_distance
                        route[adjacent]=current
    def remove(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for key in self.graph:
                self.graph[key]=[(v,w) for v,w in self.graph[key] if v!=vertex]
            
        
graph = Graph()
graph.insert(3, 5, True,10)
graph.insert(3, 4, True,5)
graph.insert(4, 4, True,8)
graph.insert(5, 6, False,95)
graph.insert(6, 3, False,15)
graph.insert(5, 88, False,15)
graph.insert(88, 3455, False,15)
graph.insert(3455, 6, False,15)
graph.display()
graph.bfs(3)
print("DFS")
graph.dfs(3)
print(graph.shortestPath(3,3455))
graph.remove(3)
graph.display()
print(graph.dijkstra(3,3455))



def dijkstra(self,start,end):
    distance = {vertex:float("inf") for vertex in self.graph}
    distance[start]=0
    route = {vertex:None for vertex in self.graph}
    unvisit = set(self.graph)
    dist = 0
    while unvisit:
        current = min(unvisit,key=lambda vertex:distance[vertex])
        if current == end:
            
            path = []
            while current is not None:
                path.insert(0,current)
                current = route[current]
            return path , dist
        unvisit.remove(current)
        for adjacent,weight in self.graph[current]:
            if adjacent in unvisit:
                new_path = distance[current]+weight
            if new_path<distance[adjacent]:
                dist = new_path
                distance[adjacent]=new_path
                route[adjacent]=current