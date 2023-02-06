class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for word in words:
            for i in range(len(word)):
                if i < len(pref) and word[i] != pref[i]:
                    break
                if i >= len(pref) - 1:
                    res += 1
                    break
                    
        return res