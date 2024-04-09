from typing import List

class TrieNode(object):
    def __init__(self):
        self.children = dict()
        self.is_word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True

    def search(self, word):
        cur = self.root
        ans = 0
        for c in word:
            if c not in cur.children:
                break
            cur = cur.children[c]
            ans += 1
        
        return ans

    def startsWith(self, prefix):
        cur = self.root
        ans = 0
        for c in prefix:
            if c not in cur.children:
                break
            cur = cur.children[c]
            ans += 1

        return ans
    
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        ans = 0
        root = Trie()
        
        for x in arr1:
            root.insert(str(x))
        
        for x in arr2:
            ans = max(ans,root.search(str(x)))
        
        return ans