import unittest

from utils.generators import face_weights_locked_one


class TestFaceWeightGenerator(unittest.TestCase):
    def test_number_of_weights_d6(self):
        faces = 6
        opposing_faces = [(1, 6), (2, 5), (3, 4)]
        expected_permutations = 12 # 4P2

        received_perms = 0
        for _ in face_weights_locked_one(num_faces=faces, opp_faces=opposing_faces):
            received_perms += 1

        self.assertEqual(expected_permutations, received_perms)

    def test_number_of_weights_d12(self):
        faces = 12
        opposing_faces = [(1,12), (2,11), (3,10), (4,9), (5,8), (6,7)]
        expected_permutations = 30240 # 10P5

        received_perms = 0
        for _ in face_weights_locked_one(num_faces=faces, opp_faces=opposing_faces):
            received_perms += 1

        self.assertEqual(expected_permutations, received_perms)

    def test_number_of_weights_d20(self):
        faces = 20
        opposing_faces = [(1,20), (2,19), (3,18), (4,17), (5,16), (6,15), (7,14), (8,13), (9,12), (10,11)]
        expected_permutations = 17643225600 # 18P9

        received_perms = 0
        for _ in face_weights_locked_one(num_faces=faces, opp_faces=opposing_faces):
            received_perms += 1

        self.assertEqual(expected_permutations, received_perms)


if __name__ == '__main__':
    unittest.main()
