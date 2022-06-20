class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        res = 0
        vowels = ('a', 'e', 'i', 'o', 'u')
        for i in range(n):
            if word[i] in vowels:
                res += (i * (n - i) + (n - i))
                
        return res