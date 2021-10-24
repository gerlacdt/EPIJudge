from test_framework import generic_test
from test_framework.test_failure import TestFailure

from collections import namedtuple
from typing import List


def int_to_string(x: int) -> str:
    if x == 0:
        return "0"
    isPositive = True if x >= 0 else False
    result: List[str] = []

    chars = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
    }

    if not isPositive:
        x = -x
    while x > 0:
        digit = x % 10
        result.append(chars[digit])
        x //= 10

    result.reverse()
    return "".join(result) if isPositive else "-" + "".join(result)


def string_to_int(s: str) -> int:
    if not s:
        raise RuntimeError("Given string is not None")
    isNegative = True if s[0] == "-" else False
    if isNegative:
        s = s[1:]  # remove - sign
    if s[0] == "+":
        s = s[1:]  # remove + sign

    digits = {
        ord("0"): 0,
        ord("1"): 1,
        ord("2"): 2,
        ord("3"): 3,
        ord("4"): 4,
        ord("5"): 5,
        ord("6"): 6,
        ord("7"): 7,
        ord("8"): 8,
        ord("9"): 9,
    }

    result = 0
    for i, c in enumerate(reversed(s)):
        result += 10 ** i * digits[ord(c)]

    return -result if isNegative else result


Case = namedtuple("Case", ["x", "expected"])


def testToString():
    cases = [
        Case(12, "12"),
        Case(-12, "-12"),
        Case(1, "1"),
        Case(0, "0"),
    ]

    for c in cases:
        actual = int_to_string(c.x)
        assert actual == c.expected


def testToInt():
    cases = [
        Case("0", 0),
        Case("1", 1),
        Case("123", 123),
        Case("-123", -123),
        Case("+123", 123),
    ]

    for c in cases:
        actual = string_to_int(c.x)
        assert actual == c.expected


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "string_integer_interconversion.py",
            "string_integer_interconversion.tsv",
            wrapper,
        )
    )
