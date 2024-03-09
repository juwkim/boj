import sys

while mod:=int(sys.stdin.readline()):
    a, b = 1, 1
    ans = 1
    while (a, b) != (0, 1):
        a, b = b, (a + b) % mod
        ans += 1
    print(mod, ans)