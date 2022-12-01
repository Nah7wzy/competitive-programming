class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        #find the element that will be at the end using one iteration of zero count
        i, last_pos = 0, len(arr) - 1
        while i < last_pos:
            if arr[i] == 0:
                last_pos -= 1
            i += 1
            
        #start from the back and build the array
        j = len(arr) - 1
        while last_pos >= 0:
            arr[j] = arr[last_pos]
            if arr[last_pos] == 0 and last_pos != i:
                j -= 1
                arr[j] = arr[last_pos]
            j -= 1
            last_pos -= 1
        
        