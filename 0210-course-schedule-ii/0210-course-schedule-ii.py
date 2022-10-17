class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for rel in prerequisites:
            indegree[rel[0]] += 1
            graph[rel[1]].append(rel[0])
        
        q = deque([])
        for i, count in enumerate(indegree):
            if count == 0:
                q.append(i)
                
        res = []
        while q:
            x = q.popleft()
            res.append(x)
            for child in graph[x]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
                    
        return res if numCourses == len(res) else []
                    
                
        