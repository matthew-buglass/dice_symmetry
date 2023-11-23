import unittest

from utils.generators import face_weights_locked_one


class TestFaceWeightGenerator(unittest.TestCase):
    d6_faces = 6
    d6_opposing_faces = [(0, 5), (1, 4), (2, 3)]

    d12_faces = 12
    d12_opposing_faces = [(0, 11), (1, 10), (2, 9), (3, 8), (4, 7), (5, 6)]

    d20_faces = 20
    d20_opposing_faces = [(0, 19), (1, 18), (2, 17), (3, 16), (4, 15), (5, 14), (6, 13), (7, 12), (8, 11), (9, 10)]

    @classmethod
    def setUpClass(cls):
        cls.d6_perms = list(face_weights_locked_one(num_faces=cls.d6_faces, opp_faces=cls.d6_opposing_faces))
        cls.d12_perms = list(face_weights_locked_one(num_faces=cls.d12_faces, opp_faces=cls.d12_opposing_faces))
        cls.d20_perms = list(face_weights_locked_one(num_faces=cls.d20_faces, opp_faces=cls.d20_opposing_faces))

    def test_number_of_weights_d6(self):
        expected_permutations = 2 # 2!

        received_perms = 0
        for _ in self.d6_perms:
            received_perms += 1

        self.assertEqual(expected_permutations, received_perms)

    def test_number_of_weights_d12(self):
        expected_permutations = 120 # 5!

        received_perms = 0
        for _ in self.d12_perms:
            received_perms += 1

        self.assertEqual(expected_permutations, received_perms)

    def test_number_of_weights_d20(self):
        expected_permutations = 362880 # 9!

        received_perms = 0
        for _ in self.d20_perms:
            received_perms += 1

        self.assertEqual(expected_permutations, received_perms)

    def test_each_number_appears_once_d6(self):
        expected_numbers = {1, 2, 3, 4, 5, 6}

        for weights in self.d6_perms:
            self.assertSetEqual(expected_numbers, set(weights))

    def test_each_number_appears_once_d12(self):
        expected_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

        for weights in self.d12_perms:
            self.assertSetEqual(expected_numbers, set(weights))

    def test_each_number_appears_once_d20(self):
        expected_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

        for weights in self.d20_perms:
            self.assertSetEqual(expected_numbers, set(weights))

    def test_opposite_sides_add_to_7_d6(self):
        expected_sum = 7

        for weights in self.d6_perms:
            for i, j in self.d6_opposing_faces:
                self.assertEqual(expected_sum, weights[i] + weights[j])

    def test_opposite_sides_add_to_13_d12(self):
        expected_sum = 13

        for weights in self.d12_perms:
            for i, j in self.d12_opposing_faces:
                self.assertEqual(expected_sum, weights[i] + weights[j])

    def test_opposite_sides_add_to_21_d20(self):
        expected_sum = 21

        for weights in self.d20_perms:
            for i, j in self.d20_opposing_faces:
                self.assertEqual(expected_sum, weights[i] + weights[j])

    def test_one_weight_per_side_d6(self):
        for weights in self.d6_perms:
            self.assertEqual(self.d6_faces, len(weights))

    def test_one_weight_per_side_d12(self):
        for weights in self.d12_perms:
            self.assertEqual(self.d12_faces, len(weights))

    def test_one_weight_per_side_d20(self):
        for weights in self.d20_perms:
            self.assertEqual(self.d20_faces, len(weights))


if __name__ == '__main__':
    unittest.main()
