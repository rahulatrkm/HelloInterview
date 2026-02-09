"""
Bus Routes

You are given a 2D-integer array routes representing bus routes where routes[i] 
is a list of stops that the i-th bus makes. For example, if routes[0] = [3, 8, 9], 
it means the first bus goes through stops 3, 8, 9, 3, 8, 9, continuously.

You are also given two integers source and target, representing the starting bus 
stop and the destination bus stop, respectively.

Write a function that takes in routes, source, and target as input, and returns 
the minimum number of buses you need to take to travel from source to target. 
Return -1 if it is not possible to reach the destination.

Example 1:
    Input: routes = [[3, 8, 9], [5, 6, 8], [1, 7, 10]], source = 3, target = 6
    Output: 2
    Explanation: You can take the first bus from stop 3 to stop 8, and then take 
                 the second bus from stop 8 to stop 6.

Example 2:
    Input: routes = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], source = 1, target = 12
    Output: -1
    Explanation: It is not possible to reach the destination

Approach:
- Model as graph where nodes are bus routes, not individual stops
- Build adjacency list: map each stop to all routes that visit it
- Use BFS starting from all routes containing source
- For each route, check if it contains target; otherwise add neighboring routes
- Track visited routes to avoid cycles

Time Complexity: O(S + R²) where S is total stops and R is number of routes
Space Complexity: O(S + R) for adjacency list, queue, and visited set
"""

from collections import deque, defaultdict

class Solution:
    def bus_routes(self, routes: list[list[int]], source: int, target: int) -> int:
        # Your code goes here
        if source == target:
            return 0
        n = len(routes)
        stop2routes = defaultdict(list)
        for i, route in enumerate(routes):
            routes[i] = set(route)
            for stop in route:
                stop2routes[stop].append(i)
        q = deque()
        q.append((source, 0))
        vis = {}
        while q:
            stop, d = q.popleft()
            if d > n:
                continue
            for i in stop2routes[stop]:
                if target in routes[i]:
                    return d+1
                if i not in vis:
                    vis[i] = d
                else:
                    continue
                for nex_stop in routes[i]:
                    q.append((nex_stop, d+1))
        return -1


def run_tests():
    solution = Solution()
    
    # Test 1: Two buses needed
    routes = [[3, 8, 9], [5, 6, 8], [1, 7, 10]]
    result = solution.bus_routes(routes, 3, 6)
    expected = 2
    assert result == expected, f"Test 1 Failed: Expected {expected}, got {result}"
    print("Test 1 Passed")
    
    # Test 2: Impossible route
    routes = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    result = solution.bus_routes(routes, 1, 12)
    expected = -1
    assert result == expected, f"Test 2 Failed: Expected {expected}, got {result}"
    print("Test 2 Passed")
    
    # Test 3: Source equals target
    routes = [[1, 2, 3], [4, 5, 6]]
    result = solution.bus_routes(routes, 2, 2)
    expected = 0
    assert result == expected, f"Test 3 Failed: Expected {expected}, got {result}"
    print("Test 3 Passed")
    
    # Test 4: Direct route
    routes = [[1, 2, 3, 4, 5]]
    result = solution.bus_routes(routes, 1, 5)
    expected = 1
    assert result == expected, f"Test 4 Failed: Expected {expected}, got {result}"
    print("Test 4 Passed")
    
    # Test 5: Three buses needed
    routes = [[1, 2], [2, 3], [3, 4], [4, 5]]
    result = solution.bus_routes(routes, 1, 4)
    expected = 3
    assert result == expected, f"Test 5 Failed: Expected {expected}, got {result}"
    print("Test 5 Passed")
    
    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
