"""
Rightmost Node

DESCRIPTION (inspired by Leetcode.com):
Given the root of a binary tree, return the rightmost node at each level of the
The output should be a list containing only the values of those nodes.

Example 1:
Input: [1,3,4,null,2,7,null,8]
Output: [1,4,7,8]

Example 2:
Input: [1,2,5,3,null,null,4]
Output: [1,5,3,4]

Approach:
- Use BFS and process level by level
- The last node processed at each level is the rightmost node

Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import deque
from typing import List

class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

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

class Solution:
    def rightmostNode(self, root: TreeNode) -> List[int]:
        q = deque()
        if root:
            q.append(root)
        ans = []
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i == n - 1:
                    ans.append(node.val)
        return ans

if __name__ == "__main__":
    sol = Solution()

    # Test 1
    tree = build_tree([1,3,4,None,2,7,None,8])
    result = sol.rightmostNode(tree)
    expected = [1,4,7,8]
    assert result == expected, f"Test 1 failed: expected {expected}, got {result}"
    print("✓ Test 1 passed")

    # Test 2
    tree = build_tree([1,2,5,3,None,None,4])
    result = sol.rightmostNode(tree)
    expected = [1,5,4]
    assert result == expected, f"Test 2 failed: expected {expected}, got {result}"
    print("✓ Test 2 passed")

    # Test 3 - Single node
    tree = build_tree([1])
    result = sol.rightmostNode(tree)
    expected = [1]
    assert result == expected, f"Test 3 failed: expected {expected}, got {result}"
    print("✓ Test 3 passed")

    # Test 4 - Empty tree
    tree = build_tree([])
    result = sol.rightmostNode(tree)
    expected = []
    assert result == expected, f"Test 4 failed: expected {expected}, got {result}"
    print("✓ Test 4 passed")

    print("\n✓ All tests passed!")
