class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, visited = set(), set()
        n = len(nums)
        def backtrack(i, ans):
            visited.add(i)
            ans.append(nums[i])
            if len(visited) == n and tuple(ans) not in res:
                res.add(tuple(ans))
            for j in range(n):
                if j not in visited:
                    backtrack(j, ans)
            visited.remove(i)
            ans.pop()
        
        for pos in range(n):
            backtrack(pos, [])
        return res