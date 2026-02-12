"""
Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing
subsequence. The subsequence does not need to be contiguous.

Example 1:
    Input: nums = [8, 2, 4, 3, 6, 12]
    Output: 4
    Explanation: The longest increasing subsequence is [2, 4, 6, 12].

Example 2:
    Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
    Output: 4
    Explanation: [2, 3, 7, 101] or [2, 3, 7, 18].

Approach:
- dp[i] = length of longest increasing subsequence ending at index i
- Initialize all dp[i] = 1 (each element is a subsequence of length 1)
- For each i, check all j < i: if nums[i] > nums[j], dp[i] = max(dp[i], dp[j]+1)
- Return max(dp)
- O(n^2) DP solution; can also be done in O(n log n) with binary search

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Your code goes here
        def findIdx(x):
            l, r = 0, len(sub)
            while l < r:
                m = (l + r) // 2
                if sub[m] < x:
                    l = m + 1
                else:
                    r = m
            return l

        sub = []
        for x in nums:
            if not sub or x > sub[-1]:
                sub.append(x)
            else:
                idx = findIdx(x)
                sub[idx] = x
        return len(sub)


def run_tests():
    solution = Solution()

    # Test 1: Mixed array
    result = solution.lengthOfLIS([8, 2, 4, 3, 6, 12])
    assert result == 4, f"Test 1 Failed: Expected 4, got {result}"
    print("Test 1 Passed")

    # Test 2: Classic example
    result = solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
    assert result == 4, f"Test 2 Failed: Expected 4, got {result}"
    print("Test 2 Passed")

    # Test 3: Already sorted
    result = solution.lengthOfLIS([1, 2, 3, 4, 5])
    assert result == 5, f"Test 3 Failed: Expected 5, got {result}"
    print("Test 3 Passed")

    # Test 4: Decreasing
    result = solution.lengthOfLIS([5, 4, 3, 2, 1])
    assert result == 1, f"Test 4 Failed: Expected 1, got {result}"
    print("Test 4 Passed")

    # Test 5: Single element
    result = solution.lengthOfLIS([7])
    assert result == 1, f"Test 5 Failed: Expected 1, got {result}"
    print("Test 5 Passed")

    # Test 6: All same
    result = solution.lengthOfLIS([3, 3, 3, 3])
    assert result == 1, f"Test 6 Failed: Expected 1, got {result}"
    print("Test 6 Passed")

    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
