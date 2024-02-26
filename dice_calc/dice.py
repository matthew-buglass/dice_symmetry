import datetime
import numpy as np

from utils.decorators import timed
from utils.generators import face_weights_locked_one
from utils.graphs import Edge, WeightedVertex, UndirectedPath, UndirectedCycle


class Die:
    cycles: list[UndirectedCycle]
    edges: list[Edge]
    verts: list[WeightedVertex]
    sides: int

    def __init__(self, num_faces: int, adjacent_faces: [tuple[int, int]],
                 num_faces_on_vertices: int, opposing_faces: list[tuple[int, int]]):
        """
        An abstract undirected graph representation of a die. Vertices in the graph represent faces on a die, and the vertex
        weights are the face values of the die. A simple cycle of a given number of vertices represents the point, or
        vertex, on the face of the die. In this way, we can calculate facial and vertex similarities of dice.

        Inside the class we refer to the graphical representation, but outside the graph we refer to components
        as the die components.

        :param num_faces: the number of faces on the die. this will be the number of vertices in the graph.
        :param adjacent_faces: an edge list of faces of the die that are adjacent to each other. A list of tuples
            containing the vertex indices of the start and end vertices of an edge.
        :param num_faces_on_vertices: simple cycles in the graph that represent the meeting of a certain number of faces. In
            perfectly fair dice (D4, D6, D8, D12, D20) this will always be the same number of faces (3, 3, 4, 3, 5) within
            the die. For unfair dice (D10, D30, etc.) this may differ in the die (3 and 5, 3 and 5), which is why this
            is a list.
        """
        self.verts = [WeightedVertex(index=i, name=i + 1, weight=0) for i in range(num_faces)]
        self.edges = [Edge(self.verts[e[0] - 1], self.verts[e[1] - 1]) for e in adjacent_faces]
        self.opposing_faces = opposing_faces
        self.edge_dict = self.__get_edge_dict__()

        self.cycles = self.__find_simple_cycles__(num_faces_on_vertices)

    def __get_edge_dict__(self) -> dict[WeightedVertex, set[WeightedVertex]]:
        edge_dict = {}
        for edge in self.edges:
            assert not edge.directed
            try:
                edge_dict[edge.src].add(edge.dst)
            except KeyError:
                edge_dict[edge.src] = set()
                edge_dict[edge.src].add(edge.dst)

            try:
                edge_dict[edge.dst].add(edge.src)
            except KeyError:
                edge_dict[edge.dst] = set()
                edge_dict[edge.dst].add(edge.src)

        return edge_dict

    def __find_simple_cycles__(self, cycle_len: int) -> list[UndirectedCycle]:
        """
        Finds all unique, undirected, simple cycles of a specific length in an edge_list.
        :param edges: The undirected edge list of the graph
        :param cycle_lens: The number of unique vertices in the cycles. The first vertex counts as the first and last.
        :return: A list of unique simple cycles in the graph. The closing edge goes from the last to the first vertex
        """

        def cycle_helper(all_cycles: set, curr_path: UndirectedPath, cycle_len: int):
            if len(curr_path) == cycle_len + 1:
                if curr_path.can_be_simple_cycle():
                    all_cycles.add(curr_path.get_cycle())
            elif len(curr_path) < cycle_len + 1:
                for v in self.edge_dict[curr_path[-1]]:
                    curr_path.append(v)
                    cycle_helper(all_cycles, curr_path, cycle_len)
                    curr_path.pop()
            # Prevent infinite recursion
            else:
                raise ValueError("Somehow the path is longer than it should be allowed")

        all_cycles = set()
        for e in self.edges:
            cycle_helper(all_cycles, UndirectedPath(verts=[e.src, e.dst]), cycle_len)

        return list(all_cycles)

    def __get_vertex_weights__(self) -> list[float]:
        """
        Calculates the weights of each of the die's vertices
        :return: a list of floats of average weights of the die's vertices
        """
        vert_weights = []
        for cycle in self.cycles:
            weight = sum([w.weight for w in cycle]) / len(cycle)
            vert_weights.append(weight)
        return vert_weights

    def __assign_weights__(self, weights: list[float]):
        """
        Assigns the provided weights to the vertices in order. There must be the same number of weights as there are
        die faces
        :param weights: the weights to assign to faces
        :return: None
        """
        assert len(weights) == len(self.verts)
        for i, w in enumerate(weights):
            self.verts[i].weight = w

    @timed
    def calc_optimum_face_weights_locked_opposing_faces(self):
        """
        Finds the weight (face number) positioning that minimizes the standard deviation of die vertex weights, keeping
        facial symmetry (average of opposing faces is identical) a requirement.
        :return: a string representation of face ids and the weights attributed.
        """
        optimal_weights = [0] * len(self.verts)
        optimal_weights_sd = 99999999999999

        for weights in face_weights_locked_one(num_faces=len(self.verts), opp_faces=self.opposing_faces):
            self.__assign_weights__(weights=weights)
            sd = np.std(self.__get_vertex_weights__())
            if sd < optimal_weights_sd:
                optimal_weights = weights
                optimal_weights_sd = sd

        # apply and return the best weights
        self.__assign_weights__(optimal_weights)
        return optimal_weights_sd

    def faces_to_string(self):
        return str([str(v) for v in self.verts])

    def vertices_to_string(self):
        return "\n\t\t".join([str(c) for c in self.cycles])

    def add_cycles(self, cycles: list[UndirectedCycle]):
        self.cycles.extend(cycles)

    def num_faces(self):
        return len(self.verts)


if __name__ == '__main__':
    d4 = Die(
        num_faces=4,
        adjacent_faces=[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)],
        num_faces_on_vertices=3,
        opposing_faces=[(1, 3), (2, 4)]
    )

    d6 = Die(
        num_faces=6,
        adjacent_faces=[(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 6), (3, 5), (3, 6), (4, 5), (5, 6)],
        num_faces_on_vertices=3,
        opposing_faces=[(1, 6), (2, 5), (3, 4)]
    )

    d8 = Die(
        num_faces=8,
        adjacent_faces=[
            (1, 2), (2, 5), (5, 6), (6, 1),
            (7, 8), (8, 3), (3, 4), (4, 7),
            (7, 6), (1, 4), (3, 2), (8, 5),
        ],
        num_faces_on_vertices=4,
        opposing_faces=[(1, 8), (2, 7), (3, 6), (4, 5)],
    )

    d10 = Die(
        num_faces=10,
        adjacent_faces=[
            (2, 6), (6, 4), (4, 10), (10, 8), (8, 2),
            (9, 5), (5, 3), (3, 7), (7, 1), (1, 9),
            (1, 4), (4, 7), (7, 10), (10, 3), (3, 8), (8, 5), (5, 2), (2, 9), (9, 6), (6, 1)
        ],
        num_faces_on_vertices=3,
        opposing_faces=[(1, 8), (9, 10), (4, 5), (6, 3), (7, 2)],
    )
    # I had issues because a d10 is a wierd shape
    d10.add_cycles([
        UndirectedCycle([d10.verts[0], d10.verts[8], d10.verts[4], d10.verts[2], d10.verts[6]]),
        UndirectedCycle([d10.verts[9], d10.verts[7], d10.verts[1], d10.verts[5], d10.verts[3]]),
    ])

    d12 = Die(
        num_faces=12,
        adjacent_faces=[
            (1, 6), (1, 5), (1, 3), (1, 2), (1, 4),
            (12, 7), (12, 9), (12, 11), (12, 10), (12, 8),
            (3, 7), (7, 2), (2, 8), (8, 4), (4, 10), (10, 6), (6, 11), (11, 5), (5, 9), (9, 3),
            (7, 9), (9, 11), (11, 10), (10, 8), (8, 7),
            (2, 4), (4, 6), (6, 5), (5, 3), (3, 2)
        ],
        num_faces_on_vertices=3,
        opposing_faces=[(1, 12), (2, 11), (3, 10), (4, 9), (5, 8), (6, 7)],
    )

    d20 = Die(
        num_faces=20,
        adjacent_faces=[
            (1, 7), (1, 19), (1, 13),
            (2, 12), (2, 20), (2, 18),
            (3, 17), (3, 19), (3, 16),
            (4, 11), (4, 18), (4, 14),
            (5, 18), (5, 13), (5, 15),
            (6, 14), (6, 9), (6, 16),
            (7, 15), (7, 17),
            (8, 16), (8, 10), (8, 20),
            (9, 19), (9, 11),
            (10, 17), (10, 12),
            (11, 13),
            (12, 15),
            (14, 20),
        ],
        num_faces_on_vertices=5,
        opposing_faces=[(1, 20), (2, 19), (3, 18), (4, 17), (5, 16), (6, 15), (7, 14), (8, 13), (9, 12), (10, 11)],
    )

    dice = [d4, d6, d8, d10, d12, d20]
    for die in dice:
        print(f"\n\n#### D{die.num_faces()} calculations ####")
        sd, t = die.calc_optimum_face_weights_locked_opposing_faces()
        print(f"\tOpt vert weight sd of a d{die.num_faces()}: {sd:.4f}")
        print(f"\tOpt face value placement of a d{die.num_faces()}: {die.faces_to_string()}")
        print(f"\tFaces around the vertices of a d{die.num_faces()}: \n\t\t{die.vertices_to_string()}")
        print(f"\tCalculated in {datetime.timedelta(milliseconds=t)}\n")
