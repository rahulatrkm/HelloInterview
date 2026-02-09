"""
Minimum Knight Moves

You are given a chessboard of infinite size where the coordinates of each cell
are defined by integer pairs (x, y). The knight piece moves in an L-shape, either 
two squares horizontally and one square vertically, or two squares vertically and 
one square horizontally.

Write a function to determine the minimum number of moves required for the
knight to move from the starting position (0, 0) to the target position (x, y). 
Assume that it is always possible to reach the target position, and that x and y 
are both integers in the range [-200, 200].

Example 1:
    Input: x = 1, y = 2
    Output: 1
    Explanation: The knight can move from (0, 0) to (1, 2) in one move.

Example 2:
    Input: x = 4, y = 4
    Output: 4
    Explanation: The knight can move from (0, 0) to (4, 4) in four moves
                 ([0, 0] -> [2, 1] -> [4, 2] -> [6, 3] -> [4, 4])

Approach:
- Model this as a graph where each cell is a node and neighbors are cells reachable by knight moves
- Use BFS to find shortest path from (0, 0) to (x, y)
- Track visited cells to avoid infinite loops
- Return the number of moves when target is reached

Time Complexity: O(max(|x|, |y|)²) - Search space grows quadratically with distance
Space Complexity: O(max(|x|, |y|)²) - Visited set stores explored cells
"""

from collections import deque

class Solution:
    def minimum_knight_moves(self, x: int, y: int) -> int:
        # Your code goes here
        q = deque()
        q.append((0, 0, 0))
        visited = set()
        dire = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        while q:
            i, j, d = q.popleft()
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if (i,j) == (x,y):
                return d
            for dx, dy in dire:
                q.append((i+dx, j+dy, d+1))
        return -1



def run_tests():
    solution = Solution()
    
    # Test 1: One move to (1, 2)
    result = solution.minimum_knight_moves(1, 2)
    expected = 1
    assert result == expected, f"Test 1 Failed: Expected {expected}, got {result}"
    print("Test 1 Passed")
    
    # Test 2: Four moves to (4, 4)
    result = solution.minimum_knight_moves(4, 4)
    expected = 4
    assert result == expected, f"Test 2 Failed: Expected {expected}, got {result}"
    print("Test 2 Passed")
    
    # Test 3: Target at origin
    result = solution.minimum_knight_moves(0, 0)
    expected = 0
    assert result == expected, f"Test 3 Failed: Expected {expected}, got {result}"
    print("Test 3 Passed")
    
    # Test 4: Negative coordinates
    result = solution.minimum_knight_moves(-5, -5)
    expected = 4
    assert result == expected, f"Test 4 Failed: Expected {expected}, got {result}"
    print("Test 4 Passed")
    
    # Test 5: Asymmetric target
    result = solution.minimum_knight_moves(2, 1)
    expected = 1
    assert result == expected, f"Test 5 Failed: Expected {expected}, got {result}"
    print("Test 5 Passed")
    
    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
