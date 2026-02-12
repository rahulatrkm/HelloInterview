"""
Course Schedule II

You have to take a total of numCourses courses, which are labeled from 0 to 
numCourses - 1. You are given a list of prerequisites pairs, where 
prerequisites[i] = [a, b] indicates that you must complete course b before course a.

Given the total number of courses and a list of prerequisite pairs, write a 
function to return the ordering of courses you should take to finish all courses.

If there are multiple valid orderings, return any valid ordering. If it is 
impossible to finish all courses, return an empty array.

Example 1:
    Input: numCourses = 4, prerequisites = [[1,0], [2,0], [3,1], [3,2]]
    Output: [0, 1, 2, 3] or [0, 2, 1, 3]

Example 2:
    Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
    Output: []
    Explanation: Impossible due to circular dependency.

Approach:
- Same as Course Schedule but return the ordering instead of just True/False
- Build adjacency list and compute in-degrees using Kahn's algorithm
- Enqueue all nodes with in-degree 0, process and build result order
- Return order if len(order) == numCourses, else return []

Time Complexity: O(V + E) where V is courses and E is prerequisites
Space Complexity: O(V + E) for graph, in-degree array, and result
"""

from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Your code goes here
        ind = [0]*numCourses
        adj = defaultdict(list)
        for a, b in prerequisites:
            ind[a] += 1
            adj[b].append(a)
        
        ans = []
        q = deque()
        for i in range(numCourses):
            if ind[i] == 0:
                q.append(i)
        
        while q:
            subj = q.popleft()
            ans.append(subj)
            for a in adj[subj]:
                ind[a] -= 1
                if ind[a] == 0:
                    q.append(a)
        return ans if len(ans) == numCourses else []



def is_valid_order(order, numCourses, prerequisites):
    """Helper to validate any valid topological ordering."""
    if len(order) != numCourses:
        return False
    position = {course: i for i, course in enumerate(order)}
    for dest, src in prerequisites:
        if position[src] > position[dest]:
            return False
    return True


def run_tests():
    solution = Solution()
    
    # Test 1: Diamond dependency
    result = solution.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert is_valid_order(result, 4, [[1, 0], [2, 0], [3, 1], [3, 2]]), \
        f"Test 1 Failed: {result} is not a valid ordering"
    print("Test 1 Passed")
    
    # Test 2: Cycle - impossible
    result = solution.findOrder(2, [[1, 0], [0, 1]])
    assert result == [], f"Test 2 Failed: Expected [], got {result}"
    print("Test 2 Passed")
    
    # Test 3: No prerequisites
    result = solution.findOrder(3, [])
    assert is_valid_order(result, 3, []), \
        f"Test 3 Failed: {result} is not a valid ordering"
    print("Test 3 Passed")
    
    # Test 4: Linear chain
    result = solution.findOrder(3, [[1, 0], [2, 1]])
    assert result == [0, 1, 2], f"Test 4 Failed: Expected [0, 1, 2], got {result}"
    print("Test 4 Passed")
    
    # Test 5: Single course
    result = solution.findOrder(1, [])
    assert result == [0], f"Test 5 Failed: Expected [0], got {result}"
    print("Test 5 Passed")
    
    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
