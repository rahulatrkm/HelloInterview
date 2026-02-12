"""
Prefix Matching
https://www.hellointerview.com/learn/code/trie/prefix-matching
https://leetcode.com/problems/counting-words-with-a-given-prefix

Description:
    Use a Trie to implement a prefix matching function.
    - match(prefix) returns a list of all words in the Trie that start with
      the given prefix. The words can be in any order.

    The creation of the Trie is already implemented for you.

Examples:
    Input: initialWords = ["apple", "app", "apartment", "ap", "apricot"], prefix = "app"
    Output: ["apple", "app"]

    Input: initialWords = ["ball", "bath", "bat", "batter"], prefix = "bat"
    Output: ["bat", "bath", "batter"]

Approach:
    1. Traverse trie to find the node corresponding to the prefix
    2. Perform DFS from that node to collect all words with that prefix
    3. If prefix not found, return empty list

Time Complexity: O(N + M) where N = prefix length, M = total chars in matching words
Space Complexity: O(M) for the output list
"""

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class Solution:
    def create_trie(self, words):
        # === DO NOT MODIFY ===
        self.root = TrieNode()
        for word in words:
            self.insert(word)

    def insert(self, word):
        # === DO NOT MODIFY ===
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    def match(self, prefix) -> List[str]:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        res = []

        def dfs(curr_node, path):
            if curr_node.isEndOfWord:
                res.append(prefix + path)
            for char, next_node in curr_node.children.items():
                dfs(next_node, path + char)

        dfs(node, "")
        return res


if __name__ == "__main__":
    s = Solution()

    # Test 1
    s.create_trie(["apple", "app", "apartment", "ap", "apricot"])
    result = s.match("app")
    assert sorted(result) == sorted(["apple", "app"])

    # Test 2
    s.create_trie(["ball", "bath", "bat", "batter"])
    result = s.match("bat")
    assert sorted(result) == sorted(["bat", "bath", "batter"])

    # Test 3
    s.create_trie(["apple", "app", "apartment"])
    result = s.match("xyz")
    assert result == []

    # Test 4
    s.create_trie(["apple", "app", "apartment"])
    result = s.match("ap")
    assert sorted(result) == sorted(["apple", "app", "apartment"])

    # Test 5
    s.create_trie(["a"])
    result = s.match("a")
    assert result == ["a"]

    print("All tests passed!")
