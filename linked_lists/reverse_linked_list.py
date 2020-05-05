"""
Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


class ListNode:
    def __init__(self, val, _next=None):
        self.val = val
        self.next = _next


def reverseListIter(head: ListNode) -> ListNode:
    prev_node = None
    cur_node = head
    while cur_node:
        _node = cur_node.next
        cur_node.next = prev_node
        prev_node = cur_node
        cur_node = _node

    return prev_node


def reverseListRecursion(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    new_head = reverseListRecursion(head.next)
    head.next.next = head
    head.next = None
    return new_head


def main():
    for reverse_func in (reverseListRecursion, reverseListIter):
        node_4 = ListNode(5)
        node_3 = ListNode(4, node_4)
        node_2 = ListNode(3, node_3)
        node_1 = ListNode(2, node_2)
        head_node = ListNode(1, node_1)

        new_head = reverse_func(head_node)
        _assert_single_linked_list(new_head, [5, 4, 3, 2, 1])

        head_node = ListNode(1)

        new_head = reverse_func(head_node)
        _assert_single_linked_list(new_head, [1])


def _assert_single_linked_list(head_node: ListNode, l: list):
    cur_node = head_node
    for i in l:
        assert cur_node.val == i
        cur_node = cur_node.next
    assert cur_node is None


if __name__ == '__main__':
    main()
