import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    n = int(input())
    a = g()
    b = g()
    ans = 0
    s = set()
    j = n - 1
    for i in range(n - 1, -1, -1):
        if a[i] == b[j]:
            j -= 1
            continue
        if a[i] in s:
            s.remove(a[i])
        else:
            s.add(a[i])
            ans += 1
    print(ans)