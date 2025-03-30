N = int(input())
p = N
for i in range(2, int(N**.5) + 1):
    if N % i == 0:
        p = i
        break
print(N - max(0, p - 2) >> 1)