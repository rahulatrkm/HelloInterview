"""
Next Greater Element (Medium)
https://www.hellointerview.com/learn/code/stack/monotonic-stack

Given an array of integers, find the next greater element for each element in the
array. The next greater element of an element x is the first element to the right
of x that is greater than x. If there is no such element, then the next greater
element is -1.

Example:
  Input: nums = [2, 1, 3, 2, 4, 3]
  Output: [3, 3, 4, 4, -1, -1]

Approach:
  - Use a monotonically decreasing stack storing indices.
  - For each element, pop indices from stack while current > element at stack top.
  - For each popped index, result[index] = current element.
  - Push current index onto stack.
  - Remaining indices in stack have no next greater element (-1).
"""

from typing import List


class Solution:
    def nextGreaterElement(self, nums: List[int]) -> List[int]:
        # ans = []
        # st = []
        # n = len(nums)
        # for i in range(n-1, -1, -1):
        #     while st and st[-1] <= nums[i]:
        #         st.pop()
        #     ans.append(st[-1] if st else -1)
        #     st.append(nums[i])
        # return ans[::-1]

        ans = [-1]*len(nums)
        st = []
        for i, num in enumerate(nums):
            while st and nums[st[-1]] < num:
                ans[st.pop()] = num
            st.append(i)
        return ans


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2, 1, 3, 2, 4, 3], [3, 3, 4, 4, -1, -1]),
        ([5, 4, 3, 2, 1], [-1, -1, -1, -1, -1]),
        ([1, 2, 3, 4, 5], [2, 3, 4, 5, -1]),
        ([1], [-1]),
        ([3, 1, 2, 4], [4, 2, 4, -1]),
        ([1, 3, 2, 4, 3, 5], [3, 4, 4, 5, 5, -1]),
    ]
    for i, (nums, expected) in enumerate(tests):
        result = sol.nextGreaterElement(nums[:])
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {nums} | Expected: {expected} | Got: {result}")
