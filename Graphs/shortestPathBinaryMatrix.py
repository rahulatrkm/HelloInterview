"""
Shortest Path in Binary Matrix

Given an n x n binary matrix grid, return the length of the shortest clear path
in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (0, 0) to the
bottom-right cell (n - 1, n - 1) such that:
- All the visited cells of the path are 0.
- All the adjacent cells of the path are 8-directionally connected.

The length of a clear path is the number of visited cells of the path.

Example 1:
    Input: grid = [[0, 1], [1, 0]]
    Output: 2
    Explanation: Path: (0,0) -> (1,1). Length = 2.

Example 2:
    Input: grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    Output: 4
    Explanation: Path: (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2). Length = 4.

Example 3:
    Input: grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
    Output: -1
    Explanation: Start cell is blocked.

Approach:
- BFS from (0,0) to (n-1, n-1), all edges have equal weight (1)
- Explore all 8 directions at each step
- First time we reach the destination is the shortest path
- Track visited cells to avoid revisiting

Time Complexity: O(n^2) — visit each cell at most once
Space Complexity: O(n^2) — for the visited set / queue
"""

from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Your code goes here
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        q = deque([(0, 0, 1)])  # (x, y, distance)
        visited = set((0, 0))
        while q:
            x, y, dist = q.popleft()
            if (x, y) == (m-1, n-1):
                return dist
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny, dist + 1))
        return -1


def run_tests():
    solution = Solution()

    # Test 1: Simple 2x2 grid with diagonal path
    result = solution.shortestPathBinaryMatrix([[0, 1], [1, 0]])
    assert result == 2, f"Test 1 Failed: Expected 2, got {result}"
    print("Test 1 Passed")

    # Test 2: 3x3 grid
    result = solution.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]])
    assert result == 4, f"Test 2 Failed: Expected 4, got {result}"
    print("Test 2 Passed")

    # Test 3: Start cell blocked
    result = solution.shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]])
    assert result == -1, f"Test 3 Failed: Expected -1, got {result}"
    print("Test 3 Passed")

    # Test 4: End cell blocked
    result = solution.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 1]])
    assert result == -1, f"Test 4 Failed: Expected -1, got {result}"
    print("Test 4 Passed")

    # Test 5: Single cell grid
    result = solution.shortestPathBinaryMatrix([[0]])
    assert result == 1, f"Test 5 Failed: Expected 1, got {result}"
    print("Test 5 Passed")

    # Test 6: All zeros — direct diagonal path
    result = solution.shortestPathBinaryMatrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    assert result == 3, f"Test 6 Failed: Expected 3, got {result}"
    print("Test 6 Passed")

    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
