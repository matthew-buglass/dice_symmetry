from itertools import permutations
from math import factorial


def npr(n: int, r: int):
    return factorial(n) // factorial(n-r)


def face_weights_locked_one(num_faces: int, opp_faces: list[tuple[int, int]]):
    face_vals_perms = permutations(iterable=range(2, num_faces), r=num_faces//2 - 1)

    # Calculate the total number of permutations
    num_perms = npr(num_faces-2, num_faces//2 - 1)
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
            perm[i] = one_side_perm[i-1]
            perm[j] = (num_faces + 1) - one_side_perm[i-1]

        yield perm

        curr_perm += 1
