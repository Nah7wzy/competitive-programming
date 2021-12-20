class Solution:
    def maxCoins(self, piles) -> int:
        piles.sort(reverse=True)
        div=len(piles)//3
        least=(div-1)+div
        max_coins=0
        for i in range(1,least+1,2):
            max_coins+=piles[i]
        return max_coins