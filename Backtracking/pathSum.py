"""
Path Sum (Backtracking)

Given a binary tree where all nodes have positive, integer values and a target
sum, find all root-to-leaf paths where the sum of the values along the path
equals the given sum.

Example:
    Input: root = [4,7,1,3,2,6,1], target = 7
    Output: [[4, 2, 1]]

Approach:
- Use DFS backtracking to explore all root-to-leaf paths
- Maintain a running path list and running total
- At each node, add its value to path and total
- Prune: if total > target, pop and return (since all values are positive)
- At leaf nodes: if total == target, add copy of path to results
- Backtrack by popping current node from path before returning

Time Complexity: O(n²) - visit each node once, copy path at leaves (up to O(n))
Space Complexity: O(n²) - result can contain O(n) paths of O(n) length each
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        # Your code goes here
        ans = []
        curr = []
        def helper(node, target):
            if target < 0:
                return None
            
            if node:
                curr.append(node.val)
                if node.val == target and not node.left and not node.right:
                    ans.append(curr.copy())
                if node.left:
                    helper(node.left, target-node.val)
                if node.right:
                    helper(node.right, target-node.val)
                curr.pop()
        helper(root, target)
        return ans



def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def run_tests():
    solution = Solution()
    
    # Test 1: target = 7
    #       4
    #      / \
    #     2   1
    #    / \
    #   1   3
    root = build_tree([4, 2, 1, 1, 3])
    result = solution.pathSum(root, 7)
    expected = [[4, 2, 1]]
    assert sorted([sorted(p) for p in result]) == sorted([sorted(p) for p in expected]), \
        f"Test 1 Failed: Expected {expected}, got {result}"
    print("Test 1 Passed")
    
    # Test 2: Multiple valid paths
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    #  / \     / \
    # 7   2   5   1
    root = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    result = solution.pathSum(root, 22)
    expected = [[5, 4, 11, 2], [5, 8, 4, 5]]
    assert sorted([sorted(p) for p in result]) == sorted([sorted(p) for p in expected]), \
        f"Test 2 Failed: Expected {expected}, got {result}"
    print("Test 2 Passed")
    
    # Test 3: No valid paths
    root = build_tree([1, 2, 3])
    result = solution.pathSum(root, 10)
    expected = []
    assert result == expected, f"Test 3 Failed: Expected {expected}, got {result}"
    print("Test 3 Passed")
    
    # Test 4: Single node matches target
    root = build_tree([5])
    result = solution.pathSum(root, 5)
    expected = [[5]]
    assert result == expected, f"Test 4 Failed: Expected {expected}, got {result}"
    print("Test 4 Passed")
    
    # Test 5: Empty tree
    result = solution.pathSum(None, 0)
    expected = []
    assert result == expected, f"Test 5 Failed: Expected {expected}, got {result}"
    print("Test 5 Passed")
    
    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
