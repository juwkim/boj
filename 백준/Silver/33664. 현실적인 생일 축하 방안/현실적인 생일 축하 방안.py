import sys
input = lambda: sys.stdin.readline().rstrip()

B, N, M = map(int, input().split())
dic = {}
for _ in range(N):
    i, p = input().split()
    dic[i] = int(p)
for _ in range(M):
    B -= dic[input()]
print(("", "un")[B < 0] + "acceptable")