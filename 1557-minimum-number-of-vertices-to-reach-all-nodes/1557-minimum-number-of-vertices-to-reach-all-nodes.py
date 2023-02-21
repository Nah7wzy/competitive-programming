class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        res = []
        seen = [0] * n
        for e in edges:
            seen[e[1]] = 1
            
        for i in range(n):
            if seen[i] == 0:
                res.append(i)
                
        return res