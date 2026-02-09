"""
01-Matrix

You are given an m x n binary matrix grid where each cell contains either a 0 or a 1.

Write a function that returns a matrix of the same dimensions where each cell
contains the distance to the nearest 0 in the original matrix. The distance
between two adjacent cells is 1. If there is no 0 in the grid, return -1 for each
cell.

Example 1:
    Input: mat = [[1, 0, 1], [0, 1, 0], [1, 1, 1]]
    Output: [[1, 0, 1], [0, 1, 0], [1, 2, 1]]
    Explanation: Cell (2, 1) is distance 2 from nearest 0

Approach:
- Use multi-source BFS starting from all cells with value 0
- Initialize output matrix with -1 for unknown distances, 0 for zero cells
- Process cells level by level, updating distances as we go
- Each level represents cells at distance d from nearest zero

Time Complexity: O(m * n) - Visit each cell at most once
Space Complexity: O(m * n) - Queue and output matrix
"""

from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        # Your code goes here
        q = deque()
        m, n = len(mat), len(mat[0])
        vis = [[float('inf')]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j, 0))

        if not q:
            return [[-1]*n for _ in range(m)]

        dire = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            i, j, d = q.popleft()
            if 0 <= i < m and 0 <= j < n and vis[i][j] > d:
                vis[i][j] = d
                for x, y in dire:
                    q.append((i+x, j+y, d+1))
        
        return vis




def run_tests():
    solution = Solution()
    
    # Test 1: Example from problem
    mat = [[1, 0, 1], [0, 1, 0], [1, 1, 1]]
    result = solution.updateMatrix(mat)
    expected = [[1, 0, 1], [0, 1, 0], [1, 2, 1]]
    assert result == expected, f"Test 1 Failed: Expected {expected}, got {result}"
    print("Test 1 Passed")
    
    # Test 2: Single cell with 0
    mat = [[0]]
    result = solution.updateMatrix(mat)
    expected = [[0]]
    assert result == expected, f"Test 2 Failed: Expected {expected}, got {result}"
    print("Test 2 Passed")
    
    # Test 3: Single cell with 1
    mat = [[1]]
    result = solution.updateMatrix(mat)
    expected = [[-1]]
    assert result == expected, f"Test 3 Failed: Expected {expected}, got {result}"
    print("Test 3 Passed")
    
    # Test 4: All zeros
    mat = [[0, 0], [0, 0]]
    result = solution.updateMatrix(mat)
    expected = [[0, 0], [0, 0]]
    assert result == expected, f"Test 4 Failed: Expected {expected}, got {result}"
    print("Test 4 Passed")
    
    # Test 5: All ones
    mat = [[1, 1], [1, 1]]
    result = solution.updateMatrix(mat)
    expected = [[-1, -1], [-1, -1]]
    assert result == expected, f"Test 5 Failed: Expected {expected}, got {result}"
    print("Test 5 Passed")
    
    # Test 6: Larger matrix
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    result = solution.updateMatrix(mat)
    expected = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    assert result == expected, f"Test 6 Failed: Expected {expected}, got {result}"
    print("Test 6 Passed")
    
    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
