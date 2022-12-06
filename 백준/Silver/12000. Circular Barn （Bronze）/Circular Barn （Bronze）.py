N = int(input())
r = [int(input()) for _ in range(N)]
r += r
ans = min(sum(x * y for x, y in zip(range(1, N), r[i:i+N-1])) for i in range(N))
print(ans)