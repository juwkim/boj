N, *A = map(int, open(0).read().split())
ans = 0
while True:
    updated = False
    for i in range(1, N - 1):
        if 2 * A[i] > A[i - 1] + A[i + 1]:
            updated = True
            num = (2 * A[i] - A[i - 1] - A[i + 1] + 1) // 2
            ans += num
            A[i] -= num
    if not updated:
        break
print(ans)