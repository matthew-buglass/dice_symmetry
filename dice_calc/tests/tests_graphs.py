import unittest

from utils.graphs import Vertex, Edge, UndirectedPath


class TestVertex(unittest.TestCase):
    def test_vertex_equivalency(self):
        v1 = Vertex(0, 1)
        v2 = Vertex(0, 1)
        v3 = Vertex(1, 2)

        self.assertEqual(v1, v2)
        self.assertNotEqual(v1, v3)

class TestEdge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.v1 = Vertex(0, 1)
        cls.v2 = Vertex(1, 2)
        cls.v3 = Vertex(2, 3)

    def test_edge_default_is_undirected(self):
        self.assertFalse(Edge(self.v1, self.v2).directed)

    def test_undirected_edge_equivalency(self):
        e1 = Edge(self.v1, self.v2, directed=False)
        e2 = Edge(self.v2, self.v1, directed=False)
        e3 = Edge(self.v1, self.v3, directed=False)

        self.assertEqual(e1, e2)
        self.assertNotEqual(e1, e3)

    def test_undirected_edge_follow(self):
        e1 = Edge(self.v1, self.v2, directed=False)

        self.assertEqual(e1.follow(self.v1), self.v2)
        self.assertEqual(e1.follow(self.v2), self.v1)
        self.assertRaises(AssertionError, e1.follow, self.v3)

    def test_directed_edge_equivalency(self):
        e1 = Edge(self.v1, self.v2, directed=True)
        e2 = Edge(self.v2, self.v1, directed=True)
        e3 = Edge(self.v1, self.v3, directed=True)

        self.assertNotEqual(e1, e2)
        self.assertNotEqual(e1, e3)

    def test_directed_edge_follow(self):
        e1 = Edge(self.v1, self.v2, directed=True)

        self.assertEqual(e1.follow(self.v1), self.v2)
        self.assertRaises(AssertionError, e1.follow, self.v2)
        self.assertRaises(AssertionError, e1.follow, self.v3)

class TestUndirectedPath(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.v1 = Vertex(0 ,1)
        cls.v2 = Vertex(1, 2)
        cls.v3 = Vertex(2, 3)
        cls.v4 = Vertex(3, 4)

    def test_path_equivalency(self):
        p1 = UndirectedPath([self.v1, self.v2, self.v3])
        p2 = UndirectedPath([self.v2, self.v1, self.v3])
        p3 = UndirectedPath([self.v1, self.v4, self.v3])

        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)

    def test_path_extension(self):
        p1 = UndirectedPath([self.v1, self.v2])
        p2 = UndirectedPath([self.v1, self.v2, self.v3])

        p1.append(self.v3)

        self.assertEqual(p1, p2)

    def test_path_deep_copy(self):
        p1 = UndirectedPath([self.v1, self.v2, self.v3])

        p2 = p1.deep_copy()

        self.assertEqual(p1, p2)

        p2.verts[0] = self.v4
        self.assertNotEqual(p1, p2)

    def test_path_length(self):
        self.assertEqual(3, len(UndirectedPath([self.v1, self.v2, self.v3])))

    def test_path_indexing(self):
        self.assertEqual(self.v2, UndirectedPath([self.v1, self.v2, self.v3])[1])


if __name__ == '__main__':
    unittest.main()
