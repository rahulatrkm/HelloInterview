"""
Counting Bits

Given an integer n, return an array dp of size n + 1 where dp[i] is the number
of 1's in the binary representation of i.

Example 1:
    Input: n = 6
    Output: [0, 1, 1, 2, 1, 2, 2]
    Explanation:
        0 -> 0    (0 ones)
        1 -> 1    (1 one)
        2 -> 10   (1 one)
        3 -> 11   (2 ones)
        4 -> 100  (1 one)
        5 -> 101  (2 ones)
        6 -> 110  (2 ones)

Example 2:
    Input: n = 2
    Output: [0, 1, 1]

Approach:
- Bottom-up DP using the recurrence: dp[i] = dp[i // 2] + (i % 2)
- Any number i can be split into: its rightmost bit (i % 2) and the rest (i // 2)
- The count of 1's in i = count of 1's in (i // 2) + the rightmost bit
- Base case: dp[0] = 0

Time Complexity: O(n)
Space Complexity: O(n) for the output array
"""

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Your code goes here
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i // 2] + (i % 2)
        return dp


def run_tests():
    solution = Solution()

    # Test 1: n = 6
    result = solution.countBits(6)
    assert result == [0, 1, 1, 2, 1, 2, 2], f"Test 1 Failed: Expected [0,1,1,2,1,2,2], got {result}"
    print("Test 1 Passed")

    # Test 2: n = 2
    result = solution.countBits(2)
    assert result == [0, 1, 1], f"Test 2 Failed: Expected [0,1,1], got {result}"
    print("Test 2 Passed")

    # Test 3: n = 0
    result = solution.countBits(0)
    assert result == [0], f"Test 3 Failed: Expected [0], got {result}"
    print("Test 3 Passed")

    # Test 4: n = 8
    result = solution.countBits(8)
    assert result == [0, 1, 1, 2, 1, 2, 2, 3, 1], f"Test 4 Failed: Expected [0,1,1,2,1,2,2,3,1], got {result}"
    print("Test 4 Passed")

    # Test 5: n = 1
    result = solution.countBits(1)
    assert result == [0, 1], f"Test 5 Failed: Expected [0,1], got {result}"
    print("Test 5 Passed")

    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
