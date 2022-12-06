while n:= int(input()):
    ans, Sum, i = 0, 3, 2
    while n >= Sum:
        ans += (n - Sum) % i == 0
        i += 1
        Sum += i
    print(ans)