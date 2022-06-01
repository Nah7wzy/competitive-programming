class Solution:
    def arrangeCoins(self, n: int) -> int:
        arr = [0]
        for i in range(n):
            x = (i+1) + arr[-1]
            if x > n:
                break
            else:
                arr.append(x)
        # print(arr)
        return len(arr) - 1
            