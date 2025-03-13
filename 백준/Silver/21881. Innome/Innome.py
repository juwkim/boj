import sys
input = sys.stdin.readline

for _ in range(int(input())):
    m, k = map(int, input().split())
    ans, i = 0, 1
    while m >= i * k:
        m -= i * k
        i += 1
        ans += k
    ans += m // i
    print(ans)