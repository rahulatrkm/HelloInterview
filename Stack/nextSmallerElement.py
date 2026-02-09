"""
Next Smaller Element
https://www.hellointerview.com/learn/code/stack/monotonic-stack

Given an array of integers, find the next smaller element for each element in the
array. The next smaller element of an element x is the first element to the right
of x that is smaller than x. If there is no such element, then the next smaller
element is -1.

Example:
  Input: nums = [2, 1, 3, 2, 4, 3]
  Output: [1, -1, 2, -1, 3, -1]

Approach:
  - Use a monotonically increasing stack.
  - For each element, pop indices from stack while current < element at stack top.
  - For each popped index, result[index] = current element.
  - Push current index onto stack.
  - Remaining indices in stack have no next smaller element (-1).
"""

from typing import List


class Solution:
    def nextSmallerElement(self, nums: List[int]) -> List[int]:
        ans = [-1]*len(nums)
        st = []
        for i, num in enumerate(nums):
            while st and nums[st[-1]] > num:
                ans[st.pop()] = num
            st.append(i)
        return ans


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2, 1, 3, 2, 4, 3], [1, -1, 2, -1, 3, -1]),
        ([1, 2, 3, 4, 5], [-1, -1, -1, -1, -1]),
        ([5, 4, 3, 2, 1], [4, 3, 2, 1, -1]),
        ([1], [-1]),
        ([4, 2, 1, 3, 5], [2, 1, -1, -1, -1]),
        ([3, 1, 4, 1, 5, 9], [1, -1, 1, -1, -1, -1]),
    ]
    for i, (nums, expected) in enumerate(tests):
        result = sol.nextSmallerElement(nums[:])
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {nums} | Expected: {expected} | Got: {result}")
