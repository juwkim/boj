import sys
input = sys.stdin.readline
for tc in range(1, 1 + int(input())):
    b, x, y = input().split()
    b = int(b)
    x, y = int(x, b), int(y, b)
    x %= y
    check = [-1] * y
    ans, i = 0, 0
    while True:
        x = x * b % y
        if x == 0:
            break
        if check[x] != -1:
            ans = i - check[x]
            break
        check[x] = i
        i += 1
    print(f"Scenario #{tc}:\n{ans}\n")