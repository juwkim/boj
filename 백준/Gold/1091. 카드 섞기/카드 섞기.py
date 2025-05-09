g = lambda: [*map(int, input().split())]

N = int(input())
P, S = g(), g()
cards = [*range(N)]
ans, check = 0, {tuple(cards)}
while any(P[cards[i]] != i % 3 for i in range(N)):
    ans += 1
    new = [-1] * N
    for i in range(N):
        new[S[i]] = cards[i]
    cards = new
    if tuple(cards) in check:
        ans = -1
        break
    check.add(tuple(cards))
print(ans)