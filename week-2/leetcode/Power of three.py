class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        print(n)
        x = n/3

        if n == 1 or n == 3:
            return True
        if x == 3:
            return True
        elif x < 3:
            print(x)
            return False

        return self.isPowerOfThree(x)


x = Solution()
print(x.isPowerOfThree(
    27))
