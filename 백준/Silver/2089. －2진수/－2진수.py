N = int(input())
cur, step = 1, 0
ans = []
while True:
    if (N >> step) & 1:
        N -= cur
        ans.append(1)
    else:
        ans.append(0)
    cur *= -2
    step += 1
    if N == 0:
        break
print(*ans[::-1], sep='')