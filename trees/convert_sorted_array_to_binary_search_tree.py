"""
Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    if not nums:
        return None

    middle = len(nums) // 2
    left_part, right_part = nums[:middle], nums[middle:]
    val = right_part.pop(0)
    root = TreeNode(val)
    root.left = sortedArrayToBST(left_part)
    root.right = sortedArrayToBST(right_part)
    return root


def main():
    nums = [-10, -3, 0, 5, 9]
    root = sortedArrayToBST(nums)
    assert isValidBST(root)
    assert maxDepth(root) - minDepth(root) <= 1


def maxDepth(root: TreeNode) -> int:
    if root is None:
        return 0

    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) + 1


def minDepth(root: TreeNode) -> int:
    if root is None:
        return 0

    left_depth = minDepth(root.left)
    right_depth = minDepth(root.right)
    return min(left_depth, right_depth) + 1


def isValidBST(root: TreeNode) -> bool:
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


if __name__ == '__main__':
    main()
