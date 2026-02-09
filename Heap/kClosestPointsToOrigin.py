"""
K Closest Points to Origin
https://www.hellointerview.com/learn/code/heap/k-closest-points-to-origin

Given a list of points [[x1,y1],[x2,y2],...] and an integer k, find the k closest
points to the origin (0,0) on the 2D plane.
Return the k closest points in any order.

Example 1:
  Input: points = [[3,4],[2,2],[1,1],[0,0],[5,5]], k = 3
  Output: [[2,2],[1,1],[0,0]]  (any order)

Approach:
- Use a max-heap of size k (negate distances for max-heap via min-heap)
- For each point, compute distance² = x² + y² (no need for sqrt)
- Push (-distance², index) into heap
- If heap size > k, pop the farthest point
- Alternatively: push first k, then heappushpop if closer

Time: O(n log k)
Space: O(k)
"""

from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k >= len(points):
            return points  # All points are among the k closest
        if k <= 0:
            return []  # No points to return
        
        hq = [(-(x**2+y**2), x, y) for x,y in points[:k]]
        heapq.heapify(hq)
        for x,y in points[k:]:
            euc_dist = x**2+y**2
            if euc_dist < -hq[0][0]:
                heapq.heappushpop(hq, (-euc_dist, x, y))
        return [(x,y) for d,x,y in hq]


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Basic case
    result = sol.kClosest([[3,4],[2,2],[1,1],[0,0],[5,5]], 3)
    expected = {(0,0),(1,1),(2,2)}
    assert set(tuple(p) for p in result) == expected, \
        f"Test 1 failed: got {result}"
    print("Test 1 passed ✓")

    # Test 2: k = 1
    result = sol.kClosest([[1,3],[-2,2]], 1)
    assert [list(p) for p in result] == [[-2,2]], \
        f"Test 2 failed: got {result}"
    print("Test 2 passed ✓")

    # Test 3: All points same distance
    result = sol.kClosest([[1,0],[0,1],[-1,0],[0,-1]], 2)
    assert len(result) == 2, f"Test 3 failed: got {result}"
    print("Test 3 passed ✓")

    # Test 4: Single point
    result = sol.kClosest([[5,5]], 1)
    assert [list(p) for p in result] == [[5,5]], f"Test 4 failed: got {result}"
    print("Test 4 passed ✓")

    # Test 5: k = all points
    result = sol.kClosest([[1,1],[2,2],[3,3]], 3)
    expected = {(1,1),(2,2),(3,3)}
    assert set(tuple(p) for p in result) == expected, \
        f"Test 5 failed: got {result}"
    print("Test 5 passed ✓")

    # Test 6: Negative coordinates
    result = sol.kClosest([[-2,-3],[3,4],[1,1]], 2)
    expected = {(-2,-3),(1,1)}
    assert set(tuple(p) for p in result) == expected, \
        f"Test 6 failed: got {result}"
    print("Test 6 passed ✓")

    print("\nAll tests passed! ✓")
