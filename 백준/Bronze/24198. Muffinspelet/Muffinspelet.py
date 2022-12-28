N = int(input())
ans = [0, 0]
idx = 1
while N:
    ans[idx] += N + 1 >> 1
    N >>= 1
    idx ^= 1
print(*ans)