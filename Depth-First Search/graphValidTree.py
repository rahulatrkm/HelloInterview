"""
Graph Valid Tree

DESCRIPTION (inspired by Lintcode.com):
You are given an integer n and a list of undirected edges where each entry in 
the list is a pair of integers representing an edge between nodes. You have to 
write a function to check whether these edges make up a valid tree.

There will be no duplicate edges in the edges list. (i.e. [0, 1] and [1, 0] 
will not appear together in the list).

A valid tree must satisfy two conditions:
1. Contains no cycles
2. Has exactly one connected component (all nodes are reachable)

Example 1:
Input: n = 4, edges = [[0, 1], [2, 3]]
Output: False

Explanation: The graph is not connected (has 2 components).

Example 2:
Input: n = 5, edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
Output: True

Explanation: All nodes are connected with no cycles.

Approach:
- A tree must have exactly n-1 edges (necessary condition)
- Build adjacency list from edges
- Use DFS to detect cycles: if we visit a node that's already visited and it's 
  not the parent, we found a cycle
- Check if all nodes are visited (connected component)
- Return true only if no cycle found and all nodes visited

Time Complexity: O(N + E) where N is nodes and E is edges
Space Complexity: O(N + E) for adjacency list and visited set
"""

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # par = list(range(n))
        # def find(node):
        #     if node == par[node]:
        #         return node
        #     par[node] = find(par[node])
        #     return par[node]
        
        # for u, v in edges:
        #     pu, pv = find(u), find(v)
        #     if pu == pv:
        #         return False
        #     par[pu] = pv
        
        # s = set()
        # for i in range(n):
        #     s.add(find(i))
        # return len(s) == 1

        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = set()
        def dfs(node, parent):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                if not dfs(neighbor, node):
                    return False
            return True

        if not dfs(0, -1):
            return False
        return len(visited) == n

if __name__ == "__main__":
    sol = Solution()
    
    # Test 1 - Disconnected
    n, edges = 4, [[0, 1], [2, 3]]
    result = sol.validTree(n, edges)
    assert result == False, f"Test 1 failed: expected False, got {result}"
    print("✓ Test 1 passed")
    
    # Test 2 - Valid tree
    n, edges = 5, [[0, 1], [1, 2], [2, 3], [3, 4]]
    result = sol.validTree(n, edges)
    assert result == True, f"Test 2 failed: expected True, got {result}"
    print("✓ Test 2 passed")
    
    # Test 3 - Cycle
    n, edges = 5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    result = sol.validTree(n, edges)
    assert result == False, f"Test 3 failed: expected False, got {result}"
    print("✓ Test 3 passed")
    
    # Test 4 - Single node
    n, edges = 1, []
    result = sol.validTree(n, edges)
    assert result == True, f"Test 4 failed: expected True, got {result}"
    print("✓ Test 4 passed")
    
    # Test 5 - Two nodes
    n, edges = 2, [[0, 1]]
    result = sol.validTree(n, edges)
    assert result == True, f"Test 5 failed: expected True, got {result}"
    print("✓ Test 5 passed")
    
    # Test 6 - Two nodes no edge
    n, edges = 2, []
    result = sol.validTree(n, edges)
    assert result == False, f"Test 6 failed: expected False, got {result}"
    print("✓ Test 6 passed")
    
    # Test 7 - Self loop
    n, edges = 1, [[0, 0]]
    result = sol.validTree(n, edges)
    assert result == False, f"Test 7 failed: expected False, got {result}"
    print("✓ Test 7 passed")
    
    # Test 8 - Too many edges
    n, edges = 4, [[0, 1], [1, 2], [2, 3], [0, 3]]
    result = sol.validTree(n, edges)
    assert result == False, f"Test 8 failed: expected False, got {result}"
    print("✓ Test 8 passed")
    
    print("\n✓ All tests passed!")
