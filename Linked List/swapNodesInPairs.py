"""
Swap Nodes in Pairs (Medium)
https://www.hellointerview.com/learn/code/linked-list/swap-nodes-in-pairs

Given a reference head of type ListNode that is the head of a singly linked list,
swap every two adjacent nodes and return its head. You must solve the problem
without modifying the values in the list's nodes (only nodes themselves may be changed).

Example 1:
  Input:  5 -> 4 -> 3 -> 2 -> 1
  Output: 4 -> 5 -> 2 -> 3 -> 1

Example 2:
  Input:  1 -> 2 -> 3 -> 4
  Output: 2 -> 1 -> 4 -> 3

Approach:
  - Use a dummy node pointing to head.
  - Iterate in pairs: for each pair (first, second), update 3 pointers:
    prev.next = second, first.next = second.next, second.next = first.
  - Advance prev to first (which is now second in the swapped pair).
"""

from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        first = head
        while first and first.next:
            second = first.next
            first.next = second.next
            second.next = first
            if prev:
                prev.next = second
            else:
                head = second
            prev = first
            first = first.next
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
        ([5, 4, 3, 2, 1], [4, 5, 2, 3, 1]),
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3], [2, 1, 3]),
        ([1, 2, 3, 4, 5, 6], [2, 1, 4, 3, 6, 5]),
    ]
    for i, (vals, expected) in enumerate(tests):
        head = build_list(vals)
        result = list_to_arr(sol.swapPairs(head))
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {vals} | Expected: {expected} | Got: {result}")
