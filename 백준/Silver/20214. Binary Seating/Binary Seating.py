n = int(input())
ans = 0
mul = 1 / 2
for num in sorted(map(int, input().split()), reverse=True):
    ans += num * mul
    mul /= 2
print(ans)