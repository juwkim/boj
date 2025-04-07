N, K = map(int, input().split())
*S, a = input()
for c in S:
    d = (65 - ord(c)) % 26
    if d <= K:
        K -= d
        c = 'A'
    print(c, end='')
print(chr((ord(a) + K - 65) % 26 + 65))