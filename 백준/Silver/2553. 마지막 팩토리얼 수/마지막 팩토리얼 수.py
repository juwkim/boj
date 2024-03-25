n = int(input())
five, num = 0, n
while num >= 5:
    num //= 5
    five += num
ans = 1
for i in range(1, n + 1):
    while i % 5 == 0:
        i //= 5
    if five and i % 2 == 0:
        five -= 1
        i >>= 1
    ans = (ans * i) % 10
print(ans)