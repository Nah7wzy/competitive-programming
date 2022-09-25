class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        mid = False #we can add one value in the middle
        res = 0
        for count in freq.values():
            if count > 1:
                res += (count // 2) * 2
            if count == 1 or count % 2 != 0:
                mid = True
             
        return res + 1 if mid else res
        