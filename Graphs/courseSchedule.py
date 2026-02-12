"""
Course Schedule

You have to take a total of numCourses courses, which are labeled from 0 to 
numCourses - 1. You are given a list of prerequisites pairs, where 
prerequisites[i] = [a, b] indicates that you must complete course b before course a.

Given the total number of courses and a list of prerequisite pairs, write a 
function to determine if it is possible to finish all courses.

Example 1:
    Input: numCourses = 3, prerequisites = [[1, 0], [2, 1]]
    Output: True
    Explanation: You can take courses in the following order: 0, 1, 2.

Example 2:
    Input: numCourses = 3, prerequisites = [[1, 0], [0, 1], [1, 2]]
    Output: False
    Explanation: It is impossible to finish all courses, as you must finish course 1
                 before course 0 and course 0 before course 1.

Approach:
- Model as a directed graph, detect if a cycle exists using topological sort (Kahn's)
- Build adjacency list and compute in-degree for each node
- Enqueue all nodes with in-degree 0
- Process queue: dequeue node, decrement neighbors' in-degrees, enqueue if in-degree becomes 0
- If total processed nodes == numCourses, no cycle exists → return True

Time Complexity: O(V + E) where V is courses and E is prerequisites
Space Complexity: O(V + E) for graph and in-degree array
"""

from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Your code goes here
        ind = [0]*numCourses
        adj = defaultdict(list)
        for a, b in prerequisites:
            ind[a] += 1
            adj[b].append(a)
        
        cnt = numCourses
        q = deque()
        for i in range(numCourses):
            if ind[i] == 0:
                q.append(i)
                cnt -= 1
        
        while q:
            subj = q.popleft()
            for a in adj[subj]:
                ind[a] -= 1
                if ind[a] == 0:
                    q.append(a)
                    cnt -= 1
        return cnt == 0


def run_tests():
    solution = Solution()
    
    # Test 1: Linear dependencies
    result = solution.canFinish(3, [[1, 0], [2, 1]])
    assert result == True, f"Test 1 Failed: Expected True, got {result}"
    print("Test 1 Passed")
    
    # Test 2: Cycle exists
    result = solution.canFinish(3, [[1, 0], [0, 1], [1, 2]])
    assert result == False, f"Test 2 Failed: Expected False, got {result}"
    print("Test 2 Passed")
    
    # Test 3: No prerequisites
    result = solution.canFinish(4, [])
    assert result == True, f"Test 3 Failed: Expected True, got {result}"
    print("Test 3 Passed")
    
    # Test 4: Single course
    result = solution.canFinish(1, [])
    assert result == True, f"Test 4 Failed: Expected True, got {result}"
    print("Test 4 Passed")
    
    # Test 5: Diamond dependency (no cycle)
    result = solution.canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert result == True, f"Test 5 Failed: Expected True, got {result}"
    print("Test 5 Passed")
    
    # Test 6: Longer cycle
    result = solution.canFinish(5, [[1, 0], [2, 1], [3, 2], [4, 3], [1, 4]])
    assert result == False, f"Test 6 Failed: Expected False, got {result}"
    print("Test 6 Passed")
    
    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
