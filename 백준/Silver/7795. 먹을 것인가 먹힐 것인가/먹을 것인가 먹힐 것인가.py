g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    N, M = g()
    A = sorted(g())
    B = sorted(g())
    
    ans = 0
    idx = 0
    for num in A:
        while idx < M and B[idx] < num:
            idx += 1
        ans += idx
    print(ans)