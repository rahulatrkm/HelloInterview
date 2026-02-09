"""
Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons):
    2: "abc"
    3: "def"
    4: "ghi"
    5: "jkl"
    6: "mno"
    7: "pqrs"
    8: "tuv"
    9: "wxyz"

Example 1:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
    Input: digits = "2"
    Output: ["a","b","c"]

Approach:
- Visualize as a solution-space tree: each level corresponds to a digit
- Use backtracking: for each digit, iterate over its mapped letters
- Append each letter to current path and recurse on next digit index
- Base case: when index == len(digits), add current combination to results

Time Complexity: O(n * 4^n) where n is the number of digits
Space Complexity: O(n) for recursion depth
"""

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Your code goes here
        pass


def run_tests():
    solution = Solution()
    
    # Test 1: Two digits
    result = solution.letterCombinations("23")
    expected = {"ad","ae","af","bd","be","bf","cd","ce","cf"}
    assert set(result) == expected, f"Test 1 Failed: Expected {expected}, got {result}"
    print("Test 1 Passed")
    
    # Test 2: Single digit
    result = solution.letterCombinations("2")
    expected = {"a","b","c"}
    assert set(result) == expected, f"Test 2 Failed: Expected {expected}, got {result}"
    print("Test 2 Passed")
    
    # Test 3: Empty input
    result = solution.letterCombinations("")
    expected = []
    assert result == expected, f"Test 3 Failed: Expected {expected}, got {result}"
    print("Test 3 Passed")
    
    # Test 4: Digit with 4 letters
    result = solution.letterCombinations("7")
    expected = {"p","q","r","s"}
    assert set(result) == expected, f"Test 4 Failed: Expected {expected}, got {result}"
    print("Test 4 Passed")
    
    # Test 5: Three digits
    result = solution.letterCombinations("234")
    assert len(result) == 27, f"Test 5 Failed: Expected 27 combinations, got {len(result)}"
    print("Test 5 Passed")
    
    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
