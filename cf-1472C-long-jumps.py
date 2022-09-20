def inp():
    t = eval(input())
    for _ in range(t):
        n = eval(input())
        arr = [int(e) for e in input().split()]
        print(solution(arr,n))
 
def solution(arr, n):
    res = 0
    memo = {}
    def dfs(i):
        if i >= n:
            return 0
        if i in memo:
            return memo[i]
            
        ans = arr[i] + dfs(i+arr[i])
        memo[i] = ans
        return ans
        
    for j in range(n):
        res = max(res, dfs(j))
    # print(memo)
    return res
 
import sys
import threading
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
thread = threading.Thread(target=inp)
thread.start(); thread.join()
