from collections import deque
class GraphUsingAdjacencyMatrix:

    def __init__(self, numVertaces):
        self.numVertaces = numVertaces
        self.vertaces = [None] * numVertaces
        self.adj_matrix = [[0] * numVertaces for _ in range(numVertaces)] 
    
    def add_vertax(self,index, lable):
        if index>=0 and index< self.numVertaces:
            self.vertaces[index] = lable
        
        else:
            return "index OOB"

    def add_edges(self, source, destination, weight = 1):
        # if source in self.vertaces and destination in self.vertaces:
        if 0<=source < self.numVertaces and 0<=destination < self.numVertaces:
            self.adj_matrix[source][destination] = weight
            self.adj_matrix[destination][source] = weight
        else:
            return "source or destination does not exist"
        
    def bfs(self, start_vertax = 0):
        visited = [False] * self.numVertaces
        queue = deque([start_vertax])
        bfs_result = []
        visited[start_vertax] = True
        while queue:
            vertax = queue.popleft()
            print(vertax)
            bfs_result.append(vertax)
            for neighbour in range(self.numVertaces):
                if self.adj_matrix[vertax][neighbour] != 0:
                    if visited[neighbour] == False:
                        queue.append(neighbour)
                        visited[neighbour] = True

graph = GraphUsingAdjacencyMatrix(5)
graph.add_vertax(0,'A')
graph.add_vertax(1,'B')
graph.add_vertax(2,'C')
graph.add_vertax(3,'D')
graph.add_vertax(4,'E')

graph.add_edges(0,1)
graph.add_edges(0,2)
graph.add_edges(0,3)
graph.add_edges(3,4)

graph.bfs()

