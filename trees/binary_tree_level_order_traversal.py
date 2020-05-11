"""
Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def levelOrder(root: TreeNode) -> List[List[int]]:
    res = []
    if not root:
        return res

    queue = deque((root, ))
    while queue:
        res.append([])
        for i in range(len(queue)):
            node = queue.popleft()
            res[-1].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return res


def main():
    _l = [3, 9, 20, None, None, 15, 7]
    root = create_binary_tree(_l)

    assert levelOrder(root) == [
        [3],
        [9, 20],
        [15, 7],
    ]


def create_binary_tree(l: list) -> Optional[TreeNode]:
    root = None
    prev_row = []
    while l:
        if prev_row:
            source_len = len(prev_row) * 2
            source, l = l[:source_len], l[source_len:]
            new_row = []
            for node in prev_row:
                for attr in ('left', 'right'):
                    try:
                        val = source.pop(0)
                    except IndexError:
                        val = None
                    if val:
                        new_node = TreeNode(val)
                        setattr(node, attr, new_node)
                        new_row.append(new_node)
            prev_row = new_row
        else:
            val, l = l[0], l[1:]
            root = TreeNode(val=val)
            prev_row = [root]

    return root


if __name__ == '__main__':
    main()
