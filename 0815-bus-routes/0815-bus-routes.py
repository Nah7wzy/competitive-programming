class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        q = collections.deque()
        graph = collections.defaultdict(set)
        routes = list(map(set, routes))
        visited, stops = set(), set()
        
        for i in range(len(routes)):
            if source in routes[i]: 
                visited.add(i)
                q.append((i, 1)) 
            if target in routes[i]:  
                stops.add(i)
                
            for j in range(i+1, len(routes)):
                if routes[j] & routes[i]: 
                    graph[i].add(j)
                    graph[j].add(i)
        
        while q:
            cur, count = q.popleft()
            if cur in stops:
                return count
            for nei in graph[cur]:
                if nei not in visited:
                    q.append((nei, count+1))
                    visited.add(nei)
        return -1