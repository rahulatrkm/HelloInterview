"""
Assign Cookies
https://www.hellointerview.com/learn/code/greedy/overview
https://leetcode.com/problems/assign-cookies

Description:
    You are given two integer arrays:
    - greeds (of size n), where each element represents the minimum size of a cookie
      that a child needs to be satisfied.
    - cookies (of size m), where each element represents the size of a cookie.

    Your task is to assign cookies to children such that as many children as possible
    are satisfied. A child is satisfied if the cookie they receive is equal to or greater
    than their greed factor. Each child can receive at most one cookie, and each cookie
    can be given to only one child. Return the maximum number of children that can be satisfied.

Examples:
    Input: greeds = [1, 2, 3], cookies = [1, 1]
    Output: 1

    Input: greeds = [1, 2], cookies = [1, 2, 3]
    Output: 2

Approach:
    - Sort both arrays
    - Use two pointers to greedily assign the smallest cookie that satisfies each child
    - If cookie >= greed, assign it and move both pointers; otherwise try next cookie

Time Complexity: O(n log n + m log m)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def findContentChildren(self, greeds: List[int], cookies: List[int]) -> int:
        greeds.sort()
        cookies.sort()
        i = j = 0
        satisfied = 0
        while i < len(greeds) and j < len(cookies):
            if cookies[j] >= greeds[i]:
                satisfied += 1
                i += 1
            j += 1
        return satisfied


if __name__ == "__main__":
    s = Solution()

    assert s.findContentChildren([1, 2, 3], [1, 1]) == 1
    assert s.findContentChildren([1, 2], [1, 2, 3]) == 2
    assert s.findContentChildren([], [1, 2]) == 0
    assert s.findContentChildren([1, 2], []) == 0
    assert s.findContentChildren([1, 1, 1], [1, 1, 1]) == 3

    print("All tests passed!")
