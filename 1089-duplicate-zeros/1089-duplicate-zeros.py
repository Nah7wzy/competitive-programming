class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        #first find last surviving element
        l, r = 0, len(arr) - 1
        while l < r:
            if arr[l] == 0:
                arr[l] = -1 #to know if to be doubled or just ending element
                r -= 1
            l += 1
            
        #starting from the previous position reorder elements, double zeros when found
        p1, p2 = r, len(arr) - 1
        while p1 >= 0 and p1 < p2:
            arr[p2] = arr[p1] if arr[p1] != -1 else 0
            if arr[p1] == -1: #to be doubled
                p2 -= 1
                arr[p2] = 0
            p2 -= 1
            p1 -= 1
        
            