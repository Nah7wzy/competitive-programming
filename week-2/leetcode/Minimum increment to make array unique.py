class Solution:
    def helper(self, nums, count):
        nums.sort()
        unique = True
        i = 1
        while i < len(nums)-1:
            if nums[i] == nums[i-1]:
                nums[i] += 1
                count += 1
                print(nums)
                if i < len(nums)-1:
                    if nums[i] > nums[i+1]:
                        nums[i], nums[i+1] = nums[i+1], nums[i]
                        # nums.sort()
                        i -= 1

            i += 1
        return count

    def minIncrementForUnique(self, nums) -> int:
        count = 0
        return self.helper(nums, count)


x = Solution()
print(x.minIncrementForUnique([2, 2, 2, 2, 0]))


# def helper(self, nums, count):
#      nums.sort()
#       unique = True
#        for i in range(len(nums)-1):
#             if nums[i] == nums[i+1]:
#                 nums[i+1] += 1
#                 count += 1
#                 if i+1 < len(nums)-1:
#                     if nums[i+1] > nums[i+2]:
#                         unique = False
#         if not unique:
#             return self.helper(nums, count)
#         else:
#             return count
