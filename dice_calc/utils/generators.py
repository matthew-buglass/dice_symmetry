from itertools import permutations
from math import factorial


def paired_face_weights_locked_one(num_faces: int, opp_faces: list[tuple[int, int]]):
    # create permutations of opposite faces (starting at 2 because we already set 1
    face_value_pairs = {(i, (num_faces + 1)-i) for i in range(2, num_faces // 2 + 1)}
    face_vals_perms = permutations(face_value_pairs)

    # Calculate the total number of permutations
    num_perms = factorial(len(face_value_pairs))
    curr_perm = 0

    # Set up the permutation
    perm = [0] * num_faces

    # remove the locked first face from the number of opposite faces
    def find_first_pairing(face_pairs):
        for fp in opp_faces:
            if fp[0] == 1:
                return fp
            elif fp[1] == 1:
                return fp[1], fp[0]

    face_one_pairing = find_first_pairing(opp_faces)
    opp_faces.remove(face_one_pairing)
    perm[face_one_pairing[0]-1] = 1
    perm[face_one_pairing[1]-1] = num_faces

    # Create the permutation
    while curr_perm < num_perms:
        one_side_perm = next(face_vals_perms)

        for i, (j, k) in enumerate(opp_faces):
            perm[j-1] = one_side_perm[i][0]
            perm[k-1] = one_side_perm[i][1]

        yield perm

        curr_perm += 1


def face_weights_locked_one(num_faces: int):
    # create permutations of faces (starting at 2 because we already set 1)
    face_vals_perms = permutations(range(2, num_faces + 1))

    # Calculate the total number of permutations
    num_perms = factorial(num_faces - 1)
    curr_perm = 0

    # Create the permutation
    while curr_perm < num_perms:
        perm = next(face_vals_perms)
        yield (1,) + perm
        curr_perm += 1
