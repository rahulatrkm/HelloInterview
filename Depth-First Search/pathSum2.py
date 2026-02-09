"""
Path Sum II

DESCRIPTION (inspired by Leetcode.com):
Given the root of a binary tree and an integer target, write a recursive function 
to find all root-to-leaf paths where the sum of all the values along the path 
sum to target.

Example 1:
Input: [1,2,4,4,7,5,1], target = 10
Output: [[1,2,7],[1,4,5]]

Explanation: The paths are 1 -> 2 -> 7 and 1 -> 4 -> 5

Approach:
- Use DFS to traverse all root-to-leaf paths
- Maintain current path as we traverse
- Pass remaining target down the tree (target - node.val)
- When reaching a leaf node, check if remaining target equals node value
- If yes, add a copy of the current path to the result
- Backtrack by popping the last node from path after exploring both children
- Use a global list to collect all valid paths

Time Complexity: O(N) where N is the number of nodes
Space Complexity: O(N) for the recursion call stack and path storage
"""

class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    """Build a binary tree from level-order array representation."""
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
    def pathSum(self, root: TreeNode, target: int) -> list:
        ans = []
        def dfs(node, remaining_target, path):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and remaining_target == node.val:
                ans.append(path.copy())
            dfs(node.left, remaining_target - node.val, path)
            dfs(node.right, remaining_target - node.val, path)
            path.pop()

        dfs(root, target, [])
        return ans

if __name__ == "__main__":
    sol = Solution()
    
    # Test 1
    tree = build_tree([1,2,4,4,7,5,1])
    result = sol.pathSum(tree, 10)
    expected = [[1,2,7],[1,4,5]]
    # Sort both lists to handle order differences
    result_sorted = [sorted(path) for path in result]
    expected_sorted = [sorted(path) for path in expected]
    assert sorted(result_sorted) == sorted(expected_sorted), f"Test 1 failed: expected {expected}, got {result}"
    print("✓ Test 1 passed")
    
    # Test 2 - Single path
    tree = build_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
    result = sol.pathSum(tree, 22)
    expected = [[5,4,11,2],[5,8,4,5]]
    result_sorted = [sorted(path) for path in result]
    expected_sorted = [sorted(path) for path in expected]
    assert sorted(result_sorted) == sorted(expected_sorted), f"Test 2 failed: expected {expected}, got {result}"
    print("✓ Test 2 passed")
    
    # Test 3 - No valid paths
    tree = build_tree([1,2,3])
    result = sol.pathSum(tree, 10)
    assert result == [], f"Test 3 failed: expected [], got {result}"
    print("✓ Test 3 passed")
    
    # Test 4 - Single node match
    tree = build_tree([5])
    result = sol.pathSum(tree, 5)
    assert result == [[5]], f"Test 4 failed: expected [[5]], got {result}"
    print("✓ Test 4 passed")
    
    # Test 5 - Empty tree
    tree = build_tree([])
    result = sol.pathSum(tree, 0)
    assert result == [], f"Test 5 failed: expected [], got {result}"
    print("✓ Test 5 passed")
    
    # Test 6 - Multiple paths with same sum
    tree = build_tree([1,2,2])
    result = sol.pathSum(tree, 3)
    assert len(result) == 2, f"Test 6 failed: expected 2 paths, got {len(result)}"
    print("✓ Test 6 passed")
    
    # Test 7 - Negative values
    tree = build_tree([1,-2,3])
    result = sol.pathSum(tree, -1)
    assert result == [[1,-2]], f"Test 7 failed: expected [[1,-2]], got {result}"
    print("✓ Test 7 passed")
    
    print("\n✓ All tests passed!")
