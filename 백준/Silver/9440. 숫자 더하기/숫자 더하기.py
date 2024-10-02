import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

while (nums:=g())[0]:
    N, *A = nums
    A.sort()
    zero = A.count(0)
    a, b = A[zero], A[zero + 1]
    ans = a * 10 ** ((N - 1) // 2) + b * 10 ** ((N - 2) // 2)
    p = N - 3 - zero
    for i in range(zero + 2, N):
        ans += A[i] * 10 ** (p // 2)
        p -= 1
    print(ans)