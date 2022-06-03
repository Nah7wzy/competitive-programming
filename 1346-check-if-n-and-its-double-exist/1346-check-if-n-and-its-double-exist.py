class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = {}
        for i in arr:
            if i * 2 in seen or i / 2 in seen:
                return True
            else:
                seen[i] = 1
                
        return False
        
            