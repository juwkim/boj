card = [*range(21)]
for _ in range(10):
    a, b = map(int, input().split())
    card = card[:a] + card[a:b+1][::-1] + card[b+1:]
print(*card[1:])