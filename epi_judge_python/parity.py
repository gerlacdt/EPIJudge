from test_framework import generic_test
from collections import namedtuple


def parity(x: int) -> int:
    """Naive solution with linear time complexity O(n), i.e. n are the
    number of bits like 64-bits.
    """
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


def parity2(x: int) -> int:
    """Uses XOR with better runtime complexity. If number of 1s are k,
    then it runs in O(k)."""
    result = 0
    while x:
        x &= x - 1
        result ^= 1
    return result


Case = namedtuple("Case", ["x", "expected"])


def test():
    cases = [Case(8, 1), Case(7, 1), Case(6, 0)]
    for c in cases:
        actual = parity(c.x)
        assert actual == c.expected


if __name__ == "__main__":
    exit(generic_test.generic_test_main("parity.py", "parity.tsv", parity))
