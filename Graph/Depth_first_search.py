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
        
    def display(self):
        for i,j in enumerate(self.vertaces):
            print(f"{i}:{j}")
        
        for edge in self.adj_matrix:
            print(edge)
    
    def dfs(self, start_vertax = 0):
        dfs_result = []
        visited = [False] * self.numVertaces
        self.dfs_recursively(start_vertax, dfs_result, visited)
    
    def dfs_recursively(self, vertax, dfs_result, visited):
        print(vertax)
        dfs_result.append(vertax)
        visited[vertax] = True

        for neighbour in range(self.numVertaces):
            if vertax == neighbour:
                continue

            if self.adj_matrix[vertax][neighbour] == 1:
                if visited[neighbour] == False:
                    self.dfs_recursively(neighbour, dfs_result, visited)

graph = GraphUsingAdjacencyMatrix(5)
graph.add_vertax(0,'A')
graph.add_vertax(1,'B')
graph.add_vertax(2,'C')
graph.add_vertax(3,'D')
graph.add_vertax(4,'E')

graph.add_edges(0,1)
graph.add_edges(1,2)
graph.add_edges(2,3)
graph.add_edges(3,4)

graph.dfs()
