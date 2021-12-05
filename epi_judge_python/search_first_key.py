from typing import List
from bisect import bisect_left

from collections import namedtuple

from test_framework import generic_test


def bin_search(nums, k):
    low = 0
    high = len(nums) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if k < nums[mid]:
            high = mid - 1
        elif k > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
            result = mid
    return result


def search_first_of_k(A: List[int], k: int) -> int:
    return bin_search(A, k)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", "search_first_key.tsv", search_first_of_k
        )
    )


Case = namedtuple("Case", ["nums", "k", "expected"])


def test_binsearch():
    cases = [
        Case([1, 3, 5, 7, 10, 14, 22], 10, 4),
        Case([1, 1, 2, 3, 4, 5, 6, 7], 1, 0),
        Case([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 285, 6),
    ]
    for c in cases:
        actual = bin_search(c.nums, c.k)
        assert actual == c.expected

        actual = bisect_left(c.nums, c.k)
        assert actual == c.expected
