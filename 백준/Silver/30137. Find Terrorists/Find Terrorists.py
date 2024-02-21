import sys
input = sys.stdin.readline

prime = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0]
ans = [0, 0]
for num in range(2, 10001):
    cnt = 0
    for i in range(1, int(num**.5) + 1):
        q, r = divmod(num, i)
        if r == 0:
            cnt += 1 + (i != q)
    ans.append(prime[cnt])
for _ in range(int(input())):
    L, H = map(int, input().split())
    buf = [i for i in range(L, H + 1) if ans[i]]
    if buf:
        print(*buf)
    else:
        print(-1)