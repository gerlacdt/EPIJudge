from typing import List, Deque

from test_framework import generic_test

from collections import namedtuple, deque


def solution(A: List[int], m: int, B: List[int], n: int) -> None:
    a, b, write_idx = m - 1, n - 1, m + n - 1

    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            A[write_idx] = A[a]
            a -= 1
            write_idx -= 1
        else:
            A[write_idx] = B[b]
            b -= 1
            write_idx -= 1

    while b >= 0:
        A[write_idx] = B[b]
        b -= 1
        write_idx -= 1

    return None


def solution2(A: List[int], m: int, B: List[int], n: int) -> None:
    tmp = []
    i = j = 0

    while i < m and j < n:
        if A[i] <= B[j]:
            tmp.append(A[i])
            i += 1
        elif B[j] < A[i]:
            tmp.append(B[j])
            j += 1

    while j < n:
        tmp.append(B[j])
        i += 1
        j += 1

    while i < m:
        tmp.append(A[i])
        i += 1
        j += 1

    for k in range(n + m):
        A[k] = tmp[k]
    return None


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int], n: int) -> None:
    solution(A, m, B, n)


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


Case = namedtuple("Case", ["A", "m", "B", "n", "expected"])


def test():
    cases = [
        Case(
            [3, 13, 17, 0, 0, 0, 0, 0],
            3,
            [3, 7, 11, 19],
            4,
            [3, 3, 7, 11, 13, 17, 19, 0],
        )
    ]

    for c in cases:
        merge_two_sorted_arrays(c.A, c.m, c.B, c.n)
        assert c.A == c.expected, "Case: {} {}".format(c.A, c.B)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "two_sorted_arrays_merge.py",
            "two_sorted_arrays_merge.tsv",
            merge_two_sorted_arrays_wrapper,
        )
    )
