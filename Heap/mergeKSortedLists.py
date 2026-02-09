"""
Merge K Sorted Lists
https://www.hellointerview.com/learn/code/heap/merge-k-sorted-lists

Given k linked lists, each sorted in ascending order, merge them into one sorted
linked list and return it.

Example 1:
  Input: lists = [[3,4,6],[2,3,5],[-1,6]]
    3 -> 4 -> 6
    2 -> 3 -> 5
   -1 -> 6
  Output: [-1,2,3,3,4,5,6,6]
   -1 -> 2 -> 3 -> 3 -> 4 -> 5 -> 6 -> 6

Approach:
- Use a min-heap of size k
- Initialize heap with the head node of each list: (value, list_index, node)
- Repeatedly pop smallest, append to result, push next node from same list
- Use a counter as tiebreaker to avoid comparing ListNode objects

Time: O(n log k) where n = total elements, k = number of lists
Space: O(k) for the heap
"""

from typing import List
import heapq

class Solution:
    def mergeKLists(self, lists: List[List[int]]) -> List[int]:
        ans = []
        hq = [(nums[0], i, 0) for i, nums in enumerate(lists) if nums]
        heapq.heapify(hq)
        while hq:
            val, list_idx, node_idx = heapq.heappop(hq)
            ans.append(val)
            if node_idx + 1 < len(lists[list_idx]):
                heapq.heappush(hq, (lists[list_idx][node_idx+1], list_idx, node_idx+1))
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Basic case
    result = sol.mergeKLists([[3,4,6],[2,3,5],[-1,6]])
    assert result == [-1,2,3,3,4,5,6,6], f"Test 1 failed: got {result}"
    print("Test 1 passed ✓")

    # Test 2: Single list
    result = sol.mergeKLists([[1,2,3]])
    assert result == [1,2,3], f"Test 2 failed: got {result}"
    print("Test 2 passed ✓")

    # Test 3: Empty input
    result = sol.mergeKLists([])
    assert result == [], f"Test 3 failed: got {result}"
    print("Test 3 passed ✓")

    # Test 4: Lists with empty lists
    result = sol.mergeKLists([[], [1], []])
    assert result == [1], f"Test 4 failed: got {result}"
    print("Test 4 passed ✓")

    # Test 5: Two lists
    result = sol.mergeKLists([[1,4,5],[1,3,4]])
    assert result == [1,1,3,4,4,5], f"Test 5 failed: got {result}"
    print("Test 5 passed ✓")

    # Test 6: All single-element lists
    result = sol.mergeKLists([[5],[2],[8],[1]])
    assert result == [1,2,5,8], f"Test 6 failed: got {result}"
    print("Test 6 passed ✓")

    # Test 7: Lists of different lengths
    result = sol.mergeKLists([[1,2,3,4,5],[10],[6,7]])
    assert result == [1,2,3,4,5,6,7,10], f"Test 7 failed: got {result}"
    print("Test 7 passed ✓")

    print("\nAll tests passed! ✓")
