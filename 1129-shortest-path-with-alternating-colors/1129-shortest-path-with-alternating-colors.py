class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        blue, red = defaultdict(list), defaultdict(list)
        for edge in redEdges:
            red[edge[0]].append(edge[1])
        for edge in blueEdges:
            blue[edge[0]].append(edge[1])
        
        def bfs(dest, color):        
            q = deque([0])
            ans = 0
            rvisited, bvisited = set(), set()
            while q:
                for _ in range(len(q)):                    
                    x = q.popleft()
                    if x == dest:
                        # print(ans)
                        return ans
                    if color:
                        for child in red[x]:
                            if child not in rvisited:
                                q.append(child)
                                rvisited.add(child)
                    else:
                        for child in blue[x]:
                            if child not in bvisited:
                                q.append(child)
                                bvisited.add(child)
                color = not color  
                ans += 1
            
            return -1
        
        res = []
        for destination in range(n):
            first, second = bfs(destination, 1), bfs(destination, 0)
            # print(first, second)
            distance = min(first, second)
            
            if distance == -1:
                res.append(max(first, second))
            else:
                res.append(distance)
            
        return res