n, k = map(int, input().split())
a, b = '0' * (k + 1), '1' * (k + 1)
ans = 0
for i in range(1 << n):
    num = bin(i)[2::].zfill(n)
    check = a not in num and b not in num
    ans += check
print(ans)