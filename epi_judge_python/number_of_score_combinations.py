from typing import List

from test_framework import generic_test


def dp(final_score: int, individual_play_scores: List[int]) -> int:
    return 0


def num_combinations_for_final_score(
    final_score: int, individual_play_scores: List[int]
) -> int:
    return dp(final_score, individual_play_scores)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "number_of_score_combinations.py",
            "number_of_score_combinations.tsv",
            num_combinations_for_final_score,
        )
    )
