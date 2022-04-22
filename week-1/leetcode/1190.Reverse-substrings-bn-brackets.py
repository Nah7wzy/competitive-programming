def reverseParentheses(s: str) -> str:
    arr = [*s]
    stack = []
    for i in range(len(arr)):
        # print(arr[i])
        if arr[i] == ')':
            # print(arr[i])
            temp = []
            while stack and stack[-1] != "(":
                temp += stack.pop()
            stack.pop()
            for x in temp:
                stack.append(x)
        else:
            stack.append(arr[i])
    return ''.join(str(e) for e in stack)
    # print(arr)


print(reverseParentheses("n(ev(t)((()lfevf))yd)cb()"))
# print(reverseParentheses("(u(love)i)"))
# print(reverseParentheses("(ed(et(oc))el)"))
