class Solution:
    def topKFrequent(self, nums, k):
        unique = []  # keep unique values
        freq = []  # keep respective freq
        answer = []

        for i in nums:
            if i not in unique:
                unique.append(i)
                freq.append(1)
            elif i in unique:
                x = unique.index(i)
                # if it exists in unique then we add freq on respective index
                freq[x] += 1
        for j in range(k):
            y = freq.index(max(freq))
            answer.append(unique[y])
            freq[y] = -1

        return answer


x = Solution()
print(x.topKFrequent([1, 1, 1, 2, 2, 3], 2))
