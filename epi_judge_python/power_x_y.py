from test_framework import generic_test
from collections import namedtuple


def power(x: float, y: int) -> float:
    result, power = 1.0, y
    if y < 0:
        x, power = 1 / x, -y  # make base 1/x and exponent positive
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    return result


Case = namedtuple("Case", ["x", "y", "expected"])


def test():
    cases = [
        Case(2, 1, 2.0),
        Case(2, 4, 16.0),
        Case(2, 3, 8.0),
        Case(2, 5, 32.0),
        Case(2, -2, 0.25),
        Case(2, -1, 0.5),
    ]
    for c in cases:
        actual = power(c.x, c.y)
        assert actual == c.expected, "Case: {}".format(c)


if __name__ == "__main__":
    exit(generic_test.generic_test_main("power_x_y.py", "power_x_y.tsv", power))
