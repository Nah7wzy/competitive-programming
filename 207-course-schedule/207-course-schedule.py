class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #register prerequisites of each
        prq = defaultdict(list)
        for pre in prerequisites:
            prq[pre[0]].append(pre[1])
            
        def finish(x, visited):
            if prq[x] == True:
                return True
            visited.add(x)
            flag = True
            for child in prq[x]:
                if child in visited:
                    return False
                flag = flag and finish(child, visited)
            visited.remove(x)
            
            return flag
         
        for course in range(numCourses):
            res = finish(course, set())
            if not res:
                return False
            else:
                prq[course] = True            
            
        return True