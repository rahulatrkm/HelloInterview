"""
Validate Binary Search Tree
https://www.hellointerview.com/learn/code/depth-first-search/validate-binary-search-tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A tree is a BST if:
- Every node in the left subtree has a value less than the current node
- Every node in the right subtree has a value greater than the current node
- The left and right subtrees must also be valid BSTs

Example 1:
  Input: [2, 1, 4]
         2
        / \
       1   4
  Output: true

Example 2:
  Input: [4, 1, 5, null, null, 3, 6]
         4
        / \
       1   5
          / \
         3   6
  Output: false (3 is in right subtree but < 4)

Approach:
- Pass min/max bounds down from parent to children
- Left child: max becomes node.val, min stays same
- Right child: min becomes node.val, max stays same
- Check if node.val is within (min, max) range
- Base case: null node → True

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
    def validateBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, min_val, max_val):
            if not node:
                return True
            if min_val < node.val < max_val:
                return helper(node.left, min_val, node.val) and helper(node.right, node.val, max_val)
            return False

        return helper(root, float('-inf'), float('inf'))


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Valid BST
    root = build_tree([2,1,4])
    assert sol.validateBST(root) == True, f"Test 1 failed: got {sol.validateBST(root)}"
    print("Test 1 passed ✓")

    # Test 2: Invalid - node in wrong subtree
    root = build_tree([4,1,5,None,None,3,6])
    assert sol.validateBST(root) == False, f"Test 2 failed: got {sol.validateBST(root)}"
    print("Test 2 passed ✓")

    # Test 3: Single node
    root = build_tree([1])
    assert sol.validateBST(root) == True, f"Test 3 failed: got {sol.validateBST(root)}"
    print("Test 3 passed ✓")

    # Test 4: Empty tree
    root = build_tree([])
    assert sol.validateBST(root) == True, f"Test 4 failed: got {sol.validateBST(root)}"
    print("Test 4 passed ✓")

    # Test 5: Valid larger BST
    root = build_tree([5,3,7,2,4,6,8])
    assert sol.validateBST(root) == True, f"Test 5 failed: got {sol.validateBST(root)}"
    print("Test 5 passed ✓")

    # Test 6: Invalid - duplicate values
    root = build_tree([5,1,5])
    assert sol.validateBST(root) == False, f"Test 6 failed: got {sol.validateBST(root)}"
    print("Test 6 passed ✓")

    # Test 7: Invalid - left child too large
    root = build_tree([5,6,7])
    assert sol.validateBST(root) == False, f"Test 7 failed: got {sol.validateBST(root)}"
    print("Test 7 passed ✓")

    # Test 8: Two nodes - valid
    root = build_tree([1,None,2])
    assert sol.validateBST(root) == True, f"Test 8 failed: got {sol.validateBST(root)}"
    print("Test 8 passed ✓")

    print("\nAll tests passed! ✓")
