class Solution: #80
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        x = max(nums)
        left, right = 0, x
        ans = x
        while left <= right:
            mid = left + (right - left) // 2
            total = 0
            for i in nums:
                total += math.ceil(i/(mid+1))
                if total > threshold:
                    left = mid + 1
                    break
            if total <= threshold and mid+1 <= ans:
                ans = mid + 1
                right = mid - 1

        return ans