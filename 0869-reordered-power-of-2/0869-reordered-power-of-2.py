class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def get_digits(x):
            res = [0] * 10
            while x:
                res[x % 10] += 1
                x //= 10
            return res
        
        def is_power_of_2(x):
            return x > 0 and (x & (x - 1)) == 0
        
        target = get_digits(n)
        for i in range(30):
            if get_digits(1 << i) == target:
                return True
        return False