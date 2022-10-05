class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0 for _ in range(len(heights))]
        stack = []
        for i, h in enumerate(heights):
            while stack and h > stack[-1][0]:
                x, pos = stack.pop()
                res[pos] += 1
            if stack:
                res[stack[-1][1]] += 1
            stack.append((h, i))

        return res
        
