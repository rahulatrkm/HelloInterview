'''
ps - https://www.hellointerview.com/learn/code/two-pointers/container-with-most-water

Container With Most Water
Given an array heights where each element represents the height of a vertical line,
pick two lines to form a container. Return the maximum area the container can hold.

Area = width × height
- Width: distance between walls (right_index - left_index)
- Height: shorter wall (water overflows at the shorter wall)

Example 1:
Input: heights = [3, 4, 1, 2, 2, 4, 1, 3, 2]
Output: 21  # walls at indices 0 and 7 (both height 3): width=7, height=3

Example 2:
Input: heights = [1, 2, 1]
Output: 2  # walls at indices 0 and 2: width=2, height=1
'''

from typing import List


class Solution:
    def max_area(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        ans = 0
        while l < r:
            ans = max(ans, min(heights[l], heights[r])*(r-l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return ans


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.max_area([3, 4, 1, 2, 2, 4, 1, 3, 2]))  # 21
    print(sol.max_area([1, 2, 1]))  # 2
    print(sol.max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
