"""
Search in Rotated Sorted Array
https://www.hellointerview.com/learn/code/binary-search/search-in-rotated-sorted-array

You are given a sorted array that has been rotated at an unknown pivot point,
along with a target value. Develop an algorithm to locate the index of the target
value in the array. If the target is not present, return -1.
The algorithm should have a time complexity of O(log n).

Note:
- The array was originally sorted in ascending order before being rotated.
- The rotation could be at any index, including 0 (no rotation).
- You may assume there are no duplicate elements in the array.

Example 1:
  Input: nums = [4,5,6,7,0,1,2], target = 0
  Output: 4

Example 2:
  Input: nums = [4,5,6,7,0,1,2], target = 3
  Output: -1

Approach:
- Binary search: at each step, one half of the array is always sorted
- Determine which half is sorted by comparing nums[left] with nums[mid]
- If nums[left] <= nums[mid]: left half is sorted
  - Check if target falls in [nums[left], nums[mid]) → search left, else search right
- Else: right half is sorted
  - Check if target falls in (nums[mid], nums[right]] → search right, else search left

Time: O(log n)
Space: O(1)
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        return -1


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Target in right portion
    assert sol.search([4,5,6,7,0,1,2], 0) == 4, \
        f"Test 1 failed: got {sol.search([4,5,6,7,0,1,2], 0)}"
    print("Test 1 passed ✓")

    # Test 2: Target not in array
    assert sol.search([4,5,6,7,0,1,2], 3) == -1, \
        f"Test 2 failed: got {sol.search([4,5,6,7,0,1,2], 3)}"
    print("Test 2 passed ✓")

    # Test 3: Target at beginning
    assert sol.search([4,5,6,7,0,1,2], 4) == 0, \
        f"Test 3 failed: got {sol.search([4,5,6,7,0,1,2], 4)}"
    print("Test 3 passed ✓")

    # Test 4: No rotation
    assert sol.search([1,2,3,4,5,6,7], 5) == 4, \
        f"Test 4 failed: got {sol.search([1,2,3,4,5,6,7], 5)}"
    print("Test 4 passed ✓")

    # Test 5: Single element found
    assert sol.search([1], 1) == 0, \
        f"Test 5 failed: got {sol.search([1], 1)}"
    print("Test 5 passed ✓")

    # Test 6: Single element not found
    assert sol.search([1], 0) == -1, \
        f"Test 6 failed: got {sol.search([1], 0)}"
    print("Test 6 passed ✓")

    # Test 7: Two elements rotated
    assert sol.search([3,1], 1) == 1, \
        f"Test 7 failed: got {sol.search([3,1], 1)}"
    print("Test 7 passed ✓")

    # Test 8: Target at end
    assert sol.search([8,9,10,12,16,17,1,2,3], 3) == 8, \
        f"Test 8 failed: got {sol.search([8,9,10,12,16,17,1,2,3], 3)}"
    print("Test 8 passed ✓")

    # Test 9: Empty array
    assert sol.search([], 5) == -1, \
        f"Test 9 failed: got {sol.search([], 5)}"
    print("Test 9 passed ✓")

    print("\nAll tests passed! ✓")
