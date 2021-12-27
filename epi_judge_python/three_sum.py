from typing import List, Set
from collections import namedtuple

from test_framework import generic_test


def two_sum(A: List[int], target: int) -> bool:
    A.sort()
    i = 0
    j = len(A) - 1
    while i <= j:
        val = A[i] + A[j]
        if val < target:
            i += 1
        elif val > target:
            j -= 1
        else:
            return True
    return False


def two_sum_hashtable(A: List[int], target: int) -> bool:
    table: Set[int] = set()
    for i, val in enumerate(A):
        table.add(val)  # add before, so same element can be used twice
        tmp = target - val
        if tmp in table:
            return True
    return False


def invariant(A: List[int], t: int) -> bool:
    A.sort()
    for i, val in enumerate(A):
        tmp_target = t - val
        if two_sum(A, tmp_target):
            return True
    return False


def hashtable(A: List[int], t: int) -> bool:
    for i, val in enumerate(A):
        tmp_target = t - val
        if two_sum_hashtable(A, tmp_target):
            return True
    return False


def has_three_sum(A: List[int], t: int) -> bool:
    # return invariant(A, t)
    return hashtable(A, t)


if __name__ == "__main__":
    exit(generic_test.generic_test_main("three_sum.py", "three_sum.tsv", has_three_sum))


Case = namedtuple("Case", ["A", "target", "expected"])


def test_two_sum():
    cases = [
        Case([2, 2, 4, 4, 3, 3], 7, True),
        Case([2, 2, 4, 4, 6], 7, False),
        Case(
            [1, 4, 5, 6],
            2,
            True,
        ),
        Case([-1], -2, True),
    ]

    for c in cases:
        actual = two_sum(c.A, c.target)
        assert actual == c.expected, "Case: {}".format(c)

        actual = two_sum_hashtable(c.A, c.target)
        assert actual == c.expected, "Case: {}".format(c)


def test_invariant():
    cases = [
        Case([2, 2, 4, 4, 3, 3], 7, True),
        Case([2, 2, 4, 4, 6], 7, False),
        Case([0, -1], -3, True),
    ]

    for c in cases:
        actual = invariant(c.A, c.target)
        assert actual == c.expected, "Case: {}".format(c)


def test_hashtable():
    cases = [
        Case([2, 2, 4, 4, 3, 3], 7, True),
        Case([2, 2, 4, 4, 6], 7, False),
        Case([0, -1], -3, True),
    ]

    for c in cases:
        actual = hashtable(c.A, c.target)
        assert actual == c.expected, "Case: {}".format(c)
