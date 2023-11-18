import unittest

from dice import Die


class DiceTestCase(unittest.TestCase):
    def test_d4_instantiation(self):
        # Setup
        faces = 4
        adjacent_faces = [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]
        num_faces_on_vertices=[3]
        opposing_faces = [(1, 3), (2, 4)]

        # Execution
        d4 = Die(
            num_faces=faces,
            adjacent_faces=adjacent_faces,
            num_faces_on_vertices=num_faces_on_vertices,
            opposing_faces=opposing_faces
        )

        # Evaluation
        self.assertEqual(len(d4.verts), faces)
        self.assertEqual(len(d4.cycles), 4)


if __name__ == '__main__':
    unittest.main()
