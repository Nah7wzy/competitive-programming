class Solution:
    def pancakeSort(self, arr):
        answer = []
        # a pointer at the right to start saving spot from the larger number and keep it from further sorting
        r = len(arr)-1
        while r > 0:
            x = arr.index(max(arr[:r+1]))
            if x == r:  # if the array or the max number is already sorted
                r -= 1
                continue

            temp = arr[:x+1]
            temp.reverse()
            arr[:x+1] = temp  # reverse the array from the index of max

            temp = arr[:r+1]
            temp.reverse()
            # reverse the array to the right pointer / put it before the last max
            arr[:r+1] = temp

            answer.append(x+1)
            answer.append(r)
            r -= 1
        return answer


x = Solution()
print(x.pancakeSort([1, 2, 3]))
