"""
Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: TreeNode) -> int:
    if root is None:
        return 0

    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) + 1


def main():
    _l = [3, 9, 20, None, None, 15, 7]
    root = create_binary_tree(_l)

    assert maxDepth(root) == 3


def create_binary_tree(l: list) -> TreeNode:
    def _get_or_create_node_by_number(_root: TreeNode, n: int) -> TreeNode:
        if n == 0:
            return _root
        n = n - 1
        is_right = n % 2
        prev_node = _get_or_create_node_by_number(_root, n // 2)
        if is_right:
            if not prev_node.right:
                prev_node.right = TreeNode()
            return prev_node.right
        else:
            if not prev_node.left:
                prev_node.left = TreeNode()
            return prev_node.left

    root = TreeNode()
    for i, val in enumerate(l):
        if val is not None:
            _node = _get_or_create_node_by_number(root, i)
            _node.val = val

    return root


if __name__ == '__main__':
    main()
