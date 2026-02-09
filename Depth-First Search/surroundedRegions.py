"""
Surrounded Regions

DESCRIPTION (inspired by Leetcode.com):
Given an m x n matrix grid containing only characters 'X' and 'O', modify grid 
to replace all regions of 'O' that are completely surrounded by 'X' with 'X'.

A region of 'O' is surrounded by 'X' if there is no adjacent path (cells that 
border each other in N, W, E, S directions) consisting of only 'O' from anywhere 
inside that region to the border of the board.

Example 1:
Input: grid = [
    ["X","X","X","X","O"],
    ["X","X","O","X","X"],
    ["X","X","O","X","O"],
    ["X","O","X","X","X"],
    ["X","O","X","X","X"]
]
Output: [
    ["X","X","X","X","O"],
    ["X","X","X","X","X"],
    ["X","X","X","X","O"],
    ["X","O","X","X","X"],
    ["X","O","X","X","X"]
]

Explanation: The O's at [1][2] and [2][2] are surrounded, so they're replaced with X.

Approach:
- Start DFS from all border cells that are 'O'
- Mark all 'O' cells reachable from border as 'S' (safe)
- After DFS completes, replace all unmarked 'O' with 'X'
- Replace all 'S' back to 'O'
- This works by inverting the problem: find O's connected to border, keep them; replace rest

Time Complexity: O(M * N) where M is rows, N is columns
Space Complexity: O(M * N) for the recursion call stack
"""

from typing import List

class Solution:
    def surroundedRegions(self, grid: List[List[str]]) -> None:
        m, n = len(grid), len(grid[0])
        vis = set()
        dire = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and (i, j) not in vis and grid[i][j] == "O":
                vis.add((i, j))
                for x,y in dire:
                    dfs(i+x, j+y)

        # DFS from all borders
        for i in range(m):
            dfs(i, 0)  # left border
            dfs(i, n-1)  # right border
        
        for j in range(n):
            dfs(0, j)  # top border
            dfs(m-1, j)  # bottom border
            
        # Replace all O's not connected to border with X
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "O" and (i, j) not in vis:
                    grid[i][j] = "X"



if __name__ == "__main__":
    sol = Solution()
    
    # Test 1
    grid = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","O","O","X"],
        ["X","X","X","X"]
    ]
    expected = [
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"]
    ]
    sol.surroundedRegions(grid)
    assert grid == expected, f"Test 1 failed: expected {expected}, got {grid}"
    print("✓ Test 1 passed")
    
    # Test 2 - No surrounded O
    grid = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","O","O","X"],
        ["X","X","O","X"]
    ]
    expected = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","O","O","X"],
        ["X","X","O","X"]
    ]
    sol.surroundedRegions(grid)
    assert grid == expected, f"Test 2 failed: expected {expected}, got {grid}"
    print("✓ Test 2 passed")
    
    # Test 3 - All O on border
    grid = [
        ["O","O"],
        ["O","X"]
    ]
    expected = [
        ["O","O"],
        ["O","X"]
    ]
    sol.surroundedRegions(grid)
    assert grid == expected, f"Test 3 failed: expected {expected}, got {grid}"
    print("✓ Test 3 passed")
    
    # Test 4 - All X
    grid = [
        ["X","X"],
        ["X","X"]
    ]
    expected = [
        ["X","X"],
        ["X","X"]
    ]
    sol.surroundedRegions(grid)
    assert grid == expected, f"Test 4 failed: expected {expected}, got {grid}"
    print("✓ Test 4 passed")
    
    # Test 5 - Single surrounded O
    grid = [
        ["X","X","X"],
        ["X","O","X"],
        ["X","X","X"]
    ]
    expected = [
        ["X","X","X"],
        ["X","X","X"],
        ["X","X","X"]
    ]
    sol.surroundedRegions(grid)
    assert grid == expected, f"Test 5 failed: expected {expected}, got {grid}"
    print("✓ Test 5 passed")
    
    # Test 6 - Connected O touching border
    grid = [
        ["X","O","X"],
        ["X","O","X"],
        ["X","X","X"]
    ]
    expected = [
        ["X","O","X"],
        ["X","O","X"],
        ["X","X","X"]
    ]
    sol.surroundedRegions(grid)
    assert grid == expected, f"Test 6 failed: expected {expected}, got {grid}"
    print("✓ Test 6 passed")
    
    # Test 7 - Mixed
    grid = [
        ["X","X","X","X","X"],
        ["X","O","O","O","X"],
        ["X","O","X","O","X"],
        ["X","O","O","O","X"],
        ["X","X","X","X","X"]
    ]
    expected = [
        ["X","X","X","X","X"],
        ["X","X","X","X","X"],
        ["X","X","X","X","X"],
        ["X","X","X","X","X"],
        ["X","X","X","X","X"]
    ]
    sol.surroundedRegions(grid)
    assert grid == expected, f"Test 7 failed: expected {expected}, got {grid}"
    print("✓ Test 7 passed")
    
    print("\n✓ All tests passed!")
