k, pos = map(int, input().split())
enc = input()
for _ in range(k):
    s = len(enc)
    enc = ''.join(enc[i+1] * int(enc[i]) for i in range(0, s, 2))
print(enc[pos])