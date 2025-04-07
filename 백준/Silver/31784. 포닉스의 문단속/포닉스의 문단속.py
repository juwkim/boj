N, K = map(int, input().split())
for i, c in enumerate(input()):
    d = (65 - ord(c)) % 26
    if i == N - 1:
        c = chr((ord(c) + K - 65) % 26 + 65)
    elif d <= K:
        K -= d
        c = 'A'
    print(c, end='')