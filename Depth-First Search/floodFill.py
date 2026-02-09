"""
Flood Fill

DESCRIPTION (inspired by Leetcode.com):
Given a m x n integer grid image and integers sr, sc, and newColor, write a 
function to perform a flood fill on the image starting from the pixel 
image[sr][sc].

In a flood fill, start by changing the color of image[sr][sc] to newColor. Then, 
change the color of all pixels connected to image[sr][sc] from either the top, 
bottom, left or right that have the same color as image[sr][sc], along with all 
the connected pixels of those pixels, and so on.

Example 1:
Input: image = [[1,0,1],[1,0,0],[0,0,1]], sr = 1, sc = 1, color = 2
Output: [[1,2,1],[1,2,2],[2,2,1]]

Explanation: The zeroes connected to the starting pixel (1, 1) are colored with
newColor (2).

Approach:
- Use DFS to traverse the connected component of the starting pixel
- Keep the original color and only recolor pixels that match it
- Base case: out of bounds or pixel color doesn't match original
- To avoid cycles, recolor as you visit, or use a visited set
- If original color equals newColor, return image immediately

Time Complexity: O(M * N) where M is rows, N is columns
Space Complexity: O(M * N) for recursion stack in worst case
"""

from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        dire = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(i, j, clr):
            if 0 <= i < m and 0 <= j < n and image[i][j] == clr:
                image[i][j] = color
                for x,y in dire:
                    dfs(i+x, j+y, clr)
        
        if image[sr][sc] != color:
            dfs(sr,sc, image[sr][sc])
        return image

if __name__ == "__main__":
    sol = Solution()

    # Test 1
    image = [[1,0,1],[1,0,0],[0,0,1]]
    result = sol.floodFill(image, 1, 1, 2)
    expected = [[1,2,1],[1,2,2],[2,2,1]]
    assert result == expected, f"Test 1 failed: expected {expected}, got {result}"
    print("✓ Test 1 passed")

    # Test 2 - No change
    image = [[1,1],[1,1]]
    result = sol.floodFill(image, 0, 0, 1)
    expected = [[1,1],[1,1]]
    assert result == expected, f"Test 2 failed: expected {expected}, got {result}"
    print("✓ Test 2 passed")

    # Test 3 - Single cell
    image = [[0]]
    result = sol.floodFill(image, 0, 0, 2)
    expected = [[2]]
    assert result == expected, f"Test 3 failed: expected {expected}, got {result}"
    print("✓ Test 3 passed")

    # Test 4 - Border connected
    image = [[0,0,0],[0,1,1]]
    result = sol.floodFill(image, 0, 0, 2)
    expected = [[2,2,2],[2,1,1]]
    assert result == expected, f"Test 4 failed: expected {expected}, got {result}"
    print("✓ Test 4 passed")

    # Test 5 - Diagonal not connected
    image = [[1,0,1],[0,1,0],[1,0,1]]
    result = sol.floodFill(image, 1, 1, 2)
    expected = [[1,0,1],[0,2,0],[1,0,1]]
    assert result == expected, f"Test 5 failed: expected {expected}, got {result}"
    print("✓ Test 5 passed")

    # Test 6 - Large fill
    image = [[3,3,3],[3,3,0],[3,0,1]]
    result = sol.floodFill(image, 0, 0, 2)
    expected = [[2,2,2],[2,2,0],[2,0,1]]
    assert result == expected, f"Test 6 failed: expected {expected}, got {result}"
    print("✓ Test 6 passed")

    # Test 7 - Starting at edge
    image = [[0,1,1],[0,1,0],[0,0,0]]
    result = sol.floodFill(image, 2, 0, 2)
    expected = [[2,1,1],[2,1,2],[2,2,2]]
    assert result == expected, f"Test 7 failed: expected {expected}, got {result}"
    print("✓ Test 7 passed")

    print("\n✓ All tests passed!")
