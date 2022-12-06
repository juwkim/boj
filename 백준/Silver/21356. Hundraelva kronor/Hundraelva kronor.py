ans = 0
N = int(input())

num = 1
while num < N:
    num = num * 10 + 1

while N:
    r, N = divmod(N, num)
    ans += r
    num //= 10
print(ans)