from itertools import permutations

import numpy as np

from utils.graphs import Edge, WeightedVertex, UndirectedPath


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
        self.verts = [WeightedVertex(i, i+1) for i in range(num_faces)]
        self.edges = [Edge(self.verts[e[0]-1], self.verts[e[1]-1])for e in adjacent_faces]
        self.opp_faces = {self.verts[p[0]-1]: self.verts[p[1]-1] for p in opposing_faces}

        self.cycles = []
        for cyc_len in num_faces_on_vertices:
            self.cycles.extend(self.__find_simple_cycles__(cyc_len))

    def __find_simple_cycles__(self, cycle_len) -> list[list[WeightedVertex]]:
        """
        Finds all unique simple cycles of a specific length in an edge_list.
        :param edges: The undirected edge list of the graph
        :param cycle_len: The number of unique vertices in the cycles. The first vertex counts as the first and last.
        :return: A list of unique simple cycles in the graph. The closing edge goes from the last to the first vertex
        """
        def cycle_helper(edge_dict: dict[int: list[Edge]], curr_path: list[WeightedVertex], cycle_len: int, cycles: list[UndirectedPath]):
            if len(curr_path) == cycle_len:
                # if there's an edge from the last to the first vertex add the path to the collected cycles
                try:
                    last_edge = edge_dict[curr_path[-1]][curr_path[0]]
                    if not curr_path in cycles:
                        cycles.append(curr_path)
                except KeyError:
                    pass
            else:
                start_vert = curr_path[-1]
                edges_to_try = [e for e in edge_dict[start_vert].values() if e.follow(start_vert) not in curr_path]
                for edge in edges_to_try:
                    new_path = curr_path.copy()
                    new_path.append(edge.follow(curr_path[-1]))
                    cycle_helper(edge_dict, new_path, cycle_len, cycles)

        cycles = []
        edge_dict = {}
        for edge in self.edges:
            try:
                edge_dict[edge.src][edge.dst] = edge
            except KeyError:
                edge_dict[edge.src] = {}
                edge_dict[edge.src][edge.dst] = edge

            try:
                edge_dict[edge.dst][edge.src] = edge
            except KeyError:
                edge_dict[edge.dst] = {}
                edge_dict[edge.dst][edge.src] = edge

        for v in self.verts:
            cycle_helper(edge_dict, UndirectedPath([v]), cycle_len, cycles)
        return cycles

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

    def __get_opposing_face_weights__(self):
        """
        Calculates the average weight of each of the die's opposing faces
        :return: a list floats of the average weight of the die's opposing sides
        """
        weights = []
        for i, j in self.opp_faces.items():
            weights.append((i.weight + j.weight) / 2)
        return weights

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

    def __expand_half_weights__(self, half_weights):
        """
        Yields a full set of weights from the lower half generator of weights
        :param half_weights: a collection of face values from 2 to half of the number of faces.
            (ie for a d8, a permutation of [2, 3, 4])
        :return: A full list of weights to apply to a die's faces, maintaining the same average face value between
        opposite faces.
        """
        num_faces = len(self.verts)
        full_weights = [0] * num_faces
        for a, b in self.opp_faces.items():
            if a.name == 0:
                full_weights[a.name] = 1
                full_weights[b.name] = num_faces
            else:
                small_face_weight = half_weights[a.name-1]
                full_weights[a.name] = small_face_weight
                full_weights[b.name] = num_faces - small_face_weight + 1

        return full_weights

    def calc_optimum_face_weights_locked_opp_faces(self):
        """
        Finds the weight (face number) positioning that minimizes the standard deviation of die vertex weights, keeping
        facial symmetry (average of opposing faces is identical) a requirement.
        :return: a string representation of face ids and the weights attributed.
        """
        # we are always going to assign 1 to face 0 to avoid rotating the same number configurations around
        # the die. This also locks it's opposing face to be the maximum face value of the die
        half_weight_perms = permutations(range(2, len(self.verts) // 2 + 1))

        optimal_weights = [0] * len(self.verts)
        optimal_weights_sd = 99999999999999

        for hw in half_weight_perms:
            weights = self.__expand_half_weights__(hw)
            self.__assign_weights__(weights=weights)
            sd = np.std(self.__get_vertex_weights__())
            if sd < optimal_weights_sd:
                optimal_weights = weights
                optimal_weights_sd = sd

        # apply and return the best weights
        self.__assign_weights__(optimal_weights)
        return optimal_weights_sd

    def verts_to_string(self):
        return str([str(v) for v in self.verts])


if __name__ == '__main__':
    d4 = Die(
        num_faces=4,
        adjacent_faces=[(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)],
        num_faces_on_vertices=[3],
        opposing_faces=[(1,3), (2,4)]
    )

    sd = d4.calc_optimum_face_weights_locked_opp_faces()
    print("#### D4 calculations ####")
    print("Opt vert weight sd of a d4: {:.4f}".format(sd))
    print(f"Opt face value placement of a d4: {d4.verts_to_string()}\n")
