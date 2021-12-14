from typing import List
from collections import namedtuple

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:

    if not A or not B:
        return []

    result: List[int] = []
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1
        elif B[j] < A[i]:
            j += 1
        else:
            # equal case
            val = A[i]
            i += 1
            j += 1
            if result and val == result[-1]:
                continue
            else:
                result.append(val)
    return result


Case = namedtuple("Case", ["A", "B", "expected"])


def test_simple():
    cases = [
        Case([1, 2, 3], [2, 7, 8], [2]),
        Case([], [1, 2, 3], []),
        Case([2, 3, 3, 4], [2, 2, 2, 5], [2]),
        Case(
            [2, 3, 3, 5, 5, 6, 7, 7, 8, 12],
            [5, 5, 6, 8, 8, 9, 10, 10],
            [5, 6, 8],
        ),
    ]

    for c in cases:
        actual = intersect_two_sorted_arrays(c.A, c.B)

        assert actual == c.expected, "Case: {} {}".format(c.A, c.B)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "intersect_sorted_arrays.py",
            "intersect_sorted_arrays.tsv",
            intersect_two_sorted_arrays,
        )
    )
