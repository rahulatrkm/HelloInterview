"""
Minimum Window Subsequence

Given a source string s1 and a pattern string s2, find the shortest contiguous
substring of s1 that contains s2 as a subsequence.

Return the shortest such substring. If no valid substring exists, return "".
When multiple substrings of equal minimum length exist, return the leftmost one.

A subsequence maintains relative order but doesn't require consecutive characters.

Example 1:
    Input: s1 = "hellointerview", s2 = "her"
    Output: "hellointer"
    Explanation: 'h'(0) → 'e'(1) → 'r'(9). Window = "hellointer" (length 10).

Example 2:
    Input: s1 = "codingisfun", s2 = "xyz"
    Output: ""
    Explanation: No characters of s2 exist in s1.

Approach:
- DP approach: dp[i][j] = starting index in s1 where we can match s2[0..j] 
  ending at s1[i]
- For each position i in s1, if s1[i] == s2[j], dp[i][j] = dp[i-1][j-1]
  (extend the match); else dp[i][j] = dp[i-1][j] (skip s1[i])
- When we complete matching all of s2 (j == len(s2)-1), check window length
- Alternative: Forward scan to find end of match, then backward scan to 
  minimize the window

Time Complexity: O(m * n) where m = len(s1), n = len(s2)
Space Complexity: O(m * n), can be optimized to O(m)
"""

class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        # Your code goes here
        m, n = len(s1), len(s2)
        start = 0
        min_len = float('inf')
        for i in range(m):
            if s1[i] == s2[-1]:
                j = n - 1
                k = i
                while j >= 0:
                    if s1[k] == s2[j]:
                        j -= 1
                    k -= 1
                    if k < 0:
                        break
                if j < 0 and (i - k) < min_len:
                    min_len = i - k
                    start = k + 1
        return s1[start:start + min_len] if min_len != float('inf') else ""


def run_tests():
    solution = Solution()

    # Test 1: Basic match
    result = solution.minWindow("hellointerview", "her")
    assert result == "hellointer", f"Test 1 Failed: Expected 'hellointer', got '{result}'"
    print("Test 1 Passed")

    # Test 2: No match possible
    result = solution.minWindow("codingisfun", "xyz")
    assert result == "", f"Test 2 Failed: Expected '', got '{result}'"
    print("Test 2 Passed")

    # Test 3: Exact match
    result = solution.minWindow("abc", "abc")
    assert result == "abc", f"Test 3 Failed: Expected 'abc', got '{result}'"
    print("Test 3 Passed")

    # Test 4: Single character pattern
    result = solution.minWindow("abcde", "c")
    assert result == "c", f"Test 4 Failed: Expected 'c', got '{result}'"
    print("Test 4 Passed")

    # Test 5: Multiple valid windows, pick shortest
    result = solution.minWindow("abcdebdde", "bde")
    assert result == "bcde", f"Test 5 Failed: Expected 'bcde', got '{result}'"
    print("Test 5 Passed")

    # Test 6: Pattern longer than source
    result = solution.minWindow("ab", "abc")
    assert result == "", f"Test 6 Failed: Expected '', got '{result}'"
    print("Test 6 Passed")

    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
