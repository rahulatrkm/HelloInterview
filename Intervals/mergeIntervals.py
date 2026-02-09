"""
Merge Intervals
https://www.hellointerview.com/learn/code/intervals/merge-intervals

DESCRIPTION (inspired by Leetcode 56):
Write a function to consolidate overlapping intervals within a given array 
intervals, where each interval intervals[i] consists of a start time and 
an end time.

Two intervals are considered overlapping if they share any common time, 
including if one ends exactly when another begins (e.g., [1,4] and [4,5] 
overlap and should be merged into [1,5]).

The function should return an array of the merged intervals so that no two 
intervals overlap.

Example 1:
Input: intervals = [[3,5],[1,4],[7,9],[6,8]]
Output: [[1,5],[6,9]]
Explanation: [3,5] and [1,4] merge into [1,5]. [7,9] and [6,8] merge into [6,9].

Example 2:
Input: intervals = [[1,5],[3,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Approach:
- Sort intervals by start time
- Iterate and merge overlapping intervals into a result list
- O(n log n) time, O(n) space
"""

from typing import List


class Solution:
    def mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        sorted_intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        for st, en in sorted_intervals:
            if not ans or st > ans[-1][1]:
                ans.append([st, en])
            else:
                ans[-1][1] = max(ans[-1][1], en)
        return ans


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[3, 5], [1, 4], [7, 9], [6, 8]], [[1, 5], [6, 9]]),
        ([[1, 5], [3, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[1, 4], [0, 4]], [[0, 4]]),
        ([[1, 4], [2, 3]], [[1, 4]]),
        ([[1, 3]], [[1, 3]]),
        ([[1, 3], [5, 7], [9, 11]], [[1, 3], [5, 7], [9, 11]]),
    ]

    sol = Solution()
    for i, (intervals, expected) in enumerate(test_cases):
        result = sol.mergeIntervals([iv[:] for iv in intervals])
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Input: {intervals} | Output: {result} | Expected: {expected}")
