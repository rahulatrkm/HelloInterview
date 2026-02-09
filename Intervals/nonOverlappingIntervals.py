"""
Non-Overlapping Intervals
https://www.hellointerview.com/learn/code/intervals/non-overlapping-intervals

DESCRIPTION (inspired by Leetcode 435):
Write a function to return the minimum number of intervals that must be 
removed from a given array intervals, where intervals[i] consists of a 
starting point starti and an ending point endi, to ensure that the remaining 
intervals do not overlap.

Note: Intervals touching at a point are non-overlapping (e.g., [1,2] and [2,3]).

Example 1:
Input: intervals = [[1,3],[5,8],[4,10],[11,13]]
Output: 1
Explanation: Removing [4,10] leaves all other intervals non-overlapping.

Example 2:
Input: intervals = [[4,6],[11,17],[2,18],[7,10]]
Output: 1
Explanation: Removing [2,18] leaves all other intervals non-overlapping.

Approach (Greedy - Sort by End Time):
- Sort intervals by end time (earliest ending first)
- Greedily pick non-overlapping intervals
- Count of removed = total - count of non-overlapping
- O(n log n) time, O(1) space
"""

from typing import List


class Solution:
    def nonOverlappingIntervals(self, intervals: List[List[int]]) -> int:
        cnt = 0
        intervals.sort(key=lambda x: (x[1], x[0]))
        last = -float('inf')
        idx = 0
        n = len(intervals)
        while idx < n:
            if intervals[idx][0] < last:
                cnt += 1
            else:
                last = intervals[idx][1]
            idx += 1
        return cnt


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1, 3], [5, 8], [4, 10], [11, 13]], 1),
        ([[4, 6], [11, 17], [2, 18], [7, 10]], 1),
        ([[1, 2], [2, 3], [3, 4]], 0),
        ([[1, 2], [1, 2], [1, 2]], 2),
        ([[1, 100], [11, 22], [1, 11], [2, 12]], 2),
        ([], 0),
        ([[1, 2]], 0),
    ]

    sol = Solution()
    for i, (intervals, expected) in enumerate(test_cases):
        result = sol.nonOverlappingIntervals(intervals)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | intervals={intervals} | Output: {result} | Expected: {expected}")
