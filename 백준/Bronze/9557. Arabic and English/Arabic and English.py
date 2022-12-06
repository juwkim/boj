for _ in range(int(input())):
    input()
    a = input().split()
    i = 0
    while i < len(a):
        if a[i].isalpha():
            break
        i += 1
    if i == len(a):
        print(*a)
    elif i == len(a) - 1:
        print(a[i], end=' ')
        print(*a[:i])
    elif i == 0:
        print(*a[i+1:], end=' ')
        print(a[i], end=' ')
    else:
        print(*a[i+1:], end=' ')
        print(a[i], end=' ')
        print(*a[:i])