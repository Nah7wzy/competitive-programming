class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = n/4

        if n == 1 or n == 4:
            return True
        if x == 4:
            return True
        elif x < 4:
            return False

        return self.isPowerOfFour(x)