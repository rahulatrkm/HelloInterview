"""
Find K Closest Elements
https://www.hellointerview.com/learn/code/heap/find-k-closest-elements

Given a sorted array nums, a target value target, and an integer k, find the k
closest elements to target in the array. Return these elements sorted in
ascending order.

"Closest" = smallest absolute difference from target.

Example 1:
  Input: nums = [-1, 0, 1, 4, 6], target = 1, k = 3
  Output: [-1, 0, 1]

Example 2:
  Input: nums = [5, 6, 7, 8, 9], target = 10, k = 2
  Output: [8, 9]

Approach (Max-Heap):
- Use a max-heap of size k (negate distances)
- Push (-abs(num - target), num) for first k elements
- For remaining, if closer than heap root, heappushpop
- Extract elements from heap and sort

Approach (Binary Search + Two Pointers):
- Binary search for starting index of the k-length window
- left=0, right=len(nums)-k
- Compare target-nums[mid] vs nums[mid+k]-target to shift window

Time: O(n log k) heap / O(log(n-k) + k) binary search
Space: O(k)
"""

from typing import List
import heapq

class Solution:
    def kClosest(self, nums: List[int], k: int, target: int) -> List[int]:
        l, r = 0, len(nums) - k
        while l < r:
            m = (l+r)//2
            if target - nums[m] > nums[m+k] - target:
                l = m + 1
            else:
                r = m
        return nums[l:l+k]


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Target in array
    assert sol.kClosest([-1, 0, 1, 4, 6], 3, 1) == [-1, 0, 1], \
        f"Test 1 failed: got {sol.kClosest([-1, 0, 1, 4, 6], 3, 1)}"
    print("Test 1 passed ✓")

    # Test 2: Target outside array (right)
    assert sol.kClosest([5, 6, 7, 8, 9], 2, 10) == [8, 9], \
        f"Test 2 failed: got {sol.kClosest([5, 6, 7, 8, 9], 2, 10)}"
    print("Test 2 passed ✓")

    # Test 3: Target outside array (left)
    assert sol.kClosest([5, 6, 7, 8, 9], 2, 1) == [5, 6], \
        f"Test 3 failed: got {sol.kClosest([5, 6, 7, 8, 9], 2, 1)}"
    print("Test 3 passed ✓")

    # Test 4: k = len(nums)
    assert sol.kClosest([1, 2, 3], 3, 2) == [1, 2, 3], \
        f"Test 4 failed: got {sol.kClosest([1, 2, 3], 3, 2)}"
    print("Test 4 passed ✓")

    # Test 5: k = 1
    assert sol.kClosest([1, 2, 3, 4, 5], 1, 3) == [3], \
        f"Test 5 failed: got {sol.kClosest([1, 2, 3, 4, 5], 1, 3)}"
    print("Test 5 passed ✓")

    # Test 6: Tie-breaking (prefer smaller index / value)
    assert sol.kClosest([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4], \
        f"Test 6 failed: got {sol.kClosest([1, 2, 3, 4, 5], 4, 3)}"
    print("Test 6 passed ✓")

    # Test 7: Single element
    assert sol.kClosest([10], 1, 5) == [10], \
        f"Test 7 failed: got {sol.kClosest([10], 1, 5)}"
    print("Test 7 passed ✓")

    print("\nAll tests passed! ✓")
