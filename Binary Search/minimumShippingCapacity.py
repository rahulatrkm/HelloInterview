"""
Minimum Shipping Capacity
https://www.hellointerview.com/learn/code/binary-search/minimum-shipping-capacity

You're a logistics manager preparing to ship products from a warehouse. You have
quantities of different product types that need to be packed into shipping boxes.

Each product type must be packed separately (different types can't share boxes).
All boxes have the same capacity. If a product has more items than fit in one box,
use multiple boxes.

Given an array of product quantities and a maximum number of boxes available,
find the minimum box capacity needed to ship all products within the box limit.

Example 1:
  Input: quantities = [1, 2, 5, 9], maxBoxes = 6
  Output: 5
  Explanation: With capacity 5: ceil(1/5)+ceil(2/5)+ceil(5/5)+ceil(9/5)
               = 1+1+1+2 = 5 boxes, fits within 6.

Example 2:
  Input: quantities = [3, 6, 7, 11], maxBoxes = 8
  Output: 4
  Explanation: With capacity 4: ceil(3/4)+ceil(6/4)+ceil(7/4)+ceil(11/4)
               = 1+2+2+3 = 8 boxes, exactly meets the limit.

Approach:
- Binary search on the answer (box capacity)
- Search space: 1 to max(quantities)
- Feasibility check: for a given capacity, count total boxes needed
  - boxes_needed = sum(ceil(q / capacity)) for each quantity q
  - Use ceiling division: (q + capacity - 1) // capacity
- If boxes_needed <= maxBoxes → capacity sufficient, try smaller → right = mid
- Else → need bigger capacity → left = mid + 1

Time: O(n * log(max(quantities)))
Space: O(1)
"""

from typing import List

class Solution:
    def minimumCapacity(self, quantities: List[int], maxBoxes: int) -> int:
        def ispossible(cap):
            cnt = 0
            for quanity in quantities:
                cnt += (quanity+cap-1)//cap
                if cnt > maxBoxes:
                    return False
            return True

        l, r = 1, sum(quantities)
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
    assert sol.minimumCapacity([1, 2, 5, 9], 6) == 5, \
        f"Test 1 failed: got {sol.minimumCapacity([1, 2, 5, 9], 6)}"
    print("Test 1 passed ✓")

    # Test 2: Exact fit
    assert sol.minimumCapacity([3, 6, 7, 11], 8) == 4, \
        f"Test 2 failed: got {sol.minimumCapacity([3, 6, 7, 11], 8)}"
    print("Test 2 passed ✓")

    # Test 3: One box per product (capacity = max)
    assert sol.minimumCapacity([4, 8, 3], 3) == 8, \
        f"Test 3 failed: got {sol.minimumCapacity([4, 8, 3], 3)}"
    print("Test 3 passed ✓")

    # Test 4: Single product
    assert sol.minimumCapacity([10], 3) == 4, \
        f"Test 4 failed: got {sol.minimumCapacity([10], 3)}"
    print("Test 4 passed ✓")

    # Test 5: Capacity 1 (unlimited boxes)
    assert sol.minimumCapacity([2, 3, 4], 100) == 1, \
        f"Test 5 failed: got {sol.minimumCapacity([2, 3, 4], 100)}"
    print("Test 5 passed ✓")

    # Test 6: All same quantities
    assert sol.minimumCapacity([6, 6, 6], 6) == 3, \
        f"Test 6 failed: got {sol.minimumCapacity([6, 6, 6], 6)}"
    print("Test 6 passed ✓")

    # Test 7: Large quantity, few boxes
    assert sol.minimumCapacity([1, 2, 3, 100], 5) == 50, \
        f"Test 7 failed: got {sol.minimumCapacity([1, 2, 3, 100], 5)}"
    print("Test 7 passed ✓")

    print("\nAll tests passed! ✓")
