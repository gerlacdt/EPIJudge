from test_framework import generic_test

from collections import Counter
import re


def is_letter_constructible_from_magazine(letter_text: str, magazine_text: str) -> bool:
    pattern = re.compile(r"\s+")
    letter_text = re.sub(pattern, "", letter_text)
    letterTable = Counter(letter_text)
    magazine_text = re.sub(pattern, "", magazine_text)
    magazineTable = Counter(magazine_text)

    for c, val in letterTable.items():
        if c not in magazineTable:
            return False
        if magazineTable[c] < val:
            return False
    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_anonymous_letter_constructible.py",
            "is_anonymous_letter_constructible.tsv",
            is_letter_constructible_from_magazine,
        )
    )
