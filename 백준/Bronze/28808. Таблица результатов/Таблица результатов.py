n, m = map(int, input().split())
ans = sum('+' in input() for _ in range(n))
print(ans)