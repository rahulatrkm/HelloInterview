'''
ps - https://www.hellointerview.com/learn/code/two-pointers/valid-triangle-number

Triangle Numbers (Valid Triangle Number)
Count the number of triplets in array that could form sides of a triangle.
For valid triangle: sum of any two sides > third side.
Triplets don't need to be unique.

Key insight: If sorted a ≤ b ≤ c, only need to check a + b > c
(other conditions automatically satisfied since c ≥ b ≥ a)

Example:
Input: nums = [11, 4, 9, 6, 15, 18]
Output: 10

Approach:
- Sort array
- Fix largest side (i), use two pointers for smaller two sides
- If nums[left] + nums[right] > nums[i], all pairs between left and right are valid
'''

from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        n = len(nums)
        for i in range(n-1, 1, -1):
            l, r = 0, i-1
            while l < r:
                if nums[i] < nums[l] + nums[r]:
                    cnt += (r-l)
                    r -= 1
                else:
                    l += 1
        return cnt


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.triangleNumber([11, 4, 9, 6, 15, 18]))  # 10
    print(sol.triangleNumber([2, 2, 3, 4]))  # 3
    print(sol.triangleNumber([1, 1, 1, 1]))  # 4
    print(sol.triangleNumber([1, 2, 3, 4]))  # 1 (2+3 > 4)
    print(sol.triangleNumber([1, 2, 3]))  # 0 (1+2 not > 3)
