class Solution:
    def calc(self, i, j, x, y):
        return abs(j-i)*min(x, y)

    def maxArea(self, height) -> int:
        n = len(height)
        a, b = 0, n-1
        max = self.calc(a, b, height[a], height[b])
        print(max)
        while a < len(height)-1:
            print(a, b, self.calc(a, b, height[a], height[b]))
            if self.calc(a, b, height[a], height[b]) > max:
                max = self.calc(a, b, height[a], height[b])
                print(max)
            b -= 1
            a += 1

        return max


x = Solution()
print(x.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
