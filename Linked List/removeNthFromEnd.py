"""
Remove Nth Node From End of List (Medium)
https://www.hellointerview.com/learn/code/linked-list/remove-nth-node-from-end-of-list

Given a reference head of type ListNode that is the head of a singly linked list
and an integer n, remove the n-th node from the end of the list and return the
head of the modified list. n is guaranteed to be between 1 and the length of the list.

Example 1:
  Input: [5, 4, 3, 2, 1], n = 2
  Output: [5, 4, 3, 1]

Example 2:
  Input: [5, 4, 3, 2, 1], n = 5
  Output: [4, 3, 2, 1]

Approach:
  - Use a dummy node to handle edge case of removing head.
  - Use two pointers: advance fast n steps ahead of slow.
  - Move both until fast reaches the last node.
  - slow.next = slow.next.next removes the target node.
"""

from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head


def build_list(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def list_to_arr(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([5, 4, 3, 2, 1], 2, [5, 4, 3, 1]),
        ([5, 4, 3, 2, 1], 5, [4, 3, 2, 1]),
        ([5, 4, 3, 2, 1], 1, [5, 4, 3, 2]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3], 2, [1, 3]),
    ]
    for i, (vals, n, expected) in enumerate(tests):
        head = build_list(vals)
        result = list_to_arr(sol.removeNthFromEnd(head, n))
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {vals}, n={n} | Expected: {expected} | Got: {result}")
