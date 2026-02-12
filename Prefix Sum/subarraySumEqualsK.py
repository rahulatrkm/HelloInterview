"""
Subarray Sum Equals K
https://www.hellointerview.com/learn/code/prefix-sum/subarray-sum-equals-k
https://leetcode.com/problems/subarray-sum-equals-k

Description:
    Write a function that returns the total number of contiguous subarrays within
    a given integer array whose elements sum up to a target K.

Examples:
    Input: nums = [3, 4, 7, 2, -3, 1, 4, 2], k = 7
    Output: 4
    Explanation: Subarrays that sum to 7: [3,4], [7], [7,2,-3,1], [1,4,2]

    Input: nums = [1, -1, 0], k = 0
    Output: 3
    Explanation: Subarrays that sum to 0: [1,-1], [0], [1,-1,0]

Approach:
    - Use a hashmap (prefix_counts) to store frequency of each prefix sum seen so far
    - Initialize with {0: 1} to handle subarrays starting at index 0
    - For each element, update running sum and check if (sum - k) exists in map
    - The count at prefix_counts[sum - k] gives number of subarrays ending here with sum k

Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        prefix_counts = {0: 1}
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if (curr_sum - k) in prefix_counts:
                ans += prefix_counts[curr_sum - k]
            prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1
        return ans


if __name__ == "__main__":
    s = Solution()

    assert s.subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4
    assert s.subarraySum([1, -1, 0], 0) == 3
    assert s.subarraySum([1, 1, 1], 2) == 2
    assert s.subarraySum([1], 1) == 1
    assert s.subarraySum([1], 0) == 0
    assert s.subarraySum([0, 0, 0], 0) == 6

    print("All tests passed!")
