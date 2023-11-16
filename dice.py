
class Die:
    faces = []
    edges = []
    vertices = []
    vertex_weights = []
    sides = 0

    def __init__(self, num_faces: int, adjacent_faces: [tuple[int, int]], faces_on_vertices: list[int]):
        """
        An abstract graph representation of a die. Vertices in the graph represent faces on a die, and the vertex
        weights are the face values of the die. A simple cycle of a given number of vertices represents the point, or
        vertex, on the face of the die. In this way, we can calculate facial and vertex similarities of dice.

        :param num_faces: the number of faces on the die. this will be the number of vertices in the graph.
        :param adjacent_faces: an edge list of faces of the die that are adjacent to each other. A list of tuples
            containing the vertex indices of the start and end vertices of an edge.
        :param faces_on_vertices: simple cycles in the graph that represent the meeting of a certain number of faces. In
            perfectly fair dice (D4, D6, D8, D12, D20) this will always be the same number of faces (3, 3, 4, 3, 5) within
            the die. For unfair dice (D10, D30, etc.) this may differ in the die (3 and 5, 3 and 5), which is why this
            is a list.
        """




if __name__ == '__main__':
    print('Hello World')
