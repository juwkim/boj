MIS = lambda: [*map(int, input().split())]

C, N = MIS()
if N == 0:
    print(C)
else:
    bank = 0
    prev = int(input())
    for i in range(N-1):
        cur = int(input())
        if cur > prev:
            cnt = C // prev
            C -= cnt * prev
            bank += cnt
        elif cur < prev:
            C += bank * prev
            bank = 0
        prev = cur
    print(C + bank * cur)