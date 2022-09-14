class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        res = []
        
        def combine(res, total, x): #add x to avoid other permutations of the same combination (doesnt restart)
            if total >= target:
                if total == target:
                    ans.append([e for e in res])
                return
                
            for i in range(x, len(candidates)):
                num = candidates[i]
                res.append(num)
                total += num
                combine(res, total, i)
                res.pop()
                total -= num
                
        combine(res, 0, 0)
        return ans