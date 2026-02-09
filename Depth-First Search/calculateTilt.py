"""
Calculate Tilt

DESCRIPTION (inspired by Leetcode.com):
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is defined as the absolute difference between the sum of 
all left subtree node values and all right subtree node values. If a node does 
not have a left child, then the sum of the left subtree node values is treated 
as 0. The rule is similar if the node does not have a right child.

Example 1:
Input: [4,2,7,1,3,6,9]
Output: 21

Explanation:
- Node 1: tilt = |0 - 0| = 0 (no left or right child)
- Node 3: tilt = |0 - 0| = 0 (no left or right child)
- Node 6: tilt = |0 - 0| = 0 (no left or right child)
- Node 9: tilt = |0 - 0| = 0 (no left or right child)
- Node 2: tilt = |1 - 3| = 2
- Node 7: tilt = |6 - 9| = 3
- Node 4: tilt = |(1 + 2 + 3) - (6 + 7 + 9)| = |6 - 22| = 16
- Sum of tilts = 0 + 0 + 0 + 0 + 2 + 3 + 16 = 21

Example 2:
Input: [1,2,3]
Output: 1

Explanation:
- Node 2: tilt = |0 - 0| = 0
- Node 3: tilt = |0 - 0| = 0
- Node 1: tilt = |2 - 3| = 1
- Sum of tilts = 0 + 0 + 1 = 1

Approach:
- Use post-order DFS traversal to calculate the sum of each subtree
- For each node, calculate tilt = |sum(left_subtree) - sum(right_subtree)|
- Use a global variable to accumulate the total tilt
- Each recursive call returns the sum of its subtree to the parent
- Base case: empty node has sum 0

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
    def findTilt(self, root: TreeNode) -> int:
        tilt_sum = 0
        def post_order(node):
            nonlocal tilt_sum
            if not node:
                return 0
            
            left_sum = post_order(node.left)
            right_sum = post_order(node.right)
            
            tilt_sum += abs(left_sum - right_sum)
            
            return left_sum + right_sum + node.val

        post_order(root)
        return tilt_sum

if __name__ == "__main__":
    sol = Solution()
    
    # Test 1
    tree = build_tree([4,2,7,1,3,6,9])
    result = sol.findTilt(tree)
    assert result == 21, f"Test 1 failed: expected 21, got {result}"
    print("✓ Test 1 passed")
    
    # Test 2
    tree = build_tree([1,2,3])
    result = sol.findTilt(tree)
    assert result == 1, f"Test 2 failed: expected 1, got {result}"
    print("✓ Test 2 passed")
    
    # Test 3 - Single node
    tree = build_tree([5])
    result = sol.findTilt(tree)
    assert result == 0, f"Test 3 failed: expected 0, got {result}"
    print("✓ Test 3 passed")
    
    # Test 4 - Empty tree
    tree = build_tree([])
    result = sol.findTilt(tree)
    assert result == 0, f"Test 4 failed: expected 0, got {result}"
    print("✓ Test 4 passed")
    
    # Test 5 - Left skewed
    tree = build_tree([1,2,None,3])
    result = sol.findTilt(tree)
    assert result == 8, f"Test 5 failed: expected 8, got {result}"
    print("✓ Test 5 passed")
    
    # Test 6 - All same values
    tree = build_tree([5,5,5,5,5])
    result = sol.findTilt(tree)
    assert result == 10, f"Test 6 failed: expected 10, got {result}"
    print("✓ Test 6 passed")
    
    # Test 7
    tree = build_tree([21,7,14,1,1,2,2,3,3])
    result = sol.findTilt(tree)
    assert result == 9, f"Test 7 failed: expected 9, got {result}"
    print("✓ Test 7 passed")
    
    print("\n✓ All tests passed!")
