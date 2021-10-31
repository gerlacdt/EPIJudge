from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


from collections import namedtuple


def toStr(node: BinaryTreeNode) -> str:
    if not node:
        return "NONE"
    return "{} ({} {})".format(node.data, toStr(node.left), toStr(node.right))


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    result = True
    # print("tree: {}".format(toStr(tree)))

    def helper(node: BinaryTreeNode) -> int:
        nonlocal result
        if not node:
            return 0
        leftHeight = helper(node.left)
        rightHeight = helper(node.right)
        if abs(leftHeight - rightHeight) > 1:
            # sub-tree not balanced
            result = False
        return 1 + max(leftHeight, rightHeight)

    helper(tree)
    return result


Case = namedtuple("Case", ["tree", "expected"])


def test():
    cases = [
        Case(
            BinaryTreeNode(
                4,
                BinaryTreeNode(-4, None, BinaryTreeNode(7)),
                BinaryTreeNode(2, BinaryTreeNode(1, None, BinaryTreeNode(6))),
            ),
            False,
        )
    ]

    for c in cases:
        actual = is_balanced_binary_tree(c.tree)
        assert actual == c.expected


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_balanced.py", "is_tree_balanced.tsv", is_balanced_binary_tree
        )
    )
