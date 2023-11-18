import numpy as np

from graphs import Edge, Vertex, WeightedVertex, UndirectedPath


class Die:
    cycles: list[list[WeightedVertex]]
    edges: list[Edge]
    verts: [WeightedVertex]
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
        self.verts = np.array([WeightedVertex(i, 0) for i in range(num_faces)], dtype=WeightedVertex)
        self.edges = [Edge(self.verts[e[0]-1], self.verts[e[1]-1])for e in adjacent_faces]

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

    def __get_vertex_weights__(self) -> list[tuple[list[int], float]]:
        """
        Calculates the weights of each of the die's vertices
        :return: a list of tuples of the faces around vertices and their floating point vertex weights
        """
        vert_weights = []
        for cycle in self.cycles:
            weight = sum([self.verts[w] for w in cycle]) / len(cycle)
            vert_weights.append((cycle, weight))
        return vert_weights

    def __get_opposing_face_weights__(self):
        pass




if __name__ == '__main__':
    d4 = Die(
        num_faces=4,
        adjacent_faces=[(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)],
        num_faces_on_vertices=[3],
        opposing_faces=[(1,3), (2,4)]
    )
    print('Hello World')
