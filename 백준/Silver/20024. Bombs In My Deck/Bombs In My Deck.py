g = lambda: [*map(int, input().split())]

A, B, C = g()

cnt = (C + 4) // 5
if cnt > B:
    print(1)
else:
    ans = 1
    for i in range(cnt):
        ans = ans * B / A
        A -= 1
        B -= 1
    print(1 - ans)