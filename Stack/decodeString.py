"""
Decode String (Medium)
https://www.hellointerview.com/learn/code/stack/decode-string

Given an encoded string, write a function to return its decoded string that follows a
specific encoding rule: k[encoded_string], where the encoded_string within the brackets
is repeated exactly k times. Note that k is always a positive integer. The input string
is well-formed without any extra spaces, and square brackets are properly matched.
The original data doesn't contain digits other than the ones that specify the number
of times to repeat.

Example 1:
  Input: s = "3[a2[c]]"
  Output: "accaccacc"

Example 2:
  Input: s = "3[a]2[bc]"
  Output: "aaabcbc"

Approach:
  - Use a stack to handle nested sequences.
  - Track current string and current number.
  - On '[', push context (current string + number) onto stack, reset.
  - On ']', pop and build: prev_string + num * curr_string.
  - On digit, build multi-digit number.
  - On letter, append to current string.
"""


class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        curr = ''
        for char in s:
            if char.isnumeric():
                if not curr.isnumeric(): 
                    st.append(curr)
                    curr = ''
                curr += char
            elif char.isalpha():
                curr += char
            elif char == '[':
                st.append(curr)
                curr = ''
            else:
                prev_num = int(st.pop())
                prev_str = st.pop() if st else ''
                curr = prev_str + prev_num * curr
        return curr



if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("3[a2[c]]", "accaccacc"),
        ("3[a]2[bc]", "aaabcbc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
        ("abc3[cd]xyz", "abccdcdcdxyz"),
        ("10[a]", "aaaaaaaaaa"),
        ("2[a2[b]]", "abbabb"),
        ("a", "a"),
    ]
    for i, (s, expected) in enumerate(tests):
        result = sol.decodeString(s)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {s!r} | Expected: {expected!r} | Got: {result!r}")
