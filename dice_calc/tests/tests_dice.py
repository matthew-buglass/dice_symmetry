import unittest

from dice import Die

class DieTestCaseMixin:
    opposing_faces = None
    num_faces_on_vertices = None
    adjacent_faces = None
    num_faces = None
    die_vertices = None
    die = None

    def instantiate_die(self):
        if not (self.opposing_faces and
                self.adjacent_faces and
                self.num_faces_on_vertices and
                self.opposing_faces and
                self.die_vertices):
            raise NotImplementedError("{} class not implemented correctly, please define:\n"
                                      "\tcls.num_faces\n"
                                      "\tcls.adjacent_faces\n"
                                      "\tcls.num_faces_on_vertices\n"
                                      "\tcls.opposing_faces\n"
                                      "\tcls.die_vertices\n".format(self.__name__))

        self.die = Die(
            num_faces=self.num_faces,
            adjacent_faces=self.adjacent_faces,
            num_faces_on_vertices=self.num_faces_on_vertices,
            opposing_faces=self.opposing_faces
        )

    def test_instantiation(self):
        self.assertEqual(self.num_faces, len(self.die.verts))
        self.assertEqual(self.die_vertices, len(self.die.cycles))

class D4TestCase(unittest.TestCase, DieTestCaseMixin):
    num_faces = 4
    adjacent_faces = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    num_faces_on_vertices = [3]
    opposing_faces = [(1, 3), (2, 4)]
    die_vertices = 4

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instantiate_die()



class D6TestCase(unittest.TestCase, DieTestCaseMixin):
    num_faces = 6
    adjacent_faces = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 6), (3, 5), (3, 6), (4, 5), (5, 6)]
    num_faces_on_vertices = [3]
    opposing_faces = [(1, 6), (2, 5), (3, 4)]
    die_vertices = 8

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instantiate_die()


if __name__ == '__main__':
    unittest.main()
