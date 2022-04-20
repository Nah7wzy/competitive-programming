class Solution:
    def findOriginalArray(self, changed):
        changed.sort()
        # l points at the smallest element, r points at the doubled elements
        l, r = 0, 1
        result = []
        while l < len(changed):
            # r must always be greater than l
            if r <= l:
                r = l + 1

            if changed[l] == -1:
                l += 1
                continue

            # move r right until it is double of l
            while r < len(changed) and changed[r] != changed[l] * 2:
                r += 1
            # couldn't find a corresponding doubled element
            if r == len(changed):
                return []

            # flag r as used
            changed[r] = -1
            result.append(changed[l])

            l += 1

            return result


x = Solution()
print(x.findOriginalArray([4, 2, 4, 2]))
