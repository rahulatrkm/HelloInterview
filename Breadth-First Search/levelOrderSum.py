"""
Level Order Sum

DESCRIPTION:
Given the root of a binary tree, return the sum of the nodes at each level.
The output should be a list containing the sum of the nodes at each level.

Example 1:
Input: [1,3,4,null,2,7,null,8]
Output: [1, 7, 9, 8]

Example 2:
Input: [1,2,5,3,null,null,4]
Output: [1, 7, 3, 4]

Approach:
- Use BFS with a queue
- Process nodes level by level and compute sum per level

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
    def levelOrderSum(self, root: TreeNode) -> List[int]:
        q = deque()
        if root:
            q.append(root)
        
        res = []
        while q:
            n = len(q)
            s = 0
            for _ in range(n):
                node = q.popleft()
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(s)
        return res


if __name__ == "__main__":
    sol = Solution()

    # Test 1
    tree = build_tree([1,3,4,None,2,7,None,8])
    result = sol.levelOrderSum(tree)
    expected = [1,7,9,8]
    assert result == expected, f"Test 1 failed: expected {expected}, got {result}"
    print("✓ Test 1 passed")

    # Test 2
    tree = build_tree([1,2,5,3,None,None,4])
    result = sol.levelOrderSum(tree)
    expected = [1,7,7]
    assert result == expected, f"Test 2 failed: expected {expected}, got {result}"
    print("✓ Test 2 passed")

    # Test 3 - Single node
    tree = build_tree([5])
    result = sol.levelOrderSum(tree)
    expected = [5]
    assert result == expected, f"Test 3 failed: expected {expected}, got {result}"
    print("✓ Test 3 passed")

    # Test 4 - Empty tree
    tree = build_tree([])
    result = sol.levelOrderSum(tree)
    expected = []
    assert result == expected, f"Test 4 failed: expected {expected}, got {result}"
    print("✓ Test 4 passed")

    print("\n✓ All tests passed!")
