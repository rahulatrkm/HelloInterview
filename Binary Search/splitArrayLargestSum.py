"""
Split Array Largest Sum
https://www.hellointerview.com/learn/code/binary-search/split-array-largest-sum

You are given an array nums and an integer k. nums represents the weights of n
consecutive tasks while k represents the number of workers. Tasks are assigned to
the workers as contiguous blocks.

Your goal is to distribute the work so that the heaviest workload (sum of task
weights for any single worker) is as small as possible.

Return the minimum possible value of the maximum workload.

Example 1:
  Input: nums = [4, 8, 15, 7, 3], k = 3
  Output: 15
  Explanation: One optimal split is [4,8] (sum=12), [15] (sum=15), [7,3] (sum=10).
  The maximum workload among workers is 15.

Example 2:
  Input: nums = [6, 3, 9, 2, 1, 8], k = 2
  Output: 18
  Explanation: Split into [6,3,9] (sum=18) and [2,1,8] (sum=11).

Approach:
- Binary search on the answer (max workload)
- Search space: max(nums) to sum(nums)
  - Lower bound: at minimum, the largest single task must be assigned
  - Upper bound: one worker does everything
- Feasibility check: can we split into <= k groups where each group sum <= mid?
  - Greedily assign tasks to current worker until adding next task exceeds mid
  - Then start a new worker
- If feasible → try smaller max (right = mid)
- If not feasible → need larger max (left = mid + 1)

Time: O(n * log(sum(nums) - max(nums)))
Space: O(1)
"""

from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def ispossible(max_task):
            worker_cnt = 0
            curr_task = 0
            for num in nums:
                curr_task += num
                if curr_task > max_task:
                    worker_cnt += 1
                    curr_task = num
            if curr_task:
                worker_cnt += 1
            return worker_cnt <= k

        l, r = max(nums), sum(nums)
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
    assert sol.splitArray([4, 8, 15, 7, 3], 3) == 15, \
        f"Test 1 failed: got {sol.splitArray([4, 8, 15, 7, 3], 3)}"
    print("Test 1 passed ✓")

    # Test 2: Two workers
    assert sol.splitArray([6, 3, 9, 2, 1, 8], 2) == 18, \
        f"Test 2 failed: got {sol.splitArray([6, 3, 9, 2, 1, 8], 2)}"
    print("Test 2 passed ✓")

    # Test 3: k = 1 (one worker does all)
    assert sol.splitArray([7, 2, 5, 10, 8], 1) == 32, \
        f"Test 3 failed: got {sol.splitArray([7, 2, 5, 10, 8], 1)}"
    print("Test 3 passed ✓")

    # Test 4: k = len(nums) (each task to one worker)
    assert sol.splitArray([7, 2, 5, 10, 8], 5) == 10, \
        f"Test 4 failed: got {sol.splitArray([7, 2, 5, 10, 8], 5)}"
    print("Test 4 passed ✓")

    # Test 5: Single element
    assert sol.splitArray([10], 1) == 10, \
        f"Test 5 failed: got {sol.splitArray([10], 1)}"
    print("Test 5 passed ✓")

    # Test 6: Equal elements
    assert sol.splitArray([5, 5, 5, 5], 2) == 10, \
        f"Test 6 failed: got {sol.splitArray([5, 5, 5, 5], 2)}"
    print("Test 6 passed ✓")

    # Test 7: Two elements, two workers
    assert sol.splitArray([1, 4], 2) == 4, \
        f"Test 7 failed: got {sol.splitArray([1, 4], 2)}"
    print("Test 7 passed ✓")

    # Test 8: Larger case
    assert sol.splitArray([1, 2, 3, 4, 5], 2) == 9, \
        f"Test 8 failed: got {sol.splitArray([1, 2, 3, 4, 5], 2)}"
    print("Test 8 passed ✓")

    print("\nAll tests passed! ✓")
