import sys
input = sys.stdin.readline
for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    ans = -1
    j = -N + y - x
    for i in range(M):
        j += N
        r, q = divmod(j, M)
        if q == 0:
            ans = M * r + x
            break;
    print(ans)