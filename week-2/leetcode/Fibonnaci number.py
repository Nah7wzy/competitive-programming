class Solution:
    def fib(self, n: int) -> int:
        print(n)
        if n <= 1:
            return n

        return self.fib(n-1)+self.fib(n-2)


x = Solution()
print(x.fib(5))
