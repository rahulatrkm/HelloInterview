"""
Combination Sum

Given an array of distinct integers candidates and a target integer target, 
generate all unique combinations of candidates which sum to target. The 
combinations may be returned in any order, and the same number may be chosen 
from candidates an unlimited number of times.

Constraints:
- All values in candidates are positive integers.
- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- All elements of candidates are distinct.
- 1 <= target <= 40

Example:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation: 2+2+3=7, 7=7. These are the only two combinations.

Approach:
- Sort candidates for easy pruning
- Use backtracking: iterate from start index, allowing reuse of same element
- Subtract current candidate from remaining target
- Prune when candidate > remaining target (since sorted, all subsequent are larger)
- Base case: target == 0 means valid combination found

Time Complexity: O(n^(T/m)) where T is target and m is min candidate
Space Complexity: O(T/m) for recursion depth
"""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Your code goes here
        pass


def run_tests():
    solution = Solution()
    
    # Test 1: Standard case
    result = solution.combinationSum([2, 3, 6, 7], 7)
    expected = [[2, 2, 3], [7]]
    assert sorted([sorted(c) for c in result]) == sorted([sorted(c) for c in expected]), \
        f"Test 1 Failed: Expected {expected}, got {result}"
    print("Test 1 Passed")
    
    # Test 2: Multiple combinations
    result = solution.combinationSum([2, 3, 5], 8)
    expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert sorted([sorted(c) for c in result]) == sorted([sorted(c) for c in expected]), \
        f"Test 2 Failed: Expected {expected}, got {result}"
    print("Test 2 Passed")
    
    # Test 3: No valid combination
    result = solution.combinationSum([3, 5], 2)
    expected = []
    assert result == expected, f"Test 3 Failed: Expected {expected}, got {result}"
    print("Test 3 Passed")
    
    # Test 4: Single candidate used multiple times
    result = solution.combinationSum([2], 4)
    expected = [[2, 2]]
    assert sorted([sorted(c) for c in result]) == sorted([sorted(c) for c in expected]), \
        f"Test 4 Failed: Expected {expected}, got {result}"
    print("Test 4 Passed")
    
    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
