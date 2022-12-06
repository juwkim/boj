g = lambda: [*map(int, input().split())]

while (i := input()) != '0 0':
    P, S = map(int, i.split())
    trap = set(g())
    N = int(input())
    pos = [0] * P
    trapped = [0] * P
    
    player = 0
    for _ in range(N):
        pos[player] += sum(g())
        
        if pos[player] > S:
            print(player + 1)
            break
        
        if pos[player] in trap:
            trapped[player] = 1
        
        player = (player + 1) % P 
        while trapped[player]:
            trapped[player] = 0
            player = (player + 1) % P