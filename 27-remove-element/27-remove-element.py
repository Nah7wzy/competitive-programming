class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = nums.count(val)
        n = len(nums)
        for i in range(x):
            nums.remove(val)
        return n - x