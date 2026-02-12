"""
Gas Station
https://www.hellointerview.com/learn/code/greedy/gas-station
https://leetcode.com/problems/gas-station

Description:
    There are n gas stations along a circular route. You are given two integer arrays:
    - gas[i] is the amount of gas available at station i
    - cost[i] is the amount of gas needed to travel from station i to station i+1

    You start with an empty tank at one of the gas stations. Return the starting
    station's index if you can travel around the circuit once in the clockwise
    direction, otherwise return -1. If a solution exists, it is guaranteed to be unique.

Examples:
    Input: gas = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2]
    Output: 3
    Explanation: Start at station 3 (gas=4). Travel 3->4->0->1->2->3 completing the circuit.

    Input: gas = [2, 3, 4], cost = [3, 4, 3]
    Output: -1
    Explanation: No starting station allows completing the circuit.

Approach:
    - If total gas < total cost, no solution exists
    - Track current tank; if it goes negative, reset start to next station
    - The greedy insight: if we can't reach station j from station i,
      then no station between i and j can be the start either

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tot = cur = 0
        start = 0
        for i in range(len(gas)):
            tot += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:
                start = i + 1
                cur = 0
        return start if tot >= 0 else -1


if __name__ == "__main__":
    s = Solution()

    assert s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert s.canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1
    assert s.canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]) == 4
    assert s.canCompleteCircuit([3], [3]) == 0

    print("All tests passed!")
