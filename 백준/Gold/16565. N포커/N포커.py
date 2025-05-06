from math import comb

N = int(input())
ans = 0
for i in range(1, 14):
    if N < 4 * i:
        break
    num = comb(13, i) * comb(52 - 4 * i, N - 4 * i) % 10007
    if i & 1:
        ans += num
    else:
        ans -= num
    ans %= 10007
print(ans)