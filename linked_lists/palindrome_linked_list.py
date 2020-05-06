"""
Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""


class ListNode:
    def __init__(self, val, _next=None):
        self.val = val
        self.next = _next


def isPalindrome(head: ListNode) -> bool:
    length = 0
    node = head
    while node:
        length += 1
        node = node.next

    if length <= 1:
        return True

    # revert suffix
    suffix_pos = (length + 1) // 2
    node = head
    for i in range(suffix_pos):
        node = node.next
    suffix_start_node = node

    cur_node = suffix_start_node
    prev_node = None
    while True:
        next_node = cur_node.next
        cur_node.next = prev_node
        if not next_node:
            break
        prev_node = cur_node
        cur_node = next_node

    revert_suffix_head = cur_node

    # determine is palindrome
    prefix_node = head
    suffix_node = revert_suffix_head
    while suffix_node:
        if prefix_node.val != suffix_node.val:
            return False
        prefix_node = prefix_node.next
        suffix_node = suffix_node.next

    return True


def main():
    node_1 = ListNode(2)
    head_node = ListNode(1, node_1)

    assert not isPalindrome(head_node)

    node_3 = ListNode(1)
    node_2 = ListNode(2, node_3)
    node_1 = ListNode(2, node_2)
    head_node = ListNode(1, node_1)

    assert isPalindrome(head_node)


if __name__ == '__main__':
    main()
