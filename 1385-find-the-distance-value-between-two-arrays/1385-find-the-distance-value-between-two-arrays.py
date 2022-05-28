class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count=0
        arr2.sort()
        
        for num in arr1:
            if self.binarySearch(num,arr2,d):
                count += 1        
        return count       
        
    def binarySearch(self,num,arr2,d):
        start, end= 0, len(arr2)-1
        
        while start<=end:
            mid = (start+end)//2            
            if abs(num-arr2[mid])<= d:
                return False            
            if arr2[mid] > num:
                end=mid-1
            else:
                start=mid+1
                
        return True