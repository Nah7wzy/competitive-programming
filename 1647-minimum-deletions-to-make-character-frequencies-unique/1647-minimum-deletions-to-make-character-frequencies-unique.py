class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        deletions = 0
        unique = set()
        
        x = sorted(count.values(), reverse = True) #start from biggest and delete gradually if not unique
        for i in x:
            while i in unique: #delete while not unique
                deletions += 1
                i -= 1
                if i == 0:
                    break
            unique.add(i)
                
        return deletions