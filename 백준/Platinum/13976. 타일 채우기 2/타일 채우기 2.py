mod = 10 ** 9 + 7
mem = {0: (1, 0), 1: (2, 1)}
for i in range(2, 61):
    a, b = mem[i-1]
    mem[i] = (a * a + 3 * b * b) % mod, (2 * a * b) % mod

N = int(input())
if N & 1:
    a, b = 0, 0
else:
    a, b = None, None
    for idx, bit in enumerate(bin(N >> 1)[2::][::-1], 1):
        if bit == '1':
            if a == None:
                a, b = mem[idx]
            else:
                s, t = mem[idx]
                a, b = (a * s + 3 * b * t) % mod, (a * t + b * s) % mod
print((a + b) % mod)