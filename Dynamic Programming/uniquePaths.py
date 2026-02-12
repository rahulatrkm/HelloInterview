"""
Unique Paths

A robot is located at the top-left corner of an m x n grid. The robot can only
move either down or right at any point in time. The robot is trying to reach the
bottom-right corner of the grid.

How many possible unique paths are there?

Example 1:
    Input: m = 2, n = 3
    Output: 3
    Explanation: 3 unique paths from top-left to bottom-right.

Example 2:
    Input: m = 3, n = 7
    Output: 28

Approach:
- dp[i][j] = number of unique paths to reach cell (i, j)
- Recurrence: dp[i][j] = dp[i-1][j] + dp[i][j-1]
- Base cases: dp[0][j] = 1 (first row), dp[i][0] = 1 (first column)
- Return dp[m-1][n-1]

Time Complexity: O(m * n)
Space Complexity: O(m * n), can be optimized to O(n)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Your code goes here
        dp = [[1]*n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


def run_tests():
    solution = Solution()

    # Test 1: 2x3 grid
    result = solution.uniquePaths(2, 3)
    assert result == 3, f"Test 1 Failed: Expected 3, got {result}"
    print("Test 1 Passed")

    # Test 2: 3x7 grid
    result = solution.uniquePaths(3, 7)
    assert result == 28, f"Test 2 Failed: Expected 28, got {result}"
    print("Test 2 Passed")

    # Test 3: 1x1 grid
    result = solution.uniquePaths(1, 1)
    assert result == 1, f"Test 3 Failed: Expected 1, got {result}"
    print("Test 3 Passed")

    # Test 4: Single row
    result = solution.uniquePaths(1, 5)
    assert result == 1, f"Test 4 Failed: Expected 1, got {result}"
    print("Test 4 Passed")

    # Test 5: Single column
    result = solution.uniquePaths(5, 1)
    assert result == 1, f"Test 5 Failed: Expected 1, got {result}"
    print("Test 5 Passed")

    # Test 6: 3x3 grid
    result = solution.uniquePaths(3, 3)
    assert result == 6, f"Test 6 Failed: Expected 6, got {result}"
    print("Test 6 Passed")

    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
