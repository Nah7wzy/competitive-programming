class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        units = 0
        for i in boxTypes:
            if i[0] > truckSize:
                units += i[1] * truckSize
                break
            else:
                units += i[1] * i[0]
                truckSize -= i[0]
                
        return units