"""
Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""


class ListNode:
    def __init__(self, val, _next=None):
        self.val = val
        self.next = _next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    cur_node = head
    for i in range(n - 1):
        cur_node = cur_node.next

    if cur_node.next is None:  # we reached end of list and should delete head
        return head.next  # so just return new head

    # make one more step to store node, during following cycle, that is the previous one for node that we need to delete
    cur_node = cur_node.next

    prev_for_delete = head
    while cur_node.next:
        prev_for_delete = prev_for_delete.next
        cur_node = cur_node.next

    # remove needed node
    prev_for_delete.next = prev_for_delete.next.next

    return head


def main():
    node_4 = ListNode(5)
    node_3 = ListNode(4, node_4)
    node_2 = ListNode(3, node_3)
    node_1 = ListNode(2, node_2)
    head_node = ListNode(1, node_1)

    new_head = removeNthFromEnd(head_node, 2)
    _assert_single_linked_list(new_head, [1, 2, 3, 5])

    node_4 = ListNode(5)
    node_3 = ListNode(4, node_4)
    node_2 = ListNode(3, node_3)
    node_1 = ListNode(2, node_2)
    head_node = ListNode(1, node_1)

    new_head = removeNthFromEnd(head_node, 5)
    _assert_single_linked_list(new_head, [2, 3, 4, 5])

    head_node = ListNode(1)

    new_head = removeNthFromEnd(head_node, 1)
    _assert_single_linked_list(new_head, [])


def _assert_single_linked_list(head_node: ListNode, l: list):
    cur_node = head_node
    for i in l:
        assert cur_node.val == i
        cur_node = cur_node.next
    assert cur_node is None


if __name__ == '__main__':
    main()
