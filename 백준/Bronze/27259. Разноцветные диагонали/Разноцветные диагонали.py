N = int(input())
for i in range(N):
    for j in range(N):
        c = min(abs(i - j), abs(N - 1 - i - j)) % 26
        print(chr(c + 97), end='')
    print()