"""
Rotate Image
https://www.hellointerview.com/learn/code/matrices/rotate-image
https://leetcode.com/problems/rotate-image

Description:
    Rotate an n x n 2D matrix representing an image by 90 degrees clockwise.
    The rotation must be done in-place without using an additional matrix.

Examples:
    Input: matrix = [[1,4,7],[2,5,8],[3,6,9]]
    Output: [[3,2,1],[6,5,4],[9,8,7]]

Approach:
    1. Transpose the matrix (swap matrix[i][j] with matrix[j][i])
    2. Reverse each row

Time Complexity: O(n²)
Space Complexity: O(1) in-place
"""

from typing import List


class Solution:
    def rotate_image(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse each row
        for i in range(n):
            matrix[i].reverse()
        


if __name__ == "__main__":
    s = Solution()

    m1 = [[1,4,7],[2,5,8],[3,6,9]]
    s.rotate_image(m1)
    assert m1 == [[3,2,1],[6,5,4],[9,8,7]]

    m2 = [[1,2],[3,4]]
    s.rotate_image(m2)
    assert m2 == [[3,1],[4,2]]

    m3 = [[1]]
    s.rotate_image(m3)
    assert m3 == [[1]]

    m4 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    s.rotate_image(m4)
    assert m4 == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    print("All tests passed!")
