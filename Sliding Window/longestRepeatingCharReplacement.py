"""
Longest Repeating Character Replacement
https://www.hellointerview.com/learn/code/sliding-window/longest-repeating-character-replacement

DESCRIPTION (inspired by Leetcode 424):
Write a function to find the length of the longest substring containing 
the same letter in a given string s, after performing at most k operations 
in which you can choose any character of the string and change it to any 
other uppercase English letter.

Example 1:
Input: s = "BBABCCDD", k = 2
Output: 5
Explanation: Replace the first 'A' and 'C' with 'B' to form "BBBBBCDD". 
The longest substring with identical letters is "BBBBB", length 5.

Example 2:
Input: s = "BCBABCCCCA", k = 2
Output: 7
Explanation: Replace 'B' and 'A' in "BCCCCCA" region to get 7 C's.

Approach (Variable-Length Sliding Window):
- Track character frequencies in the window with a dictionary
- Track max_freq: the highest frequency of any single character seen
- Window is valid when: window_length - max_freq <= k
  (i.e., we need at most k replacements to make all chars the same)
- If invalid, shrink from left by 1 (window never shrinks below best)
- max_freq never needs to decrease — we only care about improvements
- O(n) time, O(26) = O(1) space
"""
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int):
        seen = defaultdict(int)
        st = 0
        ans = 0
        curr_max = 0
        n = len(s)
        for i in range(n):
            seen[s[i]] += 1
            curr_max = max(curr_max, seen[s[i]])
            if curr_max + k < i-st+1:
                seen[s[st]] -= 1
                st += 1
            ans = max(ans, i-st+1)
        return ans


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("BBABCCDD", 2, 5),
        ("BCBABCCCCA", 2, 6),
        ("AABABBA", 1, 4),
        ("ABAB", 2, 4),
        ("ABBB", 2, 4),
        ("A", 0, 1),
        ("AAAA", 0, 4),
        ("ABCD", 0, 1),
    ]

    sol = Solution()
    for i, (s, k, expected) in enumerate(test_cases):
        result = sol.characterReplacement(s, k)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | s=\"{s}\", k={k} | Output: {result} | Expected: {expected}")
