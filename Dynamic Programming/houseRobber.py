"""
House Robber

You're a treasure hunter in a neighborhood where houses are arranged in a row,
and each house contains a different amount of treasure. Your goal is to collect
as much treasure as possible, but there's a catch: if you collect treasure from
two adjacent houses, it triggers a neighborhood-wide alert, ending your hunt
immediately.

Given an array treasure of non-negative integers, where each integer represents
the amount of treasure in a house, return the maximum amount of treasure you can
collect without triggering any alarms.

Example 1:
    Input: treasure = [3, 1, 4, 1, 5]
    Output: 12
    Explanation: Collect from houses 0, 2, and 4 for a total of 3 + 4 + 5 = 12.

Example 2:
    Input: treasure = [2, 7, 9, 3, 1]
    Output: 12
    Explanation: Collect from houses 0, 2, 4 for 2 + 9 + 1 = 12.

Approach:
- dp[i] = max treasure from first i houses
- Recurrence: dp[i] = max(dp[i-1], dp[i-2] + treasure[i-1])
  - Skip current house: dp[i-1]
  - Take current house: dp[i-2] + treasure[i-1]
- Base cases: dp[0] = 0, dp[1] = treasure[0]
- Can optimize to O(1) space since only last two values needed

Time Complexity: O(n)
Space Complexity: O(1) with space optimization, O(n) with full DP array
"""

from typing import List

class Solution:
    def rob(self, treasure: List[int]) -> int:
        # Your code goes here
        n = len(treasure)
        if n == 0:
            return 0
        if n == 1:
            return treasure[0]
        a, b = treasure[0], max(treasure[:2])
        for i in range(2, n):
            a, b = b, max(b, treasure[i]+a)
        return b


def run_tests():
    solution = Solution()

    # Test 1: Example
    result = solution.rob([3, 1, 4, 1, 5])
    assert result == 12, f"Test 1 Failed: Expected 12, got {result}"
    print("Test 1 Passed")

    # Test 2: Another example
    result = solution.rob([2, 7, 9, 3, 1])
    assert result == 12, f"Test 2 Failed: Expected 12, got {result}"
    print("Test 2 Passed")

    # Test 3: Single house
    result = solution.rob([5])
    assert result == 5, f"Test 3 Failed: Expected 5, got {result}"
    print("Test 3 Passed")

    # Test 4: Two houses
    result = solution.rob([1, 2])
    assert result == 2, f"Test 4 Failed: Expected 2, got {result}"
    print("Test 4 Passed")

    # Test 5: Empty
    result = solution.rob([])
    assert result == 0, f"Test 5 Failed: Expected 0, got {result}"
    print("Test 5 Passed")

    # Test 6: All same values
    result = solution.rob([3, 3, 3, 3, 3])
    assert result == 9, f"Test 6 Failed: Expected 9, got {result}"
    print("Test 6 Passed")

    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
