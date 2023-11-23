from itertools import permutations
from math import factorial


def npr(n: int, r: int):
    return factorial(n) // factorial(n-r)


def face_weights_locked_one(num_faces: int, opp_faces: list[tuple[int, int]]):
    # create permutations of opposite faces
    face_value_pairs = {(i, (num_faces + 1)-i) for i in range(2, num_faces // 2 + 1)}
    face_vals_perms = permutations(face_value_pairs)

    # Calculate the total number of permutations
    num_perms = factorial(len(face_value_pairs))
    curr_perm = 0

    # Set up the permutation
    perm = [0] * num_faces
    perm[0] = 1
    perm[-1] = num_faces

    # remove the locked first face from the number of opposite faces
    if (0, num_faces-1) in opp_faces:
        opp_faces.remove((0, num_faces-1))
    if (num_faces - 1, 0) in opp_faces:
        opp_faces.remove((num_faces - 1, 0))

    # Create the permutation
    while curr_perm < num_perms:
        one_side_perm = next(face_vals_perms)

        for i, j in opp_faces:
            perm[i] = one_side_perm[i-1][0]
            perm[j] = one_side_perm[i-1][1]

        yield perm

        curr_perm += 1
