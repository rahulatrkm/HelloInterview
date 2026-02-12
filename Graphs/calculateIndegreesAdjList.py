"""
Calculate Indegrees (Adjacency List)

You are given a graph with n nodes, where each node has an integer value from 0 
to n - 1. The graph is represented by an adjacency list, where each node i is 
mapped to a list of nodes that have a directed edge from node i to them.

Write a function to calculate the indegree of each node in the graph.

Example:
    Input: adj_list = {0: [1], 1: [2, 3], 2: [], 3: [2, 4], 4: []}, n = 5
    Output: [0, 1, 2, 1, 1]

Approach:
- Initialize an array of size n with all zeros
- Iterate through each node u in the adjacency list
- For each neighbor v of u, increment indegree[v] by 1
- Return the indegree array

Time Complexity: O(V + E) where V is nodes and E is edges
Space Complexity: O(V) for the indegree array
"""

from typing import Dict, List

class Solution:
    def indegree(self, adj_list: Dict[int, List[int]], n: int) -> List[int]:
        # Your code goes here
        ind = [0] * n
        for u in adj_list:
            for v in adj_list[u]:
                ind[v] += 1
        return ind


def run_tests():
    solution = Solution()
    
    # Test 1: Example from problem
    adj_list = {0: [1], 1: [2, 3], 2: [], 3: [2, 4], 4: []}
    result = solution.indegree(adj_list, 5)
    expected = [0, 1, 2, 1, 1]
    assert result == expected, f"Test 1 Failed: Expected {expected}, got {result}"
    print("Test 1 Passed")
    
    # Test 2: No edges
    adj_list = {0: [], 1: [], 2: []}
    result = solution.indegree(adj_list, 3)
    expected = [0, 0, 0]
    assert result == expected, f"Test 2 Failed: Expected {expected}, got {result}"
    print("Test 2 Passed")
    
    # Test 3: All edges point to one node
    adj_list = {0: [3], 1: [3], 2: [3], 3: []}
    result = solution.indegree(adj_list, 4)
    expected = [0, 0, 0, 3]
    assert result == expected, f"Test 3 Failed: Expected {expected}, got {result}"
    print("Test 3 Passed")
    
    # Test 4: Linear chain
    adj_list = {0: [1], 1: [2], 2: [3], 3: []}
    result = solution.indegree(adj_list, 4)
    expected = [0, 1, 1, 1]
    assert result == expected, f"Test 4 Failed: Expected {expected}, got {result}"
    print("Test 4 Passed")
    
    # Test 5: Single node
    adj_list = {0: []}
    result = solution.indegree(adj_list, 1)
    expected = [0]
    assert result == expected, f"Test 5 Failed: Expected {expected}, got {result}"
    print("Test 5 Passed")
    
    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
