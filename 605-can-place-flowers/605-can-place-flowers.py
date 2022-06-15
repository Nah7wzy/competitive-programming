class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i += 2
            else:
                if i == len(flowerbed)-1 or flowerbed [i+1] == 0:
                    n-=1
                    i += 2
                else:
                    i += 1
                
        return n <= 0
                