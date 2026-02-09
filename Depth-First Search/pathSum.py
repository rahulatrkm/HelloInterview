"""
Path Sum
https://www.hellointerview.com/learn/code/depth-first-search/path-sum

Given the root of a binary tree and an integer target, write a recursive function
to determine if the tree has a root-to-leaf path where all the values along that
path sum to the target.

Example 1:
  Input: [4, 2, 7, 1, 3, 6, 9], target = 17
         4
        / \
       2   7
      / \ / \
     1  3 6  9
  Output: true (path: 4 -> 7 -> 6 = 17)

Example 2:
  Input: [4, 2, 7, 1, 3, 6, 9], target = 13
  Output: false

Approach:
- Return value: boolean indicating if path exists from current node to leaf
- Pass remaining target down: target - node.val
- Base case: null node → False; leaf node → check if target == node.val
- Return: left OR right (either path works)

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
    def pathSum(self, root: Optional[TreeNode], target: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:  # leaf node
            return target == root.val
        remaining_target = target - root.val
        return self.pathSum(root.left, remaining_target) or self.pathSum(root.right, remaining_target)


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Path exists
    root = build_tree([4,2,7,1,3,6,9])
    assert sol.pathSum(root, 17) == True, f"Test 1 failed: got {sol.pathSum(root, 17)}"
    print("Test 1 passed ✓")

    # Test 2: Path does not exist
    root = build_tree([4,2,7,1,3,6,9])
    assert sol.pathSum(root, 13) == False, f"Test 2 failed: got {sol.pathSum(root, 13)}"
    print("Test 2 passed ✓")

    # Test 3: Single node matches
    root = build_tree([5])
    assert sol.pathSum(root, 5) == True, f"Test 3 failed: got {sol.pathSum(root, 5)}"
    print("Test 3 passed ✓")

    # Test 4: Single node doesn't match
    root = build_tree([5])
    assert sol.pathSum(root, 10) == False, f"Test 4 failed: got {sol.pathSum(root, 10)}"
    print("Test 4 passed ✓")

    # Test 5: Empty tree
    root = build_tree([])
    assert sol.pathSum(root, 0) == False, f"Test 5 failed: got {sol.pathSum(root, 0)}"
    print("Test 5 passed ✓")

    # Test 6: Path through left subtree
    root = build_tree([5,4,8,11,None,13,4,7,2])
    assert sol.pathSum(root, 22) == True, f"Test 6 failed: got {sol.pathSum(root, 22)}"
    print("Test 6 passed ✓")

    # Test 7: Negative values
    root = build_tree([1,-2,-3,1,3,-2,None,-1])
    assert sol.pathSum(root, -1) == True, f"Test 7 failed: got {sol.pathSum(root, -1)}"
    print("Test 7 passed ✓")

    # Test 8: Root only path
    root = build_tree([1,2,3])
    assert sol.pathSum(root, 1) == False, f"Test 8 failed: got {sol.pathSum(root, 1)}"
    print("Test 8 passed ✓")

    print("\nAll tests passed! ✓")
