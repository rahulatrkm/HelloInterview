"""
Word Search

Given an m x n grid of characters board and a string word, return true if word 
exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same letter cell
may not be used more than once.

Example 1:
    Input: board = [['B','L','C','H'],['D','E','L','T'],['D','A','K','A']], word = "BLEAK"
    Output: True

Example 2:
    Input: board = [['B','L','C','H'],['D','E','L','T'],['D','A','K','A']], word = "BLEED"
    Output: False

Approach:
- Use backtracking with DFS to try to find the word starting from each cell
- For each cell matching the first letter, explore all 4 directions recursively
- Mark visited cells (e.g., replace with '#') to avoid reuse, then restore (backtrack)
- Return True as soon as any path matches the full word

Time Complexity: O(m * n * 4^L) where L is the length of the word
Space Complexity: O(L) for the recursion stack
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Your code goes here
        vis = set()
        m, n = len(board), len(board[0])
        dire = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(i, j, idx):
            if idx == len(word):
                return True
            if 0 <= i < m and 0 <= j < n and (i, j) not in vis and word[idx] == board[i][j]:
                vis.add((i, j))
                for x, y in dire:
                    if dfs(i+x, j+y, idx+1):
                        return True
                vis.remove((i, j))
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
        


def run_tests():
    solution = Solution()
    
    # Test 1: Word exists - BLEAK
    board = [['B','L','C','H'],['D','E','L','T'],['D','A','K','A']]
    result = solution.exist(board, "BLEAK")
    assert result == True, f"Test 1 Failed: Expected True, got {result}"
    print("Test 1 Passed")
    
    # Test 2: Word doesn't exist - BLEED
    board = [['B','L','C','H'],['D','E','L','T'],['D','A','K','A']]
    result = solution.exist(board, "BLEED")
    assert result == False, f"Test 2 Failed: Expected False, got {result}"
    print("Test 2 Passed")
    
    # Test 3: Single cell match
    board = [['A']]
    result = solution.exist(board, "A")
    assert result == True, f"Test 3 Failed: Expected True, got {result}"
    print("Test 3 Passed")
    
    # Test 4: Single cell no match
    board = [['A']]
    result = solution.exist(board, "B")
    assert result == False, f"Test 4 Failed: Expected False, got {result}"
    print("Test 4 Passed")
    
    # Test 5: Word uses all cells
    board = [['A','B'],['C','D']]
    result = solution.exist(board, "ABDC")
    assert result == True, f"Test 5 Failed: Expected True, got {result}"
    print("Test 5 Passed")
    
    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
