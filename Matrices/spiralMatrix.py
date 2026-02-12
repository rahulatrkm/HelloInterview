"""
Spiral Matrix
https://www.hellointerview.com/learn/code/matrices/spiral-matrix
https://leetcode.com/problems/spiral-matrix

Description:
    Traverse an m x n matrix in spiral order and return all elements in a single list.
    The traversal starts from the top left corner and proceeds clockwise, spiraling
    inward until every element has been visited.

Examples:
    Input: matrix = [[0,1,2],[3,4,5],[6,7,8]]
    Output: [0,1,2,5,8,7,6,3,4]

Approach:
    - Repeatedly peel off layers: top row (L→R), right col (T→B),
      bottom row (R→L), left col (B→T)
    - Pop rows / elements from matrix as you go, or use boundary pointers

Time Complexity: O(m * n)
Space Complexity: O(m * n) for the result
"""

from typing import List


class Solution:
    def spiral_order(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix:
            ans += matrix.pop(0)  # top row
            if matrix and matrix[0]:  # right col
                for row in matrix:
                    ans.append(row.pop())
            if matrix:  # bottom row
                ans += matrix.pop()[::-1]
            if matrix and matrix[0]:  # left col
                for row in matrix[::-1]:
                    ans.append(row.pop(0))
        return ans


if __name__ == "__main__":
    s = Solution()

    assert s.spiral_order([[0,1,2],[3,4,5],[6,7,8]]) == [0,1,2,5,8,7,6,3,4]
    assert s.spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
    assert s.spiral_order([[1]]) == [1]
    assert s.spiral_order([[1,2],[3,4]]) == [1,2,4,3]
    assert s.spiral_order([[1,2,3]]) == [1,2,3]
    assert s.spiral_order([[1],[2],[3]]) == [1,2,3]

    print("All tests passed!")
