"""
Decode Ways

Given a string s containing only digits, return the number of ways to decode it
using the mapping: '1' -> 'A', '2' -> 'B', ..., '26' -> 'Z'.

A digit string may have multiple decodings. For example, "14" can be decoded as
"AD" (1,4) or "N" (14).

Note: '0' cannot be decoded on its own. "01" is not a valid encoding of 'A'.

Example 1:
    Input: s = "101"
    Output: 1
    Explanation: Only "JA" (10, 1). "01" is not valid.

Example 2:
    Input: s = "226"
    Output: 3
    Explanation: "BZ" (2,26), "VF" (22,6), "BBF" (2,2,6).

Example 3:
    Input: s = "11106"
    Output: 2
    Explanation: "AAJF" (1,1,10,6) and "KJF" (11,10,6).

Approach:
- dp[i] = number of ways to decode first i characters of s
- Base cases: dp[0] = 1 (empty string), dp[1] = 1 if s[0] != '0', else 0
- For each i from 2 to n:
  - Single digit: if s[i-1] != '0', dp[i] += dp[i-1]
  - Two digits: if 10 <= int(s[i-2:i]) <= 26, dp[i] += dp[i-2]

Time Complexity: O(n)
Space Complexity: O(n), can be optimized to O(1)
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        # Your code goes here
        # def helper(i):
        #     if i in memo:
        #         return memo[i]
        #     if i == len(s):
        #         return 1
        #     if s[i] == '0':
        #         return 0
        #     count = helper(i + 1)
        #     if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
        #         count += helper(i + 2)
        #     memo[i] = count
        #     return count
                

        # memo = {}
        # return helper(0)

        n = len(s)
        if n == 0:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, n + 1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[n]


def run_tests():
    solution = Solution()

    # Test 1: Only one valid decoding
    result = solution.numDecodings("101")
    assert result == 1, f"Test 1 Failed: Expected 1, got {result}"
    print("Test 1 Passed")

    # Test 2: Multiple decodings
    result = solution.numDecodings("226")
    assert result == 3, f"Test 2 Failed: Expected 3, got {result}"
    print("Test 2 Passed")

    # Test 3: Zeros in string
    result = solution.numDecodings("11106")
    assert result == 2, f"Test 3 Failed: Expected 2, got {result}"
    print("Test 3 Passed")

    # Test 4: Leading zero — no valid decoding
    result = solution.numDecodings("0")
    assert result == 0, f"Test 4 Failed: Expected 0, got {result}"
    print("Test 4 Passed")

    # Test 5: Single digit
    result = solution.numDecodings("1")
    assert result == 1, f"Test 5 Failed: Expected 1, got {result}"
    print("Test 5 Passed")

    # Test 6: All ones
    result = solution.numDecodings("111")
    assert result == 3, f"Test 6 Failed: Expected 3, got {result}"
    print("Test 6 Passed")

    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
