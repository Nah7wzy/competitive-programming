class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort(reverse=True)
        print(nums)
        ans = []
        for i in range(len(nums)-2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                
                if nums[left] + nums[right] == -(nums[i]):
                    x = [nums[i], nums[left], nums[right]]
                    if x not in ans:
                        ans.append(x)
                    left += 1
                    right -= 1
                    
                elif nums[left] + nums[right] < -(nums[i]):
                    right -= 1
                else:
                    left += 1
                    
        return ans
                