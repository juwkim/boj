MIS = lambda: [*map(int, input().split())]

for _ in range(1, 1 + int(input())):
    N = int(input())
    Ls = MIS()
    Ps = MIS()
    ans = [*range(N)]
    ans.sort(key=lambda x: (Ls[x] / Ps[x] if Ps[x] else 1e10, x))
    print(f'Case #{_}:', *ans)