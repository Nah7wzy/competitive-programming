class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Trie:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        node = self.trie
        
        for x in word:
            if x not in node.children:
                node.children[x] = TrieNode()
            node = node.children[x] 
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.trie
        
        for x in word:
            if x not in node.children:
                return False
            node = node.children[x]
            
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        
        for x in prefix:
            if x not in node.children:
                return False
            node = node.children[x]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)