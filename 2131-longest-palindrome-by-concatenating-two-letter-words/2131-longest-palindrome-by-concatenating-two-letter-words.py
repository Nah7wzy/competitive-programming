class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        palindromes = defaultdict(lambda: 1) #register palindromes of words with freq
        res = 0
        def palindrome(s):
            return s[-1] + s[0]
        
        for word in words:
            pal = palindrome(word)
            if palindromes[pal] > 1:
                palindromes[pal] -= 1
                res += 4
            else:
                palindromes[word] += 1
                
        #to add one stand alone palindrome in the middle if it exists     
        for elem in palindromes:
            if palindromes[elem] > 1 and elem[-1] == elem[0]:
                res += 2
                break
        
        return res