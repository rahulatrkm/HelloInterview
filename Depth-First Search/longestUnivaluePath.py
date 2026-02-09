"""
Longest Univalue Path

DESCRIPTION (inspired by Leetcode.com):
Given the root of the binary tree, find the longest path where all nodes along
the path have the same value. This path doesn't have to include the root node.
Return the number of edges on that path, not the number of nodes.

Example 1:
Input: [1,4,5,4,4,5]
Output: 2

Explanation: The longest path of the same value is the path [4,4,4], which has 
a total of 2 edges.

Example 2:
Input: [1,1,1,1,1,1,1]
Output: 4

Explanation: The longest path of the same value is the path [1,1,1,1,1], which 
has a length of 4.

Approach:
- Use post-order DFS traversal
- For each node, check if left and right children have the same value
- If left child matches, can extend path by (left_path + 1)
- If right child matches, can extend path by (right_path + 1)
- The longest path through current node = left_arrow + right_arrow
- Return max(left_arrow, right_arrow) to parent (can only extend one direction upward)
- Track maximum path length in global variable

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
    def longestUnivaluePath(self, root: TreeNode) -> int:
        longest_path = 0
        
        def dfs(node):
            nonlocal longest_path
            if not node:
                return 0
            
            left_length = dfs(node.left)
            right_length = dfs(node.right)
            
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            
            longest_path = max(longest_path, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)
        
        dfs(root)
        return longest_path

if __name__ == "__main__":
    sol = Solution()
    
    # Test 1
    tree = build_tree([1,4,5,4,4,5])
    result = sol.longestUnivaluePath(tree)
    assert result == 2, f"Test 1 failed: expected 2, got {result}"
    print("✓ Test 1 passed")
    
    # Test 2
    tree = build_tree([1,1,1,1,1,1,1])
    result = sol.longestUnivaluePath(tree)
    assert result == 4, f"Test 2 failed: expected 4, got {result}"
    print("✓ Test 2 passed")
    
    # Test 3 - Single node
    tree = build_tree([5])
    result = sol.longestUnivaluePath(tree)
    assert result == 0, f"Test 3 failed: expected 0, got {result}"
    print("✓ Test 3 passed")
    
    # Test 4 - No matching values
    tree = build_tree([1,2,3,4,5,6,7])
    result = sol.longestUnivaluePath(tree)
    assert result == 0, f"Test 4 failed: expected 0, got {result}"
    print("✓ Test 4 passed")
    
    # Test 5 - All same values
    tree = build_tree([5,5,5,5,5])
    result = sol.longestUnivaluePath(tree)
    assert result == 3, f"Test 5 failed: expected 3, got {result}"
    print("✓ Test 5 passed")
    
    # Test 6 - Left skewed with same values
    tree = build_tree([1,1,None,1,None,1])
    result = sol.longestUnivaluePath(tree)
    assert result == 3, f"Test 6 failed: expected 3, got {result}"
    print("✓ Test 6 passed")
    
    # Test 7 - Mixed
    tree = build_tree([5,4,5,1,1,None,5])
    result = sol.longestUnivaluePath(tree)
    assert result == 2, f"Test 7 failed: expected 2, got {result}"
    print("✓ Test 7 passed")
    
    print("\n✓ All tests passed!")
