import sys
input = lambda: sys.stdin.readline().rstrip()

for tc in range(1, 1 + int(input())):
    b, x, y = input().split()
    b = int(b)
    x, y = int(x, b), int(y, b)
    x %= y
    check = [-1] * y
    ans, i = 0, 0
    while True:
        q, x = divmod(x * b, y)
        if x == 0:
            break
        if check[x] != -1:
            ans = i - check[x]
            break
        check[x] = i
        i += 1
    print(f"Scenario #{tc}:")
    print(ans)
    print()