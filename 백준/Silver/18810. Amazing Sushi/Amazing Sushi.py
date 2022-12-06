g = lambda: [*map(int, input().split())]


N = int(input())
x1, y1 = g()
x2, y2 = g()
Mary, Marty, left = 0, 0, 0

for _ in range(N):
    r, q = divmod(int(input()), 2)
    Mary += r
    Marty += r
    left += q
if any(x1 <= Mary + i <= y1 and x2 <= Marty + left - i <= y2 for i in range(left+1)):
    print('Yes')
else:
    print('No')