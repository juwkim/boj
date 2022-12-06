n, k = map(int, input().split())
floor = 1
for _ in range(n):
    a, b = input().split()
    a = int(a)
    if b == 'SAFE' and a > floor:
        floor = a
    if b == 'BROKEN' and a < k:
        k = a
print(floor+1, k-1)