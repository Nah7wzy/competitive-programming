class Solution:
    def minPairSum(self, nums):
        nums.sort()
        n = len(nums)
        l, r = 0, n-1
        # sort and use pointers to match lower half with higher half
        # then find max of the matches
        max = nums[l]+nums[r]
        print(nums)
        while r > l:
            if nums[l]+nums[r] > max:
                max = nums[l]+nums[r]
            l += 1
            r -= 1

        return max


x = Solution()
print(x.minPairSum([5, 3, 5, 2, 1, 5, 5, 2, 3, 1]))
