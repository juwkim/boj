g = lambda: map(int, input().split())

for _ in range(int(input())):
    N, K = g()
    if 1 <= N % (K + 1) <= K:
        winner = 'Hektor'
    else:
        winner = 'Wiktor'
    print(winner)