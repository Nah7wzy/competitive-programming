class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if time == 0:
            return [i for i in range(len(security))]
        
        if 2 * time >= len(security): #not enough place for before + after
            return []
        
        before = 0
        after = 0
        res = []
        for i in range(1, len(security) - time):
            before = before + 1 if security[i-1] >= security[i] else 0
            after = after + 1 if security[(i + time) - 1] <= security[i + time] else 0 #i + time bc after starts after time befores                                                                                           have been covered                
            if i >= time and before >= time and after >= time: #if enough before and after covered 
                res.append(i)
            
        return res
            