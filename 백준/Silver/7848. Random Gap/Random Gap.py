a, c, m, r0 = map(int, input().split())
check = bytearray(m)
check[r0] = 1
ans = float('-inf')
while True:
    r1 = (a * r0 + c) % m
    if check[r1]:
        break
    check[r1] = 1
    r0 = r1

ans = 0
prev = float('inf')
for i in range(m):
    if check[i]:
        ans = max(ans, i - prev)
        prev = i
print(ans)