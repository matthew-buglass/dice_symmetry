import unittest

from dice import Die
from utils.graphs import UndirectedPath, Edge, UndirectedCycle


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


class D4TestCase(unittest.TestCase, DieTestCaseMixin):
    num_faces = 4
    adjacent_faces = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    num_faces_on_vertices = 3
    opposing_faces = [(1, 3), (2, 4)]
    die_vertices = 4

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instantiate_die()

    def test_instantiation(self):
        self.assertEqual(self.num_faces, len(self.die.verts))
        self.assertEqual(self.die_vertices, len(self.die.cycles))

    def test_edge_dict_building(self):
        verts = self.die.verts
        expected_dict = {
            verts[0]: {verts[1], verts[2], verts[3]},
            verts[1]: {verts[0], verts[2], verts[3]},
            verts[2]: {verts[1], verts[0], verts[3]},
            verts[3]: {verts[0], verts[1], verts[2]}
        }

        self.assertDictEqual(expected_dict, self.die.__get_edge_dict__())

    def test_cycle_finding(self):
        # Setup
        verts = self.die.verts
        expected_cycles = [
            UndirectedCycle([verts[0], verts[1], verts[2]]),
            UndirectedCycle([verts[0], verts[1], verts[3]]),
            UndirectedCycle([verts[0], verts[2], verts[3]]),
            UndirectedCycle([verts[1], verts[2], verts[3]])
        ]

        # Execute
        actual_cycles = self.die.__find_simple_cycles__(cycle_len=self.num_faces_on_vertices)

        # Assert
        self.assertEqual(len(expected_cycles), len(actual_cycles))
        for cycle in expected_cycles:
            self.assertIn(cycle, actual_cycles)


class D6TestCase(unittest.TestCase, DieTestCaseMixin):
    num_faces = 6
    adjacent_faces = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 6), (3, 5), (3, 6), (4, 5), (4, 6), (5, 6)]
    num_faces_on_vertices = 3
    opposing_faces = [(1, 6), (2, 5), (3, 4)]
    die_vertices = 8

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instantiate_die()

    def test_instantiation(self):
        self.assertEqual(self.num_faces, len(self.die.verts))
        self.assertEqual(self.die_vertices, len(self.die.cycles))

    def test_cycle_finding(self):
        # Setup
        verts = self.die.verts
        expected_cycles = [
            UndirectedCycle([verts[0], verts[1], verts[2]]),
            UndirectedCycle([verts[0], verts[1], verts[3]]),
            UndirectedCycle([verts[0], verts[4], verts[3]]),
            UndirectedCycle([verts[0], verts[4], verts[2]]),
            UndirectedCycle([verts[5], verts[1], verts[2]]),
            UndirectedCycle([verts[5], verts[1], verts[3]]),
            UndirectedCycle([verts[5], verts[4], verts[3]]),
            UndirectedCycle([verts[5], verts[4], verts[2]])
        ]

        # Execute
        actual_cycles = self.die.__find_simple_cycles__(cycle_len=self.num_faces_on_vertices)

        # Assert
        self.assertEqual(len(expected_cycles), len(actual_cycles))
        for cycle in expected_cycles:
            self.assertIn(cycle, actual_cycles)


class D8TestCase(unittest.TestCase, DieTestCaseMixin):
    num_faces = 8
    adjacent_faces = [
        (1, 8), (8, 5), (5, 4), (4, 1),
        (7, 6), (6, 3), (3, 2), (2, 7),
        (7, 4), (1, 6), (3, 8), (2, 5),
    ]
    num_faces_on_vertices = 4
    opposing_faces = [(7, 8), (3, 4), (2, 1), (6, 5)]
    die_vertices = 6

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instantiate_die()

    def test_instantiation(self):
        self.assertEqual(self.num_faces, len(self.die.verts))
        self.assertEqual(self.die_vertices, len(self.die.cycles))

    def test_cycle_finding(self):
        # Setup
        verts = self.die.verts
        expected_cycles = [
            UndirectedCycle([verts[0], verts[5], verts[2], verts[7]]),
            UndirectedCycle([verts[7], verts[2], verts[1], verts[4]]),
            UndirectedCycle([verts[4], verts[1], verts[6], verts[3]]),
            UndirectedCycle([verts[3], verts[6], verts[5], verts[0]]),
            UndirectedCycle([verts[0], verts[3], verts[4], verts[7]]),
            UndirectedCycle([verts[2], verts[1], verts[6], verts[5]]),
        ]

        # Execute
        actual_cycles = self.die.__find_simple_cycles__(cycle_len=self.num_faces_on_vertices)

        # Assert
        self.assertEqual(len(expected_cycles), len(actual_cycles))
        for cycle in expected_cycles:
            self.assertIn(cycle, actual_cycles)


class D10TestCase(unittest.TestCase, DieTestCaseMixin):
    num_faces = 10
    adjacent_faces = [
        (2, 6), (6, 4), (4, 10), (10, 8), (8, 2),
        (9, 5), (5, 3), (3, 7), (7, 1), (1, 9),
        (1, 4), (4, 7), (7, 10), (10, 3), (3, 8), (8, 5), (5, 2), (2, 9), (9, 6), (6, 1)
    ]
    num_faces_on_vertices = 3
    opposing_faces = [(1, 8), (9, 10), (4, 5), (6, 3), (7, 2)]
    die_vertices = 10  # before adding the weird ones.

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instantiate_die()

    def test_instantiation(self):
        self.assertEqual(self.num_faces, len(self.die.verts))
        self.assertEqual(self.die_vertices, len(self.die.__find_simple_cycles__(self.num_faces_on_vertices)))

    def test_cycle_finding(self):
        # Setup
        verts = self.die.verts
        expected_cycles = [
            UndirectedCycle([verts[0], verts[3], verts[6]]),
            UndirectedCycle([verts[3], verts[6], verts[9]]),
            UndirectedCycle([verts[6], verts[9], verts[2]]),
            UndirectedCycle([verts[9], verts[2], verts[7]]),
            UndirectedCycle([verts[2], verts[7], verts[4]]),
            UndirectedCycle([verts[7], verts[4], verts[1]]),
            UndirectedCycle([verts[4], verts[1], verts[8]]),
            UndirectedCycle([verts[1], verts[8], verts[5]]),
            UndirectedCycle([verts[8], verts[5], verts[0]]),
            UndirectedCycle([verts[5], verts[0], verts[3]]),
            UndirectedCycle([verts[0], verts[8], verts[4], verts[2], verts[6]]),
            UndirectedCycle([verts[9], verts[7], verts[1], verts[5], verts[3]]),
        ]

        # Execute
        self.die.add_cycles([
            UndirectedCycle([verts[0], verts[8], verts[4], verts[2], verts[6]]),
            UndirectedCycle([verts[9], verts[7], verts[1], verts[5], verts[3]]),
        ])
        actual_cycles = self.die.cycles

        # Assert
        self.assertEqual(len(expected_cycles), len(actual_cycles))
        for cycle in expected_cycles:
            self.assertIn(cycle, actual_cycles)


if __name__ == '__main__':
    unittest.main()
