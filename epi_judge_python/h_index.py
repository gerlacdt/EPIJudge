from typing import List
from collections import namedtuple

from test_framework import generic_test


def h_index(citations: List[int]) -> int:
    if not citations:
        return 0
    citations.sort()
    hindices = []
    n = len(citations)
    for i, cit in enumerate(citations):
        diff = n - i
        hindices.append(min(cit, diff))
    return max(hindices)


Case = namedtuple("Case", ["citations", "expected"])


def test():
    cases = [
        Case([], 0),
        Case([1, 4, 1, 4, 2, 1, 3, 5, 6], 4),
        Case([100], 1),
        Case([0], 0),
        Case([1, 2], 1),
    ]
    for c in cases:
        actual = h_index(c.citations)
        assert actual == c.expected


if __name__ == "__main__":
    exit(generic_test.generic_test_main("h_index.py", "h_index.tsv", h_index))
