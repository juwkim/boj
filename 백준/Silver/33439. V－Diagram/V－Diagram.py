import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    i = 1
    while a[i] > a[i - 1] or a[i] > a[i + 1]:
        i += 1
    ans = 0
    tot = sum(a[:i + 1])
    for j in range(i + 1, n): 
        tot += a[j]
        ans = max(ans, tot / (j + 1))
    tot = sum(a[i:])
    for j in range(i - 1, -1, -1):
        tot += a[j]
        ans = max(ans, tot / (n - j))    
    print(ans)