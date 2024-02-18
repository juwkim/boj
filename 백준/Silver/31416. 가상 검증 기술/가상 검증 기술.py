import sys
input = sys.stdin.readline

for _ in range(int(input())):
    ta, tb, va, vb = map(int, input().split())
    ans = tb * vb
    t = ta * va
    if t > ans:
        q, r = divmod(ans, ta)
        if (va - q) & 1:
            ans += (va - q + 1) // 2 * ta - r
        else:
            ans += (va - q) // 2 * ta
    print(ans)