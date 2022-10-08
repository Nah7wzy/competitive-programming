class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(num, temp, total):
            temp.append(num)
            if total > n:
                return 
            if len(temp) == k:
                if total == n:
                    res.append(temp.copy())
                return
            
            for j in range(num+1, 10):
                backtrack(j, temp, total + j)
                temp.pop()
                
        for i in range(1, 10):
            backtrack(i, [], i)
        return res
                