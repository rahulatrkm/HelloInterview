"""
Paint House II

You are given n houses in a row and k colors. The cost of painting each house
with each color is given in a 2D array costs where costs[i][j] is the cost of
painting house i with color j. No two adjacent houses can have the same color.

Return the minimum cost to paint all houses.

Follow-up: Solve in O(n * k) time instead of O(n * k^2).

Example 1:
    Input: costs = [[4, 2, 8], [7, 1, 5], [3, 9, 6]]
    Output: 8
    Explanation: Color 0(4) + Color 1(1) + Color 0(3) = 8.

Example 2:
    Input: costs = [[8, 3, 12, 5], [15, 9, 4, 7]]
    Output: 7
    Explanation: Color 1(3) + Color 2(4) = 7.

Approach:
- Extension of Paint House with k colors instead of 3
- Naive: dp[i][j] = costs[i][j] + min(dp[i-1][c] for c != j) → O(n*k^2)
- Optimized: For each row, track the two smallest dp values (min1, min2) and
  their indices. For the next row, if j == min1_index, use min2; else use min1.
  This avoids the inner k loop → O(n*k)

Time Complexity: O(n * k)
Space Complexity: O(k) with space optimization
"""

from typing import List

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        # Your code goes here
        # if not costs:
        #     return 0
        # n, k = len(costs), len(costs[0])
        # dp = [0] * k
        # for i in range(n):
        #     old_dp = dp[:]
        #     min1 = min(old_dp)
        #     min1_index = old_dp.index(min1)
        #     min2 = min(x for idx, x in enumerate(old_dp) if idx != min1_index)
        #     for j in range(k):
        #         if i == 0:
        #             dp[j] = costs[i][j]
        #         else:
        #             dp[j] = costs[i][j] + (min2 if j == min1_index else min1)
        # return min(dp)

        if not costs:
            return 0
        n, k = len(costs), len(costs[0])
        min1 = min2 = 0
        min1_index = -1
        for i in range(n):
            new_min1 = new_min2 = float('inf')
            new_min1_index = -1
            for j in range(k):
                cost = costs[i][j] + (min2 if j == min1_index else min1)
                if cost < new_min1:
                    new_min2 = new_min1
                    new_min1 = cost
                    new_min1_index = j
                elif cost < new_min2:
                    new_min2 = cost
            min1, min2, min1_index = new_min1, new_min2, new_min1_index
        return min1


def run_tests():
    solution = Solution()

    # Test 1: 3 houses, 3 colors
    result = solution.minCostII([[4, 2, 8], [7, 1, 5], [3, 9, 6]])
    assert result == 8, f"Test 1 Failed: Expected 8, got {result}"
    print("Test 1 Passed")

    # Test 2: 2 houses, 4 colors
    result = solution.minCostII([[8, 3, 12, 5], [15, 9, 4, 7]])
    assert result == 7, f"Test 2 Failed: Expected 7, got {result}"
    print("Test 2 Passed")

    # Test 3: Single house
    result = solution.minCostII([[5, 3, 7, 1]])
    assert result == 1, f"Test 3 Failed: Expected 1, got {result}"
    print("Test 3 Passed")

    # Test 4: 2 colors only
    result = solution.minCostII([[1, 2], [2, 1], [1, 2]])
    assert result == 3, f"Test 4 Failed: Expected 3, got {result}"
    print("Test 4 Passed")

    # Test 5: All same costs
    result = solution.minCostII([[5, 5, 5], [5, 5, 5], [5, 5, 5]])
    assert result == 15, f"Test 5 Failed: Expected 15, got {result}"
    print("Test 5 Passed")

    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
