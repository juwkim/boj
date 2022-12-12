N = int(input()) % 100
cur = 10
while N - cur >= 0:
    N -= cur
    cur += 10
ans = (min(N, cur - N) + 4) // 5
print(ans)