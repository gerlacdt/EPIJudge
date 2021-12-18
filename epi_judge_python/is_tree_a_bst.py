from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def str_bst(node):
    """String representation of a binary tree"""
    if not node:
        return "None"
    if not node.data:
        return "No data"
    return "{} ({} {})".format(node.data, rec_str(node.left), rec_str(node.right))


def is_bst_inorder(tree: BinaryTreeNode):
    result = []

    def helper(node):
        if not node:
            return
        helper(node.left)
        result.append(node.data)
        helper(node.right)

    helper(tree)
    return result == list(sorted(result))


def is_bst_preorder(tree: BinaryTreeNode) -> bool:
    def helper(node: BinaryTreeNode, node_min, node_max):
        if not node:
            return True
        if node.data < node_min or node.data > node_max:
            return False

        return helper(node.left, node_min, node.data) and helper(
            node.right, node.data, node_max
        )

    return helper(tree, float("-inf"), float("inf"))


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    return is_bst_preorder(tree)
    # return is_bst_inorder(tree)
    # return is_bst_postorder(tree)


def is_bst_postorder(tree: BinaryTreeNode) -> bool:
    if not tree:
        return True

    def helper(node):
        if node.left:
            left, left_max, left_min = helper(node.left)
            if not left:
                return False, 0, 1

        if node.right:
            right, right_max, right_min = helper(node.right)
            if not right:
                return False, 0, 1

        if node.left and node.right:
            if left_max <= node.data and right_min >= node.data:
                return (
                    True,
                    max([node.data, right_max]),
                    min([node.data, left_min]),
                )
            else:
                return False, 2, 3
        elif node.left:
            if left_max <= node.data:
                return True, node.data, min(node.data, left_min)
            else:
                return False, 4, 5
        elif node.right:
            if right_min >= node.data:
                return True, max(node.data, right_max), node.data
            else:
                return False, 6, 7
        else:
            return True, node.data, node.data

    is_bst, _, _ = helper(tree)
    return is_bst


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_a_bst.py", "is_tree_a_bst.tsv", is_binary_tree_bst
        )
    )
