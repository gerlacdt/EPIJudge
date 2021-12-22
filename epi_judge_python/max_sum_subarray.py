from typing import List

from test_framework import generic_test


def dp(A: List[int]):
    if not A:
        return 0
    table: List[int] = [0] * len(A)
    table[0] = A[0]
    for i in range(1, len(A)):
        table[i] = max(table[i - 1] + A[i], A[i])

    return max(table) if max(table) > 0 else 0


def dp_constant_space(A: List[int]):
    current_max = total_max = 0
    for a in A:
        current_max = max(current_max + a, a)
        total_max = max(total_max, current_max)

    return total_max


def find_maximum_subarray(A: List[int]) -> int:
    return dp(A)
    # return dp_constant_space(A)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "max_sum_subarray.py", "max_sum_subarray.tsv", find_maximum_subarray
        )
    )
