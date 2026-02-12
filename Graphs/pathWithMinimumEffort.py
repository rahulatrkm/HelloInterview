"""
Path With Minimum Effort

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array 
of size rows x columns, where heights[row][col] represents the height of cell 
(row, col). You are situated in the top-left cell (0, 0), and you hope to travel 
to the bottom-right cell (rows-1, columns-1).

You can move up, down, left, or right, and you wish to find a route that requires 
the minimum effort. A route's effort is the maximum absolute difference in heights 
between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the 
bottom-right cell.

Example 1:
    Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
    Output: 2
    Explanation: Route [1,3,5,3,5] has max diff = 2. Route [1,2,2,2,5] has max diff = 3.

Example 2:
    Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
    Output: 1
    Explanation: Route [1,2,3,4,5] has max diff = 1.

Example 3:
    Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
    Output: 0
    Explanation: A path exists where all consecutive cells have the same height.

Approach:
- Modified Dijkstra's algorithm where "distance" is the max absolute difference 
  along the path (instead of sum of weights)
- Use a min-heap with (effort, row, col), starting at (0, 0, 0)
- For each cell, explore 4 neighbors; the effort to reach a neighbor is 
  max(current_effort, abs(height difference))
- First time we reach (rows-1, cols-1) gives the minimum effort

Time Complexity: O(m * n * log(m * n)) — Dijkstra with heap on grid
Space Complexity: O(m * n) for distance matrix and heap
"""

import heapq
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Your code goes here
        m, n = len(heights), len(heights[0])
        efforts = [[float('inf')]*n for _ in range(m)]
        hq = [(0, 0, 0)]
        dire = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while hq:
            i, j, effort = heapq.heappop(hq)
            if efforts[i][j] <= effort:
                continue
            efforts[i][j] = effort
            for x,y in dire:
                nx, ny = i+x, j+y
                if 0 <= nx < m and 0 <= ny < n:
                    curr_effort = max(effort, abs(heights[i][j] - heights[nx][ny]))
                    if curr_effort < efforts[nx][ny]:
                        heapq.heappush(hq, (nx, ny, curr_effort))
        return efforts[-1][-1]



def run_tests():
    solution = Solution()

    # Test 1: Basic grid
    result = solution.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]])
    assert result == 2, f"Test 1 Failed: Expected 2, got {result}"
    print("Test 1 Passed")

    # Test 2: Path with effort 1
    result = solution.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]])
    assert result == 1, f"Test 2 Failed: Expected 1, got {result}"
    print("Test 2 Passed")

    # Test 3: Zero effort path exists
    result = solution.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]])
    assert result == 0, f"Test 3 Failed: Expected 0, got {result}"
    print("Test 3 Passed")

    # Test 4: Single cell
    result = solution.minimumEffortPath([[1]])
    assert result == 0, f"Test 4 Failed: Expected 0, got {result}"
    print("Test 4 Passed")

    # Test 5: Single row
    result = solution.minimumEffortPath([[1, 10, 6, 7, 9, 10, 4, 9]])
    assert result == 9, f"Test 5 Failed: Expected 9, got {result}"
    print("Test 5 Passed")

    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
