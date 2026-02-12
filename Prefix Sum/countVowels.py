"""
Count Vowels in Substrings
https://www.hellointerview.com/learn/code/prefix-sum/count-vowels
https://leetcode.com/problems/count-vowel-strings-in-ranges

Description:
    Write a function to efficiently count vowels within specified substrings of a
    given string. The substrings are given as a list of queries [left, right] pairs,
    corresponding to word[left:right+1]. Return a list of integers where each integer
    represents the vowel count for the corresponding query. The input string contains
    only lowercase letters.

Examples:
    Input: word = "prefixsum", queries = [[0, 2], [1, 4], [3, 5]]
    Output: [1, 2, 1]
    Explanation:
        word[0:3] -> "pre" contains 1 vowel
        word[1:5] -> "refi" contains 2 vowels
        word[3:6] -> "fix" contains 1 vowel

Approach:
    - Build a prefix sum array where prefix[i] = number of vowels in word[0:i]
    - For each query [left, right], answer = prefix[right+1] - prefix[left]

Time Complexity: O(N + Q) where N = len(word), Q = number of queries
Space Complexity: O(N + Q)
"""

from typing import List


class Solution:
    def vowelStrings(self, word: str, queries: List[List[int]]) -> List[int]:
        pre_cnt = [0] * (len(word) + 1)
        vowels = set('aeiou')
        for i in range(len(word)):
            pre_cnt[i + 1] = pre_cnt[i] + (1 if word[i] in vowels else 0)
        res = []
        for left, right in queries:
            res.append(pre_cnt[right + 1] - pre_cnt[left])
        return res


if __name__ == "__main__":
    s = Solution()

    assert s.vowelStrings("prefixsum", [[0, 2], [1, 4], [3, 5]]) == [1, 2, 1]
    assert s.vowelStrings("aeiou", [[0, 4]]) == [5]
    assert s.vowelStrings("bcdfg", [[0, 4], [1, 3]]) == [0, 0]
    assert s.vowelStrings("picture", [[0, 4], [1, 4], [0, 6]]) == [2, 2, 3]
    assert s.vowelStrings("a", [[0, 0]]) == [1]

    print("All tests passed!")
