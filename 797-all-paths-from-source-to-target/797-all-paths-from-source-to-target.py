class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        def bt(x, ans):
            ans.append(x)
            if x == n - 1:
                res.append([e for e in ans])
            
            for child in graph[x]:
                bt(child, ans)
            ans.pop()
        bt(0, [])        
        return res