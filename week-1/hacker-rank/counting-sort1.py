def countingSort(arr):
    n=len(arr)
    x=[0]*n
    for i in arr:
        x[i]=x[i]+1
        
    return x