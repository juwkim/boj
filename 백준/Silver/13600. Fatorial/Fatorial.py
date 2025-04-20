N = int(input())
F = []
f, i = 1, 1
while f <= N:
    F.append(f)
    i += 1
    f *= i
cnt = 0
for f in reversed(F):
    if N == 0:
        break
    use = N // f
    cnt += use
    N -= use * f
print(cnt)