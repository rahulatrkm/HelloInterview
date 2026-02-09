"""
Subsets

Given an integer array nums of unique elements, return all possible subsets 
that can be made from the elements in nums.

The solution set must not contain duplicate subsets, and the subsets can be
returned in any order.

Example 1:
    Input: nums = [1, 2]
    Output: [[], [1], [2], [1, 2]]

Example 2:
    Input: nums = [0]
    Output: [[], [0]]

Approach:
- Visualize as a binary solution-space tree: include or exclude each element
- Use DFS backtracking: at each index, choose to include or exclude nums[index]
- Base case: when index == len(nums), add current subset copy to results
- Backtrack by popping the last element after the include branch

Time Complexity: O(n * 2^n) - 2^n subsets, each up to n elements to copy
Space Complexity: O(n) - recursion depth, not counting output
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Your code goes here
        pass


def run_tests():
    solution = Solution()
    
    # Test 1: Two elements
    result = solution.subsets([1, 2])
    expected = [[], [1], [1, 2], [2]]
    assert sorted([sorted(s) for s in result]) == sorted([sorted(s) for s in expected]), \
        f"Test 1 Failed: Expected {expected}, got {result}"
    print("Test 1 Passed")
    
    # Test 2: Single element
    result = solution.subsets([0])
    expected = [[], [0]]
    assert sorted([sorted(s) for s in result]) == sorted([sorted(s) for s in expected]), \
        f"Test 2 Failed: Expected {expected}, got {result}"
    print("Test 2 Passed")
    
    # Test 3: Three elements
    result = solution.subsets([1, 2, 3])
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert sorted([sorted(s) for s in result]) == sorted([sorted(s) for s in expected]), \
        f"Test 3 Failed: Expected {expected}, got {result}"
    print("Test 3 Passed")
    
    # Test 4: Empty input
    result = solution.subsets([])
    expected = [[]]
    assert result == expected, f"Test 4 Failed: Expected {expected}, got {result}"
    print("Test 4 Passed")
    
    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
