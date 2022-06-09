"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        total = 0
        seen = set()
        for i in employees:
            if i.id == id:
                root = i
                break
        
        def dfs(root):
            nonlocal total
            seen.add(root.id)
            total += root.importance
            if not root.subordinates:
                return
            for j in employees:
                for x in root.subordinates:
                    if j.id == x:
                        dfs(j)
            
        dfs(root)
        return total