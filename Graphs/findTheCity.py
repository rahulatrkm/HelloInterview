"""
Find the City With the Smallest Number of Neighbors at a Threshold Distance

There are n cities numbered from 0 to n-1. Given the array edges where 
edges[i] = [from_i, to_i, weight_i] represents a bidirectional weighted edge 
between cities from_i and to_i, and an integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through 
some path whose distance is at most distanceThreshold. If there are multiple 
such cities, return the city with the greatest number.

Example 1:
    Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
    Output: 3
    Explanation: 
        City 0 -> [1, 2, 3] (reachable within threshold: cities 1,2,3 → 3 neighbors)
        City 1 -> [0, 2, 3] (reachable within threshold: cities 0,2,3 → 3 neighbors)
        City 2 -> [1, 3] (reachable within threshold: cities 1,3 → 2 neighbors)
        City 3 -> [1, 2] (reachable within threshold: cities 1,2 → 2 neighbors)
        Cities 2 and 3 both have 2 reachable neighbors, return 3 (greatest number).

Example 2:
    Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 
           distanceThreshold = 2
    Output: 0
    Explanation: City 0 can only reach city 1 within distance 2. Other cities 
                 can reach at least 2 cities.

Approach:
- Use Floyd-Warshall to compute all-pairs shortest paths
- Initialize dist[i][j] = weight if edge exists, infinity otherwise, dist[i][i] = 0
- For each intermediate node k, update dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
- Count reachable cities within threshold for each city
- Return the city with minimum count (tie-break: largest city number)

Time Complexity: O(n^3) for Floyd-Warshall
Space Complexity: O(n^2) for distance matrix
"""

from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Your code goes here
        dist = [[float('inf')]*n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        ans = 0
        mn_cnt = n
        for i in range(n):
            cnt = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    cnt += 1
            if cnt <= mn_cnt:
                mn_cnt = cnt
                ans = i
        return ans



def run_tests():
    solution = Solution()

    # Test 1: Example from problem
    result = solution.findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4)
    assert result == 3, f"Test 1 Failed: Expected 3, got {result}"
    print("Test 1 Passed")

    # Test 2: Tight threshold
    result = solution.findTheCity(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2)
    assert result == 0, f"Test 2 Failed: Expected 0, got {result}"
    print("Test 2 Passed")

    # Test 3: Two disconnected components
    result = solution.findTheCity(4, [[0,1,1],[2,3,1]], 1)
    assert result == 3, f"Test 3 Failed: Expected 3, got {result}"
    print("Test 3 Passed")

    # Test 4: All cities connected, large threshold
    result = solution.findTheCity(3, [[0,1,1],[1,2,1],[0,2,5]], 10)
    assert result == 2, f"Test 4 Failed: Expected 2, got {result}"
    print("Test 4 Passed")

    # Test 5: Threshold of 0 — no city reachable from any other
    result = solution.findTheCity(3, [[0,1,1],[1,2,1]], 0)
    assert result == 2, f"Test 5 Failed: Expected 2, got {result}"
    print("Test 5 Passed")

    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
