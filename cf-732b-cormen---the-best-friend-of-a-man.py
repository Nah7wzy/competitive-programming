def inp():
    n, k = input().split()
    n, k = eval(n), eval(k)
    arr = [eval(e) for e in input().split()]
    solution(arr, n, k)

def solution(arr, n, k):
    additional = 0
    for i in range(1, n):
        dif = k - (arr[i-1] + arr[i])
        if dif > 0:
            additional += dif
            arr[i] += dif
            
    print(additional)
    print(*arr)
    
inp()
