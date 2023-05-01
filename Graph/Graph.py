class Graph:
    def __init__(self):
        self.dict = {}

    def add(self, data):
        self.dict.update({data: []})

    def insert(self, vertex, edge, isBidirectional,weight = 1):
        if vertex not in self.dict:
            self.add(vertex)
        if edge not in self.dict:
            self.add(edge)
        self.dict.get(vertex).append((edge,weight))
        if isBidirectional:
            self.dict.get(edge).append((vertex,weight))

    def display(self):
        for key in self.dict:
            print(key, ":", end=" ")
            for value in self.dict[key]:
                print(value, end=" ")
            print()
    def bfs(self,vertex):
        visited=[vertex]
        queue=[vertex]
        while queue:
            deQueue = queue.pop(0)
            print(deQueue)
            for adjacent in self.dict[deQueue]:
                if adjacent[0] not in visited:
                    visited.append(adjacent[0])
                    queue.append(adjacent[0])
    def dfs(self,vertex):
        visited=[vertex]
        stack=[vertex]
        while stack:
            pop = stack.pop()
            print(pop)
            for adjacent in self.dict[pop]:
                if adjacent[0] not in visited:
                    visited.append(adjacent[0])
                    stack.append(adjacent[0])
                    
    def toplogicalSort(self):
        visited=[]
        stack=[]
        for k in list(self.dict):
            if k not in visited:
                self.toplogicalSortHelper(k,visited,stack)
        print(stack)
    def toplogicalSortHelper(self,v,visited,stack):
        visited.append(v)
        for i in self.dict[v]:
            if i[0] not in visited:
                self.toplogicalSortHelper(i[0],visited,stack)
        stack.insert(0,v)
        
    def shortestPath(self,start,end):
        queue = []
        queue.append([start])
        print(queue)
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node==end:
                return path
            for adjacent in self.dict.get(node,[]):
                new_path = list(path)
                new_path.append(adjacent[0])
                queue.append(new_path)
    def dijkstra(self, start, end):
        distance = {vertex: float("inf") for vertex in self.dict}
        distance[start] = 0
        predecessors = {vertex: None for vertex in self.dict}
        unvisited = set(self.dict)
        dist=0
        while unvisited:
            current = min(unvisited, key=lambda vertex: distance[vertex])
            if current == end:
                path = []
                while current is not None:
                    path.insert(0, current)
                    current = predecessors[current]
                return path,dist
            unvisited.remove(current)
            for adjacent, weight in self.dict[current]:
                if adjacent in unvisited:
                    new_distance = distance[current] + weight
                    if new_distance < distance[adjacent]:
                        dist = new_distance
                        distance[adjacent] = new_distance
                        predecessors[adjacent] = current
        return []

graph = Graph()
graph.insert(3, 5, True,10)
graph.insert(3, 4, True,5)
graph.insert(4, 4, True,8)
graph.insert(5, 6, False,15)
graph.insert(5, 88, False,15)
graph.insert(88, 3455, False,15)
graph.insert(3455, 6, False,15)
graph.display()
graph.bfs(3)
graph.toplogicalSort()
print("SHORTEST")
print(graph.shortestPath(3,6))
print(graph.dijkstra(3,3455))