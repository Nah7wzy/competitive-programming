class Solution:
    def minSetSize(self, arr):
        freq = {}
        answer = 0
        n = len(arr)/2  # to know when half is passed
        for i in arr:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1

        # to start from higher values
        arr = sorted(freq.values(), reverse=True)
        # print(arr)
        count = 0  # keep count of frequencies

        for i in arr:
            count += i
            answer += 1
            if count >= n:
                break

        return answer


x = Solution()
print(x.minSetSize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#   unique = []  # keep unique values
#    freq = []  # keep respective freq
#     answer = 0
#      n = len(arr)/2  # to know when half is passed
#       print(n)
#        for i in arr:
#             if i not in unique:
#                 unique.append(i)
#                 freq.append(1)
#             elif i in unique:
#                 x = unique.index(i)
#                 # if it exists in unique then we add freq on respective index
#                 freq[x] += 1

#         freq.sort(reverse=True)  # to start from higher values

#         count = 0  # keep count of frequencies
#         for i in freq:
#             count += i
#             answer += 1
#             if count >= n:
#                 break

#         return answer
