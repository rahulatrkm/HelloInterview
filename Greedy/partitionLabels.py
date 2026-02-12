"""
Partition Labels
https://www.hellointerview.com/learn/code/greedy/partition-labels
https://leetcode.com/problems/partition-labels

Description:
    Given a string of lowercase letters, split it into as many segments as possible
    so that each character appears in exactly one segment. When you concatenate all
    segments, they should form the original string.
    Return a list of integers representing the length of each segment.

Examples:
    Input: s = "abacbcdd"
    Output: [6, 2]
    Explanation: 'a' at 0,2; 'b' at 1,4; 'c' at 3,5; 'd' at 6,7.
                 Partition into "abacbc" (6) and "dd" (2).

    Input: s = "eccbbbbdec"
    Output: [10]
    Explanation: All characters are interleaved, entire string must be one segment.

Approach:
    - Record the last occurrence of each character
    - Iterate through string, expanding partition end to max last occurrence
    - When current index == partition end, a partition is complete

Time Complexity: O(n)
Space Complexity: O(1) - at most 26 characters
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {c: i for i, c in enumerate(s)}
        partitions = []
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, last_occurrence[c])
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1
        return partitions


if __name__ == "__main__":
    sol = Solution()

    assert sol.partitionLabels("abacbcdd") == [6, 2]
    assert sol.partitionLabels("eccbbbbdec") == [10]
    assert sol.partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert sol.partitionLabels("a") == [1]
    assert sol.partitionLabels("abc") == [1, 1, 1]

    print("All tests passed!")
