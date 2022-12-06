ans = 'Valid'
board = [[0] * 6 for _ in range(6)]

start = input()

cur = start
a, b = ord(cur[0]) - 65, int(cur[1]) - 1
board[a][b] = 1

for i in range(35):
    now = input()
    s, t = ord(now[0]) - 65, int(now[1]) - 1
    if board[s][t] == 1:
        ans = 'Invalid'
        break
    elif str(abs(s - a)) + str(abs(t - b)) not in '12 21':
        ans = 'Invalid'
        break
    else:
        board[s][t] = 1
        cur = now
        a, b = s, t

s, t = ord(start[0]) - 65, int(start[1]) - 1
if abs(s - a) + abs(t - b) != 3:
    ans = 'Invalid'
print(ans)