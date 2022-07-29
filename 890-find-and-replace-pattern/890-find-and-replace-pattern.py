class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def check(word):
            d1, d2 = {}, {}
            for i in range(len(word)):
                if pattern[i] not in d1 and word[i] not in d2:
                    d1[pattern[i]] = word[i]
                    d2[word[i]] = pattern[i]
                    
                else:
                    if pattern[i] not in d1 or word[i] not in d2:
                        return False
                    elif d1[pattern[i]] != word[i] or d2[word[i]] != pattern[i]:
                        return False
            return True
        
        res = []
        for word in words:
            if check(word):
                res.append(word)
            
        return res