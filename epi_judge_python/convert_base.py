from test_framework import generic_test
import string
import functools


def to_int(s, base):
    result = power = 0
    s = list(reversed(s))
    for i in range(len(s)):
        result += base ** i * string.hexdigits.index(s[i].lower())
    return result


def to_base(num, base):
    if not num:
        # handle special case
        return "0"
    result = []
    while num:
        val = num % base
        result.append(string.hexdigits[val].upper())
        num //= base

    return "".join(reversed(result))


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    # return option1(num_as_string, b1, b2)
    return option2(num_as_string, b1, b2)


def option1(num_as_string: str, b1: int, b2: int) -> str:
    is_negative = num_as_string[0] == "-"
    n = to_int(num_as_string[1:], b1) if is_negative else to_int(num_as_string, b1)
    result = to_base(n, b2)
    return "-" + result if is_negative else result


def option2(num_as_string: str, b1: int, b2: int) -> str:
    def construct_from_base(num_as_int, base):
        return (
            ""
            if num_as_int == 0
            else construct_from_base(num_as_int // base, base)
            + string.hexdigits[num_as_int % base].upper()
        )

    is_negative = num_as_string[0] == "-"
    num_as_int = functools.reduce(
        lambda acc, c: acc * b1 + string.hexdigits.index(c.lower()),
        num_as_string[is_negative:],
        0,
    )

    return ("-" if is_negative else "") + (
        "0" if num_as_int == 0 else construct_from_base(num_as_int, b2)
    )


def test1():
    actual = option1("0", 6, 6)
    expected = "0"

    assert actual == expected


def testToInt():
    actual = to_int("1011", 2)
    expected = 11

    assert actual == expected


def testToBase():
    actual = to_base(11, 2)
    expected = "1011"

    assert actual == expected


def testConvertBase():
    actual = option1("615", 7, 13)
    expected = "1A7"

    assert actual == expected


def testConvertBaseNegative():
    actual = option1("-615", 7, 13)
    expected = "-1A7"

    assert actual == expected


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "convert_base.py", "convert_base.tsv", convert_base
        )
    )
