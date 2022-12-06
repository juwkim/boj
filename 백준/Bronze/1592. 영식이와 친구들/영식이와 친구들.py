N, M, L = map(int, input().split())
game = [0] * N
now, count = 0, 0
while M not in game:
    game[now] += 1
    count += 1
    now = (now - L + game[now]%2*2*L) % N
print(count-1)