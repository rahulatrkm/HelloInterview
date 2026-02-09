"""
Fruit Into Baskets
https://www.hellointerview.com/learn/code/sliding-window/variable-length
(inspired by Leetcode 904)

DESCRIPTION:
Write a function to calculate the maximum number of fruits you can collect 
from an integer array fruits, where each element represents a type of fruit. 
You can start collecting fruits from any position in the array, but you must 
stop once you encounter a third distinct type of fruit. The goal is to find 
the longest subarray where at most two different types of fruits are collected.

Example 1:
Input: fruits = [3, 3, 2, 1, 2, 1, 0]
Output: 4
Explanation: We can pick up 4 fruits from the subarray [2, 1, 2, 1].

Example 2:
Input: fruits = [1, 2, 3, 2, 2]
Output: 4
Explanation: We can pick up 4 fruits from the subarray [2, 3, 2, 2].

Approach (Variable-Length Sliding Window):
- Use a dictionary to track fruit type counts in the current window
- Expand window by adding fruits[end]
- When len(state) > 2, contract from start until valid again
- Track max window length throughout
- O(n) time, O(1) space (state has at most 3 keys)
"""

from typing import List


class Solution:
    def fruitIntoBaskets(self, fruits: List[int]) -> int:
        ans = 0
        n = len(fruits)
        seen = {}
        st = 0
        for i in range(n):
            seen[fruits[i]] = seen.get(fruits[i], 0) + 1
            while len(seen) > 2:
                seen[fruits[st]] -= 1
                if seen[fruits[st]] == 0:
                    del seen[fruits[st]]
                st += 1
            ans = max(ans, i-st+1)
        return ans


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([3, 3, 2, 1, 2, 1, 0], 4),
        ([1, 2, 3, 2, 2], 4),
        ([1, 2, 1], 3),
        ([0, 1, 2, 2], 3),
        ([1, 1, 1, 1], 4),
        ([1], 1),
        ([1, 2], 2),
        ([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], 5),
    ]

    sol = Solution()
    for i, (fruits, expected) in enumerate(test_cases):
        result = sol.fruitIntoBaskets(fruits)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | fruits={fruits} | Output: {result} | Expected: {expected}")
