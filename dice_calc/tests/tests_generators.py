import unittest

from utils.generators import face_weights_locked_one


class TestFaceWeightGenerator(unittest.TestCase):
    def test_number_of_weights_d6(self):
        faces = 6
        opposing_faces = [(0,5), (1,4), (2,3)]
        expected_permutations = 2 # 2!

        received_perms = 0
        for _ in face_weights_locked_one(num_faces=faces, opp_faces=opposing_faces):
            received_perms += 1

        self.assertEqual(expected_permutations, received_perms)

    def test_number_of_weights_d12(self):
        faces = 12
        opposing_faces = [(0,11), (1,10), (2,9), (3,8), (4,7), (5,6)]
        expected_permutations = 120 # 5!

        received_perms = 0
        for _ in face_weights_locked_one(num_faces=faces, opp_faces=opposing_faces):
            received_perms += 1

        self.assertEqual(expected_permutations, received_perms)

    def test_number_of_weights_d20(self):
        faces = 20
        opposing_faces = [(0,19), (1,18), (2,17), (3,16), (4,15), (5,14), (6,13), (7,12), (8,11), (9, 10)]
        expected_permutations = 362880 # 9!

        received_perms = 0
        for _ in face_weights_locked_one(num_faces=faces, opp_faces=opposing_faces):
            received_perms += 1

        self.assertEqual(expected_permutations, received_perms)

    def test_each_number_appears_once_d6(self):
        faces = 6
        opposing_faces = [(0,5), (1,4), (2,3)]
        expected_numbers = {1, 2, 3, 4, 5, 6}

        for weights in face_weights_locked_one(num_faces=faces, opp_faces=opposing_faces):
            self.assertSetEqual(expected_numbers, set(weights))

    def test_each_number_appears_once_d12(self):
        faces = 12
        opposing_faces = [(0,11), (1,10), (2,9), (3,8), (4,7), (5,6)]
        expected_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

        for weights in face_weights_locked_one(num_faces=faces, opp_faces=opposing_faces):
            self.assertSetEqual(expected_numbers, set(weights))

    def test_each_number_appears_once_d20(self):
        faces = 20
        opposing_faces = [(0,19), (1,18), (2,17), (3,16), (4,15), (5,14), (6,13), (7,12), (8,11), (9, 10)]
        expected_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

        for weights in face_weights_locked_one(num_faces=faces, opp_faces=opposing_faces):
            self.assertSetEqual(expected_numbers, set(weights))

    def test_opposite_sides_add_to_7_d6(self):
        faces = 6
        opposing_faces = [(0,5), (1,4), (2,3)]
        expected_sum = 7

        for weights in face_weights_locked_one(num_faces=faces, opp_faces=opposing_faces):
            for i, j in opposing_faces:
                self.assertEqual(expected_sum, weights[i] + weights[j])

    def test_opposite_sides_add_to_13_d12(self):
        faces = 12
        opposing_faces = [(0,11), (1,10), (2,9), (3,8), (4,7), (5,6)]
        expected_sum = 13

        for weights in face_weights_locked_one(num_faces=faces, opp_faces=opposing_faces):
            for i, j in opposing_faces:
                self.assertEqual(expected_sum, weights[i] + weights[j])

    def test_opposite_sides_add_to_21_d20(self):
        faces = 20
        opposing_faces = [(0,19), (1,18), (2,17), (3,16), (4,15), (5,14), (6,13), (7,12), (8,11), (9, 10)]
        expected_sum = 21

        for weights in face_weights_locked_one(num_faces=faces, opp_faces=opposing_faces):
            for i, j in opposing_faces:
                self.assertEqual(expected_sum, weights[i] + weights[j])

    def test_one_weight_per_side_d6(self):
        faces = 6
        opposing_faces = [(0,5), (1,4), (2,3)]

        for weights in face_weights_locked_one(num_faces=faces, opp_faces=opposing_faces):
            self.assertEqual(faces, len(weights))

    def test_one_weight_per_side_d12(self):
        faces = 12
        opposing_faces = [(0,11), (1,10), (2,9), (3,8), (4,7), (5,6)]

        for weights in face_weights_locked_one(num_faces=faces, opp_faces=opposing_faces):
            self.assertEqual(faces, len(weights))

    def test_one_weight_per_side_d20(self):
        faces = 20
        opposing_faces = [(0,19), (1,18), (2,17), (3,16), (4,15), (5,14), (6,13), (7,12), (8,11), (9, 10)]

        for weights in face_weights_locked_one(num_faces=faces, opp_faces=opposing_faces):
            self.assertEqual(faces, len(weights))


if __name__ == '__main__':
    unittest.main()
