class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        a, b = len(nums)-2, len(nums) - 1
        if n == 1:  return 1 if nums[0] == x else -1
        for i in range(len(nums)-1):
            nums[i+1] += nums[i]
        print(nums)
            
        #do prefix sum and start decreasing a if its greater and if its less compare with b and decide which to move
        ans = len(nums) + 2
        while a >= 0 and b > a:
            if nums[n-1] - nums[b-1] == x:
                ans = min(ans, n - b)

            if nums[a] == x:
                ans = min(ans, a+1)
            elif nums[a] < x:
                if nums[a] + (nums[(n-1)] - nums[b-1]) == x:
                    ans = min(ans, a+1+(n-b))
                elif nums [a] + (nums[(n-1)] - nums[b-1]) < x:
                    a += 1
                    b -= 1
            else:
                if a == 0:
                    a += 1
                    b -= 1
            a -= 1
                    
        return ans if ans < len(nums) + 2 else -1