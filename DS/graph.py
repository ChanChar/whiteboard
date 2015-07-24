class Vertex:
    def __init__(self, value):
        self.value = value
        self.in_edges = []
        self.out_edges = []

class Edge:
    def __init__(self, from_vertex, to_vertex, cost=1):
        self.from_vertex = from_vertex
        self.to_vertex = from_vertex
        self.cost = cost

        self.to_vertex.in_edges.append(self)
        self.from_vertex.out_edges.append(self)

    def destroy:
        self.to_vertex.out_edges.remove(self)
        self.to_vertex = None
        self.from_vertex.in_edges.remove(self)
        self.from_vertex = None
