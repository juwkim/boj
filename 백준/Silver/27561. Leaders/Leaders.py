import sys
input = sys.stdin.readline

N = int(input())
S = input()
E = [*map(int, input().split())]
G_leader, H_leader = -1, -1
if E[i:=S.index('G')] > S.rfind('G'): G_leader = i
if E[i:=S.index('H')] > S.rfind('H'): H_leader = i
ans = 0
for i in range(N):
    if S[i] == 'G':
        ans += i < H_leader and (i == G_leader or H_leader < E[i])
    else:
        ans += i < G_leader and (i == H_leader or G_leader < E[i])
print(ans)