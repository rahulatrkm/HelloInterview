"""
Reorder List (Medium)
https://www.hellointerview.com/learn/code/linked-list/reorder-list

Given a reference head of type ListNode that is the head of a singly linked list,
reorder the list in-place such that the nodes are reordered to:
  1st -> last -> 2nd -> 2nd-to-last -> 3rd -> ...

Example 1:
  Input:  5 -> 4 -> 3 -> 2 -> 1
  Output: 5 -> 1 -> 4 -> 2 -> 3

Example 2:
  Input:  0 -> 1 -> 2
  Output: 0 -> 2 -> 1

Approach:
  1. Find the middle of the linked list (fast/slow pointers).
  2. Reverse the second half of the list.
  3. Merge the first half and reversed second half alternately.
"""

from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow
        while curr:
            ne = curr.next
            curr.next = prev
            prev = curr
            curr = ne
        
        left, right = head, prev
        while right.next:
            left.next, left = right, left.next
            right.next, right = left, right.next
        
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
        ([5, 4, 3, 2, 1], [5, 1, 4, 2, 3]),
        ([0, 1, 2], [0, 2, 1]),
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 2, 3], [1, 3, 2]),
        ([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4]),
    ]
    for i, (vals, expected) in enumerate(tests):
        head = build_list(vals)
        sol.reorderList(head)
        result = list_to_arr(head)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {vals} | Expected: {expected} | Got: {result}")
