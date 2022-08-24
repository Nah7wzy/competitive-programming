class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        jumps = defaultdict(lambda: set())
        
        for i in range(n):
            forward, backward = i + arr[i], i - arr[i]
            if forward < n:
                jumps[forward].add(i)
            if backward >= 0:
                jumps[backward].add(i)
        
        visited = set()
        res = False
        
        def bfs(x):
            nonlocal res
            if x == start:
                return True
            
            if x not in visited:
                visited.add(x)
                for jump in jumps[x]:
                    res = bfs(jump)
                visited.remove(x)
            return res
        
        for idx, num in enumerate(arr):
            if num == 0:
                if bfs(idx):
                    return True
        return False