N, S = map(int, input().split())
cnt = 0
cur = S
for _ in range(N):
    p = input().rstrip()
    if p[-1] == 'L':
        water = int(p[:-1]) + 1
    else:
        water = int(p)
    if water > cur:
        cnt += 1
        cur = S
    cur -= water
print(cnt)