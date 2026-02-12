"""
Jump Game
https://www.hellointerview.com/learn/code/greedy/jump-game
https://leetcode.com/problems/jump-game

Description:
    Given an integer array nums, you are initially positioned at the first index.
    Each element represents the maximum jump length from that position.
    Return true if you can reach the last index, false otherwise.

Examples:
    Input: nums = [1, 3, 0, 1, 4]
    Output: True
    Explanation: Jump 0->1, then 1->4 (last index).

    Input: nums = [3, 2, 1, 0, 4]
    Output: False
    Explanation: You always end up at index 3 where nums[3]=0, stuck.

Approach:
    - Track max_reach (farthest index reachable so far)
    - Iterate through array: if i > max_reach, we're stuck -> return False
    - Update max_reach = max(max_reach, i + nums[i])
    - If we finish the loop, return True

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)
        return True


if __name__ == "__main__":
    s = Solution()

    assert s.canJump([1, 3, 0, 1, 4]) == True
    assert s.canJump([3, 2, 1, 0, 4]) == False
    assert s.canJump([2, 3, 1, 1, 4]) == True
    assert s.canJump([0]) == True
    assert s.canJump([0, 1]) == False

    print("All tests passed!")
