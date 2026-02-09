"""
Sort Colors (Dutch National Flag)
https://www.hellointerview.com/learn/code/two-pointers/sort-colors

DESCRIPTION:
Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, 
white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2, 1, 2, 0, 1, 0, 1, 0, 1]
Output: [0, 0, 0, 1, 1, 1, 1, 2, 2]

Example 2:
Input: nums = [2, 0, 1]
Output: [0, 1, 2]

Approach (Dutch National Flag Algorithm):
- Use three pointers: left, right, and i (current)
- left marks the boundary for 0s (everything before left is 0)
- right marks the boundary for 2s (everything after right is 2)
- i iterates through the array:
  - If nums[i] == 0: swap with left, increment both left and i
  - If nums[i] == 2: swap with right, decrement right (don't increment i)
  - If nums[i] == 1: just increment i
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j, k = 0, 0, n-1
        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1
        return nums



# Test cases
if __name__ == "__main__":
    test_cases = [
        ([2, 1, 2, 0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 1, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        ([0], [0]),
        ([1], [1]),
        ([2], [2]),
        ([2, 2, 2, 1, 1, 0, 0], [0, 0, 1, 1, 2, 2, 2]),
        ([0, 0, 0], [0, 0, 0]),
        ([1, 2, 0], [0, 1, 2]),
    ]
    
    sol = Solution()
    for i, (nums, expected) in enumerate(test_cases):
        nums_copy = nums.copy()
        sol.sortColors(nums_copy)
        status = "✓" if nums_copy == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {nums} | Output: {nums_copy} | Expected: {expected}")
