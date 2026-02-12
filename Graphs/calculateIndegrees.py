"""
Calculate Indegrees

You are given a graph with n nodes, where each node has an integer value from 0 
to n - 1. The graph is represented by a list of edges, where edges[i] = [u, v] 
is a directed edge from node u to node v.

Write a function to calculate the indegree of each node in the graph.

Example:
    Input: edges = [(0, 1), (1, 2), (1, 3), (3, 2), (3, 4)], n = 5
    Output: [0, 1, 2, 1, 1]

Approach:
- Initialize an array of size n with all zeros
- Iterate through each edge (u, v) and increment indegree[v] by 1
- Return the indegree array

Time Complexity: O(E) where E is the number of edges
Space Complexity: O(V) where V is the number of nodes
"""

from typing import List, Tuple

class Solution:
    def indegree(self, n: int, edges: List[Tuple[int, int]]) -> List[int]:
        # Your code goes here
        ind = [0] * n
        for u, v in edges:
            ind[v] += 1
        return ind


def run_tests():
    solution = Solution()
    
    # Test 1: Example from problem
    result = solution.indegree(5, [(0, 1), (1, 2), (1, 3), (3, 2), (3, 4)])
    expected = [0, 1, 2, 1, 1]
    assert result == expected, f"Test 1 Failed: Expected {expected}, got {result}"
    print("Test 1 Passed")
    
    # Test 2: No edges
    result = solution.indegree(3, [])
    expected = [0, 0, 0]
    assert result == expected, f"Test 2 Failed: Expected {expected}, got {result}"
    print("Test 2 Passed")
    
    # Test 3: All edges point to one node
    result = solution.indegree(4, [(0, 3), (1, 3), (2, 3)])
    expected = [0, 0, 0, 3]
    assert result == expected, f"Test 3 Failed: Expected {expected}, got {result}"
    print("Test 3 Passed")
    
    # Test 4: Linear chain
    result = solution.indegree(4, [(0, 1), (1, 2), (2, 3)])
    expected = [0, 1, 1, 1]
    assert result == expected, f"Test 4 Failed: Expected {expected}, got {result}"
    print("Test 4 Passed")
    
    # Test 5: Single node
    result = solution.indegree(1, [])
    expected = [0]
    assert result == expected, f"Test 5 Failed: Expected {expected}, got {result}"
    print("Test 5 Passed")
    
    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
