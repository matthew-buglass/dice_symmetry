import unittest

from utils.graphs import Vertex, Edge


class TestVertex(unittest.TestCase):
    def test_vertex_equivalency(self):
        v1 = Vertex(0)
        v2 = Vertex(0)
        v3 = Vertex(1)

        self.assertEqual(v1, v2)
        self.assertNotEqual(v1, v3)

class TestEdge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.v1 = Vertex(0)
        cls.v2 = Vertex(1)
        cls.v3 = Vertex(2)

    def test_edge_default_is_undirected(self):
        self.assertFalse(Edge(self.v1, self.v2).directed)

    def test_undirected_edge_equivalency(self):
        e1 = Edge(self.v1, self.v2, directed=False)
        e2 = Edge(self.v2, self.v1, directed=False)
        e3 = Edge(self.v1, self.v3, directed=False)

        self.assertEqual(e1, e2)
        self.assertNotEqual(e1, e3)

    def test_directed_edge_equivalency(self):
        e1 = Edge(self.v1, self.v2, directed=True)
        e2 = Edge(self.v2, self.v1, directed=True)
        e3 = Edge(self.v1, self.v3, directed=True)

        self.assertNotEqual(e1, e2)
        self.assertNotEqual(e1, e3)


class TestUndirectedPath(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
