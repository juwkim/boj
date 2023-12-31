import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

tc = 1
while (s:=input())[0] != '-':
    ans = 0
    stack = 0
    for c in s:
        if c == '{':
            stack += 1
        else:
            if stack:
                stack -= 1
            else:
                stack += 1
                ans += 1
    ans += stack // 2
    print(f"{tc}. {ans}")
    tc += 1