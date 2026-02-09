"""
Max Points You Can Obtain From Cards
https://www.hellointerview.com/learn/code/sliding-window/maximum-points-you-can-obtain-from-cards

DESCRIPTION (inspired by Leetcode 1423):
Given an array of integers representing card values, write a function to
calculate the maximum score you can achieve by picking exactly k cards.

You must pick cards in order from either end. You can take some cards from 
the beginning, then switch to taking cards from the end, but you cannot 
skip cards or pick from the middle.

Constraints: 1 <= k <= cards.length

Example 1:
Input: cards = [2, 11, 4, 5, 3, 9, 2], k = 3
Output: 17
Explanation:
  First 3 cards: 2 + 11 + 4 = 17
  Last 3 cards: 3 + 9 + 2 = 14
  First 1 + last 2: 2 + 9 + 2 = 13
  First 2 + last 1: 2 + 11 + 2 = 15
  Maximum score is 17.

Example 2:
Input: cards = [1, 100, 10, 0, 4, 5, 6], k = 3
Output: 111
Explanation: Take the first three cards: 1 + 100 + 10 = 111.

Approach:
- Picking k cards from ends = leaving (n-k) consecutive cards in the middle
- Use a fixed-length sliding window of size (n-k) to find the minimum sum
- Answer = total_sum - min_window_sum
- O(n) time, O(1) space
"""

from typing import List


class Solution:
    def maxScore(self, cards: List[int], k: int):
        curr_points = ans = sum(cards[-k:])
        for i in range(k):
            curr_points += cards[i]-cards[-k+i]
            ans = max(ans, curr_points)
        return ans

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([2, 11, 4, 5, 3, 9, 2], 3, 17),
        ([1, 100, 10, 0, 4, 5, 6], 3, 111),
        ([9, 7, 7, 9, 7, 7, 9], 7, 55),
        ([1, 2, 3, 4, 5], 1, 5),
        ([1, 2, 3, 4, 5], 5, 15),
        ([100, 1, 1, 1, 100], 2, 200),
    ]

    sol = Solution()
    for i, (cards, k, expected) in enumerate(test_cases):
        result = sol.maxScore(cards, k)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} | cards={cards}, k={k} | Output: {result} | Expected: {expected}")
