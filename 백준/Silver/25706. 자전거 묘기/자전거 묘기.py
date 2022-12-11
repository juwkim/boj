N = int(input())
buf = [*map(int, input().split())]
ans = [0] * N
for i in range(N - 1, -1, -1):
    if buf[i]:
        idx = i + buf[i] + 1
        if idx < N:
            ans[i] = ans[idx] + 1
        else:
            ans[i] = 1
    else:
        idx = i + 1
        if idx < N:
            ans[i] = ans[idx] + 1
        else:
            ans[i] = 1
print(*ans)