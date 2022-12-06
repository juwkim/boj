g = lambda: [*map(int, input().split())]

N = int(input())
patals = g()
cnt = 0
for i in range(N):
    for j in range(1, N - i + 1):
        s = patals[i:i+j]
        r, q = divmod(sum(s), j)
        if q == 0 and r in s:
            cnt += 1
print(cnt)