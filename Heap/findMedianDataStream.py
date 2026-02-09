"""
Find Median from Data Stream
https://www.hellointerview.com/learn/code/heap/find-median-from-data-stream

A live analytics dashboard starts with nums. New readings arrive in order via adds.
After each incoming value is inserted, return the current median of all readings
seen so far. If the count is even, the median is the average of the two middle values.

Example 1:
  Input: nums = [5, 2, 8], adds = [3, 10, 4]
  Output: [4, 5, 4.5]
  Explanation:
    After adding 3: [2, 3, 5, 8] → median = (3+5)/2 = 4
    After adding 10: [2, 3, 5, 8, 10] → median = 5
    After adding 4: [2, 3, 4, 5, 8, 10] → median = (4+5)/2 = 4.5

Approach:
- Use two heaps: max-heap (left half) and min-heap (right half)
- max_heap stores the smaller half (negate values for max-heap)
- min_heap stores the larger half
- Keep balanced: len(max_heap) == len(min_heap) or len(max_heap) == len(min_heap) + 1
- addNum: push to max_heap, then move max_heap root to min_heap,
  then rebalance if min_heap is larger
- findMedian: if odd total → max_heap root; if even → average of both roots

Time: O(log n) per addNum, O(1) per findMedian
Space: O(n)
"""

from typing import List
import heapq

class MedianFinder:
    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not self.left:
            self.left.append(-num)
            return None
        if len(self.left) == len(self.right):
            if self.right[0] < num:
                num = heapq.heappushpop(self.right, num)
            heapq.heappush(self.left, -num)
            return None
        num = -heapq.heappushpop(self.left, -num)
        heapq.heappush(self.right, num)


    def findMedian(self) -> float:
        if not self.left:
            return 0
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0])/2
        return -self.left[0]


if __name__ == "__main__":
    # Test 1: Example from problem
    mf = MedianFinder()
    for num in [5, 2, 8]:
        mf.addNum(num)
    results = []
    for num in [3, 10, 4]:
        mf.addNum(num)
        results.append(mf.findMedian())
    assert results == [4, 5, 4.5], f"Test 1 failed: got {results}"
    print("Test 1 passed ✓")

    # Test 2: Single element
    mf = MedianFinder()
    mf.addNum(1)
    assert mf.findMedian() == 1, f"Test 2 failed: got {mf.findMedian()}"
    print("Test 2 passed ✓")

    # Test 3: Two elements
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5, f"Test 3 failed: got {mf.findMedian()}"
    print("Test 3 passed ✓")

    # Test 4: Odd count
    mf = MedianFinder()
    for num in [3, 1, 5]:
        mf.addNum(num)
    assert mf.findMedian() == 3, f"Test 4 failed: got {mf.findMedian()}"
    print("Test 4 passed ✓")

    # Test 5: Sequential adds
    mf = MedianFinder()
    mf.addNum(6)
    assert mf.findMedian() == 6
    mf.addNum(10)
    assert mf.findMedian() == 8
    mf.addNum(2)
    assert mf.findMedian() == 6
    mf.addNum(6)
    assert mf.findMedian() == 6
    print("Test 5 passed ✓")

    # Test 6: Negative numbers
    mf = MedianFinder()
    for num in [-1, -2, -3]:
        mf.addNum(num)
    assert mf.findMedian() == -2, f"Test 6 failed: got {mf.findMedian()}"
    print("Test 6 passed ✓")

    # Test 7: Duplicates
    mf = MedianFinder()
    for num in [5, 5, 5, 5]:
        mf.addNum(num)
    assert mf.findMedian() == 5, f"Test 7 failed: got {mf.findMedian()}"
    print("Test 7 passed ✓")

    # Test 8: Large numbers
    mf = MedianFinder()
    mf.addNum(100000)
    mf.addNum(200000)
    mf.addNum(300000)
    assert mf.findMedian() == 200000, f"Test 8 failed: got {mf.findMedian()}"
    print("Test 8 passed ✓")

    # Test 9: Zero values
    mf = MedianFinder()
    mf.addNum(0)
    mf.addNum(0)
    mf.addNum(0)
    assert mf.findMedian() == 0, f"Test 9 failed: got {mf.findMedian()}"
    print("Test 9 passed ✓")

    # Test 10: Descending order
    mf = MedianFinder()
    for num in [10, 8, 6, 4, 2]:
        mf.addNum(num)
    assert mf.findMedian() == 6, f"Test 10 failed: got {mf.findMedian()}"
    print("Test 10 passed ✓")

    # Test 11: Ascending order
    mf = MedianFinder()
    for num in [1, 2, 3, 4, 5]:
        mf.addNum(num)
    assert mf.findMedian() == 3, f"Test 11 failed: got {mf.findMedian()}"
    print("Test 11 passed ✓")

    # Test 12: Mixed positive, negative, and zero
    mf = MedianFinder()
    for num in [-5, 0, 5, -10, 10]:
        mf.addNum(num)
    assert mf.findMedian() == 0, f"Test 12 failed: got {mf.findMedian()}"
    print("Test 12 passed ✓")

    # Test 13: Very small negative numbers
    mf = MedianFinder()
    mf.addNum(-100000)
    mf.addNum(-200000)
    assert mf.findMedian() == -150000, f"Test 13 failed: got {mf.findMedian()}"
    print("Test 13 passed ✓")

    # Test 14: Alternating small and large
    mf = MedianFinder()
    for num in [1, 100, 2, 99, 3]:
        mf.addNum(num)
    assert mf.findMedian() == 3, f"Test 14 failed: got {mf.findMedian()}"
    print("Test 14 passed ✓")

    # Test 15: Many duplicates with different values
    mf = MedianFinder()
    for num in [1, 1, 1, 2, 2, 2]:
        mf.addNum(num)
    assert mf.findMedian() == 1.5, f"Test 15 failed: got {mf.findMedian()}"
    print("Test 15 passed ✓")

    print("\nAll tests passed! ✓")
