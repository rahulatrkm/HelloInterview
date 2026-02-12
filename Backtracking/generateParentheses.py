"""
Generate Parentheses

Given an integer n, write a function to return all well-formed (valid) expressions 
that can be made using n pairs of parentheses.

Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
    Input: n = 2
    Output: ["(())","()()"]

Approach:
- Visualize as a solution-space tree where each node adds '(' or ')'
- Use backtracking with two rules:
  1. Add '(' if count of open parens < n
  2. Add ')' if count of close parens < count of open parens
- Base case: when string length == 2 * n, add to results

Time Complexity: O(4^n / sqrt(n)) - Catalan number bound
Space Complexity: O(n) - recursion depth
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Your code goes here
        ans = []
        curr = []
        def helper(n, oc):
            if n == 0:
                curr.append(')'*oc)
                ans.append("".join(curr))
                curr.pop()
                return
            
            if oc:
                curr.append(")")
                helper(n, oc-1)
                curr.pop()
            curr.append('(')
            helper(n-1, oc+1)
            curr.pop()
        helper(n, 0)
        return ans

def run_tests():
    solution = Solution()
    
    # Test 1: n = 3
    result = solution.generateParenthesis(3)
    expected = {"((()))", "(()())", "(())()", "()(())", "()()()"}
    assert set(result) == expected, f"Test 1 Failed: Expected {expected}, got {result}"
    print("Test 1 Passed")
    
    # Test 2: n = 2
    result = solution.generateParenthesis(2)
    expected = {"(())", "()()"}
    assert set(result) == expected, f"Test 2 Failed: Expected {expected}, got {result}"
    print("Test 2 Passed")
    
    # Test 3: n = 1
    result = solution.generateParenthesis(1)
    expected = {"()"}
    assert set(result) == expected, f"Test 3 Failed: Expected {expected}, got {result}"
    print("Test 3 Passed")
    
    # Test 4: n = 4
    result = solution.generateParenthesis(4)
    assert len(result) == 14, f"Test 4 Failed: Expected 14 combinations, got {len(result)}"
    print("Test 4 Passed")
    
    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
