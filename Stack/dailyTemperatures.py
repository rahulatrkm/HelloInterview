"""
Daily Temperatures (Medium)
https://www.hellointerview.com/learn/code/stack/daily-temperatures

Given an integer array temps representing daily temperatures, write a function to
calculate the number of days one has to wait for a warmer temperature after each
given day. Return an array answer where answer[i] represents the wait time for a
warmer day after the ith day. If no warmer day is expected in the future, set
answer[i] to 0.

Example:
  Input: temps = [65, 70, 68, 60, 55, 75, 80, 74]
  Output: [1, 4, 3, 2, 1, 1, 0, 0]

Approach:
  - Use a monotonically decreasing stack storing indices.
  - For each temperature, pop indices from stack while current temp > temp at stack top.
  - For each popped index, answer = current index - popped index.
  - Push current index onto stack.
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        ans = [0]*len(temps)
        st = []
        for i, temp in enumerate(temps):
            while st and temps[st[-1]] < temp:
                ans[st.pop()] = i - st[-1]
            st.append(i)
        return ans


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([65, 70, 68, 60, 55, 75, 80, 74], [1, 4, 3, 2, 1, 1, 0, 0]),
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([60, 50, 40, 30], [0, 0, 0, 0]),
        ([70], [0]),
        ([70, 70, 70], [0, 0, 0]),
        ([55, 60, 55, 60, 55, 60], [1, 0, 1, 0, 1, 0]),
    ]
    for i, (temps, expected) in enumerate(tests):
        result = sol.dailyTemperatures(temps[:])
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {temps} | Expected: {expected} | Got: {result}")
