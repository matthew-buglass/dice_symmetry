from itertools import permutations

import numpy as np

from utils.decorators import timed
from utils.generators import face_weights_locked_one
from utils.graphs import Edge, WeightedVertex, UndirectedPath, UndirectedCycle


class Die:
    cycles: list[list[WeightedVertex]]
    edges: list[Edge]
    verts: list[WeightedVertex]
    sides: int

    def __init__(self, num_faces: int, adjacent_faces: [tuple[int, int]],
                 num_faces_on_vertices: list[int], opposing_faces: list[tuple[int, int]]):
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

        self.cycles = self.__find_simple_cycles__(num_faces_on_vertices)

    def __get_edge_dict__(self) -> dict[WeightedVertex, list[Edge]]:
        edge_dict = {}
        for edge in self.edges:
            assert not edge.directed
            try:
                edge_dict[edge.src].append(edge)
            except KeyError:
                edge_dict[edge.src] = []
                edge_dict[edge.src].append(edge)

            try:
                edge_dict[edge.dst].append(edge)
            except KeyError:
                edge_dict[edge.dst] = []
                edge_dict[edge.dst].append(edge)

        return edge_dict

    def __find_simple_cycles__(self, cycle_lens) -> list[UndirectedCycle]:
        """
        Finds all unique simple cycles of a specific length in an edge_list.
        :param edges: The undirected edge list of the graph
        :param cycle_lens: The list of number of unique vertices in the cycles. The first vertex counts as the first and last.
        :return: A list of unique simple cycles in the graph. The closing edge goes from the last to the first vertex
        """

        def cycle_helper(edge_dict: dict[WeightedVertex, list[Edge]],
                         curr_path: UndirectedPath,
                         cycle_len: int,
                         cycles: list[UndirectedPath]):
            if len(curr_path) == cycle_len:
                # if there's an edge from the last to the first vertex add the path to the collected cycles
                for edge in edge_dict[curr_path[-1]]:
                    try:
                        edge.follow(curr_path[0])
                        cycles.append(UndirectedCycle(curr_path.verts))
                    except AssertionError:
                        pass
            else:
                last_vertex = curr_path[-1]
                verts_to_try = [e.follow(last_vertex) for e in edge_dict[last_vertex] if e.follow(last_vertex) not in curr_path]
                for vert in verts_to_try:
                    new_path = curr_path.deep_copy()
                    new_path.append(vert)
                    cycle_helper(edge_dict, new_path, cycle_len, cycles)

        all_cycles = []

        for cycle_len in cycle_lens:
            cycles = []
            for e in self.edges:
                cycle_helper(self.__get_edge_dict__(), UndirectedPath([e.src, e.dst]), cycle_len, cycles)
            all_cycles.extend(cycles)
        return list(set(all_cycles))

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


if __name__ == '__main__':
    d4 = Die(
        num_faces=4,
        adjacent_faces=[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)],
        num_faces_on_vertices=[3],
        opposing_faces=[(1, 3), (2, 4)]
    )

    sd, t = d4.calc_optimum_face_weights_locked_opposing_faces()
    print("#### D4 calculations ####")
    print("\tOpt vert weight sd of a d4: {:.4f}".format(sd))
    print(f"\tOpt face value placement of a d4: {d4.faces_to_string()}")
    print(f"\tFaces around the vertices of a d4: \n\t\t{d4.vertices_to_string()}")
    print("\tCalculated in {:.4f} ms\n".format(t))

    d6 = Die(
        num_faces=6,
        adjacent_faces=[(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 6), (3, 5), (3, 6), (4, 5), (5, 6)],
        num_faces_on_vertices=[3],
        opposing_faces=[(1, 6), (2, 5), (3, 4)]
    )
    sd, t = d6.calc_optimum_face_weights_locked_opposing_faces()
    print("#### D6 calculations ####")
    print("\tOpt vert weight sd of a d4: {:.4f}".format(sd))
    print(f"\tOpt face value placement of a d4: {d6.faces_to_string()}")
    print(f"\tFaces around the vertices of a d6: \n\t\t{d6.vertices_to_string()}")
    print("\tCalculated in {:.4f} ms\n".format(t))
