class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, visited = [], set()
        n = len(nums)
        def bt(i, ans):
            visited.add(i)
            ans.append(nums[i])
            if len(visited) == n:
                res.append([e for e in ans])
            for x in range(n):
                if x not in visited:
                    bt(x, ans)
            visited.remove(i)
            ans.pop()
        
        for pos in range(n):
            bt(pos, [])
        return res
                