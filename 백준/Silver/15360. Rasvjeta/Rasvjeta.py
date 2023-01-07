N, M, K = int(input()), int(input()), int(input())
ans, need = 0, 1
for _ in range(M):
    num = int(input())
    left, right = num - K, num + K
    while need < left:
        need += 2 * K + 1
        ans += 1
    need = right + 1

while need <= N:
    need += 2 * K + 1
    ans += 1
print(ans)