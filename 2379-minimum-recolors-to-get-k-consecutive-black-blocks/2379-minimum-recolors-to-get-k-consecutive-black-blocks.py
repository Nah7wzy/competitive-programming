class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, count, changed = 0, 0, 0
        res = float('inf')
        for r in range(len(blocks)+1):
            while count >= k and l < r:                
                res = min(res, changed)
                if blocks[l] == 'W':
                    changed -= 1
                count -= 1
                l += 1
            if r < len(blocks) and blocks[r] == 'W':
                changed += 1
            count += 1

        return res if res != float('inf') else changed