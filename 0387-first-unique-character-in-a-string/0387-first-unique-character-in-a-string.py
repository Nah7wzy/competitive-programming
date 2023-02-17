class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        for i, letter in enumerate(s):
            if freq[letter] == 1:
                return i
            
        return -1