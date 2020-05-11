"""
Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Follow up: Solve it both recursively and iteratively.
"""
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def isSymmetric_iter(root: TreeNode) -> bool:
    queue = deque((root, root))
    while queue:
        first = queue.popleft()
        second = queue.popleft()

        if not first and not second:
            continue
        if not first or not second or first.val != second.val:
            return False

        queue.append(first.left)
        queue.append(second.right)
        queue.append(first.right)
        queue.append(second.left)

    return True


def isSymmetric_rec(root: TreeNode) -> bool:

    def compare(first, second):
        if not first and not second:
            return True
        if not first or not second or first.val != second.val:
            return False
        return compare(first.left, second.right) and compare(first.right, second.left)

    return compare(root, root)


def main():
    for isSymmetric in (isSymmetric_iter, isSymmetric_rec):
        _l = [1, 2, 2, 3, 4, 4, 3]
        root = create_binary_tree(_l)

        assert isSymmetric(root)

        _l = [1, 2, 2, None, 3, None, 3]
        root = create_binary_tree(_l)

        assert not isSymmetric(root)

        _l = [1, 2, 2, None, 3, 3]
        root = create_binary_tree(_l)

        assert isSymmetric(root)

        _l = [7, 10, 10, None, 22, 22, None, -8, 35, 35, -8, None, 57, -66, 26, 26, -66, 57]
        root = create_binary_tree(_l)

        assert isSymmetric(root)


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
