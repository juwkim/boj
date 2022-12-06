R, C = map(int, input().split())
card = []
for _ in range(R):
    s = input()
    card += [s + s[::-1]]
card += card[::-1]

A, B = map(int, input().split())

if card[A-1][B-1] == '.':
    card[A-1] = card[A-1][:B-1] + '#' + card[A-1][B:]
else:
    card[A-1] = card[A-1][:B-1] + '.' + card[A-1][B:]
print(*card, sep='\n')