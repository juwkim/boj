import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
v1, k1, v2, k2 = input(), input(), input(), input()
ans = []
for i in range(N):
    if v1[i] != v2[i]:
        continue
    if k1[i] != k2[i]:
        ans = []
        break
    ans.append(k1[i])
if ans:
    print(*ans, sep='')
else:
    print("htg!")