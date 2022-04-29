class Solution:
    def invert(self, x):
        res = []
        for i in range(len(x)):
            if x[i] == "0":
                res.append(1)
            else:
                res.append(0)
        return ''.join(str(e) for e in res)

    def reverse(self, y):
        return y[::-1]

    def binaryString(self, n):
        if n == 1:
            return "0"
        s = self.binaryString(n-1)
        return (s+"1"+self.reverse(self.invert(s)))

    def findKthBit(self, n: int, k: int) -> str:
        print(self.binaryString(n))
        return self.binaryString(n)[k-1]


x = Solution()
print(x.findKthBit(5, 11))
# print(x.invert("1101"))
