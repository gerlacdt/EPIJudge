from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    def helper(node, mirror):
        if mirror is None and node is None:
            return True
        elif node is None or mirror is None:
            return False
        leftSubtree = helper(node.left, mirror.right)
        rightSubtree = helper(node.right, mirror.left)
        return leftSubtree and rightSubtree and (node.data == mirror.data)

    return helper(tree, tree)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_symmetric.py", "is_tree_symmetric.tsv", is_symmetric
        )
    )
