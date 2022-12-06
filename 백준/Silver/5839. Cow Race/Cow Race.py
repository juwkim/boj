import sys
input = lambda: sys.stdin.readline().rstrip()


g = lambda: [*map(int, input().split())]


N, M = g()
Bessie = [g() for _ in range(N)]
Elsie = [g() for _ in range(M)]
total = sum(l[1] for l in Elsie)

ans = 0

pos_B, pos_E = 0, 0
idx_B, idx_E = 0, 0
who_winning = None
for t in range(total):
    pos_B += Bessie[idx_B][0]
    Bessie[idx_B][1] -= 1
    if Bessie[idx_B][1] == 0:
        idx_B += 1
    
    pos_E += Elsie[idx_E][0]
    Elsie[idx_E][1] -= 1
    if Elsie[idx_E][1] == 0:
        idx_E += 1
    
    cur_winning = (pos_B > pos_E) - (pos_B < pos_E)
    if who_winning == None:
        if cur_winning:
            who_winning = cur_winning
    elif who_winning * cur_winning == -1:
        ans += 1
        who_winning = cur_winning
    
print(ans)