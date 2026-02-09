"""
Number of Islands

DESCRIPTION (inspired by Leetcode.com):
You are given binary matrix grid of size m x n, where '1' denotes land and '0' 
signifies water. Determine the count of islands present in this grid. An island 
is defined as a region of contiguous land cells connected either vertically or 
horizontally, and it is completely encircled by water. Assume that the grid is 
bordered by water on all sides.

Example 1:
Input: grid = [
    [1,1,0,1],
    [1,1,0,1],
    [1,1,0,0],
]
Output: 2

Explanation: The grid contains 2 islands (connected components of 1s).

Example 2:
Input: grid = [
    [1,1],
    [1,1]
]
Output: 1

Explanation: All cells are connected, forming a single island.

Approach:
- Use DFS to traverse connected components
- Count each connected component as one island
- For each unvisited '1' cell, start a DFS and increment island count
- During DFS, mark visited cells as '0' (or use a visited set)
- Only traverse to adjacent cells (up, down, left, right)
- Base case: out of bounds or water cell returns

Time Complexity: O(M * N) where M is rows, N is columns
Space Complexity: O(M * N) for the recursion call stack
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        vis = set()
        dire = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and (i,j) not in vis and grid[i][j] == "1":
                vis.add((i, j))
                for x, y in dire:
                    dfs(i+x, j+y)
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in vis:
                    dfs(i, j)
                    cnt += 1
        return cnt

if __name__ == "__main__":
    sol = Solution()
    
    # Test 1
    grid = [
        ["1","1","0","1"],
        ["1","1","0","1"],
        ["1","1","0","0"]
    ]
    result = sol.numIslands(grid)
    assert result == 2, f"Test 1 failed: expected 2, got {result}"
    print("✓ Test 1 passed")
    
    # Test 2 - Single island
    grid = [
        ["1","1"],
        ["1","1"]
    ]
    result = sol.numIslands(grid)
    assert result == 1, f"Test 2 failed: expected 1, got {result}"
    print("✓ Test 2 passed")
    
    # Test 3 - No islands
    grid = [
        ["0","0"],
        ["0","0"]
    ]
    result = sol.numIslands(grid)
    assert result == 0, f"Test 3 failed: expected 0, got {result}"
    print("✓ Test 3 passed")
    
    # Test 4 - All islands
    grid = [
        ["1","0"],
        ["0","1"]
    ]
    result = sol.numIslands(grid)
    assert result == 2, f"Test 4 failed: expected 2, got {result}"
    print("✓ Test 4 passed")
    
    # Test 5 - Single cell
    grid = [["1"]]
    result = sol.numIslands(grid)
    assert result == 1, f"Test 5 failed: expected 1, got {result}"
    print("✓ Test 5 passed")
    
    # Test 6 - Large grid
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    result = sol.numIslands(grid)
    assert result == 3, f"Test 6 failed: expected 3, got {result}"
    print("✓ Test 6 passed")
    
    # Test 7 - Complex pattern
    grid = [
        ["1","0","1","1","0"],
        ["1","0","1","1","0"],
        ["1","0","0","1","0"],
        ["1","1","0","1","1"]
    ]
    result = sol.numIslands(grid)
    assert result == 2, f"Test 7 failed: expected 2, got {result}"
    print("✓ Test 7 passed")
    
    print("\n✓ All tests passed!")
