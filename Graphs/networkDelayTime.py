"""
Network Delay Time

You are given a network of n nodes, labeled from 1 to n. You are also given 
times, a list of travel times as directed edges times[i] = (u, v, w), where u 
is the source node, v is the target node, and w is the time it takes for a 
signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for 
all of the n nodes to receive the signal. If it is impossible for all the n nodes 
to receive the signal, return -1.

Example 1:
    Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
    Output: 2
    Explanation: Signal reaches node 1 and 3 at time 1, and node 4 at time 2.

Example 2:
    Input: times = [[1,2,1]], n = 2, k = 2
    Output: -1
    Explanation: Node 1 cannot be reached from node 2.

Approach:
- Classic Dijkstra's algorithm — find shortest path from source k to all nodes
- Build adjacency list with weights
- Use a min-heap (priority queue) starting from node k with distance 0
- Greedily process the closest unvisited node, relax edges
- Answer is the maximum distance among all nodes (time for last node to receive signal)
- If any node is unreachable, return -1

Time Complexity: O(E log V) where E = edges, V = nodes
Space Complexity: O(V + E) for adjacency list and heap
"""

import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Your code goes here
        adj = defaultdict(dict)
        for u, v, w in times:
            adj[u-1][v-1] = w
        
        dist = [float('inf')] * n
        dist[k-1] = 0
        heap = [(0, k-1)]
        while heap:
            delay, node = heapq.heappop(heap)
            if delay > dist[node]:
                continue
            for nei, w in adj[node].items():
                if delay + w < dist[nei]:
                    dist[nei] = delay + w
                    heapq.heappush(heap, (dist[nei], nei))

        max_delay = max(dist)
        return max_delay if max_delay != float('inf') else -1


def run_tests():
    solution = Solution()

    # Test 1: Basic network
    result = solution.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)
    assert result == 2, f"Test 1 Failed: Expected 2, got {result}"
    print("Test 1 Passed")

    # Test 2: Unreachable node
    result = solution.networkDelayTime([[1,2,1]], 2, 2)
    assert result == -1, f"Test 2 Failed: Expected -1, got {result}"
    print("Test 2 Passed")

    # Test 3: Single node
    result = solution.networkDelayTime([], 1, 1)
    assert result == 0, f"Test 3 Failed: Expected 0, got {result}"
    print("Test 3 Passed")

    # Test 4: Two paths, pick shorter
    result = solution.networkDelayTime([[1,2,1],[1,3,4],[2,3,2]], 3, 1)
    assert result == 3, f"Test 4 Failed: Expected 3, got {result}"
    print("Test 4 Passed")

    # Test 5: All nodes directly connected
    result = solution.networkDelayTime([[1,2,5],[1,3,2],[1,4,9]], 4, 1)
    assert result == 9, f"Test 5 Failed: Expected 9, got {result}"
    print("Test 5 Passed")

    # Test 6: Longer chain
    result = solution.networkDelayTime([[1,2,1],[2,3,2],[3,4,3],[4,5,4]], 5, 1)
    assert result == 10, f"Test 6 Failed: Expected 10, got {result}"
    print("Test 6 Passed")

    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
