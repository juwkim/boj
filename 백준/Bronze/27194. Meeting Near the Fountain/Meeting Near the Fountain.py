N, T = map(int, input().split())
m = int(input())
x, y = map(int, input().split())

s = m / x + (N - m) / y - 60 * T
if s <= 0:
    print(0)
else:
    print(int((s + 59.999) // 60))