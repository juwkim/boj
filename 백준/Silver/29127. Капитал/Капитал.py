a, n = map(int, input().split())
if 9 * n < a:
    print(-1)
else:
    ans = []
    for _ in range(n):
        num = min(a, 9)
        a -= num
        ans.append(num)
    print(*ans, sep='')