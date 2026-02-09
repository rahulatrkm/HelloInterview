"""
Longest Substring Without Repeating Characters
https://www.hellointerview.com/learn/code/sliding-window/longest-substring-without-repeating-characters

DESCRIPTION (inspired by Leetcode 3):
Write a function to return the length of the longest substring in a 
provided string s where all characters in the substring are distinct.

Example 1:
Input: s = "eghghhgg"
Output: 3
Explanation: The longest substring without repeating characters is "egh" 
with length of 3.

Example 2:
Input: s = "substring"
Output: 8
Explanation: The answer is "ubstring" with length of 8.

Approach (Variable-Length Sliding Window):
- Use a dictionary/set to track characters in the current window
- Expand window by moving end pointer
- When a duplicate is found, contract from start until valid
- Track max window length throughout
- O(n) time, O(min(n, alphabet_size)) space
"""


class Solution:
    def longestSubstringWithoutRepeat(self, s: str):
        seen = set()
        st = i = 0
        ans = 0
        while i < len(s):
            while s[i] in seen:
                seen.remove(s[st])
                st += 1
            seen.add(s[i])
            i += 1
            ans = max(ans, i-st)
        return ans


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("eghghhgg", 3),
        ("substring", 8),
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("a", 1),
        ("abcdef", 6),
        ("aab", 2),
    ]

    sol = Solution()
    for i, (s, expected) in enumerate(test_cases):
        result = sol.longestSubstringWithoutRepeat(s)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | s=\"{s}\" | Output: {result} | Expected: {expected}")
