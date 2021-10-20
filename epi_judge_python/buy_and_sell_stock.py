from typing import List
from collections import namedtuple

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    total = 0.0
    current_min = prices[0]
    for i in range(1, len(prices)):
        current = prices[i]
        if current > current_min:
            total = max(total, current - current_min)
        else:
            current_min = current
    return total


def option1(prices: List[float]) -> float:
    total = 0.0
    for i in range(len(prices)):
        current = prices[i]
        for j in range(i + 1, len(prices)):
            profit = prices[j] - current
            if profit > total:
                total = profit
    return total


Case = namedtuple("Case", ["prices", "expected"])


def test():

    cases = [
        Case(
            [310, 315, 275, 295, 260, 270, 290, 230, 255, 250],
            30,
        )
    ]

    for c in cases:
        actual = buy_and_sell_stock_once(c.prices)
        assert actual == c.expected, "Case: {}".format(c.prices)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "buy_and_sell_stock.py", "buy_and_sell_stock.tsv", buy_and_sell_stock_once
        )
    )
