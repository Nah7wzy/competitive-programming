class Solution: 
    def select(self, arr, i):
        # code here 
        return
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            min = arr[i]
            k=i+1
            mid=i
            for j in range(k, n):
                if arr[j]<min:
                    min=arr[j]
                    mid=j
            temp=arr[i]
            arr[i]=arr[mid]
            arr[mid]=temp           
        return arr