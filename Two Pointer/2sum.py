'''
ps - https://www.hellointerview.com/learn/code/two-pointers/overview

Two Sum (Sorted Array)
Given a sorted array and a target, find if two numbers exist that add up to target.
Return True if found, False otherwise.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: True

Constraints:
- Array is sorted in ascending order
- Exactly one solution exists
'''

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                return True
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
        return False



# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.twoSum([2, 7, 11, 15], 9))  # True
    print(sol.twoSum([1, 2, 3, 4, 5], 6))  # True
    print(sol.twoSum([1, 3, 5, 7], 8))  # True
    print(sol.twoSum([1, 2, 3], 10))  # False

