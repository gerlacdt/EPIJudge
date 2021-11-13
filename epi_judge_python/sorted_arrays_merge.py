from typing import List

from test_framework import generic_test
from collections import namedtuple
from heapq import heapify, heappop, heappush

import linecache


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    result: List[int] = []
    heap = [(arr[0], i, 0) for i, arr in enumerate(sorted_arrays) if arr]
    heapify(heap)
    while heap:
        val, index_arr, index = heappop(heap)
        result.append(val)
        if index < len(sorted_arrays[index_arr]) - 1:
            item = sorted_arrays[index_arr][index + 1]
            heappush(heap, (item, index_arr, index + 1))
    return result


def merge_sorted_files(sorted_files: List[List[str]]) -> List[int]:
    sorted_arrays = []
    for filename in sorted_files:
        with open(filename) as file:
            lines = file.readlines()
            lines = [int(line.strip()) for line in lines if line]
            sorted_arrays.append(lines)

    return merge_sorted_arrays(sorted_arrays)


Case = namedtuple("Case", ["arrs", "expected"])


def test():
    cases = [
        Case(
            [[1, 2], [3, 4], [1, 3]],
            [1, 1, 2, 3, 3, 4],
        ),
        Case([[1, 2, 3], [], [1]], [1, 1, 2, 3]),
    ]

    for c in cases:
        actual = merge_sorted_arrays(c.arrs)
        assert actual == c.expected


def test_files():
    files = ["foo_1.txt", "foo_2.txt", "foo_3.txt"]
    cases = [Case(files, [1, 1, 1, 2, 2, 3, 4, 4, 5, 6])]

    for c in cases:
        actual = merge_sorted_files(c.arrs)
        assert actual == c.expected


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_arrays_merge.py", "sorted_arrays_merge.tsv", merge_sorted_arrays
        )
    )
