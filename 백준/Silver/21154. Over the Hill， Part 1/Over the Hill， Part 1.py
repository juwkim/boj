n = int(input())
matrix = [[*map(int, input().split())] for _ in range(n)]
message = [*map(lambda s: ord(s) + 4 if s == ' ' else ord(s) - 65 if 'A' <= s <= 'Z' else ord(s) - 22, input())]

while len(message) % n:
    message.append(36)

s = ''
for x in [message[i:i+n] for i in range(0, len(message), n)]:
    for v in matrix:
        p = sum(a * b for a, b in zip(x, v)) % 37
        s += chr(p + 22 + 43 * (p < 26) - 26 * (p == 36))

print(s)