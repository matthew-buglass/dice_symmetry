import unittest

from utils.generators import face_weights_locked_one


class TestFaceWeightGenerator(unittest.TestCase):
    def test_number_of_weights_d6(self):
        faces = 6
        opposing_faces = [(0,5), (1,4), (2,3)]
        expected_permutations = 12 # 4P2

        received_perms = 0
        for _ in face_weights_locked_one(num_faces=faces, opp_faces=opposing_faces):
            received_perms += 1

        self.assertEqual(expected_permutations, received_perms)

    def test_number_of_weights_d12(self):
        faces = 12
        opposing_faces = [(0,11), (1,10), (2,9), (3,8), (4,7), (5,6)]
        expected_permutations = 30240 # 10P5

        received_perms = 0
        for _ in face_weights_locked_one(num_faces=faces, opp_faces=opposing_faces):
            received_perms += 1

        self.assertEqual(expected_permutations, received_perms)

    def test_number_of_weights_d20(self):
        faces = 20
        opposing_faces = [(0,19), (1,18), (2,17), (3,16), (4,15), (5,14), (6,13), (7,12), (8,11), (9,10)]
        expected_permutations = 17643225600 # 18P9

        received_perms = 0
        for _ in face_weights_locked_one(num_faces=faces, opp_faces=opposing_faces):
            received_perms += 1

        self.assertEqual(expected_permutations, received_perms)


if __name__ == '__main__':
    unittest.main()
