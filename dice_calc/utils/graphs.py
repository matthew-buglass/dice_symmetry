class Vertex:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        assert other.__class__.__name__ == self.__class__.__name__
        return other.name == self.name

class WeightedVertex(Vertex):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def __str__(self):
        return "{}|{}".format(self.name, self.weight)

    def __key__(self):
        return self.name, self.weight
    def __hash__(self):
        return hash(self.__key__())

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

    def __str__(self):
        if self.directed:
            return "{}->{}".format(self.src, self.dst)
        else:
            return "{}--{}".format(self.src, self.dst)

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

class UndirectedPath:
    def __init__(self, verts=[]):
        self.verts = verts

    def __eq__(self, other):
        other_set = set(other.verts)
        self_set = set(self.verts)
        return len(self_set.difference(other_set)) == 0

    def append(self, other):
        self.verts.append(other)

    def __str__(self):
        return str([str(v) for v in self.verts])

    def copy(self):
        return UndirectedPath(self.verts.copy())

    def __len__(self):
        return len(self.verts)

    def __getitem__(self, *args, **kwargs):
        return self.verts.__getitem__(*args, **kwargs)

class Graph:
    def __init__(self, vertices: list[Vertex], edges: list[Edge]):
        self.verts = vertices
        self.edges = edges
