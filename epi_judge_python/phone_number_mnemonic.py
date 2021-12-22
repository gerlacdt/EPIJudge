from typing import List

from test_framework import generic_test, test_utils


NUMBER_MAPPINGS = {
    "0": "0",
    "1": "1",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
}


def recursive(phone_number: str) -> List[str]:
    result = []

    def helper(rest, assignment):
        if not rest:
            result.append("".join(assignment))
            return
        number = rest[0]
        for c in NUMBER_MAPPINGS[number]:
            helper(rest[1:], assignment + [c])

    helper(phone_number, [])
    return result


def iterative(phone_number: str) -> List[str]:
    result: List[str] = []

    # fill frontier with start values
    frontier: List = [(phone_number[1:], [c]) for c in NUMBER_MAPPINGS[phone_number[0]]]

    while frontier:
        rest, assignment = frontier.pop()
        if not rest:
            result.append("".join(assignment))
            continue
        for c in NUMBER_MAPPINGS[rest[0]]:
            frontier.append((rest[1:], assignment + [c]))

    return result


def phone_mnemonic(phone_number: str) -> List[str]:
    # return recursive(phone_number)
    return iterative(phone_number)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            "phone_number_mnemonic.tsv",
            phone_mnemonic,
            comparator=test_utils.unordered_compare,
        )
    )
