from test_framework import generic_test
from test_framework.test_failure import TestFailure

from collections import namedtuple
from typing import List

Element = namedtuple("Element", ["value", "localMax"])


class Stack:
    def __init__(self):
        self._data: List[Element] = []

    def empty(self) -> bool:
        return True if not self._data else False

    def max(self) -> int:
        return self._data[-1].localMax

    def pop(self) -> int:
        return self._data.pop().value

    def push(self, x: int) -> None:
        if not self._data:
            self._data.append(Element(x, x))
        else:
            self._data.append(Element(x, max(x, self._data[-1].localMax)))


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == "Stack":
                s = Stack()
            elif op == "push":
                s.push(arg)
            elif op == "pop":
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result)
                    )
            elif op == "max":
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result)
                    )
            elif op == "empty":
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result)
                    )
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure("Unexpected IndexError exception")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "stack_with_max.py", "stack_with_max.tsv", stack_tester
        )
    )
