import sys
input = sys.stdin.readline

N = int(input())
H = [0] + [int(input()) for _ in range(N)] + [0]
check = [1] + [0] * N + [1]
indexes = sorted(range(1, N + 1), key=lambda i: H[i])
ans, cur = 1, 1
for i, idx in enumerate(indexes):
    cur += 1 - check[idx-1] - check[idx+1]
    check[idx] = 1
    if i == N - 1 or H[idx] != H[indexes[i+1]]:
        ans = max(ans, cur)
print(ans)