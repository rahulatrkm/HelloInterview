"""
Palindrome Linked List (Easy)
https://www.hellointerview.com/learn/code/linked-list/palindrome-linked-list

Given a reference head of type ListNode that is the head of a singly linked list,
determine if the linked list is a palindrome. An empty list is considered a palindrome.

Example 1:
  Input: 5 -> 4 -> 3 -> 4 -> 5
  Output: True

Example 2:
  Input: 5 -> 4 -> 3
  Output: False

Approach (Optimal O(1) space):
  - Use fast/slow pointers to find the middle.
  - Reverse the second half of the list.
  - Compare first half and reversed second half node by node.
"""

from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


def build_list(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([5, 4, 3, 4, 5], True),
        ([5, 4, 3], False),
        ([], True),
        ([1], True),
        ([1, 1], True),
        ([1, 2], False),
        ([1, 2, 1], True),
        ([1, 2, 2, 1], True),
        ([1, 2, 3, 1], False),
    ]
    for i, (vals, expected) in enumerate(tests):
        head = build_list(vals)
        result = sol.isPalindrome(head)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {vals} | Expected: {expected} | Got: {result}")
