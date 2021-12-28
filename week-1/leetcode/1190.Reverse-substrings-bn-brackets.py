def reverseParentheses(s: str) -> str:
    arr=[*s]
    for i in range(len(arr)):
        # print(arr[i])
        if arr[i]==')':
            # print(arr[i])
            for j in range(i,-1,-1):
                # print(arr[j])
                if arr[j]=='(':
                    temp=arr[j:arr.index(')')+1]
                    # print(temp)
                    temp.reverse()
                    temp.pop(0)
                    temp.pop()
                    # print(temp)
                    arr[j:arr.index(')')+1]=temp
                    # print(arr)
                if '(' not in arr or ')' not in arr:
                    print(arr)
                    answer=''.join(str(e) for e in arr)
                    return answer
    # print(arr)



reverseParentheses("(abcd)")
print(reverseParentheses("(u(love)i)"))
print(reverseParentheses("(ed(et(oc))el)"))