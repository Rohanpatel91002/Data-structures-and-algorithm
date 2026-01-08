class GraphUsingEdgeList:

    def __init__(self):
        self.vertax = []
        self.edges = []
    
    def add_vertax(self, value):
        if value not in self.vertax:
            self.vertax.append(value)
        else:
            return "Vertax already exists"
    
    def add_edges(self, source, destination, weight=1):
        if source in self.vertax and destination in self.vertax:
            edge = (source, destination, weight)
            self.edges.append(edge)
        
        else:
            return "source or destination does not exist"
    
    def display(self):
        for vertax in self.vertax:
            print(f"vertax - {vertax}")
        
        for source, destination, weight in self.edges:
            print(f"{source} ------> {destination}")

graph = GraphUsingEdgeList()
graph.add_vertax(1)
graph.add_vertax(2)
graph.add_vertax(3)
graph.add_vertax(4)

graph.add_edges(1,2)
graph.add_edges(2,3)

graph.display()