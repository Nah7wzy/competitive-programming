class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        x = max(nums)
        div = [i for i in range(x+1)]
        left, right = 0, len(div)-1
        ans = div[-1]
        while left <= right:
            mid = left + (right - left) // 2
            total = 0
            for i in nums:
                total += math.ceil(i/(mid+1))
            if total > threshold:
                left = mid + 1
            elif total <= threshold and mid+1 <= ans:
                ans = mid + 1
                right = mid - 1

        return ans