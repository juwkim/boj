import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

ans = 0
for _ in range(int(input())):
    s = input()
    ans += '01' in s or 'OI' in s
print(ans)