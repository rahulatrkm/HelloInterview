"""
Maximum Sum of Subarrays of Size K
https://www.hellointerview.com/learn/code/sliding-window/maximum-sum-of-subarrays-of-size-k

DESCRIPTION:
Given an array of integers nums and an integer k, find the maximum sum 
of any contiguous subarray of size k.

Example 1:
Input: nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: The subarray with the maximum sum is [5, 1, 3] with a sum of 9.

Approach (Fixed-Length Sliding Window):
- Maintain a running sum of the current window
- Slide the window by adding the new element and removing the leftmost
- Update max_sum whenever window size == k
- O(n) time, O(1) space
"""

from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int):
        n = len(nums)
        curr_sum = sum(nums[:k])
        ans = curr_sum
        for i in range(k, n):
            curr_sum += nums[i]-nums[i-k]
            ans = max(ans, curr_sum)
        return ans

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([2, 1, 5, 1, 3, 2], 3, 9),
        ([1, 2, 3, 4, 5], 2, 9),
        ([5], 1, 5),
        ([1, 1, 1, 1, 1], 3, 3),
        ([10, -2, 3, -1, 5], 2, 8),
        ([-1, -2, -3, -4], 2, -3),
    ]

    sol = Solution()
    for i, (nums, k, expected) in enumerate(test_cases):
        result = sol.maxSum(nums, k)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | nums={nums}, k={k} | Output: {result} | Expected: {expected}")
