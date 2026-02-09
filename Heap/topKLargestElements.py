"""
Top-K Largest Elements in an Array
https://www.hellointerview.com/learn/code/heap/overview

Given an integer array nums and an integer k, return the k largest elements
in the array in any order.

Example 1:
  Input: nums = [9, 3, 7, 1, -2, 6, 8], k = 3
  Output: [7, 8, 9]  (any order)

Approach:
- Use a min-heap of size k
- Push first k elements onto the heap
- For remaining elements, if element > heap root, heappushpop
- Heap always holds the k largest elements seen so far
- Root of heap = smallest among the k largest

Time: O(n log k)
Space: O(k)
"""

from typing import List
import heapq

class Solution:
    def topKLargest(self, nums: List[int], k: int) -> List[int]:
        hq = nums[:k]
        heapq.heapify(hq)
        for num in nums[k:]:
            if num > hq[0]:
                heapq.heappop(hq)
                heapq.heappush(hq, num)
        return hq


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Basic case
    result = sorted(sol.topKLargest([9, 3, 7, 1, -2, 6, 8], 3))
    assert result == [7, 8, 9], f"Test 1 failed: got {result}"
    print("Test 1 passed ✓")

    # Test 2: k = 1
    result = sol.topKLargest([5, 3, 1, 4, 2], 1)
    assert result == [5], f"Test 2 failed: got {result}"
    print("Test 2 passed ✓")

    # Test 3: k = len(nums)
    result = sorted(sol.topKLargest([3, 1, 2], 3))
    assert result == [1, 2, 3], f"Test 3 failed: got {result}"
    print("Test 3 passed ✓")

    # Test 4: Negative numbers
    result = sorted(sol.topKLargest([-1, -5, -3, -2, -4], 2))
    assert result == [-2, -1], f"Test 4 failed: got {result}"
    print("Test 4 passed ✓")

    # Test 5: Duplicates
    result = sorted(sol.topKLargest([4, 4, 4, 2, 2], 3))
    assert result == [4, 4, 4], f"Test 5 failed: got {result}"
    print("Test 5 passed ✓")

    # Test 6: Single element
    result = sol.topKLargest([42], 1)
    assert result == [42], f"Test 6 failed: got {result}"
    print("Test 6 passed ✓")

    # Test 7: Mixed positive and negative
    result = sorted(sol.topKLargest([10, -10, 20, -20, 0], 3))
    assert result == [0, 10, 20], f"Test 7 failed: got {result}"
    print("Test 7 passed ✓")

    print("\nAll tests passed! ✓")
