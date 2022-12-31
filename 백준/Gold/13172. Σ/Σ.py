input = __import__('sys').stdin.readline
mod = 10 ** 9 + 7
ans = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = (ans + b * pow(a, - 1, mod)) % mod
print(ans)