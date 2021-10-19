import functools
from collections import namedtuple
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # option1(pivot_index, A)
    option2(pivot_index, A)


def option1(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]

    lower = []
    equal = []
    higher = []

    for n in A:
        if n < pivot:
            lower.append(n)
        elif n > pivot:
            higher.append(n)
        else:
            equal.append(n)

    nums = lower + equal + higher

    for i in range(len(A)):
        A[i] = nums[i]


def option2(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1

    larger = len(A) - 1
    for i in range(len(A) - 1, -1, -1):
        if A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure("Not partitioned after {}th element".format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


Case = namedtuple("Case", ["k", "arr", "expected"])


def test():
    cases = [
        Case(0, [0], [0]),
        Case(1, [2, 1], [1, 2]),
        Case(
            1,
            [0, 1, 2, 1],
            [0, 1, 1, 2],
        ),
        Case(1, [1, 1, 0, 2], [0, 1, 1, 2]),
        Case(5, [7, 3, 2, 1, 8, 4, 5, 7, 9], [3, 2, 1, 4, 7, 8, 5, 7, 9]),
    ]

    for c in cases:
        dutch_flag_partition(c.k, c.arr)
        assert c.arr == c.expected


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "dutch_national_flag.py",
            "dutch_national_flag.tsv",
            dutch_flag_partition_wrapper,
        )
    )
