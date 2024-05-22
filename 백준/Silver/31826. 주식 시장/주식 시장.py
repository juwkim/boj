import sys
input = sys.stdin.readline

s = [0] * 601
cur = 10000
for _ in range(int(input())):
    p, x, f = map(int, input().split())
    i = (p - 7000) // 10
    if (f == -1 and s[i] > 0) or (f == 1 and s[i] < 0):
        cur = p
    s[i] += f * x
print(cur)