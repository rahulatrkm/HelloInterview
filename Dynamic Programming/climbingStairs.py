"""
Climbing Stairs

You can climb a staircase by taking either 1 or 2 steps at a time. If there are 
n steps in the staircase, how many distinct ways are there to climb to the top step?

Example 1:
    Input: n = 3
    Output: 3
    Explanation: 1+1+1, 1+2, 2+1

Example 2:
    Input: n = 5
    Output: 8
    Explanation: 8 distinct ways to climb 5 steps.

Approach:
- This is the classic DP introduction problem
- Recurrence: dp[i] = dp[i-1] + dp[i-2] (take 1 step from i-1, or 2 steps from i-2)
- Base cases: dp[0] = 1, dp[1] = 1
- Can solve top-down (recursion + memoization) or bottom-up (iterative DP)
- Space can be optimized to O(1) since we only need the last two values

Time Complexity: O(n)
Space Complexity: O(1) with space optimization, O(n) with full DP array
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # Your code goes here
        # a, b = 1, 1
        # for _ in range(2, n+1):
        #     a, b = b, a + b
        # return b

        def dp(n):
            if n <= 1:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = dp(n-1) + dp(n-2)
            return memo[n]
        memo = {}
        return dp(n)
        

def run_tests():
    solution = Solution()

    # Test 1: Base case n=1
    result = solution.climbStairs(1)
    assert result == 1, f"Test 1 Failed: Expected 1, got {result}"
    print("Test 1 Passed")

    # Test 2: n=2
    result = solution.climbStairs(2)
    assert result == 2, f"Test 2 Failed: Expected 2, got {result}"
    print("Test 2 Passed")

    # Test 3: n=3
    result = solution.climbStairs(3)
    assert result == 3, f"Test 3 Failed: Expected 3, got {result}"
    print("Test 3 Passed")

    # Test 4: n=5
    result = solution.climbStairs(5)
    assert result == 8, f"Test 4 Failed: Expected 8, got {result}"
    print("Test 4 Passed")

    # Test 5: Larger n=10
    result = solution.climbStairs(10)
    assert result == 89, f"Test 5 Failed: Expected 89, got {result}"
    print("Test 5 Passed")

    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
