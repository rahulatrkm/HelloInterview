"""
Rotting Oranges

You are given an m x n grid representing a box of oranges. Each cell in the grid 
can have one of three values:

1. "E" representing an empty cell
2. "F" representing a fresh orange
3. "R" representing a rotten orange

Every minute, any fresh orange that is adjacent (4-directionally: up, down,
left, right) to a rotten orange becomes rotten.

Write a function that takes this grid as input and returns the minimum number of
minutes that must elapse until no cell has a fresh orange. If it is impossible
to rot every fresh orange, return -1.

Example 1:
    Input: grid = [["R", "F"], ["F", "F"]]
    Output: 2
    Explanation: After Minute 1: The rotting orange at grid[0][0] rots the fresh oranges 
                 at grid[0][1] and grid[1][0]. After Minute 2: The rotting orange at 
                 grid[1][0] (or grid[0][1]) rots the fresh orange at grid[1][1].

Example 2:
    Input: grid = [["R", "E"], ["E", "F"]]
    Output: -1
    Explanation: The two adjacent oranges to the rotten orange at grid[0][0] are empty, 
                 so after 1 minute, there are no fresh oranges to rot.

Example 3:
    Input: grid = [["R", "F", "F", "F"], ["F", "F", "F", "R"], ["E", "E", "F", "F"]]
    Output: 2

Approach:
- Model this as a graph where each cell is a node and edges are 4-directional connections
- Use multi-source BFS starting from all rotten oranges simultaneously
- Count fresh oranges and simulate rotting process level by level
- Return -1 if any fresh oranges remain after BFS completes

Time Complexity: O(m * n) - Visit each cell at most once
Space Complexity: O(m * n) - Queue can contain all cells in worst case
"""

from collections import deque

class Solution:
    def rotting_oranges(self, grid: list[list[str]]) -> int:
        # Your code goes here
        m, n = len(grid), len(grid[0])
        q = deque()
        vis = [[float('inf')]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "E":
                    vis[i][j] = 0
                elif grid[i][j] == "R":
                    vis[i][j] = 0
                    q.append((i, j, 0))
        
        dire = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while q:
            i, j, d = q.popleft()
            if 0 <= i < m and 0 <= j < n and vis[i][j] >= d:
                vis[i][j] = d
                for x, y in dire:
                    q.append((i+x, j+y, d+1))
        ans = max(max(row) for row in vis)
        return ans if ans != float('inf') else -1


def run_tests():
    solution = Solution()
    
    # Test 1: Simple 2x2 grid
    grid = [["R", "F"], ["F", "F"]]
    result = solution.rotting_oranges(grid)
    expected = 2
    assert result == expected, f"Test 1 Failed: Expected {expected}, got {result}"
    print("Test 1 Passed")
    
    # Test 2: Impossible case
    grid = [["R", "E"], ["E", "F"]]
    result = solution.rotting_oranges(grid)
    expected = -1
    assert result == expected, f"Test 2 Failed: Expected {expected}, got {result}"
    print("Test 2 Passed")
    
    # Test 3: Larger grid
    grid = [["R", "F", "F", "F"], ["F", "F", "F", "R"], ["E", "E", "F", "F"]]
    result = solution.rotting_oranges(grid)
    expected = 2
    assert result == expected, f"Test 3 Failed: Expected {expected}, got {result}"
    print("Test 3 Passed")
    
    # Test 4: All fresh oranges
    grid = [["F", "F"], ["F", "F"]]
    result = solution.rotting_oranges(grid)
    expected = -1
    assert result == expected, f"Test 4 Failed: Expected {expected}, got {result}"
    print("Test 4 Passed")
    
    # Test 5: All rotten oranges
    grid = [["R", "R"], ["R", "R"]]
    result = solution.rotting_oranges(grid)
    expected = 0
    assert result == expected, f"Test 5 Failed: Expected {expected}, got {result}"
    print("Test 5 Passed")
    
    # Test 6: No oranges
    grid = [["E", "E"], ["E", "E"]]
    result = solution.rotting_oranges(grid)
    expected = 0
    assert result == expected, f"Test 6 Failed: Expected {expected}, got {result}"
    print("Test 6 Passed")
    
    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
