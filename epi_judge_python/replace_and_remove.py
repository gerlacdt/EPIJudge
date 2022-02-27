import functools
from typing import List
from collections import namedtuple, deque

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    # return my_solution(size, s)
    return book_solution(size, s)


def my_solution(size: int, s: List[str]) -> int:
    result = []
    for i in range(size):
        c = s[i]
        if c == "a":
            result.append("d")
            result.append("d")
        elif c == "b":
            continue
        else:
            result.append(c)

    for i, c in enumerate(result):
        s[i] = result[i]

    return len(result)


def book_solution(size: int, s: List[str]) -> int:
    # forward iteration; remove b's and count the number of a's
    write_idx = a_count = 0
    for i in range(size):
        if s[i] != "b":
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == "a":
            a_count += 1

    # backward iteration; replace a's with dd's starting from end
    cur_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1
    while cur_idx >= 0:
        if s[cur_idx] == "a":
            s[write_idx] = "d"
            s[write_idx - 1] = "d"
            write_idx -= 2
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1
        cur_idx -= 1

    return final_size


Case = namedtuple("Case", ["size", "s", "expected"])


def test():
    cases = [Case(1, list("acdbbca"), list("ddcdcdd"))]

    for c in cases:
        actual = replace_and_remove(c.size, c.s)
        print(c.s)
        assert c.s == list(c.expected)


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "replace_and_remove.py",
            "replace_and_remove.tsv",
            replace_and_remove_wrapper,
        )
    )
