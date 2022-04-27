class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        push, pop = 0, 0
        reverse = False
        n = len(pushed)
        print(popped)
        print("")
        if n == 1:
            if pushed[0] == popped[0]:
                return True
            else:
                return False

        while pop < n:
            print(pushed, push)
            if push >= len(pushed):
                break
            if not reverse and pushed[push] == popped[pop]:
                pop += 1
                print(pushed[push])
                pushed.remove(pushed[push])
                push -= 1
                if push != -1 and pushed[push] == pushed[-1]:
                    reverse = True

                    push = -1
                if not reverse and push != -1:
                    push -= 1
            elif reverse and pushed[-1] == popped[pop]:
                pushed.remove(pushed[-1])

                pop += 1
            elif reverse:
                pop += 1
            if not reverse:
                push += 1
        print(pushed, popped)
        if pushed == []:
            return True
        else:
            return False


x = Solution()
print(x.validateStackSequences([1, 2, 3, 4, 5, 6, 7],
                               [1, 2, 5, 3, 6, 7, 4]))
