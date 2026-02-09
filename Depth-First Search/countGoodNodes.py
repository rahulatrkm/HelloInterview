"""
Count Good Nodes in Binary Tree
https://www.hellointerview.com/learn/code/depth-first-search/

Given the root node of a binary tree, write a function to find the number of 
"good nodes" in the tree. A node X in the tree is considered "good" if in the 
path from the root to the node X, there are no nodes with a value greater than 
X's value.

Example 1:
  Input: [3, 1, 4, 3, null, 1, 5]
         3
        / \
       1   4
      /   / \
     3   1   5
  Output: 4
  Explanation: Good nodes are: 3 (root), 4 (3->4), 3 (3->1->3), 5 (3->4->5)

Example 2:
  Input: [3, 3, null, 4, 2]
         3
        /
       3
      / \
     4   2
  Output: 3
  Explanation: Good nodes are: 3 (root), 3 (3->3), 4 (3->3->4)

Approach:
- Pass max value seen so far down from parent to children
- At each node, check if node.val >= max_so_far → increment count
- Update max_so_far = max(max_so_far, node.val) for children
- Use helper function to pass down max_so_far
- Count good nodes in left and right subtrees

Time: O(n)
Space: O(h) for call stack, where h is height
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
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        cnt = 0
        def helper(node, max_so_far):
            nonlocal cnt
            if not node:
                return 0
            cnt += 1 if node.val >= max_so_far else 0
            new_max = max(max_so_far, node.val)
            helper(node.left, new_max)
            helper(node.right, new_max)
        
        helper(root, float('-inf'))
        return cnt


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Example 1
    root = build_tree([3,1,4,3,None,1,5])
    assert sol.goodNodes(root) == 4, f"Test 1 failed: got {sol.goodNodes(root)}"
    print("Test 1 passed ✓")

    # Test 2: Example 2
    root = build_tree([3,3,None,4,2])
    assert sol.goodNodes(root) == 3, f"Test 2 failed: got {sol.goodNodes(root)}"
    print("Test 2 passed ✓")

    # Test 3: Single node
    root = build_tree([1])
    assert sol.goodNodes(root) == 1, f"Test 3 failed: got {sol.goodNodes(root)}"
    print("Test 3 passed ✓")

    # Test 4: All increasing path
    root = build_tree([1,2,3,4,5,6,7])
    assert sol.goodNodes(root) == 7, f"Test 4 failed: got {sol.goodNodes(root)}"
    print("Test 4 passed ✓")

    # Test 5: All decreasing path
    root = build_tree([7,6,5,4,3,2,1])
    assert sol.goodNodes(root) == 1, f"Test 5 failed: got {sol.goodNodes(root)}"
    print("Test 5 passed ✓")

    # Test 6: All same values
    root = build_tree([5,5,5,5,5])
    assert sol.goodNodes(root) == 5, f"Test 6 failed: got {sol.goodNodes(root)}"
    print("Test 6 passed ✓")

    # Test 7: Two nodes
    root = build_tree([3,1])
    assert sol.goodNodes(root) == 1, f"Test 7 failed: got {sol.goodNodes(root)}"
    print("Test 7 passed ✓")

    # Test 8: Negative values
    root = build_tree([-1,5,-2,4,None,3])
    assert sol.goodNodes(root) == 3, f"Test 8 failed: got {sol.goodNodes(root)}"
    print("Test 8 passed ✓")

    print("\nAll tests passed! ✓")
