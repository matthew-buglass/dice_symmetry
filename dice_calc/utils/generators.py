from itertools import permutations
from math import factorial


def npr(n, r):
    return factorial(n) / factorial(n-r)


def face_weights_locked_one(num_faces, opp_faces):
    face_vals_perms = permutations(iterable=range(2, num_faces), r=num_faces/2 - 1)

    num_perms = npr(num_faces-2, num_faces/2 - 1)
    curr_perm = 0

    perm = [0] * num_faces
    perm[0] = 1
    perm[-1] = num_faces

    while curr_perm < num_perms:
        one_side_perm = next(face_vals_perms)

        for i, j in opp_faces:
            perm[i] = one_side_perm[i]
            perm[j] = (num_faces + 1) - one_side_perm[i]

        yield perm

        curr_perm += 1
