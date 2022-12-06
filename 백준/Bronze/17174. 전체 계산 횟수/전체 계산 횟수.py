N, M = map(int, input().split())
count = 0
while N:
    count += N
    N //= M
print(count)