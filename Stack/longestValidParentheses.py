"""
Longest Valid Parentheses (Hard)
https://www.hellointerview.com/learn/code/stack/longest-valid-parentheses

Given a string containing just the characters '(' and ')', find the length of the
longest valid (well-formed) parentheses substring.

Example 1:
  Input: s = "())))""
  Output: 2
  (The longest valid parentheses substring is "()")

Example 2:
  Input: s = "((()()())"
  Output: 8
  (The longest valid parentheses substring is "(()()())")

Example 3:
  Input: s = ""
  Output: 0

Approach:
  - Use a stack initialized with [-1] as the base index.
  - For '(', push index onto stack.
  - For ')', pop top. If stack empty, push current index as new base.
    Otherwise, length = current index - stack[-1].
  - Track max length throughout.
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        st = [-1]
        for i, c in enumerate(s):
            if c == '(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    ans = max(ans, i-st[-1])
        return ans


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("()))))", 2),
        ("((()()())", 8),
        ("", 0),
        ("(()", 2),
        (")()())", 4),
        ("()()", 4),
        ("(()())", 6),
        ("()(()", 2),
        ("()(())", 6),
    ]
    for i, (s, expected) in enumerate(tests):
        result = sol.longestValidParentheses(s)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {s!r} | Expected: {expected} | Got: {result}")
