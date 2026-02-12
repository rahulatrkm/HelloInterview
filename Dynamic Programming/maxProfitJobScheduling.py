"""
Maximum Profit in Job Scheduling

Given three arrays starts, ends, and profits representing jobs (start time, end
time, and profit), schedule non-overlapping jobs to maximize total profit. You
can only work on one job at a time and must finish a job before starting another.

Example 1:
    Input: starts = [1, 3, 6, 10], ends = [4, 5, 10, 12], profits = [20, 20, 100, 70]
    Output: 190
    Explanation: Schedule jobs [1,4,20], [6,10,100], [10,12,70] → 20+100+70=190.

Example 2:
    Input: starts = [1, 2, 3, 3], ends = [3, 4, 5, 6], profits = [50, 10, 40, 70]
    Output: 120
    Explanation: Schedule jobs [1,3,50] + [3,6,70] = 120.

Approach:
- Sort jobs by end time
- dp[i] = max profit from first i jobs (sorted by end time)
- For each job i, use binary search to find the latest non-overlapping job
- Recurrence: dp[i] = max(dp[i-1], dp[num_jobs] + profit)
  - Skip: dp[i-1]
  - Take: dp[latest_non_overlapping] + current profit

Time Complexity: O(n log n) — sorting + binary search per job
Space Complexity: O(n) for dp array
"""

from bisect import bisect_right
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Your code goes here
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        ends = [j[1] for j in jobs]
        dp = [0] * (len(jobs) + 1)
        for i in range(1, len(jobs) + 1):
            st, en, p = jobs[i - 1]
            # Find the number of jobs whose end time <= current start time
            num_jobs = bisect_right(ends, st)
            dp[i] = max(dp[i - 1], dp[num_jobs] + p)
        return dp[-1]


def run_tests():
    solution = Solution()

    # Test 1: Standard example
    result = solution.jobScheduling([1, 3, 6, 10], [4, 5, 10, 12], [20, 20, 100, 70])
    assert result == 190, f"Test 1 Failed: Expected 190, got {result}"
    print("Test 1 Passed")

    # Test 2: Overlapping jobs, pick best combo
    result = solution.jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70])
    assert result == 120, f"Test 2 Failed: Expected 120, got {result}"
    print("Test 2 Passed")

    # Test 3: Single job
    result = solution.jobScheduling([1], [3], [50])
    assert result == 50, f"Test 3 Failed: Expected 50, got {result}"
    print("Test 3 Passed")

    # Test 4: All overlapping — pick highest profit
    result = solution.jobScheduling([1, 1, 1], [5, 5, 5], [10, 20, 30])
    assert result == 30, f"Test 4 Failed: Expected 30, got {result}"
    print("Test 4 Passed")

    # Test 5: No overlap — take all
    result = solution.jobScheduling([1, 3, 5], [2, 4, 6], [10, 20, 30])
    assert result == 60, f"Test 5 Failed: Expected 60, got {result}"
    print("Test 5 Passed")

    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
