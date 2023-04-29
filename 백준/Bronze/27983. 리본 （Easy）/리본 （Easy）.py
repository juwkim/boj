g = lambda: [*map(int, input().split())]

N = int(input())
X = g()
L = g()
C = input().split()

ans = None
for i in range(N - 1):
    for j in range(1, N):
        if C[i] != C[j] and abs(X[i] - X[j]) <= L[i] + L[j]:
            ans = i + 1, j + 1
            break
    else:
        continue
    break
if ans:
    print('YES')
    print(*ans)
else:
    print('NO')