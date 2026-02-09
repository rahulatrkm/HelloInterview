"""
Linked List Cycle (Easy)
https://www.hellointerview.com/learn/code/linked-list/linked-list-cycle

Given a reference head of type ListNode that is the head of a linked list,
return True if the linked list contains a cycle, and False otherwise,
without modifying the linked list in any way.

Example 1:
  Input: [5, 4, 3, 2, 0], tail connects to index 2
  Output: True (cycle between node 0 and node 3)

Example 2:
  Input: [5, 4, 3, 2, 0], no cycle
  Output: False

Approach:
  - Use fast and slow pointers.
  - slow advances 1 step, fast advances 2 steps.
  - If they meet, there's a cycle. If fast reaches None, no cycle.
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


def build_list_with_cycle(vals, cycle_index):
    """Build linked list; last node connects to node at cycle_index (-1 = no cycle)."""
    if not vals:
        return None
    nodes = [ListNode(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if cycle_index >= 0:
        nodes[-1].next = nodes[cycle_index]
    return nodes[0]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        # (vals, cycle_index, expected)
        ([5, 4, 3, 2, 0], 2, True),
        ([5, 4, 3, 2, 0], -1, False),
        ([1], 0, True),
        ([1], -1, False),
        ([], -1, False),
        ([1, 2], 0, True),
        ([1, 2], -1, False),
        ([5, 4, 3, 2], 0, True),
    ]
    for i, (vals, cycle_idx, expected) in enumerate(tests):
        head = build_list_with_cycle(vals, cycle_idx)
        result = sol.hasCycle(head)
        status = "✓" if result == expected else "✗"
        cycle_str = f"cycle at {cycle_idx}" if cycle_idx >= 0 else "no cycle"
        print(f"Test {i+1}: {status} | Input: {vals}, {cycle_str} | Expected: {expected} | Got: {result}")
