"""
Valid Parentheses (Easy)
https://www.hellointerview.com/learn/code/stack/valid-parentheses

Given an input string s consisting solely of the characters '(', ')', '{', '}', '[' and ']',
determine whether s is a valid string. A string is considered valid if every opening bracket
is closed by a matching type of bracket and in the correct order, and every closing bracket
has a corresponding opening bracket of the same type.

Example 1:
  Input: s = "(){({})}"
  Output: True

Example 2:
  Input: s = "(){({}})""
  Output: False

Approach:
  - Use a stack. Push opening brackets, pop on closing brackets.
  - When encountering a closing bracket, check if it matches the top of the stack.
  - Return True if the stack is empty at the end.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c in mapping:
                top = stack.pop() if stack else '#'
                if mapping[c] != top:
                    return False
            else:
                stack.append(c)
        return not stack


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("(){({})}", True),
        ("(){({}})}", False),
        ("", True),
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("(", False),
        (")", False),
    ]
    for i, (s, expected) in enumerate(tests):
        result = sol.isValid(s)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {s!r} | Expected: {expected} | Got: {result}")
