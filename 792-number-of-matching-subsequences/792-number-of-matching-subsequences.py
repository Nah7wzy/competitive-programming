class TrieNode:
    def __init__(self):
        self.children = {}
        self.ind = None
        
class Trie:
    def __init__(self):
        self.trie = TrieNode()
        
    def insert(self, word):
        node = self.trie
        
        for x in word:
            if x not in node.children:
                node.children[x] = TrieNode()
            node = node.children[x] 
            
    def search(self, word, s):
        curr = self.trie
        temp = 0
        
        for i, wrd in enumerate(word):
            if curr.children[wrd].ind == None:
                curr.children[wrd].ind = -1
                for j in range(temp, len(s)):
                    if s[j] == wrd:
                        curr.children[wrd].ind = j
                        temp = j + 1
                        break
            if curr.children[wrd].ind < 0:
                return False
            
            temp = curr.children[wrd].ind + 1
            curr = curr.children[wrd]
        return True
                
        
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        words.sort()
        
        for word in words:
            trie.insert(word)
        
        count = 0
        for word in words:
            if trie.search(word, s):
                count += 1
                
        return count
                
     