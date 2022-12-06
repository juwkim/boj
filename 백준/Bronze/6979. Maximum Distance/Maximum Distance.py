for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    i, j = 0, 0
    m = 0
    while True:
        j = i
        while j < n and b[j] >= a[i]:
            j += 1
        if j == n:
            if b[j-1] >= a[i]:
                m = max(m, j - i - 1)
            break
        m = max(m, j - i - 1)
        t = a[i]
        while i < n and t == a[i]:
            i += 1
        if i == n:
            break
    print(f'The maximum distance is {m}\n')