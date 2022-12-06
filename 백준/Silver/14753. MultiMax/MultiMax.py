N = int(input())
minus, plus = [], []
for num in map(int, input().split()):
    if num > 0:
        plus.append(num)
    elif num < 0:
        minus.append(num)

plus.sort(reverse=True)
minus.sort()
ans = 0
if len(plus) >= 3:
    a, b, c = plus[:3]
    ans = max(ans, a * b * c)
if len(plus) == 2:
    a, b = plus[:2]
    ans = max(ans, a * b)

if len(minus) >= 2:
    a, b = minus[:2]
    if len(plus):
        ans = max(ans, plus[0] * a * b)
    else:
        ans = max(ans, a * b)
print(ans)