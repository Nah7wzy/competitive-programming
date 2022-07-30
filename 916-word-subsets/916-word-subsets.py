class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:  
        subset = {} #keep track of max count for each letter in words2
        for sub in words2:
            temp = Counter(sub)
            for i in temp:
                if i in subset:
                    subset[i] = max(subset[i], temp[i])
                else:
                    subset[i] = temp[i]
                    
        res = []
        for word in words1:
            if self.check(word, subset):
                res.append(word)
                
        return res
    
    def check(self, word, subset):
        count = Counter(word)
        for letter in subset:
            if letter not in count or subset[letter] > count[letter]: #if max appearance of letter dont fit in
                return False
        return True
        
        