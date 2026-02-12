"""
Cheapest Flights Within K Stops

There are n cities connected by some number of flights. You are given an array 
flights where flights[i] = [from_i, to_i, price_i] indicates that there is a 
flight from city from_i to city to_i with cost price_i.

You are also given three integers src, dst, and k. Return the cheapest price from 
src to dst with at most k stops. If there is no such route, return -1.

Example 1:
    Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 
           src = 0, dst = 3, k = 1
    Output: 700
    Explanation: 0 -> 1 -> 3 costs 100 + 600 = 700.

Example 2:
    Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
    Output: 200
    Explanation: 0 -> 1 -> 2 costs 100 + 100 = 200 (1 stop at node 1).

Example 3:
    Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
    Output: 500
    Explanation: Direct flight 0 -> 2 costs 500 (no stops allowed).

Approach:
- Use Bellman-Ford with at most k+1 relaxation rounds (k stops = k+1 edges)
- Initialize dist array with infinity, dist[src] = 0
- For each round, create a copy of distances and relax all edges
- Using a copy prevents using updates from the same round (ensures stop count)
- After k+1 rounds, dist[dst] is the answer (or -1 if still infinity)

Time Complexity: O(k * E) where E is number of flights
Space Complexity: O(V) for the distance array
"""

from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Your code goes here
        prices = [float('inf')] * n
        prices[src] = 0
        for _ in range(k+1):
            new_prices = prices.copy()
            for u, v, w in flights:
                if prices[u] != float('inf'):
                    new_prices[v] = min(new_prices[v], prices[u] + w)
            prices = new_prices
        return prices[dst] if prices[dst] != float('inf') else -1


def run_tests():
    solution = Solution()

    # Test 1: Multiple paths, pick cheapest within 1 stop
    result = solution.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)
    assert result == 700, f"Test 1 Failed: Expected 700, got {result}"
    print("Test 1 Passed")

    # Test 2: Cheaper path with 1 stop
    result = solution.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)
    assert result == 200, f"Test 2 Failed: Expected 200, got {result}"
    print("Test 2 Passed")

    # Test 3: No stops allowed, must take direct flight
    result = solution.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0)
    assert result == 500, f"Test 3 Failed: Expected 500, got {result}"
    print("Test 3 Passed")

    # Test 4: No route possible
    result = solution.findCheapestPrice(3, [[0,1,100]], 0, 2, 1)
    assert result == -1, f"Test 4 Failed: Expected -1, got {result}"
    print("Test 4 Passed")

    # Test 5: Direct flight is cheapest
    result = solution.findCheapestPrice(3, [[0,1,100],[1,2,200],[0,2,150]], 0, 2, 1)
    assert result == 150, f"Test 5 Failed: Expected 150, got {result}"
    print("Test 5 Passed")

    # Test 6: Need exactly k stops
    result = solution.findCheapestPrice(5, [[0,1,1],[1,2,1],[2,3,1],[3,4,1]], 0, 4, 3)
    assert result == 4, f"Test 6 Failed: Expected 4, got {result}"
    print("Test 6 Passed")

    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
