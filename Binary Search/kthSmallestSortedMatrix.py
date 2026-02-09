"""
Kth Smallest Element in a Sorted Matrix
https://www.hellointerview.com/learn/code/binary-search/kth-smallest-element-in-a-sorted-matrix

You're given a square grid (n × n matrix) where each row is sorted in ascending
order from left to right, and each column is also sorted in ascending order from
top to bottom.

Given the matrix and an integer k, find the k-th smallest element among all
elements in the matrix.

Note: k is 1-indexed, meaning k = 1 returns the smallest element.

Example 1:
  Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
  Output: 13
  Explanation: Sorted = [1,5,9,10,11,12,13,13,15]. The 8th smallest is 13.

Example 2:
  Input: matrix = [[-5]], k = 1
  Output: -5

Approach:
- Binary search on the VALUE (not index)
- Search space: matrix[0][0] (min) to matrix[n-1][n-1] (max)
- For a candidate value mid, count how many elements in the matrix are <= mid
  - Use the sorted property: start from bottom-left corner
  - If matrix[row][col] <= mid → all elements above in this column are also <= mid,
    add (row+1) to count and move right
  - Else move up
- If count < k → answer is larger, left = mid + 1
- Else → answer could be mid or smaller, right = mid

Time: O(n * log(max - min))
Space: O(1)
"""

from typing import List
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # hq = [(nums[0], 0, i) for i, nums in enumerate(matrix)]
        # heapq.heapify(hq)
        # while k:
        #     num, j, i = heapq.heappop(hq)
        #     k -= 1
        #     if k == 0:
        #         return num
        #     c = j + 1
        #     if c < len(matrix[i]):
        #         heapq.heappush(hq, (matrix[i][c], c, i))
        # return -1  # This line should never be reached if k is valid

        n = len(matrix)
        left, right = matrix[0][0], matrix[n-1][n-1]
        while left < right:
            mid = (left + right) // 2
            count = 0
            row, col = n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Basic case
    assert sol.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8) == 13, \
        f"Test 1 failed: got {sol.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8)}"
    print("Test 1 passed ✓")

    # Test 2: Single element
    assert sol.kthSmallest([[-5]], 1) == -5, \
        f"Test 2 failed: got {sol.kthSmallest([[-5]], 1)}"
    print("Test 2 passed ✓")

    # Test 3: k = 1 (smallest)
    assert sol.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 1) == 1, \
        f"Test 3 failed: got {sol.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 1)}"
    print("Test 3 passed ✓")

    # Test 4: k = n*n (largest)
    assert sol.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 9) == 15, \
        f"Test 4 failed: got {sol.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 9)}"
    print("Test 4 passed ✓")

    # Test 5: 2x2 matrix
    assert sol.kthSmallest([[1,2],[3,4]], 3) == 3, \
        f"Test 5 failed: got {sol.kthSmallest([[1,2],[3,4]], 3)}"
    print("Test 5 passed ✓")

    # Test 6: Duplicates in matrix
    assert sol.kthSmallest([[1,3,5],[6,7,12],[11,14,14]], 6) == 11, \
        f"Test 6 failed: got {sol.kthSmallest([[1,3,5],[6,7,12],[11,14,14]], 6)}"
    print("Test 6 passed ✓")

    # Test 7: Negative values
    assert sol.kthSmallest([[-5,-4],[-3,-2]], 2) == -4, \
        f"Test 7 failed: got {sol.kthSmallest([[-5,-4],[-3,-2]], 2)}"
    print("Test 7 passed ✓")

    print("\nAll tests passed! ✓")
