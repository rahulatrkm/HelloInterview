"""
Palindrome Partitioning

Given a string s, split it into segments where each segment is a palindrome 
(reads the same forwards and backwards).

Return all possible ways to partition the string into palindromic segments.

Constraints:
- 1 <= s.length <= 16
- s contains only lowercase English letters

Example 1:
    Input: s = "noon"
    Output: [["n","o","o","n"], ["n","oo","n"], ["noon"]]
    Explanation:
    - ["n","o","o","n"] - All single characters are palindromes
    - ["n","oo","n"] - "oo" is a palindrome in the middle
    - ["noon"] - The entire word is a palindrome

Example 2:
    Input: s = "civic"
    Output: [["c","i","v","i","c"], ["c","ivi","c"], ["civic"]]

Approach:
- Use backtracking to try all possible partitions
- At each position, try all substrings starting from that position
- If the substring is a palindrome, add it to the path and recurse on the remainder
- Base case: when start index == len(s), all parts are palindromes, add path to result
- Backtrack by popping the last partition

Time Complexity: O(n * 2^n) where n is the length of the string
Space Complexity: O(n) for recursion depth
"""

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Your code goes here
        pass


def run_tests():
    solution = Solution()
    
    # Test 1: "noon"
    result = solution.partition("noon")
    expected = [["n","o","o","n"], ["n","oo","n"], ["noon"]]
    assert sorted([tuple(p) for p in result]) == sorted([tuple(p) for p in expected]), \
        f"Test 1 Failed: Expected {expected}, got {result}"
    print("Test 1 Passed")
    
    # Test 2: "civic"
    result = solution.partition("civic")
    expected = [["c","i","v","i","c"], ["c","ivi","c"], ["civic"]]
    assert sorted([tuple(p) for p in result]) == sorted([tuple(p) for p in expected]), \
        f"Test 2 Failed: Expected {expected}, got {result}"
    print("Test 2 Passed")
    
    # Test 3: Single character
    result = solution.partition("a")
    expected = [["a"]]
    assert result == expected, f"Test 3 Failed: Expected {expected}, got {result}"
    print("Test 3 Passed")
    
    # Test 4: Two same characters
    result = solution.partition("aa")
    expected = [["a", "a"], ["aa"]]
    assert sorted([tuple(p) for p in result]) == sorted([tuple(p) for p in expected]), \
        f"Test 4 Failed: Expected {expected}, got {result}"
    print("Test 4 Passed")
    
    # Test 5: No palindrome partitions beyond singles
    result = solution.partition("abc")
    expected = [["a", "b", "c"]]
    assert result == expected, f"Test 5 Failed: Expected {expected}, got {result}"
    print("Test 5 Passed")
    
    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
