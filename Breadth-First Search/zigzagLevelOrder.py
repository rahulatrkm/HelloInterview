"""
Zigzag Level Order

DESCRIPTION (inspired by Leetcode.com):
Given the root of a binary tree, return the zigzag level-order traversal of its
nodes' values.

The output should be a list of lists containing the values of the nodes at each
level. The first list should contain the value of the root, the second list
should contain the values of the nodes at the second level from right to left,
the third list should contain the values of the third level from left to right,
and so on.

Example 1:
Input: [1,3,4,null,2,7,null,8]
Output: [[1], [4,3], [2,7], [8]]

Example 2:
Input: [4,2,7,1,3,6,9,null,5,null,2]
Output: [[4], [7,2], [1,3,6,9], [2,5]]

Approach:
- Use BFS and process level by level
- Maintain a boolean flag for direction
- Append nodes in normal order or reversed order depending on the level

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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        q = deque()
        if root:
            q.append(root)
        ans = []
        isl2r = True
        while q:
            n = len(q)
            level = []
            for _ in range(n):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if isl2r:
                ans.append(level)
            else:
                ans.append(level[::-1])
            isl2r = not isl2r
        return ans

if __name__ == "__main__":
    sol = Solution()

    # Test 1
    tree = build_tree([1,3,4,None,2,7,None,8])
    result = sol.zigzagLevelOrder(tree)
    expected = [[1],[4,3],[2,7],[8]]
    assert result == expected, f"Test 1 failed: expected {expected}, got {result}"
    print("✓ Test 1 passed")

    # Test 2
    tree = build_tree([4,2,7,1,3,6,9,None,5,None,2])
    result = sol.zigzagLevelOrder(tree)
    expected = [[4],[7,2],[1,3,6,9],[2,5]]
    assert result == expected, f"Test 2 failed: expected {expected}, got {result}"
    print("✓ Test 2 passed")

    # Test 3 - Single node
    tree = build_tree([1])
    result = sol.zigzagLevelOrder(tree)
    expected = [[1]]
    assert result == expected, f"Test 3 failed: expected {expected}, got {result}"
    print("✓ Test 3 passed")

    # Test 4 - Empty tree
    tree = build_tree([])
    result = sol.zigzagLevelOrder(tree)
    expected = []
    assert result == expected, f"Test 4 failed: expected {expected}, got {result}"
    print("✓ Test 4 passed")

    print("\n✓ All tests passed!")
