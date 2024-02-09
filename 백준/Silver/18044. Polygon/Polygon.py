import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    l = sorted(map(int, input().split()), reverse=True)
    s = sum(l)
    for i in range(n):
        if l[i] * 2 < s:
            break
        s -= l[i]
    print(s)