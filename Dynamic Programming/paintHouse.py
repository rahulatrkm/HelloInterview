"""
Paint House

There are n houses in a row. Each house can be painted with one of three colors:
Red (0), Blue (1), or Green (2). The cost of painting each house with each color
is given in a 2D array costs where costs[i][j] is the cost of painting house i
with color j.

No two adjacent houses can have the same color. Return the minimum cost to paint
all houses.

Example 1:
    Input: costs = [[8, 4, 15], [10, 7, 3], [6, 9, 12]]
    Output: 13
    Explanation: Blue(4) + Green(3) + Red(6) = 13.

Example 2:
    Input: costs = [[5, 8, 6], [19, 14, 13], [7, 5, 12], [14, 5, 9]]
    Output: 30
    Explanation: Red(5) → Green(13) → Red(7) → Blue(5) = 30.

Approach:
- dp[i][j] = minimum cost to paint houses 0..i with house i painted color j
- Recurrence: dp[i][j] = costs[i][j] + min(dp[i-1][k]) for k != j
- Base case: dp[0][j] = costs[0][j]
- Answer: min(dp[n-1])
- Can optimize space to O(1) by only tracking previous row

Time Complexity: O(n) — 3 colors is constant factor
Space Complexity: O(1) with optimization, O(n) with full DP
"""

from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # Your code goes here
        if not costs:
            return 0
        n = len(costs)
        for i in range(1, n):
            costs[i][0] += min(costs[i-1][1], costs[i-1][2])
            costs[i][1] += min(costs[i-1][0], costs[i-1][2])
            costs[i][2] += min(costs[i-1][0], costs[i-1][1])
        return min(costs[-1])


def run_tests():
    solution = Solution()

    # Test 1: 3 houses
    result = solution.minCost([[8, 4, 15], [10, 7, 3], [6, 9, 12]])
    assert result == 13, f"Test 1 Failed: Expected 13, got {result}"
    print("Test 1 Passed")

    # Test 2: 4 houses
    result = solution.minCost([[5, 8, 6], [19, 14, 13], [7, 5, 12], [14, 5, 9]])
    assert result == 30, f"Test 2 Failed: Expected 30, got {result}"
    print("Test 2 Passed")

    # Test 3: Single house
    result = solution.minCost([[3, 5, 7]])
    assert result == 3, f"Test 3 Failed: Expected 3, got {result}"
    print("Test 3 Passed")

    # Test 4: Two houses
    result = solution.minCost([[1, 2, 3], [1, 2, 3]])
    assert result == 3, f"Test 4 Failed: Expected 3, got {result}"
    print("Test 4 Passed")

    # Test 5: All same costs
    result = solution.minCost([[5, 5, 5], [5, 5, 5], [5, 5, 5]])
    assert result == 15, f"Test 5 Failed: Expected 15, got {result}"
    print("Test 5 Passed")

    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
