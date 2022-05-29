class Solution:
    def maxProduct(self, words: List[str]) -> int:
        chars = [set(word) for word in words]
        prod = 0
        
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if not (chars[i] & chars[j]):
                    prod = max(prod, len(words[i]) * len(words[j]))
        
        return prod