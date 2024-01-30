import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
a, b = [], []
for _ in range(N):
    num = int(input())
    if num < 0:
        a.append(-num)
    elif num > 0:
        b.append(num)
apos = sorted(a, reverse=True)[0:len(a):K]
bpos = sorted(b, reverse=True)[0:len(b):K]
ans = 2 * (sum(apos) + sum(bpos)) - max(apos + bpos)
print(ans)