class TrieNode:
    def __init__(self):
        self.children = {}
        
class Trie:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str):
        node = self.trie
        
        for i in range(len(word)):
            if word[i] not in node.children and i == len(word) - 1: #if only needed to add the last letter
                node.children[word[i]] = TrieNode()
                return len(word)
            elif word[i] not in node.children: #if more than one letter left to add
                return 0
            node = node.children[word[i]] 
        return 0

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        trie = Trie()
        res = ""
        temp = 0
        for x in words:
            length = trie.insert(x)
            if length > temp:
                temp = length
                res = x
            
        print(words, temp)
        return res