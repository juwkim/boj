queens = []
ans = 'invalid'
for i in range(8):
    idx = input().find('*')
    if idx == -1:
        break
    queens.append((i, idx))
if len(queens) == 8:
    a = set(queens[i][1] for i in range(8))
    b = set(map(sum, queens))
    c = set(queen[0] - queen[1]  for queen in queens)
    if all(len(i) == 8 for i in [a, b, c]):
        ans = 'valid'
print(ans)