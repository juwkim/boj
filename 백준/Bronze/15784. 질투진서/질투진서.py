N, a, b = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
jinseo = room[a-1][b-1]
state = 'HAPPY'
for row in range(1, N+1):
    if row != a and room[row-1][b-1] > jinseo:
        state = 'ANGRY'
        break
    if row == a and any([room[row-1][i] > jinseo for i in range(N)]):
        state = 'ANGRY'
        break
print(state)