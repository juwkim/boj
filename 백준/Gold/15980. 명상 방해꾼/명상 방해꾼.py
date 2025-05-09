import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a, b = zip(*[input().split() for _ in range(N)])
cnt = [0] * M
for j in range(M):
    num = 0
    for i in range(N):
        if b[i][j] == '1':
            num += (a[i] == 'R') - (a[i] == 'L')
    cnt[j] = num
ans = 1e9, 1e9
for i in range(N):
    cur, num = 0, 0
    for j in range(M):
        num += cnt[j]
        if b[i][j] == '1':
            num += (a[i] == 'L') - (a[i] == 'R')
        cur = max(cur, abs(num))
    ans = min(ans, (cur, i + 1))
num, idx = ans
print(idx)
print(num)