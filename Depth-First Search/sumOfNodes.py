"""
Sum of Nodes
https://www.hellointerview.com/learn/code/depth-first-search/return-values

Given a binary tree, use Depth-First Search to find the sum of all nodes in the tree.

Example:
  Input: [4, 2, 7, 1, 3, 6, 9]
         4
        / \
       2   7
      / \ / \
     1  3 6  9
  Output: 32 (4+2+7+1+3+6+9 = 32)

Approach:
- Return value: sum of all nodes in the subtree
- sum(node) = sum(node.left) + sum(node.right) + node.val
- Base case: empty tree → 0; leaf node → node.val
- Recursive formula: left_sum + right_sum + node.val

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
    def sumOfNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_sum = self.sumOfNodes(root.left)
        right_sum = self.sumOfNodes(root.right)
        return left_sum + right_sum + root.val


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Basic case
    root = build_tree([4,2,7,1,3,6,9])
    assert sol.sumOfNodes(root) == 32, f"Test 1 failed: got {sol.sumOfNodes(root)}"
    print("Test 1 passed ✓")

    # Test 2: Single node
    root = build_tree([5])
    assert sol.sumOfNodes(root) == 5, f"Test 2 failed: got {sol.sumOfNodes(root)}"
    print("Test 2 passed ✓")

    # Test 3: Empty tree
    root = build_tree([])
    assert sol.sumOfNodes(root) == 0, f"Test 3 failed: got {sol.sumOfNodes(root)}"
    print("Test 3 passed ✓")

    # Test 4: Left-skewed tree
    root = build_tree([1,2,None,3,None,4])
    assert sol.sumOfNodes(root) == 10, f"Test 4 failed: got {sol.sumOfNodes(root)}"
    print("Test 4 passed ✓")

    # Test 5: Negative values
    root = build_tree([1,-2,3,-4,5])
    assert sol.sumOfNodes(root) == 3, f"Test 5 failed: got {sol.sumOfNodes(root)}"
    print("Test 5 passed ✓")

    # Test 6: All zeros
    root = build_tree([0,0,0])
    assert sol.sumOfNodes(root) == 0, f"Test 6 failed: got {sol.sumOfNodes(root)}"
    print("Test 6 passed ✓")

    # Test 7: Two nodes
    root = build_tree([10,5])
    assert sol.sumOfNodes(root) == 15, f"Test 7 failed: got {sol.sumOfNodes(root)}"
    print("Test 7 passed ✓")

    # Test 8: Larger tree
    root = build_tree([1,2,3,4,5,6,7])
    assert sol.sumOfNodes(root) == 28, f"Test 8 failed: got {sol.sumOfNodes(root)}"
    print("Test 8 passed ✓")

    print("\nAll tests passed! ✓")
