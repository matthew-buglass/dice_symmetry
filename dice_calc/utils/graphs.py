import functools

@functools.total_ordering
class Vertex:
    def __init__(self, index, name):
        """
        A vertex
        :param index: the index of the vertex in the vertex list
        :param name: a unique identifier of the vertex such that it imposes a total ordering.
                        (ie. a vertex with a name 1 is less than a vertex with the name 2)
        """
        self.index = index
        self.name = name

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        assert other.__class__.__name__ == self.__class__.__name__, "Comparison between {} and {} not supported".format(
            other.__class__.__name__,
            self.__class__.__name__
        )
        return self.name == other.name

    def __lt__(self, other):
        assert other.__class__.__name__ == self.__class__.__name__, "Comparison between {} and {} not supported".format(
            other.__class__.__name__,
            self.__class__.__name__
        )
        return self.name < other.name

    def __key__(self):
        return self.name

    def __hash__(self):
        return hash(self.__key__())


class WeightedVertex(Vertex):
    def __init__(self, index, name, weight):
        super().__init__(index, name)
        self.weight = weight

    def __str__(self):
        return "{}|{}".format(self.name, self.weight)

    def __key__(self):
        return self.name, self.weight

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

    def __repr__(self):
        return str(self)

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
        other_rev = other.verts.copy()
        other_rev.reverse()
        return self.verts == other.verts or self.verts == other_rev

    def append(self, other):
        self.verts.append(other)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        """
        Because This is an undirected path, it can be traversed from front-to-back or back-to-front. So the unique
        representation will be the lexicographically first path.
        :return:
        """
        options = [self.verts, self.verts.copy()]
        options[1].reverse()
        options.sort()

        return str(options[0])

    def can_be_cycle(self) -> bool:
        """
        Evaluates whether a path can be a cycle

        :return: A boolean of whether it can be a cycle
        """
        return self.verts[0] == self.verts[-1]

    def can_be_simple_cycle(self) -> bool:
        """
        Evaluates whether a path can be a simple cycle

        :return: A boolean of whether it can be a simple cycle
        """
        # If we can be a cycle and the only repeated vertex is the first and last
        return self.can_be_cycle() and len(set(self.verts)) == len(self.verts) - 1

    def get_cycle(self):
        """
        Creates an undirected cycle representation of the path
        :throws: a Value Error if the path cannot be converted to a cycle
        :return: and UndirectedCycle
        """
        if self.can_be_cycle():
            return UndirectedCycle(self.verts[0: len(self.verts) - 1])
        else:
            raise ValueError("Path cannot be converted to a cycle")

    def pop(self):
        """
        Pops the last vertex in the path

        :return: None
        """
        self.verts.pop()

    def deep_copy(self):
        return UndirectedPath(self.verts.copy())

    def __len__(self):
        return len(self.verts)

    def __getitem__(self, *args, **kwargs):
        return self.verts.__getitem__(*args, **kwargs)

    def __key__(self):
        return self.__repr__()

    def __hash__(self):
        return hash(self.__key__())


class UndirectedCycle(UndirectedPath):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.circ_perms = self.__calc_circ_perms__()

    def append(self, other):
        super().append(other)
        self.circ_perms = self.__calc_circ_perms__()

    def __calc_circ_perms__(self):
        """
        Construct a list of a circular permutations and reversed circular permutations and reverse circular permutations
        of the path
        :return: a list of circular permutations of the path's vertices
        """
        double_perm = self.verts.copy() + self.verts.copy()
        len_perm = len(double_perm)
        circ_perms = []

        for i in range(len(self)):
            # Forward permutation
            circ_perms.append(double_perm[i:i + len(self)])
            # Backwards permutation
            circ_perms.append(double_perm[len_perm-i-1:len_perm-i-len(self)-1:-1])

        circ_perms.sort()

        return circ_perms

    def __repr__(self):
        """
        Because this is an undirected cycle, any circular permutation of the vertices in the path or a circular
        permutation of the reverse of the path is the same path. Therefore, I define the representation as the
        lexicographically first circular permutation as the unique representation of the path.
        :return:
        """
        return str(self.circ_perms[0])

    def __eq__(self, other):
        return other.verts in self.circ_perms

    def __key__(self):
        return self.__repr__()

    def __hash__(self):
        return hash(self.__key__())

class Graph:
    def __init__(self, vertices: list[Vertex], edges: list[Edge]):
        self.verts = vertices
        self.edges = edges
