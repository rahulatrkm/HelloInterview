"""
Copy Graph

DESCRIPTION:
Given a reference to a variable node which is part of an undirected, connected 
graph, write a function to return a copy of the graph as an adjacency list in 
dictionary form. The keys of the adjacency list are the values of the nodes, 
and the values are the neighbors of the nodes.

node is an instance of the following class:
class IntGraphNode:
    def __init__(self, value = 0, neighbors = None):
        self.value = value
        self.neighbors = neighbors if neighbors is not None else []

Example 1:
Input: node = IntGraphNode(1, [IntGraphNode(2), IntGraphNode(3)])
Output: {1: [2, 3], 2: [1], 3: [1]}

Example 2:
Input:
    n1 = IntGraphNode(1)
    n2 = IntGraphNode(2)
    n3 = IntGraphNode(3)
    n4 = IntGraphNode(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]
Output: {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}

Approach:
- Use DFS to traverse the graph starting from the input node
- For each node, create an entry in adjacency list: key=node.value, value=[neighbor values]
- Check if node already visited to avoid infinite loops
- Recursively call DFS on all neighbors
- Return the adjacency list dictionary

Time Complexity: O(N + M) where N is nodes and M is edges
Space Complexity: O(N + M) for the adjacency list and recursion stack
"""

from typing import Dict, List

class IntGraphNode:
    def __init__(self, value: int = 0, neighbors: 'List[IntGraphNode]' = None):
        self.value = value
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def copyGraph(self, node: IntGraphNode) -> Dict[int, List[int]]:
        adjacency_list = {}
        visited = set()
        
        def dfs(current):
            if current.value in visited:
                return
            visited.add(current.value)
            adjacency_list[current.value] = [neighbor.value for neighbor in current.neighbors]
            for neighbor in current.neighbors:
                dfs(neighbor)
        
        dfs(node)
        return adjacency_list

if __name__ == "__main__":
    sol = Solution()
    
    # Test 1
    n1 = IntGraphNode(1)
    n2 = IntGraphNode(2)
    n3 = IntGraphNode(3)
    n1.neighbors = [n2, n3]
    n2.neighbors = [n1]
    n3.neighbors = [n1]
    
    result = sol.copyGraph(n1)
    assert result == {1: [2, 3], 2: [1], 3: [1]}, f"Test 1 failed: got {result}"
    print("✓ Test 1 passed")
    
    # Test 2
    n1 = IntGraphNode(1)
    n2 = IntGraphNode(2)
    n3 = IntGraphNode(3)
    n4 = IntGraphNode(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]
    
    result = sol.copyGraph(n1)
    assert result == {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}, f"Test 2 failed: got {result}"
    print("✓ Test 2 passed")
    
    # Test 3 - Single node
    n1 = IntGraphNode(1)
    result = sol.copyGraph(n1)
    assert result == {1: []}, f"Test 3 failed: got {result}"
    print("✓ Test 3 passed")
    
    # Test 4 - Two nodes
    n1 = IntGraphNode(1)
    n2 = IntGraphNode(2)
    n1.neighbors = [n2]
    n2.neighbors = [n1]
    
    result = sol.copyGraph(n1)
    assert result == {1: [2], 2: [1]}, f"Test 4 failed: got {result}"
    print("✓ Test 4 passed")
    
    # Test 5 - Self loop
    n1 = IntGraphNode(1)
    n1.neighbors = [n1]
    result = sol.copyGraph(n1)
    assert result == {1: [1]}, f"Test 5 failed: got {result}"
    print("✓ Test 5 passed")
    
    # Test 6 - Star graph
    n1 = IntGraphNode(1)
    n2 = IntGraphNode(2)
    n3 = IntGraphNode(3)
    n4 = IntGraphNode(4)
    n1.neighbors = [n2, n3, n4]
    n2.neighbors = [n1]
    n3.neighbors = [n1]
    n4.neighbors = [n1]
    
    result = sol.copyGraph(n1)
    assert result == {1: [2, 3, 4], 2: [1], 3: [1], 4: [1]}, f"Test 6 failed: got {result}"
    print("✓ Test 6 passed")
    
    # Test 7 - Triangle
    n1 = IntGraphNode(1)
    n2 = IntGraphNode(2)
    n3 = IntGraphNode(3)
    n1.neighbors = [n2, n3]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n1, n2]
    
    result = sol.copyGraph(n1)
    assert result == {1: [2, 3], 2: [1, 3], 3: [1, 2]}, f"Test 7 failed: got {result}"
    print("✓ Test 7 passed")
    
    print("\n✓ All tests passed!")
