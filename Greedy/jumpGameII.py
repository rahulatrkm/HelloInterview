"""
Jump Game II
https://www.hellointerview.com/learn/code/greedy/jump-game-ii
https://leetcode.com/problems/jump-game-ii

Description:
    You are given an integer array nums. You start at the first index and each
    element represents the maximum jump length from that position. Your goal is
    to reach the last index in the minimum number of jumps. You may assume you
    can always reach the last index.

Examples:
    Input: nums = [3, 4, 2, 1, 2, 1]
    Output: 2
    Explanation: Jump 0->1, then 1->5. Total = 2 jumps.

    Input: nums = [1, 2, 1, 1, 1]
    Output: 3
    Explanation: Jump 0->1, 1->3, 3->4. Total = 3 jumps.

Approach:
    - BFS-like level traversal: treat reachable indices as levels
    - Track current level end and farthest reachable
    - When we reach the current level end, increment jumps and set new end = farthest

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        cnt = 0
        end = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                cnt += 1
                end = farthest
        return cnt


if __name__ == "__main__":
    s = Solution()

    assert s.jump([3, 4, 2, 1, 2, 1]) == 2
    assert s.jump([1, 2, 1, 1, 1]) == 3
    assert s.jump([2, 3, 1, 1, 4]) == 2
    assert s.jump([1]) == 0
    assert s.jump([1, 2, 3]) == 2

    print("All tests passed!")
