import sys
input = lambda: sys.stdin.readline().rstrip('\n')


g = lambda: [*map(int, input().split())]

B, E = g()
move_B = []
for _ in range(B):
    amount, d = input().split()
    amount = int(amount)
    if d == 'L':
        amount *= -1
    move_B.append(amount)

move_E = []
for _ in range(E):
    amount, d = input().split()
    amount = int(amount)
    if d == 'L':
        amount *= -1
    move_E.append(amount)
    
Bessie, Elsie = 0, 0
cur_B, cur_E = 0, 0

now = 1
ans = 0
while cur_B < B and cur_E < E:
    
    if move_B[cur_B] > 0:
        Bessie += 1
        move_B[cur_B] -= 1
    else:
        Bessie -= 1
        move_B[cur_B] += 1
        
    if move_E[cur_E] > 0:
        Elsie += 1
        move_E[cur_E] -= 1
    else:
        Elsie -= 1
        move_E[cur_E] += 1
    
    if move_B[cur_B] == 0:
        cur_B += 1

    if move_E[cur_E] == 0:
        cur_E += 1
    
    cur = Bessie == Elsie
    if now == 0 and cur == 1:
        ans += 1
    
    now = cur
    
if cur_B < B:
    while cur_B < B:
        
        if move_B[cur_B] > 0:
            Bessie += 1
            move_B[cur_B] -= 1
        else:
            Bessie -= 1
            move_B[cur_B] += 1
        
        if move_B[cur_B] == 0:
            cur_B += 1
        
        cur = Bessie == Elsie
        if now == 0 and cur == 1:
            ans += 1
    
        now = cur        
elif cur_E < E:
    
    while cur_E < E:
            
        if move_E[cur_E] > 0:
            Elsie += 1
            move_E[cur_E] -= 1
        else:
            Elsie -= 1
            move_E[cur_E] += 1
    
        if move_E[cur_E] == 0:
            cur_E += 1
        
        cur = Bessie == Elsie
        if now == 0 and cur == 1:
            ans += 1
        
        now = cur
print(ans)