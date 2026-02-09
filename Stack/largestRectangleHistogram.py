"""
Largest Rectangle in Histogram (Hard)
https://www.hellointerview.com/learn/code/stack/largest-rectangle-in-histogram

Given an integer array heights representing the heights of histogram bars, write a
function to find the largest rectangular area possible in a histogram, where each
bar's width is 1.

Example:
  Input: heights = [2, 8, 5, 6, 2, 3]
  Output: 15

Approach:
  - Use a monotonically increasing stack storing indices.
  - When current height < stack top height, pop and calculate area:
    - Height = heights[popped index]
    - Width = (current index - 1) - stack[-1]  (or full width if stack empty)
  - After iteration, drain remaining indices using end of array as right boundary.
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        st = []
        for i, h in enumerate(heights):
            while st and heights[st[-1]] >= h:
                height = heights[st.pop()]
                width = i - st[-1] - 1 if st else i
                result = max(result, height*width)
            st.append(i)
        
        while st:
            height = heights[st.pop()]
            width = len(heights) - st[-1] - 1 if st else len(heights)
            result = max(result, height*width)
        return result


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2, 8, 5, 6, 2, 3], 15),
        ([2, 1, 5, 6, 2, 3], 10),
        ([2, 4], 4),
        ([1], 1),
        ([5, 5, 5, 5], 20),
        ([1, 2, 3, 4, 5], 9),
        ([5, 4, 3, 2, 1], 9),
        ([2, 1, 2], 3),
    ]
    for i, (heights, expected) in enumerate(tests):
        result = sol.largestRectangleArea(heights[:])
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {heights} | Expected: {expected} | Got: {result}")
