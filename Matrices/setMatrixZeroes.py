"""
Set Matrix Zeroes
https://www.hellointerview.com/learn/code/matrices/set-matrix-zeroes
https://leetcode.com/problems/set-matrix-zeroes

Description:
    Given an m x n integer matrix, if any element is 0, set its entire row and
    column to 0. Do it in-place.

Examples:
    Input: matrix = [[0,2,3],[4,5,6],[7,8,9]]
    Output: [[0,0,0],[0,5,6],[0,8,9]]

    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]

Approach:
    - Use first row and first column as markers (O(1) space)
    - Save whether first row/col originally have zeros
    - Scan inner matrix, mark matrix[i][0] and matrix[0][j] when matrix[i][j]==0
    - Zero inner cells based on markers, then handle first row/col last

Time Complexity: O(m * n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        is_first_row_zero = any(matrix[0][j] == 0 for j in range(len(matrix[0])))
        is_first_col_zero = any(matrix[i][0] == 0 for i in range(len(matrix)))
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if is_first_row_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if is_first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0


if __name__ == "__main__":
    s = Solution()

    m1 = [[0,2,3],[4,5,6],[7,8,9]]
    s.setZeroes(m1)
    assert m1 == [[0,0,0],[0,5,6],[0,8,9]]

    m2 = [[1,1,1],[1,0,1],[1,1,1]]
    s.setZeroes(m2)
    assert m2 == [[1,0,1],[0,0,0],[1,0,1]]

    m3 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    s.setZeroes(m3)
    assert m3 == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

    m4 = [[1,2],[3,4]]
    s.setZeroes(m4)
    assert m4 == [[1,2],[3,4]]

    print("All tests passed!")
