"""
Insert Interval
https://www.hellointerview.com/learn/code/intervals/insert-interval

DESCRIPTION (inspired by Leetcode 57):
Given a list of non-overlapping intervals sorted by their starting points, 
and a new interval newInterval, write a function to insert newInterval into 
the list. The function should ensure that after insertion, the list remains 
sorted without any overlapping intervals, merging them if needed.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Explanation: [2,5] overlaps with [1,3], merged into [1,5].

Example 2:
Input: intervals = [[1,3],[4,6],[6,7],[8,10],[11,15]], newInterval = [5,8]
Output: [[1,3],[4,10],[11,15]]
Explanation: [5,8] overlaps with [4,6],[6,7],[8,10], merged into [4,10].

Approach (3 Phases):
- Phase 1: Add all intervals ending before newInterval starts
- Phase 2: Merge all intervals overlapping with newInterval
- Phase 3: Add all remaining intervals
- O(n) time, O(n) space
"""

from typing import List


class Solution:
    def insertIntervals(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        idx = 0
        n = len(intervals)
        while idx < n and intervals[idx][1] < newInterval[0]:
            ans.append(intervals[idx])
            idx += 1

        while idx < n and intervals[idx][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[idx][0])
            newInterval[1] = max(newInterval[1], intervals[idx][1])
            idx += 1
        ans.append(newInterval)

        while idx < n:
            ans.append(intervals[idx])
            idx += 1
            
        return ans


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        ([[1, 3], [4, 6], [6, 7], [8, 10], [11, 15]], [5, 8], [[1, 3], [4, 10], [11, 15]]),
        ([], [2, 5], [[2, 5]]),
        ([[1, 5]], [2, 3], [[1, 5]]),
        ([[1, 5]], [6, 8], [[1, 5], [6, 8]]),
        ([[3, 5], [8, 10]], [1, 2], [[1, 2], [3, 5], [8, 10]]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
    ]

    sol = Solution()
    for i, (intervals, newInterval, expected) in enumerate(test_cases):
        result = sol.insertIntervals([iv[:] for iv in intervals], newInterval[:])
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Output: {result} | Expected: {expected}")
