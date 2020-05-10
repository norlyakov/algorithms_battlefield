"""
Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST_common(root: TreeNode) -> bool:

    def _is_valid_bst(node, less_than=float('inf'), more_than=float('-inf')):
        if not node:
            return True
        if node.val <= more_than or node.val >= less_than:
            return False
        return (
                _is_valid_bst(node.left, less_than=node.val, more_than=more_than)
                and
                _is_valid_bst(node.right, less_than=less_than, more_than=node.val)
        )

    return _is_valid_bst(root)


def isValidBST_inorder_rec(root: TreeNode) -> bool:
    more_than = float('-inf')

    def _is_valid_bst(node):
        if not node:
            return True

        if not _is_valid_bst(node.left):
            return False

        nonlocal more_than
        if node.val <= more_than:
            return False
        more_than = node.val

        return _is_valid_bst(node.right)

    return _is_valid_bst(root)


def isValidBST_inorder_stack(root: TreeNode) -> bool:
    stack = []
    more_than = float('-inf')

    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()

        if node.val <= more_than:
            return False
        more_than = node.val
        node = node.right

    return True


def main():
    for isValidBST in (isValidBST_common, isValidBST_inorder_rec, isValidBST_inorder_stack):
        _l = [5, 1, 4, None, None, 3, 6]
        root = create_binary_tree(_l)

        assert not isValidBST(root)

        _l = [3, 1, 5, 0, 2, 4, 6, None, None, None, 3]
        root = create_binary_tree(_l)

        assert not isValidBST(root)

        _l = [10, 5, 15, None, None, 6, 20]
        root = create_binary_tree(_l)

        assert not isValidBST(root)

        _l = [2, 1, 3]
        root = create_binary_tree(_l)

        assert isValidBST(root)


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
