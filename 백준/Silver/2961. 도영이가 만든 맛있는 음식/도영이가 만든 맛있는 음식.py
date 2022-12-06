g = lambda: [*map(int, input().split())]

N = int(input())
S, B = zip(*[g() for _ in range(N)])
ans = 1e9
def solve(idx, Mul, Sum):
    global ans
    if idx == N:
        if Mul != 1 or Sum != 0:
            ans = min(ans, abs(Mul - Sum))
        return
    
    solve(idx + 1, Mul * S[idx], Sum + B[idx])
    solve(idx + 1, Mul, Sum)
    
solve(0, 1, 0)
print(ans)