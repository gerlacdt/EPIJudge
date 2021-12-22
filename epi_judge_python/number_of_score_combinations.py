from typing import List
from functools import lru_cache

from test_framework import generic_test


def coins(target: int):
    start_coins = [1, 5, 10, 25, 50]

    def helper(rest, coins):
        if rest == 0:
            return 1
        elif rest < 0 or not coins:
            return 0
        return helper(rest - coins[-1], coins) + helper(rest, coins[:-1])

    return helper(target, start_coins)


def recursive(final_score: int, individual_play_scores: List[int]) -> int:
    @lru_cache(maxsize=None)
    def helper(rest, scores):
        if rest == 0:
            return 1
        elif rest < 0 or not scores:
            return 0
        return helper(rest - scores[-1], scores) + helper(rest, tuple(scores[:-1]))

    return helper(final_score, tuple(sorted(individual_play_scores)))


def dp(final_score: int, individual_play_scores: List[int]) -> int:
    # initialize dp cache
    m = len(individual_play_scores)
    n = final_score + 1
    table = [[0 for _ in range(n)] for row in range(m)]
    for row in table:
        # if we hit a score of zero then it's a solution
        row[0] = 1

    # fill dp cache
    for i in range(m):
        for j in range(1, n):
            # if we are in first row, previous_scores are zero
            previous_scores = table[i - 1][j] if i > 0 else 0
            current_scores = (
                table[i][j - individual_play_scores[i]]
                if j >= individual_play_scores[i]
                else 0
            )
            table[i][j] = previous_scores + current_scores
    return table[m - 1][n - 1]


def num_combinations_for_final_score(
    final_score: int, individual_play_scores: List[int]
) -> int:
    # return recursive(final_score, individual_play_scores)
    return dp(final_score, individual_play_scores)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "number_of_score_combinations.py",
            "number_of_score_combinations.tsv",
            num_combinations_for_final_score,
        )
    )


def test_coins():
    actual = coins(100)
    expected = 292

    assert actual == expected


def test_recursive():
    actual = recursive(12, [2, 3, 7])
    expected = 4

    assert actual == expected


def test_dp():
    actual = dp(12, [2, 3, 7])
    expected = 4

    assert actual == expected


def test_dp_coins():
    start_coins = [1, 5, 10, 25, 50]
    actual = dp(100, start_coins)
    expected = 292

    assert actual == expected
