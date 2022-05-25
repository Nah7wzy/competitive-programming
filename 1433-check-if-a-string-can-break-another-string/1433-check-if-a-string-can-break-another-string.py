class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        
        count1 = count2 = 0
        for i in range(len(s1)):
            if s1[i] > s2[i]: count1 += 1
            elif s2[i] > s1[i]: count2 += 1
            
            if count1 != 0 and count2 != 0:
                return False
        return True
