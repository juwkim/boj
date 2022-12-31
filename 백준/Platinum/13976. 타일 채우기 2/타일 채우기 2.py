mod = 10 ** 9 + 7
mem = [(2, 1)]
for i in range(2, 61): a, b = mem[-1]; mem.append(((a * a + 3 * b * b) % mod, 2 * a * b % mod))
N = int(input())
a, b = 0, 0
if N % 2 == 0:
    idx = -1
    while N:= N >> 1:
        idx += 1
        if N & 1 == 0: continue
        if a: s, t = mem[idx]; a, b = (a * s + 3 * b * t) % mod, (a * t + b * s) % mod
        else: a, b = mem[idx]
print((a + b) % mod)