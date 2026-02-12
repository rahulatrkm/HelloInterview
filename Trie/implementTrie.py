"""
Implement Trie Methods
https://www.hellointerview.com/learn/code/trie/implement-trie
https://leetcode.com/problems/implement-trie-prefix-tree

Description:
    Implement the search and delete methods of a Trie.
    - search(word) returns True if the word is in the Trie, False otherwise.
    - delete(word) removes the word from the Trie, and does not return a value.

    The creation of the Trie and the insert method are already implemented for you.

Examples:
    Input:
        initialWords = ["apple", "app", "apartment"]
        commands = [
            ["search", "apple"],
            ["search", "apartment"],
            ["search", "appl"],
            ["delete", "app"],
            ["search", "app"],
        ]
    Output: [True, True, False, False]

Approach:
    Search: Traverse trie character by character, return node.isEndOfWord at end
    Delete: Recursively traverse to end of word, unmark end-of-word, then
            delete nodes bottom-up if they have no children and aren't end of other words

Time Complexity: O(L) for search and delete, where L is the length of the word
Space Complexity: O(1) for search, O(L) for delete (recursion stack)
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

    def search(self, word) -> bool:
        curr_node = self.root
        for char in word:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        return curr_node.isEndOfWord

    def delete(self, word) -> None:
        def helper(node, idx):
            if idx == len(word):
                node.isEndOfWord = False
                return not node.children and not node.isEndOfWord
            if node and word[idx] in node.children:
                should_delete_child = helper(node.children[word[idx]], idx+1)
                if should_delete_child:
                    del node.children[word[idx]]
                return not node.children and not node.isEndOfWord
            return False
        helper(self.root, 0)
            


if __name__ == "__main__":
    s = Solution()

    # Test 1
    s.create_trie(["apple", "app", "apartment"])
    assert s.search("apple") == True
    assert s.search("apartment") == True
    assert s.search("appl") == False
    s.delete("app")
    assert s.search("app") == False
    assert s.search("apple") == True

    # Test 2
    s.create_trie(["bat", "bats", "ball", "ballet"])
    assert s.search("bat") == True
    assert s.search("bats") == True
    s.delete("bat")
    assert s.search("bat") == False
    assert s.search("bats") == True
    s.delete("ballet")
    assert s.search("ballet") == False
    assert s.search("ball") == True

    # Test 3
    s.create_trie(["hello"])
    assert s.search("hello") == True
    assert s.search("hell") == False
    s.delete("hello")
    assert s.search("hello") == False

    print("All tests passed!")
