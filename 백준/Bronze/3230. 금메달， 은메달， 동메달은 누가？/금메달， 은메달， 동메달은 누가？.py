N, M = map(int, input().split())
buf = []
for i in range(1, 1 + N):
    buf.insert(int(input()) - 1, i)
board = []
for player in buf[:M][::-1]:
    board.insert(int(input()) - 1, player)
print(*board[:3])