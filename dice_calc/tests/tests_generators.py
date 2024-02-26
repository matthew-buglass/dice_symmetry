import unittest

from utils.generators import face_weights_locked_one


class TestFaceWeightGenerator(unittest.TestCase):
    d4_faces = 4
    d4_opposing_faces = [(1, 3), (2, 4)]

    d6_faces = 6
    d6_opposing_faces = [(1, 6), (2, 5), (3, 4)]

    d12_faces = 12
    d12_opposing_faces = [(1, 12), (2, 11), (3, 10), (4, 9), (5, 8), (6, 7)]

    d20_faces = 20
    d20_opposing_faces = [(1, 20), (2, 19), (3, 18), (4, 17), (5, 16), (6, 15), (7, 14), (8, 13), (9, 12), (10, 11)]

    @classmethod
    def setUpClass(cls):
        cls.d4_perms = list(face_weights_locked_one(num_faces=cls.d4_faces, opp_faces=cls.d4_opposing_faces))
        cls.d6_perms = list(face_weights_locked_one(num_faces=cls.d6_faces, opp_faces=cls.d6_opposing_faces))
        cls.d12_perms = list(face_weights_locked_one(num_faces=cls.d12_faces, opp_faces=cls.d12_opposing_faces))
        cls.d20_perms = list(face_weights_locked_one(num_faces=cls.d20_faces, opp_faces=cls.d20_opposing_faces))

    def test_number_of_weights_d4(self):
        expected_permutations = 2 # 2!

        received_perms = 0
        for _ in self.d6_perms:
            received_perms += 1

        self.assertEqual(expected_permutations, received_perms)

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

    def test_opposite_sides_add_to_5_d4(self):
        expected_sum = 5

        for weights in self.d4_perms:
            for i, j in self.d4_opposing_faces:
                self.assertEqual(expected_sum, weights[i-1] + weights[j-1])

    def test_opposite_sides_add_to_7_d6(self):
        expected_sum = 7

        for weights in self.d6_perms:
            for i, j in self.d6_opposing_faces:
                self.assertEqual(expected_sum, weights[i-1] + weights[j-1])

    def test_opposite_sides_add_to_13_d12(self):
        expected_sum = 13

        for weights in self.d12_perms:
            for i, j in self.d12_opposing_faces:
                self.assertEqual(expected_sum, weights[i-1] + weights[j-1])

    def test_opposite_sides_add_to_21_d20(self):
        expected_sum = 21

        for weights in self.d20_perms:
            for i, j in self.d20_opposing_faces:
                self.assertEqual(expected_sum, weights[i-1] + weights[j-1])

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
