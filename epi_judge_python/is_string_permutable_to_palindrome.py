from test_framework import generic_test

from collections import namedtuple, Counter


def can_form_palindrome(s: str) -> bool:
    charSums = Counter(s)
    return sum([1 for occurences in charSums.values() if occurences % 2 != 0]) <= 1


Case = namedtuple("Case", ["s", "expected"])


def test():
    cases = [Case("aabbc", True), Case("bbaacc", True), Case("fooboo", False)]
    for c in cases:
        actual = can_form_palindrome(c.s)
        assert actual == c.expected, "Case: {}".format(c.s)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            "is_string_permutable_to_palindrome.tsv",
            can_form_palindrome,
        )
    )
