class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        #4 options for prime numbers that go in odd places and 5 options for even numbers that go in even places
        
        return (pow (4, n // 2, mod) * pow (5, (n // 2) + (n % 2) , mod)) % mod