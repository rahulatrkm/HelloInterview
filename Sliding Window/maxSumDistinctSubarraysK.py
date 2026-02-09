"""
Max Sum of Distinct Subarrays of Length K
https://www.hellointerview.com/learn/code/sliding-window/maximum-sum-of-distinct-subarrays-with-length-k

DESCRIPTION (inspired by Leetcode 2461):
Given an integer array nums and an integer k, write a function to identify 
the highest possible sum of a subarray within nums, where the subarray meets 
the following criteria: its length is k, and all of its elements are unique.
If no such subarray exists, return 0.

Example 1:
Input: nums = [3, 2, 2, 3, 4, 6, 7, 7, -1], k = 4
Output: 20
Explanation: The subarrays of nums with length 4 are:
  [3, 2, 2, 3] - elements 3 and 2 are repeated
  [2, 2, 3, 4] - element 2 is repeated
  [2, 3, 4, 6] - meets requirements, sum = 15
  [3, 4, 6, 7] - meets requirements, sum = 20  ← maximum
  [4, 6, 7, 7] - element 7 is repeated
  [6, 7, 7, -1] - element 7 is repeated

Example 2:
Input: nums = [5, 5, 5, 5, 5], k = 3
Output: 0
Explanation: Every subarray of length 3 contains duplicate elements.

Approach (Fixed-Length Sliding Window + Dictionary):
- Use a dictionary to track element counts in the window
- Use curr_sum to track the running sum
- When window size == k, check if len(dict) == k (all distinct)
- If valid, update max_sum
- Contract window by removing leftmost element
- O(n) time, O(k) space
"""

from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int):
        ans = 0
        seen = {}
        st = i = 0
        curr_sum = 0
        n = len(nums)
        while i < n:
            curr_sum += nums[i]
            seen[nums[i]] = seen.get(nums[i], 0) + 1
            if i-st+1 == k:
                if len(seen) == k:
                    ans = max(ans, curr_sum)
                curr_sum -= nums[st]
                seen[nums[st]] -= 1
                if seen[nums[st]] == 0:
                    del seen[nums[st]]
                st += 1
            i += 1
        return ans



# Test cases
if __name__ == "__main__":
    test_cases = [
        ([3, 2, 2, 3, 4, 6, 7, 7, -1], 4, 20),
        ([5, 5, 5, 5, 5], 3, 0),
        ([1, 2, 3, 4, 5], 3, 12),
        ([1, 2, 3], 3, 6),
        ([9, 9, 9, 1, 2, 3], 3, 12),
        ([1, 1, 1, 2, 3, 1], 2, 5),
    ]

    sol = Solution()
    for i, (nums, k, expected) in enumerate(test_cases):
        result = sol.maxSum(nums, k)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | nums={nums}, k={k} | Output: {result} | Expected: {expected}")
