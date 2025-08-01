import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

a, b, c = g()
move = [*range(101)]
for _ in range(b):
    u, v = g()
    move[u] = v
pos = [1] * a
game_over = False
cur = 0
for _ in range(c):
    r = int(input())
    if not game_over:
        pos[cur] = move[min(pos[cur] + r, 100)]
        game_over = pos[cur] == 100
    cur = (cur + 1) % a

for i in range(a):
    print(f"Position of player {i+1} is {pos[i]}.")