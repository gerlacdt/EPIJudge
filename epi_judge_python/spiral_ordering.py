from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    def matrix_layer_in_clockwise(offset):
        nonlocal spiral_ordering
        if offset == len(square_matrix) - offset - 1:
            # special case for the center of an odd-dimension matrix like 3x3 or 5x5
            spiral_ordering.append(square_matrix[offset][offset])
            return

        # row forwards
        spiral_ordering.extend(square_matrix[offset][offset : -1 - offset])
        # print("row forwards: {}".format(spiral_ordering))

        # col downwards
        spiral_ordering.extend(
            list(zip(*square_matrix))[-1 - offset][offset : -1 - offset]
        )
        # print("col downwards: {}".format(spiral_ordering))

        # row backwards
        spiral_ordering.extend(square_matrix[-1 - offset][-1 - offset : offset : -1])
        # print("row backwards: {}".format(spiral_ordering))

        # col upwards
        spiral_ordering.extend(
            list(zip(*square_matrix))[offset][-1 - offset : offset : -1]
        )
        # print("col upwards: {}".format(spiral_ordering))

    spiral_ordering: List[int] = []
    for offset in range((len(square_matrix) + 1) // 2):
        matrix_layer_in_clockwise(offset)
    return spiral_ordering


def test():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    actual = matrix_in_spiral_order(matrix)
    expected = [
        1,
        2,
        3,
        6,
        9,
        8,
        7,
        4,
        5,
    ]
    assert actual == expected


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "spiral_ordering.py", "spiral_ordering.tsv", matrix_in_spiral_order
        )
    )
