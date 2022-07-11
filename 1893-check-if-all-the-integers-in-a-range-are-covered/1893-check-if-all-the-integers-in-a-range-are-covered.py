class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        numbers = set()
        for i in ranges:
            for j in range(i[0], i[1] + 1):
                numbers.add(j)
                
        for x in range(left, right + 1):
            if x not in numbers:
                return False
            
        return True