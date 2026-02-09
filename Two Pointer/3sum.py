'''
ps - https://www.hellointerview.com/learn/code/two-pointers/3-sum

3-Sum
Given an array nums, find all unique triplets [nums[i], nums[j], nums[k]] such that
i, j, k are distinct indices and nums[i] + nums[j] + nums[k] = 0.
Return list of unique triplets (no duplicates).

Example:
Input: nums = [-1, 0, 1, 2, -1, -1]
Output: [[-1, -1, 2], [-1, 0, 1]]

Approach:
- Sort array, then for each element, use two pointers to find pairs that sum to its negative
- Skip duplicates to avoid duplicate triplets
'''

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-2):
            if nums[i] > 0:
                break
            if i and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            l, r = i+1, n-1
            while l < r:
                curr = nums[l] + nums[r]
                if curr == target:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif curr < target:
                    l += 1
                else:
                    r -= 1
        return ans
            

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.threeSum([-1, 0, 1, 2, -1, -1]))  # [[-1, -1, 2], [-1, 0, 1]]
    print(sol.threeSum([0, 0, 0, 0]))  # [[0, 0, 0]]
    print(sol.threeSum([1, 2, 3]))  # []
