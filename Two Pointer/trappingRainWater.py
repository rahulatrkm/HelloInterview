"""
Trapping Rain Water
https://www.hellointerview.com/learn/code/two-pointers/trapping-rain-water

DESCRIPTION:
Write a function to calculate the total amount of water trapped between bars 
on an elevation map, where each bar's width is 1. The input is given as an 
array of n non-negative integers height representing the height of each bar.

Visual Example:
#                        x
#            x  .  .  .  x
#         x  x  .  .  .  x
#         x  x  .  x  x  x  .  .  x
#         x  x  x  x  x  x  x  .  x
# ==================================
height = [3, 4, 1, 2, 2, 5, 1, 0, 2]

(x = bar, . = trapped water)

Example 1:
Input: height = [3, 4, 1, 2, 2, 5, 1, 0, 2]
Output: 10

Example 2:
Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6

Approach:
- Use two pointers (left, right) at opposite ends
- Track leftMax and rightMax (highest bars seen from each side)
- At each step, move the pointer with smaller max value
- Water trapped at index = min(leftMax, rightMax) - height[index]
- O(n) time, O(1) space
"""

from typing import List


class Solution:
    def trappingWater(self, height: List[int]) -> int:
        if not height:
            return 0
        ans = 0
        n = len(height)
        l, r = 0, n-1
        lm, rm = height[l], height[r]
        while l <= r:
            if lm <= rm:
                if lm < height[l]:
                    lm = height[l]
                else:
                    ans += lm-height[l]
                l += 1
            else:
                if rm < height[r]:
                    rm = height[r]
                else:
                    ans += rm-height[r]
                r -= 1
        return ans


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([3, 4, 1, 2, 2, 5, 1, 0, 2], 10),
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([], 0),
        ([1], 0),
        ([1, 2], 0),
        ([2, 0, 2], 2),
        ([3, 0, 0, 2, 0, 4], 10),
    ]
    
    sol = Solution()
    for i, (height, expected) in enumerate(test_cases):
        result = sol.trappingWater(height)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {height} | Output: {result} | Expected: {expected}")
