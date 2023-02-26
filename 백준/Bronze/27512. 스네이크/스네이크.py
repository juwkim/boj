n, m = map(int, input().split())
ans = n * m
ans -= ans & 1
print(ans)