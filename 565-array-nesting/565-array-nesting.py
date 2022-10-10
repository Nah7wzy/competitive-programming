class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        memo = {}
        def dfs(node, visited):
            if node in visited:
                return 0
            if node in memo:
                return memo[node]
            visited.add(node)
            memo[node] = dfs(nums[node], visited)
            return 1 + memo[node]
        
        res = 0
        for i in range(len(nums)):
            res = max(res, dfs(i, set()))
        
        return res