"""
Apple Harvest (Koko Eating Bananas)
https://www.hellointerview.com/learn/code/binary-search/apple-harvest

Bobby has an orchard of apple trees, and each tree has a certain number of apples on it.
Bobby wants to collect all the apples by the end of the day by collecting a fixed number
of apples per hour. He can only harvest apples from one tree per hour - if he finishes
collecting apples from a tree before the hour is up, he must wait until the next hour to
move to the next tree.

Write a function to determine the slowest rate of apples Bobby can harvest per hour to
finish the job in at most 'h' hours.

Example 1:
  Input: apples = [3, 6, 7], h = 8
  Output: 3

Example 2:
  Input: apples = [25, 9, 23, 8, 3], h = 5
  Output: 25

Approach:
- Binary search on the answer (harvest rate)
- Search space: 1 to max(apples)
- For each candidate rate, check if total hours needed <= h
- Ceiling division: (apples[i] + rate - 1) // rate
- If time_taken(mid) > h, rate too slow → left = mid + 1
- Else rate is sufficient, try slower → right = mid

Time: O(n * log(max(apples)))
Space: O(1)
"""

from typing import List

class Solution:
    def minHarvestRate(self, apples: List[int], h: int) -> int:
        if h < len(apples):
            return -1  # Not enough hours to harvest all trees
        
        def ispossible(rate):
            hrs = 0
            for apple in apples:
                hrs += (apple + rate - 1) // rate  # ceiling division
                if hrs > h:
                    return False
            return True

        l, r = 1, max(apples)
        while l < r:
            m = (l+r)//2
            if ispossible(m):
                r = m
            else:
                l = m+1
        return l


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Basic case
    assert sol.minHarvestRate([3, 6, 7], 8) == 3, \
        f"Test 1 failed: got {sol.minHarvestRate([3, 6, 7], 8)}"
    print("Test 1 passed ✓")

    # Test 2: Each tree needs its own hour
    assert sol.minHarvestRate([25, 9, 23, 8, 3], 5) == 25, \
        f"Test 2 failed: got {sol.minHarvestRate([25, 9, 23, 8, 3], 5)}"
    print("Test 2 passed ✓")

    # Test 3: Plenty of time
    assert sol.minHarvestRate([3, 6, 7, 11], 8) == 4, \
        f"Test 3 failed: got {sol.minHarvestRate([3, 6, 7, 11], 8)}"
    print("Test 3 passed ✓")

    # Test 4: Single tree
    assert sol.minHarvestRate([10], 5) == 2, \
        f"Test 4 failed: got {sol.minHarvestRate([10], 5)}"
    print("Test 4 passed ✓")

    # Test 5: Rate = 1 (lots of time)
    assert sol.minHarvestRate([3, 6, 7], 100) == 1, \
        f"Test 5 failed: got {sol.minHarvestRate([3, 6, 7], 100)}"
    print("Test 5 passed ✓")

    # Test 6: Exact fit
    assert sol.minHarvestRate([30, 11, 23, 4, 20], 5) == 30, \
        f"Test 6 failed: got {sol.minHarvestRate([30, 11, 23, 4, 20], 5)}"
    print("Test 6 passed ✓")

    # Test 7: h equals number of trees (must eat each pile in 1 hour)
    assert sol.minHarvestRate([1, 1, 1], 3) == 1, \
        f"Test 7 failed: got {sol.minHarvestRate([1, 1, 1], 3)}"
    print("Test 7 passed ✓")

    print("\nAll tests passed! ✓")
