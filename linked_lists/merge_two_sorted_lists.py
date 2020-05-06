"""
Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


class ListNode:
    def __init__(self, val, _next=None):
        self.val = val
        self.next = _next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    if not l2:
        return l1

    first_pointer = l1
    second_pointer = l2

    head_node = ListNode('dummy')
    cur_node = head_node
    while first_pointer or second_pointer:
        if not first_pointer or (second_pointer and first_pointer.val > second_pointer.val):
            cur_node.next = ListNode(second_pointer.val)
            second_pointer = second_pointer.next
        else:
            cur_node.next = ListNode(first_pointer.val)
            first_pointer = first_pointer.next

        cur_node = cur_node.next

    return head_node.next


def main():
    head_node1 = ListNode(2)

    head_node2 = ListNode(1)

    new_head = mergeTwoLists(head_node1, head_node2)
    _assert_single_linked_list(new_head, [1, 2])

    node_2 = ListNode(4)
    node_1 = ListNode(2, node_2)
    head_node1 = ListNode(1, node_1)

    node_2 = ListNode(4)
    node_1 = ListNode(3, node_2)
    head_node2 = ListNode(1, node_1)

    new_head = mergeTwoLists(head_node1, head_node2)
    _assert_single_linked_list(new_head, [1, 1, 2, 3, 4, 4])




def _assert_single_linked_list(head_node: ListNode, l: list):
    cur_node = head_node
    for i in l:
        assert cur_node.val == i
        cur_node = cur_node.next
    assert cur_node is None


if __name__ == '__main__':
    main()
