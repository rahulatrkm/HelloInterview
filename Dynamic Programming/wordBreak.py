"""
Word Break

Given a string s and a list of words wordDict, determine if s can be segmented
into a space-separated sequence of one or more dictionary words. Words can be
reused multiple times.

Example 1:
    Input: s = "hellointerview", wordDict = ["hello", "interview"]
    Output: True
    Explanation: "hellointerview" = "hello" + "interview"

Example 2:
    Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    Output: False
    Explanation: No valid segmentation exists.

Example 3:
    Input: s = "leetcode", wordDict = ["leet", "code"]
    Output: True

Approach:
- dp[i] = True if first i characters of s can be segmented into dictionary words
- Base case: dp[0] = True (empty string is valid)
- For each i from 1 to n, for each j from 0 to i:
  if dp[j] is True and s[j:i] is in wordDict, set dp[i] = True
- Return dp[n]

Time Complexity: O(n^2) where n is length of s
Space Complexity: O(n + m) for dp array and word set
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Your code goes here
        wordDict = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]


def run_tests():
    solution = Solution()

    # Test 1: Simple split
    result = solution.wordBreak("hellointerview", ["hello", "interview"])
    assert result == True, f"Test 1 Failed: Expected True, got {result}"
    print("Test 1 Passed")

    # Test 2: No valid segmentation
    result = solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
    assert result == False, f"Test 2 Failed: Expected False, got {result}"
    print("Test 2 Passed")

    # Test 3: Valid split
    result = solution.wordBreak("leetcode", ["leet", "code"])
    assert result == True, f"Test 3 Failed: Expected True, got {result}"
    print("Test 3 Passed")

    # Test 4: Reuse words
    result = solution.wordBreak("applepenapple", ["apple", "pen"])
    assert result == True, f"Test 4 Failed: Expected True, got {result}"
    print("Test 4 Passed")

    # Test 5: Single character
    result = solution.wordBreak("a", ["a"])
    assert result == True, f"Test 5 Failed: Expected True, got {result}"
    print("Test 5 Passed")

    # Test 6: Empty string
    result = solution.wordBreak("", ["a", "b"])
    assert result == True, f"Test 6 Failed: Expected True, got {result}"
    print("Test 6 Passed")

    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
