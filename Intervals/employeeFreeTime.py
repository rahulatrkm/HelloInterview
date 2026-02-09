"""
Employee Free Time
https://www.hellointerview.com/learn/code/intervals/employee-free-time

DESCRIPTION (inspired by Leetcode 759):
Write a function to find the common free time for all employees from a list 
called schedule. Each employee's schedule is represented by a list of 
non-overlapping intervals sorted by start times. The function should return 
a list of finite, non-zero length intervals where all employees are free, 
also sorted in order.

Example 1:
Input: schedule = [[[2,4],[7,10]],[[1,5]],[[6,9]]]
Output: [[5,6]]
Explanation: The three employees collectively have only one common free time 
interval, which is from 5 to 6.

Example 2:
Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]

Approach:
- Phase 1: Flatten all employee intervals into one list, sort by start time
- Phase 2: Merge overlapping intervals
- Phase 3: Gaps between merged intervals = free times
- O(n log n) time, O(n) space
"""

from typing import List
from collections import defaultdict


class Solution:
    def employeeFreeTime(self, schedule: List[List[List[int]]]) -> List[List[int]]:
        merged_sched = defaultdict(int)
        
        for table in schedule:
            for st, en in table:
                merged_sched[st] += 1
                merged_sched[en] -= 1
        
        ans = []
        sor_time = sorted(merged_sched.keys())
        curr = 0
        for i,t in enumerate(sor_time):
            curr += merged_sched[t]
            if curr == 0 and i+1 < len(sor_time):
                ans.append([t, sor_time[i+1]])
        return ans


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[[2, 4], [7, 10]], [[1, 5]], [[6, 9]]], [[5, 6]]),
        ([[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]], [[5, 6], [7, 9]]),
        ([[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]], [[3, 4]]),
        ([[[1, 3]], [[3, 5]], [[5, 7]]], []),
        ([[[0, 2]], [[4, 6]], [[8, 10]]], [[2, 4], [6, 8]]),
    ]

    sol = Solution()
    for i, (schedule, expected) in enumerate(test_cases):
        result = sol.employeeFreeTime(schedule)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | Output: {result} | Expected: {expected}")
