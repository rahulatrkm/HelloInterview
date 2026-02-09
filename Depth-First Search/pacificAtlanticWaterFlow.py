"""
Pacific Atlantic Water Flow

DESCRIPTION (inspired by Leetcode.com):
You are given an m x n matrix of non-negative integers representing a grid of 
land, where rain falls on every cell. Each value in the grid represents the 
height of that piece of land.

The Pacific Ocean touches the left and top edges of the matrix, while the 
Atlantic Ocean touches the right and bottom edges. Water can only flow from a 
cell to its neighboring cells directly north, south, east, or west, but only if 
the height of the neighboring cell is equal to or lower than the current cell.

Write a function to return a list of grid coordinates (i, j) where water can 
flow to both the Pacific and Atlantic Oceans.

Example 1:
Input: grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Output: [[0,2],[1,2],[2,0],[2,1],[2,2]]

Explanation: Water can flow from [0,2], [1,2], [2,0], [2,1], [2,2] to both oceans.

Approach:
- Use "boundary DFS" starting from ocean boundaries
- Start DFS from all Pacific boundary cells (top and left edges)
- Start DFS from all Atlantic boundary cells (bottom and right edges)
- For each ocean, do DFS only to cells with height >= current cell height
- (water flows downhill, so we search uphill to find cells that flow to ocean)
- Find intersection of cells reachable from both oceans

Time Complexity: O(M * N) where M is rows, N is columns
Space Complexity: O(M * N) for visited sets
"""

from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        dire = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(i, j, ht, vis):
            if 0 <= i < m and 0 <= j < n and heights[i][j] >= ht and (i, j) not in vis:
                vis.add((i, j))
                for x, y in dire:
                    dfs(i+x, j+y, heights[i][j], vis)
        pac, atl = set(), set()
        for i in range(m):
            dfs(i, 0, heights[i][0], pac)
            dfs(i, n-1, heights[i][n-1], atl)
        
        for j in range(n):
            dfs(0, j, heights[0][j], pac)
            dfs(m-1, j, heights[m-1][j], atl)

        return [[i, j] for i, j in pac & atl]




if __name__ == "__main__":
    sol = Solution()
    
    # Test 1
    heights = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result = sol.pacificAtlantic(heights)
    expected = [[0,2],[1,2],[2,0],[2,1],[2,2]]
    assert sorted(result) == sorted(expected), f"Test 1 failed: expected {expected}, got {result}"
    print("✓ Test 1 passed")
    
    # Test 2 - Single cell
    heights = [[1]]
    result = sol.pacificAtlantic(heights)
    expected = [[0, 0]]
    assert sorted(result) == sorted(expected), f"Test 2 failed: expected {expected}, got {result}"
    print("✓ Test 2 passed")
    
    # Test 3 - Two cells
    heights = [[1, 1]]
    result = sol.pacificAtlantic(heights)
    expected = [[0,0],[0,1]]
    assert sorted(result) == sorted(expected), f"Test 3 failed: expected {expected}, got {result}"
    print("✓ Test 3 passed")
    
    # Test 4 - Ascending
    heights = [
        [1, 2],
        [3, 4]
    ]
    result = sol.pacificAtlantic(heights)
    expected = [[0,1],[1,0],[1,1]]
    assert sorted(result) == sorted(expected), f"Test 4 failed: expected {expected}, got {result}"
    print("✓ Test 4 passed")
    
    # Test 5 - Only corners
    heights = [
        [1, 9],
        [9, 1]
    ]
    result = sol.pacificAtlantic(heights)
    expected = [[0,1],[1,0]]
    assert sorted(result) == sorted(expected), f"Test 5 failed: expected {expected}, got {result}"
    print("✓ Test 5 passed")
    
    # Test 6 - Complex
    heights = [
        [1, 1, 1],
        [1, 2, 1],
        [1, 1, 1]
    ]
    result = sol.pacificAtlantic(heights)
    expected = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    assert sorted(result) == sorted(expected), f"Test 6 failed: expected {expected}, got {result}"
    print("✓ Test 6 passed")
    
    # Test 7 - Descending
    heights = [
        [4, 3],
        [2, 1]
    ]
    result = sol.pacificAtlantic(heights)
    expected = [[0,0],[0,1],[1,0]]
    assert sorted(result) == sorted(expected), f"Test 7 failed: expected {expected}, got {result}"
    print("✓ Test 7 passed")
    
    print("\n✓ All tests passed!")
