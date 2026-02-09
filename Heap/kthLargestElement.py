"""
Kth Largest Element in an Array
https://www.hellointerview.com/learn/code/heap/kth-largest-element-in-an-array

Write a function that takes an array of unsorted integers nums and an integer k,
and returns the kth largest element in the array.
This function should run in O(n log k) time.

Example 1:
  Input: nums = [5, 3, 2, 1, 4], k = 2
  Output: 4

Approach:
- Use a min-heap of size k
- Iterate through nums; maintain the k largest elements in the heap
- If heap size < k, push element
- Else if element > heap root, heappushpop
- After iteration, heap root = kth largest

Time: O(n log k)
Space: O(k)
"""

from typing import List
import heapq

class Solution:
    def kthLargest(self, nums: List[int], k: int) -> int:
        hq = nums[:k]
        heapq.heapify(hq)
        for num in nums[k:]:
            if num > hq[0]:
                heapq.heappushpop(hq, num)
        return hq[0]


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Basic case
    assert sol.kthLargest([5, 3, 2, 1, 4], 2) == 4, \
        f"Test 1 failed: got {sol.kthLargest([5, 3, 2, 1, 4], 2)}"
    print("Test 1 passed ✓")

    # Test 2: k = 1 (max element)
    assert sol.kthLargest([3, 1, 2, 4, 5], 1) == 5, \
        f"Test 2 failed: got {sol.kthLargest([3, 1, 2, 4, 5], 1)}"
    print("Test 2 passed ✓")

    # Test 3: k = len(nums) (min element)
    assert sol.kthLargest([3, 1, 2, 4, 5], 5) == 1, \
        f"Test 3 failed: got {sol.kthLargest([3, 1, 2, 4, 5], 5)}"
    print("Test 3 passed ✓")

    # Test 4: Duplicates
    assert sol.kthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4, \
        f"Test 4 failed: got {sol.kthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)}"
    print("Test 4 passed ✓")

    # Test 5: Single element
    assert sol.kthLargest([1], 1) == 1, \
        f"Test 5 failed: got {sol.kthLargest([1], 1)}"
    print("Test 5 passed ✓")

    # Test 6: Negative numbers
    assert sol.kthLargest([-1, -3, -2, -4, -5], 2) == -2, \
        f"Test 6 failed: got {sol.kthLargest([-1, -3, -2, -4, -5], 2)}"
    print("Test 6 passed ✓")

    # Test 7: All same
    assert sol.kthLargest([7, 7, 7, 7], 3) == 7, \
        f"Test 7 failed: got {sol.kthLargest([7, 7, 7, 7], 3)}"
    print("Test 7 passed ✓")

    print("\nAll tests passed! ✓")
