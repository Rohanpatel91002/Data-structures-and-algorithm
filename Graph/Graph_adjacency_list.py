class GraphAdjacencyList:
    def __init__(self):
        self.vertaces = []
        self.adj_list = {}
    
    def add_vertax(self, vertax):
        if vertax not in self.vertaces:
            self.vertaces.append(vertax)
            self.adj_list[vertax] = []
        else:
            return "vertax already exists"
    
    def add_edges(self, source, destination, weight =1):
        if source in self.vertaces and destination in self.vertaces:
            self.adj_list[source].append((destination, weight))
            self.adj_list[destination].append((source, weight))
        else:
            return "source or destination does not exist"
    
    def display(self):
        for source, neighbour in self.adj_list.items():
            print(f"{source} : {neighbour}")

graph = GraphAdjacencyList()
graph.add_vertax(1)
graph.add_vertax(2)
graph.add_vertax(3)
graph.add_vertax(4)

graph.add_edges(1,2)
graph.add_edges(1,3)
graph.add_edges(2,3)

graph.display()
        