"""
Maximal Square

Given an m x n 2D matrix filled with 0's and 1's, find the largest square
containing only 1's and return its area.

Example 1:
    Input: matrix = [[0,0,1,0,0],[1,1,1,0,1],[0,1,1,0,0]]
    Output: 4
    Explanation: The largest square of 1's has side length 2, area = 4.

Example 2:
    Input: matrix = [[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]
    Output: 4

Approach:
- dp[i][j] = side length of largest square with bottom-right corner at (i-1, j-1)
- Recurrence: if matrix[i-1][j-1] == 1:
    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
- Use (r+1) x (c+1) dp array to avoid boundary checks
- Track max_side throughout, return max_side^2

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[int]]) -> int:
        # Your code goes here
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        dp = [[0]*(n+1) for _ in range(m+1)]
        max_side = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])
        return max_side * max_side


def run_tests():
    solution = Solution()

    # Test 1: Small matrix
    result = solution.maximalSquare([[0,0,1,0,0],[1,1,1,0,1],[0,1,1,0,0]])
    assert result == 4, f"Test 1 Failed: Expected 4, got {result}"
    print("Test 1 Passed")

    # Test 2: Larger matrix
    result = solution.maximalSquare([[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]])
    assert result == 4, f"Test 2 Failed: Expected 4, got {result}"
    print("Test 2 Passed")

    # Test 3: All zeros
    result = solution.maximalSquare([[0,0],[0,0]])
    assert result == 0, f"Test 3 Failed: Expected 0, got {result}"
    print("Test 3 Passed")

    # Test 4: All ones (3x3)
    result = solution.maximalSquare([[1,1,1],[1,1,1],[1,1,1]])
    assert result == 9, f"Test 4 Failed: Expected 9, got {result}"
    print("Test 4 Passed")

    # Test 5: Single element 1
    result = solution.maximalSquare([[1]])
    assert result == 1, f"Test 5 Failed: Expected 1, got {result}"
    print("Test 5 Passed")

    # Test 6: Single element 0
    result = solution.maximalSquare([[0]])
    assert result == 0, f"Test 6 Failed: Expected 0, got {result}"
    print("Test 6 Passed")

    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
