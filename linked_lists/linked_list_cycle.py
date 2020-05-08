"""
Linked List Cycle

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


Follow up:

Can you solve it using O(1) (i.e. constant) memory?
"""


class ListNode:
    def __init__(self, val, _next=None):
        self.val = val
        self.next = _next


def hasCycle_first(head: ListNode) -> bool:
    """
    This function takes only one iteration, but it changes the list
    """
    if head:
        prev_node = None
        cur_node = head
        while cur_node.next:
            if cur_node.next is head:
                return True
            _next = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = _next

    return False


def hasCycle_second(head: ListNode) -> bool:
    """
    This function uses two pointers
    """
    if head:
        slow_pntr = fast_pntr = head
        while fast_pntr and fast_pntr.next:
            slow_pntr = slow_pntr.next
            fast_pntr = fast_pntr.next.next
            if slow_pntr is fast_pntr:
                return True

    return False


def main():
    for hasCycle in (hasCycle_first, hasCycle_second):
        node_3 = ListNode(2)
        node_2 = ListNode(2, node_3)
        node_1 = ListNode(2, node_2)
        head_node = ListNode(1, node_1)
        node_3.next = node_1

        assert hasCycle(head_node)

        node_1 = ListNode(2, node_2)
        head_node = ListNode(1, node_1)
        node_1.next = head_node

        assert hasCycle(head_node)

        head_node = ListNode(1)

        assert not hasCycle(head_node)

        head_node = ListNode(1)
        head_node.next = head_node

        assert hasCycle(head_node)


if __name__ == '__main__':
    main()
