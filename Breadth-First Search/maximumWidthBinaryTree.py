"""
Maximum Width of Binary Tree

DESCRIPTION (inspired by Leetcode.com):
Given the root of a binary tree, write a function to find its maximum width.
Each level of the binary tree has a width, which is the number of nodes between
 the leftmost and rightmost nodes at that level, including the null nodes between
them. Return the maximum width of the binary tree.

Example 1:
Input: [4,2,7,1,None,None,9]
Output: 4

Example 2:
Input: [4,2,7,1]
Output: 2

Example 3:
Input: [4,2,7,1,None,6,9,7,None,None,1,1,None]
Output: 7

Approach:
- Use BFS and track each node's position index
- For each level, width = rightmost_index - leftmost_index + 1
- Normalize positions per level to avoid overflow

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
    def maximumWidth(self, root: TreeNode) -> int:
        q = deque()
        if root:
            q.append((root, 0))
        ans = 0
        while q:
            ans = max(ans, q[-1][1]-q[0][1]+1)
            n = len(q)
            for _ in range(n):
                node, idx = q.popleft()
                if node.left:
                    q.append((node.left, 2*idx))
                if node.right:
                    q.append((node.right, 2*idx+1))
        return ans

if __name__ == "__main__":
    sol = Solution()

    # Test 1
    tree = build_tree([4,2,7,1,None,None,9])
    result = sol.maximumWidth(tree)
    assert result == 4, f"Test 1 failed: expected 4, got {result}"
    print("✓ Test 1 passed")

    # Test 2
    tree = build_tree([4,2,7,1])
    result = sol.maximumWidth(tree)
    assert result == 2, f"Test 2 failed: expected 2, got {result}"
    print("✓ Test 2 passed")

    # Test 3
    tree = build_tree([4,2,7,1,None,6,9,7,None,None,1,1,None])
    result = sol.maximumWidth(tree)
    assert result == 7, f"Test 3 failed: expected 7, got {result}"
    print("✓ Test 3 passed")

    # Test 4 - Single node
    tree = build_tree([1])
    result = sol.maximumWidth(tree)
    assert result == 1, f"Test 4 failed: expected 1, got {result}"
    print("✓ Test 4 passed")

    # Test 5 - Empty tree
    tree = build_tree([])
    result = sol.maximumWidth(tree)
    assert result == 0, f"Test 5 failed: expected 0, got {result}"
    print("✓ Test 5 passed")

    print("\n✓ All tests passed!")
