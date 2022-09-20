class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(len(isConnected))]
        # rank = [1 for _ in range()]
        def find(i):
            if i == parent[i]:
                return i
            
            parent[i] = find(parent[i])
            return parent[i]
        
        provinces = len(isConnected)
        def unite(a, b):
            nonlocal provinces
            
            par_a = find(a)
            par_b = find(b)
            
            if par_a != par_b:
                provinces -= 1
                parent[par_a] = par_b
                
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i != j and isConnected[i][j] == 1:
                    unite(i, j)
        
        return provinces