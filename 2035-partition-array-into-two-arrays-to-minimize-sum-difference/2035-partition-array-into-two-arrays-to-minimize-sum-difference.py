class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        sum_ = sum(nums)
        N = n // 2
        left = [[] for _ in range(N+1)]
        right = [[] for _ in range(N+1)]

        #storing all possible sum in left and right part
        for mask in range(1<<N):
            sz, l, r = 0, 0, 0
            for i in range(N):
                if mask & (1<<i):
                    sz += 1
                    l += nums[i]
                    r += nums[i+N]
            left[sz].append(l)
            right[sz].append(r)

        for sz in range(N+1):
            right[sz].sort()

        res = abs(sum_ - 2 * left[N][0])

        #iterating over left part
        for sz in range(1, N):
            for a in left[sz]:
                b = (sum_ - 2*a) // 2
                rsz = N - sz
                v = right[rsz]
                idx = bisect.bisect_left(v, b)
                if idx < len(v):
                    res = min(res, abs(sum_ - 2 * (a + v[idx])))
                if idx > 0:
                    res = min(res, abs(sum_ - 2 * (a + v[idx-1])))

        return res

