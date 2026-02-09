"""
Diameter of a Binary Tree

DESCRIPTION (inspired by Leetcode.com):
Given the root of a binary tree, write a recursive function to find the diameter
of the tree. The diameter of a binary tree is the length of the longest path (# 
of edges) between any two nodes in a tree. This path may or may not pass 
through the root.

Example 1:
Input: [3,9,2,1,4,null,null,null,5]
Output: 4

Explanation: The longest path is 5 -> 1 -> 9 -> 3 -> 2, which has 4 edges.

Example 2:
Input: [3,9,null,1,4,null,null,2,null,3]
Output: 4

Explanation: The longest path is 2 -> 1 -> 9 -> 4 -> 3, which has 4 edges.

Approach:
- The diameter at any node = max_depth(left_subtree) + max_depth(right_subtree)
- Use post-order DFS to calculate the max depth of each subtree
- Track the maximum diameter seen so far in a global variable
- Each recursive call returns the max depth of the current subtree (1 + max(left, right))
- Base case: empty node has depth 0

Time Complexity: O(N) where N is the number of nodes
Space Complexity: O(N) for the recursion call stack
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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0
        
        def max_depth(node):
            nonlocal diameter
            if not node:
                return 0
            left_depth = max_depth(node.left)
            right_depth = max_depth(node.right)
            diameter = max(diameter, left_depth + right_depth)
            return 1 + max(left_depth, right_depth)
        
        max_depth(root)
        return diameter

if __name__ == "__main__":
    sol = Solution()
    
    # Test 1
    tree = build_tree([3,9,2,1,4,None,None,None,5])
    result = sol.diameterOfBinaryTree(tree)
    assert result == 4, f"Test 1 failed: expected 4, got {result}"
    print("✓ Test 1 passed")
    
    # Test 2
    tree = build_tree([3,9,None,1,4,None,None,2,None,3])
    result = sol.diameterOfBinaryTree(tree)
    assert result == 4, f"Test 2 failed: expected 4, got {result}"
    print("✓ Test 2 passed")
    
    # Test 3 - Single node
    tree = build_tree([1])
    result = sol.diameterOfBinaryTree(tree)
    assert result == 0, f"Test 3 failed: expected 0, got {result}"
    print("✓ Test 3 passed")
    
    # Test 4 - Two nodes
    tree = build_tree([1,2])
    result = sol.diameterOfBinaryTree(tree)
    assert result == 1, f"Test 4 failed: expected 1, got {result}"
    print("✓ Test 4 passed")
    
    # Test 5 - Balanced tree
    tree = build_tree([1,2,3,4,5])
    result = sol.diameterOfBinaryTree(tree)
    assert result == 3, f"Test 5 failed: expected 3, got {result}"
    print("✓ Test 5 passed")
    
    # Test 6 - Left skewed
    tree = build_tree([1,2,None,3,None,4])
    result = sol.diameterOfBinaryTree(tree)
    assert result == 3, f"Test 6 failed: expected 3, got {result}"
    print("✓ Test 6 passed")
    
    # Test 7 - Complete binary tree
    tree = build_tree([1,2,3,4,5,6,7])
    result = sol.diameterOfBinaryTree(tree)
    assert result == 4, f"Test 7 failed: expected 4, got {result}"
    print("✓ Test 7 passed")
    
    print("\n✓ All tests passed!")
