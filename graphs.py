class Vertex:
    def __init__(self, name):
        self.name = self.name

class WeightedVertex(Vertex):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

class Edge:
    def __init__(self, src_vert: Vertex, dst_vert: Vertex, directed: bool=False):
        self.src = src_vert
        self.dst = dst_vert
        self.directed = directed

    def __eq__(self, other):
        assert other.__class__.__name__ == self.__class__.__name__
        if self.directed:
            return self.src == other.src and self.dst == other.dst
        else:
            return self.src == other.src and self.dst == other.dst or self.src == other.dst and self.dst == other.src

    def follow(self, src_vertex):
        if self.directed:
            assert self.src == src_vertex
            return self.dst
        else:
            assert self.src == src_vertex or self.dst == src_vertex
            if src_vertex == self.src:
                return self.dst
            else:
                return self.src

class Graph:
    def __init__(self, vertices: list[Vertex], edges: list[Edge]):
        self.verts = vertices
        self.edges = edges
