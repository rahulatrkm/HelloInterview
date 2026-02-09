"""
Move Zeroes
https://www.hellointerview.com/learn/code/two-pointers/move-zeroes

DESCRIPTION:
Given an integer array nums, move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.

Note: You must do this in-place without making a copy of the array.

Example 1:
Input: nums = [2, 0, 4, 0, 9]
Output: [2, 4, 9, 0, 0]

Example 2:
Input: nums = [0]
Output: [0]

Approach:
- Use a "nextNonZero" pointer to track where the next non-zero element should go
- Iterate through array with another pointer
- When we find a non-zero, swap it with position at nextNonZero pointer
- This is a same-direction two pointer technique
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = i = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[idx] = nums[idx], nums[i]
                idx += 1
            i += 1
        return nums


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([2, 0, 4, 0, 9], [2, 4, 9, 0, 0]),
        ([0], [0]),
        ([0, 0, 0, 1], [1, 0, 0, 0]),
        ([1, 2, 3], [1, 2, 3]),
        ([0, 0, 0], [0, 0, 0]),
        ([1, 0, 1], [1, 1, 0]),
    ]
    
    sol = Solution()
    for i, (nums, expected) in enumerate(test_cases):
        nums_copy = nums.copy()
        sol.moveZeroes(nums_copy)
        status = "✓" if nums_copy == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {nums} | Output: {nums_copy} | Expected: {expected}")
