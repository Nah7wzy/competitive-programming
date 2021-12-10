def solution():
    m,n,a = input("").split(' ')
    m,n,a = int(m), int(n), int(a)
    
    if m%a!=0:
        x = (m//a + 1)
    else:
        x = m//a
    
    if n%a!=0:
        y = (n//a + 1)
    else:
        y = n//a

    result = x*y

    print(result)

solution()
