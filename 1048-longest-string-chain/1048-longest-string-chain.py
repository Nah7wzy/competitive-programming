class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        #initialize dp with 1 chain for each word
        dp = {}
        for word in words:
            if word not in dp:
                dp[word] = 1
                
        # sort to work up
        for word in sorted(words, key=len):
            for i in range(len(word)): #remove each letter of the word and look if the remaining letters exist in our dp
                s = word[:i] + word[i+1:]
                
                if s in dp:
                    dp[word] = max(dp[word], dp[s] + 1) #if it exists take the chain of the value and add it to current(which is 1)
                    
        #so we increasingly chain words that have predecessors
        return max(dp.values())