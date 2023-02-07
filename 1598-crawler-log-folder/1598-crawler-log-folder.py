class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        
        for i in logs:
            if i[0] == "." and i[1] == ".":
                res -= 1 if res else 0
            elif i[0] == "." and i[1] == "/":
                continue
            else:
                res +=1
                
        return res