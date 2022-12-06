N, K = map(int, input().split())
i = 0
while K and i <= N:
    i += 1
    if N%i == 0:
        K -= 1
print(0 if K else i)