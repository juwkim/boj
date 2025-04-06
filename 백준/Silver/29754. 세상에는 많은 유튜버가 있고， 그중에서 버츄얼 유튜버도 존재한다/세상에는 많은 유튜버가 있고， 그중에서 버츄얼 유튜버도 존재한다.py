import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
dic = defaultdict(lambda: [[0, 0] for _ in range(M // 7)])
for _ in range(N):
    name, day, s, e = input().split()
    h1, m1 = map(int, s.split(':'))
    h2, m2 = map(int, e.split(':'))
    i = (int(day) - 1) // 7
    dic[name][i][0] += (h2 - h1) * 60 + (m2 - m1)
    dic[name][i][1] += 1
ans = [name for name, l in dic.items() if all(a >= 3600 and b >= 5 for a, b in l)]
if ans:
    print(*sorted(ans), sep='\n')
else:
    print(-1)