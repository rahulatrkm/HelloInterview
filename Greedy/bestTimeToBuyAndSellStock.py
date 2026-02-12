"""
Best Time to Buy and Sell Stock
https://www.hellointerview.com/learn/code/greedy/best-time-to-buy-and-sell-stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock

Description:
    You are given an array prices where prices[i] is the price of a given stock on
    the ith day. You want to maximize your profit by choosing a single day to buy
    one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot
    achieve any profit, return 0.

Examples:
    Input: prices = [7, 1, 5, 3, 6, 4]
    Output: 5
    Explanation: Buy on day 2 (price=1) and sell on day 5 (price=6), profit = 6-1 = 5.

    Input: prices = [7, 6, 4, 3, 1]
    Output: 0
    Explanation: No profitable transaction is possible.

Approach:
    - Track the minimum price seen so far
    - At each step, compute profit = current price - min price
    - Update max profit accordingly

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


if __name__ == "__main__":
    s = Solution()

    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
    assert s.maxProfit([1, 2]) == 1
    assert s.maxProfit([2, 1]) == 0
    assert s.maxProfit([1]) == 0

    print("All tests passed!")
