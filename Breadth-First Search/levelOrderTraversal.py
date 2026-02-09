"""
Level Order Traversal

DESCRIPTION (inspired by Leetcode.com):
Given a binary tree, return the level-order traversal of its nodes' values.
(i.e., from left to right, level by level).

Example:
Input: [4,2,7,1,3,6,9]
Output: [[4], [2,7], [1,3,6,9]]

Approach:
- Use BFS with a queue
- Process nodes level by level using the queue size
- Collect values for each level in a list

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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            res.append([node.val for node in q])
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res

if __name__ == "__main__":
    sol = Solution()

    # Test 1
    tree = build_tree([4,2,7,1,3,6,9])
    result = sol.levelOrder(tree)
    expected = [[4],[2,7],[1,3,6,9]]
    assert result == expected, f"Test 1 failed: expected {expected}, got {result}"
    print("✓ Test 1 passed")

    # Test 2 - Single node
    tree = build_tree([1])
    result = sol.levelOrder(tree)
    expected = [[1]]
    assert result == expected, f"Test 2 failed: expected {expected}, got {result}"
    print("✓ Test 2 passed")

    # Test 3 - Empty tree
    tree = build_tree([])
    result = sol.levelOrder(tree)
    expected = []
    assert result == expected, f"Test 3 failed: expected {expected}, got {result}"
    print("✓ Test 3 passed")

    # Test 4 - Skewed
    tree = build_tree([1,2,None,3,None,4])
    result = sol.levelOrder(tree)
    expected = [[1],[2],[3],[4]]
    assert result == expected, f"Test 4 failed: expected {expected}, got {result}"
    print("✓ Test 4 passed")

    print("\n✓ All tests passed!")
