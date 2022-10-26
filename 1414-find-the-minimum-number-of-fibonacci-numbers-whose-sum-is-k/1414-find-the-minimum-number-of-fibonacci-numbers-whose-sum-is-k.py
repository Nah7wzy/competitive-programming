class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib_seq = [1, 1]
        pointer = 1
        while fib_seq[-1] < k: #build fibonnacci sequence
            to_append = fib_seq[pointer] + fib_seq[pointer - 1]
            fib_seq.append(to_append)
            pointer += 1

        j = len(fib_seq) - 1
        no_of_operations = 0
        while j >= 0 and k > 0:
            if fib_seq[j] <= k:
                no_of_operations += 1
                k -= fib_seq[j]
            j -= 1

        return no_of_operations