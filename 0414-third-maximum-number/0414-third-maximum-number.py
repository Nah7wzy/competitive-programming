class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        visited = set()
        
        for num in nums:
            if num not in visited:
                visited.add(num)
                if len(visited) == 3:
                    return num
                
        return nums[0]
            
            