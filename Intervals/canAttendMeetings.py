"""
Can Attend Meetings
https://www.hellointerview.com/learn/code/intervals/can-attend-meetings

DESCRIPTION (inspired by Leetcode 252):
Write a function to check if a person can attend all the meetings scheduled
without any time conflicts. Given an array intervals, where each element 
[s1, e1] represents a meeting starting at time s1 and ending at time e1, 
determine if there are any overlapping meetings. If there is no overlap 
between any meetings, return true; otherwise, return false.

Note that meetings ending and starting at the same time, such as (0,5) and 
(5,10), do not conflict.

Example 1:
Input: intervals = [[1,5],[3,9],[6,8]]
Output: false
Explanation: The meetings (1,5) and (3,9) overlap.

Example 2:
Input: intervals = [[10,12],[6,9],[13,15]]
Output: true
Explanation: There are no overlapping meetings.

Approach:
- Sort intervals by start time
- Check if any consecutive pair overlaps (start_i < end_{i-1})
- O(n log n) time, O(1) space
"""

from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        last = -float('inf')
        for st, en in intervals:
            if st < last:
                return False
            last = en
        return True


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([[1, 5], [3, 9], [6, 8]], False),
        ([[10, 12], [6, 9], [13, 15]], True),
        ([[2, 4], [9, 12], [6, 9], [13, 15]], True),
        ([[0, 5], [5, 10]], True),
        ([[1, 3], [2, 4]], False),
        ([[7, 10], [2, 4]], True),
        ([], True),
        ([[1, 5]], True),
    ]

    sol = Solution()
    for i, (intervals, expected) in enumerate(test_cases):
        result = sol.canAttendMeetings(intervals)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | intervals={intervals} | Output: {result} | Expected: {expected}")
