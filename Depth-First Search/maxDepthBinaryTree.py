"""
Maximum Depth of Binary Tree
https://www.hellointerview.com/learn/code/depth-first-search/maximum-depth-of-binary-tree

Given the root of a binary tree, write a recursive function to find its maximum
depth, where maximum depth is defined as the number of nodes along the longest
path from the root node down to a leaf node.

Example 1:
  Input: [4, 2, 7, 1, null, 6, 9, null, 8]
         4
        / \
       2   7
      /   / \
     1   6   9
      \
       8
  Output: 4 (path: 4 -> 2 -> 1 -> 8)

Approach:
- Return values: max depth of left subtree, max depth of right subtree
- Each node returns: 1 + max(left_depth, right_depth)
- Base case: empty tree has depth 0

Time: O(n)
Space: O(n) for call stack
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(arr):
    """Build tree from level-order array (None for null nodes)"""
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        node = queue.pop(0)
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Basic case
    root = build_tree([4,2,7,1,None,6,9,None,8])
    assert sol.maxDepth(root) == 4, f"Test 1 failed: got {sol.maxDepth(root)}"
    print("Test 1 passed ✓")

    # Test 2: Single node
    root = build_tree([1])
    assert sol.maxDepth(root) == 1, f"Test 2 failed: got {sol.maxDepth(root)}"
    print("Test 2 passed ✓")

    # Test 3: Empty tree
    root = build_tree([])
    assert sol.maxDepth(root) == 0, f"Test 3 failed: got {sol.maxDepth(root)}"
    print("Test 3 passed ✓")

    # Test 4: Left-skewed tree
    root = build_tree([1,2,None,3,None,4])
    assert sol.maxDepth(root) == 4, f"Test 4 failed: got {sol.maxDepth(root)}"
    print("Test 4 passed ✓")

    # Test 5: Right-skewed tree
    root = build_tree([1,None,2,None,3,None,4])
    assert sol.maxDepth(root) == 4, f"Test 5 failed: got {sol.maxDepth(root)}"
    print("Test 5 passed ✓")

    # Test 6: Balanced tree
    root = build_tree([1,2,3,4,5,6,7])
    assert sol.maxDepth(root) == 3, f"Test 6 failed: got {sol.maxDepth(root)}"
    print("Test 6 passed ✓")

    # Test 7: Two nodes
    root = build_tree([1,2])
    assert sol.maxDepth(root) == 2, f"Test 7 failed: got {sol.maxDepth(root)}"
    print("Test 7 passed ✓")

    print("\nAll tests passed! ✓")
