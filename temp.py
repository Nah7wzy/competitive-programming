class Solution:
    def decodeString(self, s: str) -> str:
        temp = ''
        temp_no = ''
        stack = []
        curr = 0  # register the digit
        for i in s:
            # print(i)
            if i == ']':
                # print(stack.pop())
                while stack[-1] != '[':
                    # print(stack[-1])
                    s = stack.pop()
                    temp += s
                    print(s)
                stack.pop()
                while stack[-1].isdigit():
                    x = stack.pop()
                    temp_no += x
                    print("popped digit " + x)
                    if stack == []:
                        break
                curr = int(temp_no[::-1])
                print(curr)
                for i in range(curr):
                    print(temp)
                    stack.append(temp[::-1])
            else:
                stack.append(i)
            temp = ''
            temp_no = ''

        answer = ''.join(str(i) for i in stack)
        return answer


x = Solution()
print(x.decodeString(


    "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
