class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        start, end = 0, 0
        ptr = 0
        started = False
        curr = nums[0]
        possible = 0
        while ptr < len(nums)-1:
            print(ptr)
            if nums[ptr] > curr:
                curr = nums[ptr]
                possible = ptr-1
            if nums[ptr+1] < nums[ptr] and not started:
                if nums[ptr] == curr:
                    start = possible+1
                if nums[ptr+1] <= curr:
                    start = possible
                else:
                    start = ptr
                started = True
                curr = nums[ptr]
                end = ptr+1
                ptr += 1
            elif started and nums[ptr+1] < nums[ptr]:
                end = ptr+1
            elif started and nums[ptr+1] < curr:
                end = ptr+1

            ptr += 1
        print(end, start, curr)
        if end-start < 1:
            return 0
        else:
            return (end-start)+1


x = Solution()
print(x.findUnsortedSubarray(
    [1, 2, 4, 5, 3]))
